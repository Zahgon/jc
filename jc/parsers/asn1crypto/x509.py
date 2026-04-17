# coding: utf-8

"""
ASN.1 type classes for X.509 certificates. Exports the following items:

 - Attributes()
 - Certificate()
 - Extensions()
 - GeneralName()
 - GeneralNames()
 - Name()

Other type classes are defined that help compose the types listed above.
"""

from __future__ import unicode_literals, division, absolute_import, print_function

from collections import OrderedDict
from contextlib import contextmanager
from encodings import idna  # noqa
import hashlib
import re
import socket
import stringprep
import sys
import unicodedata

from ._errors import unwrap
from ._iri import iri_to_uri, uri_to_iri
from ._types import type_name
from .algos import AlgorithmIdentifier, AnyAlgorithmIdentifier, DigestAlgorithm, SignedDigestAlgorithm
from .core import (
    Any,
    BitString,
    BMPString,
    Boolean,
    Choice,
    Concat,
    Enumerated,
    GeneralizedTime,
    GeneralString,
    IA5String,
    Integer,
    Null,
    NumericString,
    ObjectIdentifier,
    OctetBitString,
    OctetString,
    ParsableOctetString,
    PrintableString,
    Sequence,
    SequenceOf,
    Set,
    SetOf,
    TeletexString,
    UniversalString,
    UTCTime,
    UTF8String,
    VisibleString,
    VOID,
)
from .keys import PublicKeyInfo
from .util import int_to_bytes, int_from_bytes, inet_ntop, inet_pton


# The structures in this file are taken from https://tools.ietf.org/html/rfc5280
# and a few other supplementary sources, mostly due to extra supported
# extension and name OIDs


class DNSName(IA5String):

    _encoding = 'idna'
    _bad_tag = (12, 19)

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        """
        Equality as defined by https://tools.ietf.org/html/rfc5280#section-7.2

        :param other:
            Another DNSName object

        :return:
            A boolean
        """

        if not isinstance(other, DNSName):
            return False

        return self.__unicode__().lower() == other.__unicode__().lower()

    def set(self, value):
        """
        Sets the value of the DNS name

        :param value:
            A unicode string
        """
        pass


class URI(IA5String):

    def set(self, value):
        """
        Sets the value of the string

        :param value:
            A unicode string
        """
        pass

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        """
        Equality as defined by https://tools.ietf.org/html/rfc5280#section-7.4

        :param other:
            Another URI object

        :return:
            A boolean
        """

        if not isinstance(other, URI):
            return False

        return iri_to_uri(self.native, True) == iri_to_uri(other.native, True)

    def __unicode__(self):
        """
        :return:
            A unicode string
        """

        if self.contents is None:
            return ''
        if self._unicode is None:
            self._unicode = uri_to_iri(self._merge_chunks())
        return self._unicode


class EmailAddress(IA5String):

    _contents = None

    # If the value has gone through the .set() method, thus normalizing it
    _normalized = False

    # In the wild we've seen this encoded as a UTF8String and PrintableString
    _bad_tag = (12, 19)

    @property
    def contents(self):
        """
        :return:
            A byte string of the DER-encoded contents of the sequence
        """
        pass

    @contents.setter
    def contents(self, value):
        """
        :param value:
            A byte string of the DER-encoded contents of the sequence
        """
        pass

    def set(self, value):
        """
        Sets the value of the string

        :param value:
            A unicode string
        """
        pass

    def __unicode__(self):
        """
        :return:
            A unicode string
        """

        # We've seen this in the wild as a PrintableString, and since ascii is a
        # subset of cp1252, we use the later for decoding to be more user friendly
        if self._unicode is None:
            contents = self._merge_chunks()
            if contents.find(b'@') == -1:
                self._unicode = contents.decode('cp1252')
            else:
                mailbox, hostname = contents.rsplit(b'@', 1)

                # fix to allow incorrectly encoded email addresses to succeed with warning
                try:
                    self._unicode = mailbox.decode('cp1252') + '@' + hostname.decode('idna')
                except (UnicodeDecodeError, UnicodeError):
                    ascii_mailbox = mailbox.decode('ascii', errors='backslashreplace')
                    ascii_hostname = hostname.decode('ascii', errors='backslashreplace')
                    from jc.utils import warning_message
                    import jc.parsers.asn1crypto.jc_global as jc_global
                    if not jc_global.quiet:
                        warning_message([f'Invalid email address found: {ascii_mailbox}@{ascii_hostname}'])
                    self._unicode = ascii_mailbox + '@' + ascii_hostname
        return self._unicode

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        """
        Equality as defined by https://tools.ietf.org/html/rfc5280#section-7.5

        :param other:
            Another EmailAddress object

        :return:
            A boolean
        """

        if not isinstance(other, EmailAddress):
            return False

        if not self._normalized:
            self.set(self.native)
        if not other._normalized:
            other.set(other.native)

        if self._contents.find(b'@') == -1 or other._contents.find(b'@') == -1:
            return self._contents == other._contents

        other_mailbox, other_hostname = other._contents.rsplit(b'@', 1)
        mailbox, hostname = self._contents.rsplit(b'@', 1)

        if mailbox != other_mailbox:
            return False

        if hostname.lower() != other_hostname.lower():
            return False

        return True


class IPAddress(OctetString):
    def parse(self, spec=None, spec_params=None):
        """
        This method is not applicable to IP addresses
        """
        pass

    def set(self, value):
        """
        Sets the value of the object

        :param value:
            A unicode string containing an IPv4 address, IPv4 address with CIDR,
            an IPv6 address or IPv6 address with CIDR
        """
        pass

    @property
    def native(self):
        """
        The native Python datatype representation of this value

        :return:
            A unicode string or None
        """
        pass

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        """
        :param other:
            Another IPAddress object

        :return:
            A boolean
        """

        if not isinstance(other, IPAddress):
            return False

        return self.__bytes__() == other.__bytes__()


class Attribute(Sequence):
    _fields = [
        ('type', ObjectIdentifier),
        ('values', SetOf, {'spec': Any}),
    ]


class Attributes(SequenceOf):
    _child_spec = Attribute


class KeyUsage(BitString):
    _map = {
        0: 'digital_signature',
        1: 'non_repudiation',
        2: 'key_encipherment',
        3: 'data_encipherment',
        4: 'key_agreement',
        5: 'key_cert_sign',
        6: 'crl_sign',
        7: 'encipher_only',
        8: 'decipher_only',
    }


class PrivateKeyUsagePeriod(Sequence):
    _fields = [
        ('not_before', GeneralizedTime, {'implicit': 0, 'optional': True}),
        ('not_after', GeneralizedTime, {'implicit': 1, 'optional': True}),
    ]


class NotReallyTeletexString(TeletexString):
    """
    OpenSSL (and probably some other libraries) puts ISO-8859-1
    into TeletexString instead of ITU T.61. We use Windows-1252 when
    decoding since it is a superset of ISO-8859-1, and less likely to
    cause encoding issues, but we stay strict with encoding to prevent
    us from creating bad data.
    """

    _decoding_encoding = 'cp1252'

    def __unicode__(self):
        """
        :return:
            A unicode string
        """

        if self.contents is None:
            return ''
        if self._unicode is None:
            self._unicode = self._merge_chunks().decode(self._decoding_encoding)
        return self._unicode


@contextmanager
def strict_teletex():
    pass


class DirectoryString(Choice):
    _alternatives = [
        ('teletex_string', NotReallyTeletexString),
        ('printable_string', PrintableString),
        ('universal_string', UniversalString),
        ('utf8_string', UTF8String),
        ('bmp_string', BMPString),
        # This is an invalid/bad alternative, but some broken certs use it
        ('ia5_string', IA5String),
    ]


class NameType(ObjectIdentifier):
    _map = {
        '2.5.4.3': 'common_name',
        '2.5.4.4': 'surname',
        '2.5.4.5': 'serial_number',
        '2.5.4.6': 'country_name',
        '2.5.4.7': 'locality_name',
        '2.5.4.8': 'state_or_province_name',
        '2.5.4.9': 'street_address',
        '2.5.4.10': 'organization_name',
        '2.5.4.11': 'organizational_unit_name',
        '2.5.4.12': 'title',
        '2.5.4.15': 'business_category',
        '2.5.4.17': 'postal_code',
        '2.5.4.20': 'telephone_number',
        '2.5.4.41': 'name',
        '2.5.4.42': 'given_name',
        '2.5.4.43': 'initials',
        '2.5.4.44': 'generation_qualifier',
        '2.5.4.45': 'unique_identifier',
        '2.5.4.46': 'dn_qualifier',
        '2.5.4.65': 'pseudonym',
        '2.5.4.97': 'organization_identifier',
        # https://www.trustedcomputinggroup.org/wp-content/uploads/Credential_Profile_EK_V2.0_R14_published.pdf
        '2.23.133.2.1': 'tpm_manufacturer',
        '2.23.133.2.2': 'tpm_model',
        '2.23.133.2.3': 'tpm_version',
        '2.23.133.2.4': 'platform_manufacturer',
        '2.23.133.2.5': 'platform_model',
        '2.23.133.2.6': 'platform_version',
        # https://tools.ietf.org/html/rfc2985#page-26
        '1.2.840.113549.1.9.1': 'email_address',
        # Page 10 of https://cabforum.org/wp-content/uploads/EV-V1_5_5.pdf
        '1.3.6.1.4.1.311.60.2.1.1': 'incorporation_locality',
        '1.3.6.1.4.1.311.60.2.1.2': 'incorporation_state_or_province',
        '1.3.6.1.4.1.311.60.2.1.3': 'incorporation_country',
        # https://tools.ietf.org/html/rfc4519#section-2.39
        '0.9.2342.19200300.100.1.1': 'user_id',
        # https://tools.ietf.org/html/rfc2247#section-4
        '0.9.2342.19200300.100.1.25': 'domain_component',
        # http://www.alvestrand.no/objectid/0.2.262.1.10.7.20.html
        '0.2.262.1.10.7.20': 'name_distinguisher',
    }

    # This order is largely based on observed order seen in EV certs from
    # Symantec and DigiCert. Some of the uncommon name-related fields are
    # just placed in what seems like a reasonable order.
    preferred_order = [
        'incorporation_country',
        'incorporation_state_or_province',
        'incorporation_locality',
        'business_category',
        'serial_number',
        'country_name',
        'postal_code',
        'state_or_province_name',
        'locality_name',
        'street_address',
        'organization_name',
        'organizational_unit_name',
        'title',
        'common_name',
        'user_id',
        'initials',
        'generation_qualifier',
        'surname',
        'given_name',
        'name',
        'pseudonym',
        'dn_qualifier',
        'telephone_number',
        'email_address',
        'domain_component',
        'name_distinguisher',
        'organization_identifier',
        'tpm_manufacturer',
        'tpm_model',
        'tpm_version',
        'platform_manufacturer',
        'platform_model',
        'platform_version',
    ]

    @classmethod
    def preferred_ordinal(cls, attr_name):
        """
        Returns an ordering value for a particular attribute key.

        Unrecognized attributes and OIDs will be sorted lexically at the end.

        :return:
            An orderable value.

        """
        pass

    @property
    def human_friendly(self):
        """
        :return:
            A human-friendly unicode string to display to users
        """
        pass


class NameTypeAndValue(Sequence):
    _fields = [
        ('type', NameType),
        ('value', Any),
    ]

    _oid_pair = ('type', 'value')
    _oid_specs = {
        'common_name': DirectoryString,
        'surname': DirectoryString,
        'serial_number': DirectoryString,
        'country_name': DirectoryString,
        'locality_name': DirectoryString,
        'state_or_province_name': DirectoryString,
        'street_address': DirectoryString,
        'organization_name': DirectoryString,
        'organizational_unit_name': DirectoryString,
        'title': DirectoryString,
        'business_category': DirectoryString,
        'postal_code': DirectoryString,
        'telephone_number': PrintableString,
        'name': DirectoryString,
        'given_name': DirectoryString,
        'initials': DirectoryString,
        'generation_qualifier': DirectoryString,
        'unique_identifier': OctetBitString,
        'dn_qualifier': DirectoryString,
        'pseudonym': DirectoryString,
        # https://tools.ietf.org/html/rfc2985#page-26
        'email_address': EmailAddress,
        # Page 10 of https://cabforum.org/wp-content/uploads/EV-V1_5_5.pdf
        'incorporation_locality': DirectoryString,
        'incorporation_state_or_province': DirectoryString,
        'incorporation_country': DirectoryString,
        'domain_component': DNSName,
        'name_distinguisher': DirectoryString,
        'organization_identifier': DirectoryString,
        'tpm_manufacturer': UTF8String,
        'tpm_model': UTF8String,
        'tpm_version': UTF8String,
        'platform_manufacturer': UTF8String,
        'platform_model': UTF8String,
        'platform_version': UTF8String,
        'user_id': DirectoryString,
    }

    _prepped = None

    @property
    def prepped_value(self):
        """
        Returns the value after being processed by the internationalized string
        preparation as specified by RFC 5280

        :return:
            A unicode string
        """
        pass

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        """
        Equality as defined by https://tools.ietf.org/html/rfc5280#section-7.1

        :param other:
            Another NameTypeAndValue object

        :return:
            A boolean
        """

        if not isinstance(other, NameTypeAndValue):
            return False

        if other['type'].native != self['type'].native:
            return False

        return other.prepped_value == self.prepped_value

    def _ldap_string_prep(self, string):
        """
        Implements the internationalized string preparation algorithm from
        RFC 4518. https://tools.ietf.org/html/rfc4518#section-2

        :param string:
            A unicode string to prepare

        :return:
            A prepared unicode string, ready for comparison
        """
        pass


class RelativeDistinguishedName(SetOf):
    _child_spec = NameTypeAndValue

    @property
    def hashable(self):
        """
        :return:
            A unicode string that can be used as a dict key or in a set
        """
        pass

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        """
        Equality as defined by https://tools.ietf.org/html/rfc5280#section-7.1

        :param other:
            Another RelativeDistinguishedName object

        :return:
            A boolean
        """

        if not isinstance(other, RelativeDistinguishedName):
            return False

        if len(self) != len(other):
            return False

        self_types = self._get_types(self)
        other_types = self._get_types(other)

        if self_types != other_types:
            return False

        self_values = self._get_values(self)
        other_values = self._get_values(other)

        for type_name_ in self_types:
            if self_values[type_name_] != other_values[type_name_]:
                return False

        return True

    def _get_types(self, rdn):
        """
        Returns a set of types contained in an RDN

        :param rdn:
            A RelativeDistinguishedName object

        :return:
            A set object with unicode strings of NameTypeAndValue type field
            values
        """
        pass

    def _get_values(self, rdn):
        """
        Returns a dict of prepped values contained in an RDN

        :param rdn:
            A RelativeDistinguishedName object

        :return:
            A dict object with unicode strings of NameTypeAndValue value field
            values that have been prepped for comparison
        """
        pass


class RDNSequence(SequenceOf):
    _child_spec = RelativeDistinguishedName

    @property
    def hashable(self):
        """
        :return:
            A unicode string that can be used as a dict key or in a set
        """
        pass

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        """
        Equality as defined by https://tools.ietf.org/html/rfc5280#section-7.1

        :param other:
            Another RDNSequence object

        :return:
            A boolean
        """

        if not isinstance(other, RDNSequence):
            return False

        if len(self) != len(other):
            return False

        for index, self_rdn in enumerate(self):
            if other[index] != self_rdn:
                return False

        return True


class Name(Choice):
    _alternatives = [
        ('', RDNSequence),
    ]

    _human_friendly = None
    _sha1 = None
    _sha256 = None

    @classmethod
    def build(cls, name_dict, use_printable=False):
        """
        Creates a Name object from a dict of unicode string keys and values.
        The keys should be from NameType._map, or a dotted-integer OID unicode
        string.

        :param name_dict:
            A dict of name information, e.g. {"common_name": "Will Bond",
            "country_name": "US", "organization_name": "Codex Non Sufficit LC"}

        :param use_printable:
            A bool - if PrintableString should be used for encoding instead of
            UTF8String. This is for backwards compatibility with old software.

        :return:
            An x509.Name object
        """
        pass

    @property
    def hashable(self):
        """
        :return:
            A unicode string that can be used as a dict key or in a set
        """
        pass

    def __len__(self):
        return len(self.chosen)

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        """
        Equality as defined by https://tools.ietf.org/html/rfc5280#section-7.1

        :param other:
            Another Name object

        :return:
            A boolean
        """

        if not isinstance(other, Name):
            return False
        return self.chosen == other.chosen

    @property
    def native(self):
        pass

    @property
    def human_friendly(self):
        """
        :return:
            A human-friendly unicode string containing the parts of the name
        """
        pass

    def _recursive_humanize(self, value):
        """
        Recursively serializes data compiled from the RDNSequence

        :param value:
            An Asn1Value object, or a list of Asn1Value objects

        :return:
            A unicode string
        """
        pass

    @property
    def sha1(self):
        """
        :return:
            The SHA1 hash of the DER-encoded bytes of this name
        """
        pass

    @property
    def sha256(self):
        """
        :return:
            The SHA-256 hash of the DER-encoded bytes of this name
        """
        pass


class AnotherName(Sequence):
    _fields = [
        ('type_id', ObjectIdentifier),
        ('value', Any, {'explicit': 0}),
    ]


class CountryName(Choice):
    class_ = 1
    tag = 1

    _alternatives = [
        ('x121_dcc_code', NumericString),
        ('iso_3166_alpha2_code', PrintableString),
    ]


class AdministrationDomainName(Choice):
    class_ = 1
    tag = 2

    _alternatives = [
        ('numeric', NumericString),
        ('printable', PrintableString),
    ]


class PrivateDomainName(Choice):
    _alternatives = [
        ('numeric', NumericString),
        ('printable', PrintableString),
    ]


class PersonalName(Set):
    _fields = [
        ('surname', PrintableString, {'implicit': 0}),
        ('given_name', PrintableString, {'implicit': 1, 'optional': True}),
        ('initials', PrintableString, {'implicit': 2, 'optional': True}),
        ('generation_qualifier', PrintableString, {'implicit': 3, 'optional': True}),
    ]


class TeletexPersonalName(Set):
    _fields = [
        ('surname', TeletexString, {'implicit': 0}),
        ('given_name', TeletexString, {'implicit': 1, 'optional': True}),
        ('initials', TeletexString, {'implicit': 2, 'optional': True}),
        ('generation_qualifier', TeletexString, {'implicit': 3, 'optional': True}),
    ]


class OrganizationalUnitNames(SequenceOf):
    _child_spec = PrintableString


class TeletexOrganizationalUnitNames(SequenceOf):
    _child_spec = TeletexString


class BuiltInStandardAttributes(Sequence):
    _fields = [
        ('country_name', CountryName, {'optional': True}),
        ('administration_domain_name', AdministrationDomainName, {'optional': True}),
        ('network_address', NumericString, {'implicit': 0, 'optional': True}),
        ('terminal_identifier', PrintableString, {'implicit': 1, 'optional': True}),
        ('private_domain_name', PrivateDomainName, {'explicit': 2, 'optional': True}),
        ('organization_name', PrintableString, {'implicit': 3, 'optional': True}),
        ('numeric_user_identifier', NumericString, {'implicit': 4, 'optional': True}),
        ('personal_name', PersonalName, {'implicit': 5, 'optional': True}),
        ('organizational_unit_names', OrganizationalUnitNames, {'implicit': 6, 'optional': True}),
    ]


class BuiltInDomainDefinedAttribute(Sequence):
    _fields = [
        ('type', PrintableString),
        ('value', PrintableString),
    ]


class BuiltInDomainDefinedAttributes(SequenceOf):
    _child_spec = BuiltInDomainDefinedAttribute


class TeletexDomainDefinedAttribute(Sequence):
    _fields = [
        ('type', TeletexString),
        ('value', TeletexString),
    ]


class TeletexDomainDefinedAttributes(SequenceOf):
    _child_spec = TeletexDomainDefinedAttribute


class PhysicalDeliveryCountryName(Choice):
    _alternatives = [
        ('x121_dcc_code', NumericString),
        ('iso_3166_alpha2_code', PrintableString),
    ]


class PostalCode(Choice):
    _alternatives = [
        ('numeric_code', NumericString),
        ('printable_code', PrintableString),
    ]


class PDSParameter(Set):
    _fields = [
        ('printable_string', PrintableString, {'optional': True}),
        ('teletex_string', TeletexString, {'optional': True}),
    ]


class PrintableAddress(SequenceOf):
    _child_spec = PrintableString


class UnformattedPostalAddress(Set):
    _fields = [
        ('printable_address', PrintableAddress, {'optional': True}),
        ('teletex_string', TeletexString, {'optional': True}),
    ]


class E1634Address(Sequence):
    _fields = [
        ('number', NumericString, {'implicit': 0}),
        ('sub_address', NumericString, {'implicit': 1, 'optional': True}),
    ]


class NAddresses(SetOf):
    _child_spec = OctetString


class PresentationAddress(Sequence):
    _fields = [
        ('p_selector', OctetString, {'explicit': 0, 'optional': True}),
        ('s_selector', OctetString, {'explicit': 1, 'optional': True}),
        ('t_selector', OctetString, {'explicit': 2, 'optional': True}),
        ('n_addresses', NAddresses, {'explicit': 3}),
    ]


class ExtendedNetworkAddress(Choice):
    _alternatives = [
        ('e163_4_address', E1634Address),
        ('psap_address', PresentationAddress, {'implicit': 0})
    ]


class TerminalType(Integer):
    _map = {
        3: 'telex',
        4: 'teletex',
        5: 'g3_facsimile',
        6: 'g4_facsimile',
        7: 'ia5_terminal',
        8: 'videotex',
    }


class ExtensionAttributeType(Integer):
    _map = {
        1: 'common_name',
        2: 'teletex_common_name',
        3: 'teletex_organization_name',
        4: 'teletex_personal_name',
        5: 'teletex_organization_unit_names',
        6: 'teletex_domain_defined_attributes',
        7: 'pds_name',
        8: 'physical_delivery_country_name',
        9: 'postal_code',
        10: 'physical_delivery_office_name',
        11: 'physical_delivery_office_number',
        12: 'extension_of_address_components',
        13: 'physical_delivery_personal_name',
        14: 'physical_delivery_organization_name',
        15: 'extension_physical_delivery_address_components',
        16: 'unformatted_postal_address',
        17: 'street_address',
        18: 'post_office_box_address',
        19: 'poste_restante_address',
        20: 'unique_postal_name',
        21: 'local_postal_attributes',
        22: 'extended_network_address',
        23: 'terminal_type',
    }


class ExtensionAttribute(Sequence):
    _fields = [
        ('extension_attribute_type', ExtensionAttributeType, {'implicit': 0}),
        ('extension_attribute_value', Any, {'explicit': 1}),
    ]

    _oid_pair = ('extension_attribute_type', 'extension_attribute_value')
    _oid_specs = {
        'common_name': PrintableString,
        'teletex_common_name': TeletexString,
        'teletex_organization_name': TeletexString,
        'teletex_personal_name': TeletexPersonalName,
        'teletex_organization_unit_names': TeletexOrganizationalUnitNames,
        'teletex_domain_defined_attributes': TeletexDomainDefinedAttributes,
        'pds_name': PrintableString,
        'physical_delivery_country_name': PhysicalDeliveryCountryName,
        'postal_code': PostalCode,
        'physical_delivery_office_name': PDSParameter,
        'physical_delivery_office_number': PDSParameter,
        'extension_of_address_components': PDSParameter,
        'physical_delivery_personal_name': PDSParameter,
        'physical_delivery_organization_name': PDSParameter,
        'extension_physical_delivery_address_components': PDSParameter,
        'unformatted_postal_address': UnformattedPostalAddress,
        'street_address': PDSParameter,
        'post_office_box_address': PDSParameter,
        'poste_restante_address': PDSParameter,
        'unique_postal_name': PDSParameter,
        'local_postal_attributes': PDSParameter,
        'extended_network_address': ExtendedNetworkAddress,
        'terminal_type': TerminalType,
    }


class ExtensionAttributes(SequenceOf):
    _child_spec = ExtensionAttribute


class ORAddress(Sequence):
    _fields = [
        ('built_in_standard_attributes', BuiltInStandardAttributes),
        ('built_in_domain_defined_attributes', BuiltInDomainDefinedAttributes, {'optional': True}),
        ('extension_attributes', ExtensionAttributes, {'optional': True}),
    ]


class EDIPartyName(Sequence):
    _fields = [
        ('name_assigner', DirectoryString, {'implicit': 0, 'optional': True}),
        ('party_name', DirectoryString, {'implicit': 1}),
    ]


class GeneralName(Choice):
    _alternatives = [
        ('other_name', AnotherName, {'implicit': 0}),
        ('rfc822_name', EmailAddress, {'implicit': 1}),
        ('dns_name', DNSName, {'implicit': 2}),
        ('x400_address', ORAddress, {'implicit': 3}),
        ('directory_name', Name, {'explicit': 4}),
        ('edi_party_name', EDIPartyName, {'implicit': 5}),
        ('uniform_resource_identifier', URI, {'implicit': 6}),
        ('ip_address', IPAddress, {'implicit': 7}),
        ('registered_id', ObjectIdentifier, {'implicit': 8}),
    ]

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        """
        Does not support other_name, x400_address or edi_party_name

        :param other:
            The other GeneralName to compare to

        :return:
            A boolean
        """

        if self.name in ('other_name', 'x400_address', 'edi_party_name'):
            raise ValueError(unwrap(
                '''
                Comparison is not supported for GeneralName objects of
                choice %s
                ''',
                self.name
            ))

        if other.name in ('other_name', 'x400_address', 'edi_party_name'):
            raise ValueError(unwrap(
                '''
                Comparison is not supported for GeneralName objects of choice
                %s''',
                other.name
            ))

        if self.name != other.name:
            return False

        return self.chosen == other.chosen


class GeneralNames(SequenceOf):
    _child_spec = GeneralName


class Time(Choice):
    _alternatives = [
        ('utc_time', UTCTime),
        ('general_time', GeneralizedTime),
    ]


class Validity(Sequence):
    _fields = [
        ('not_before', Time),
        ('not_after', Time),
    ]


class BasicConstraints(Sequence):
    _fields = [
        ('ca', Boolean, {'default': False}),
        ('path_len_constraint', Integer, {'optional': True}),
    ]


class AuthorityKeyIdentifier(Sequence):
    _fields = [
        ('key_identifier', OctetString, {'implicit': 0, 'optional': True}),
        ('authority_cert_issuer', GeneralNames, {'implicit': 1, 'optional': True}),
        ('authority_cert_serial_number', Integer, {'implicit': 2, 'optional': True}),
    ]


class DistributionPointName(Choice):
    _alternatives = [
        ('full_name', GeneralNames, {'implicit': 0}),
        ('name_relative_to_crl_issuer', RelativeDistinguishedName, {'implicit': 1}),
    ]


class ReasonFlags(BitString):
    _map = {
        0: 'unused',
        1: 'key_compromise',
        2: 'ca_compromise',
        3: 'affiliation_changed',
        4: 'superseded',
        5: 'cessation_of_operation',
        6: 'certificate_hold',
        7: 'privilege_withdrawn',
        8: 'aa_compromise',
    }


class GeneralSubtree(Sequence):
    _fields = [
        ('base', GeneralName),
        ('minimum', Integer, {'implicit': 0, 'default': 0}),
        ('maximum', Integer, {'implicit': 1, 'optional': True}),
    ]


class GeneralSubtrees(SequenceOf):
    _child_spec = GeneralSubtree


class NameConstraints(Sequence):
    _fields = [
        ('permitted_subtrees', GeneralSubtrees, {'implicit': 0, 'optional': True}),
        ('excluded_subtrees', GeneralSubtrees, {'implicit': 1, 'optional': True}),
    ]


class DistributionPoint(Sequence):
    _fields = [
        ('distribution_point', DistributionPointName, {'explicit': 0, 'optional': True}),
        ('reasons', ReasonFlags, {'implicit': 1, 'optional': True}),
        ('crl_issuer', GeneralNames, {'implicit': 2, 'optional': True}),
    ]

    _url = False

    @property
    def url(self):
        """
        :return:
            None or a unicode string of the distribution point's URL
        """
        pass


class CRLDistributionPoints(SequenceOf):
    _child_spec = DistributionPoint


class DisplayText(Choice):
    _alternatives = [
        ('ia5_string', IA5String),
        ('visible_string', VisibleString),
        ('bmp_string', BMPString),
        ('utf8_string', UTF8String),
    ]


class NoticeNumbers(SequenceOf):
    _child_spec = Integer


class NoticeReference(Sequence):
    _fields = [
        ('organization', DisplayText),
        ('notice_numbers', NoticeNumbers),
    ]


class UserNotice(Sequence):
    _fields = [
        ('notice_ref', NoticeReference, {'optional': True}),
        ('explicit_text', DisplayText, {'optional': True}),
    ]


class PolicyQualifierId(ObjectIdentifier):
    _map = {
        '1.3.6.1.5.5.7.2.1': 'certification_practice_statement',
        '1.3.6.1.5.5.7.2.2': 'user_notice',
    }


class PolicyQualifierInfo(Sequence):
    _fields = [
        ('policy_qualifier_id', PolicyQualifierId),
        ('qualifier', Any),
    ]

    _oid_pair = ('policy_qualifier_id', 'qualifier')
    _oid_specs = {
        'certification_practice_statement': IA5String,
        'user_notice': UserNotice,
    }


class PolicyQualifierInfos(SequenceOf):
    _child_spec = PolicyQualifierInfo


class PolicyIdentifier(ObjectIdentifier):
    _map = {
        '2.5.29.32.0': 'any_policy',
    }


class PolicyInformation(Sequence):
    _fields = [
        ('policy_identifier', PolicyIdentifier),
        ('policy_qualifiers', PolicyQualifierInfos, {'optional': True})
    ]


class CertificatePolicies(SequenceOf):
    _child_spec = PolicyInformation


class PolicyMapping(Sequence):
    _fields = [
        ('issuer_domain_policy', PolicyIdentifier),
        ('subject_domain_policy', PolicyIdentifier),
    ]


class PolicyMappings(SequenceOf):
    _child_spec = PolicyMapping


class PolicyConstraints(Sequence):
    _fields = [
        ('require_explicit_policy', Integer, {'implicit': 0, 'optional': True}),
        ('inhibit_policy_mapping', Integer, {'implicit': 1, 'optional': True}),
    ]


class KeyPurposeId(ObjectIdentifier):
    _map = {
        # https://tools.ietf.org/html/rfc5280#page-45
        '2.5.29.37.0': 'any_extended_key_usage',
        '1.3.6.1.5.5.7.3.1': 'server_auth',
        '1.3.6.1.5.5.7.3.2': 'client_auth',
        '1.3.6.1.5.5.7.3.3': 'code_signing',
        '1.3.6.1.5.5.7.3.4': 'email_protection',
        '1.3.6.1.5.5.7.3.5': 'ipsec_end_system',
        '1.3.6.1.5.5.7.3.6': 'ipsec_tunnel',
        '1.3.6.1.5.5.7.3.7': 'ipsec_user',
        '1.3.6.1.5.5.7.3.8': 'time_stamping',
        '1.3.6.1.5.5.7.3.9': 'ocsp_signing',
        # http://tools.ietf.org/html/rfc3029.html#page-9
        '1.3.6.1.5.5.7.3.10': 'dvcs',
        # http://tools.ietf.org/html/rfc6268.html#page-16
        '1.3.6.1.5.5.7.3.13': 'eap_over_ppp',
        '1.3.6.1.5.5.7.3.14': 'eap_over_lan',
        # https://tools.ietf.org/html/rfc5055#page-76
        '1.3.6.1.5.5.7.3.15': 'scvp_server',
        '1.3.6.1.5.5.7.3.16': 'scvp_client',
        # https://tools.ietf.org/html/rfc4945#page-31
        '1.3.6.1.5.5.7.3.17': 'ipsec_ike',
        # https://tools.ietf.org/html/rfc5415#page-38
        '1.3.6.1.5.5.7.3.18': 'capwap_ac',
        '1.3.6.1.5.5.7.3.19': 'capwap_wtp',
        # https://tools.ietf.org/html/rfc5924#page-8
        '1.3.6.1.5.5.7.3.20': 'sip_domain',
        # https://tools.ietf.org/html/rfc6187#page-7
        '1.3.6.1.5.5.7.3.21': 'secure_shell_client',
        '1.3.6.1.5.5.7.3.22': 'secure_shell_server',
        # https://tools.ietf.org/html/rfc6494#page-7
        '1.3.6.1.5.5.7.3.23': 'send_router',
        '1.3.6.1.5.5.7.3.24': 'send_proxied_router',
        '1.3.6.1.5.5.7.3.25': 'send_owner',
        '1.3.6.1.5.5.7.3.26': 'send_proxied_owner',
        # https://tools.ietf.org/html/rfc6402#page-10
        '1.3.6.1.5.5.7.3.27': 'cmc_ca',
        '1.3.6.1.5.5.7.3.28': 'cmc_ra',
        '1.3.6.1.5.5.7.3.29': 'cmc_archive',
        # https://tools.ietf.org/html/draft-ietf-sidr-bgpsec-pki-profiles-15#page-6
        '1.3.6.1.5.5.7.3.30': 'bgpspec_router',
        # https://www.ietf.org/proceedings/44/I-D/draft-ietf-ipsec-pki-req-01.txt
        '1.3.6.1.5.5.8.2.2': 'ike_intermediate',
        # https://msdn.microsoft.com/en-us/library/windows/desktop/aa378132(v=vs.85).aspx
        # and https://support.microsoft.com/en-us/kb/287547
        '1.3.6.1.4.1.311.10.3.1': 'microsoft_trust_list_signing',
        '1.3.6.1.4.1.311.10.3.2': 'microsoft_time_stamp_signing',
        '1.3.6.1.4.1.311.10.3.3': 'microsoft_server_gated',
        '1.3.6.1.4.1.311.10.3.3.1': 'microsoft_serialized',
        '1.3.6.1.4.1.311.10.3.4': 'microsoft_efs',
        '1.3.6.1.4.1.311.10.3.4.1': 'microsoft_efs_recovery',
        '1.3.6.1.4.1.311.10.3.5': 'microsoft_whql',
        '1.3.6.1.4.1.311.10.3.6': 'microsoft_nt5',
        '1.3.6.1.4.1.311.10.3.7': 'microsoft_oem_whql',
        '1.3.6.1.4.1.311.10.3.8': 'microsoft_embedded_nt',
        '1.3.6.1.4.1.311.10.3.9': 'microsoft_root_list_signer',
        '1.3.6.1.4.1.311.10.3.10': 'microsoft_qualified_subordination',
        '1.3.6.1.4.1.311.10.3.11': 'microsoft_key_recovery',
        '1.3.6.1.4.1.311.10.3.12': 'microsoft_document_signing',
        '1.3.6.1.4.1.311.10.3.13': 'microsoft_lifetime_signing',
        '1.3.6.1.4.1.311.10.3.14': 'microsoft_mobile_device_software',
        # https://support.microsoft.com/en-us/help/287547/object-ids-associated-with-microsoft-cryptography
        '1.3.6.1.4.1.311.20.2.2': 'microsoft_smart_card_logon',
        # https://opensource.apple.com/source
        #  - /Security/Security-57031.40.6/Security/libsecurity_keychain/lib/SecPolicy.cpp
        #  - /libsecurity_cssm/libsecurity_cssm-36064/lib/oidsalg.c
        '1.2.840.113635.100.1.2': 'apple_x509_basic',
        '1.2.840.113635.100.1.3': 'apple_ssl',
        '1.2.840.113635.100.1.4': 'apple_local_cert_gen',
        '1.2.840.113635.100.1.5': 'apple_csr_gen',
        '1.2.840.113635.100.1.6': 'apple_revocation_crl',
        '1.2.840.113635.100.1.7': 'apple_revocation_ocsp',
        '1.2.840.113635.100.1.8': 'apple_smime',
        '1.2.840.113635.100.1.9': 'apple_eap',
        '1.2.840.113635.100.1.10': 'apple_software_update_signing',
        '1.2.840.113635.100.1.11': 'apple_ipsec',
        '1.2.840.113635.100.1.12': 'apple_ichat',
        '1.2.840.113635.100.1.13': 'apple_resource_signing',
        '1.2.840.113635.100.1.14': 'apple_pkinit_client',
        '1.2.840.113635.100.1.15': 'apple_pkinit_server',
        '1.2.840.113635.100.1.16': 'apple_code_signing',
        '1.2.840.113635.100.1.17': 'apple_package_signing',
        '1.2.840.113635.100.1.18': 'apple_id_validation',
        '1.2.840.113635.100.1.20': 'apple_time_stamping',
        '1.2.840.113635.100.1.21': 'apple_revocation',
        '1.2.840.113635.100.1.22': 'apple_passbook_signing',
        '1.2.840.113635.100.1.23': 'apple_mobile_store',
        '1.2.840.113635.100.1.24': 'apple_escrow_service',
        '1.2.840.113635.100.1.25': 'apple_profile_signer',
        '1.2.840.113635.100.1.26': 'apple_qa_profile_signer',
        '1.2.840.113635.100.1.27': 'apple_test_mobile_store',
        '1.2.840.113635.100.1.28': 'apple_otapki_signer',
        '1.2.840.113635.100.1.29': 'apple_test_otapki_signer',
        '1.2.840.113625.100.1.30': 'apple_id_validation_record_signing_policy',
        '1.2.840.113625.100.1.31': 'apple_smp_encryption',
        '1.2.840.113625.100.1.32': 'apple_test_smp_encryption',
        '1.2.840.113635.100.1.33': 'apple_server_authentication',
        '1.2.840.113635.100.1.34': 'apple_pcs_escrow_service',
        # http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.201-2.pdf
        '2.16.840.1.101.3.6.8': 'piv_card_authentication',
        '2.16.840.1.101.3.6.7': 'piv_content_signing',
        # https://tools.ietf.org/html/rfc4556.html
        '1.3.6.1.5.2.3.4': 'pkinit_kpclientauth',
        '1.3.6.1.5.2.3.5': 'pkinit_kpkdc',
        # https://www.adobe.com/devnet-docs/acrobatetk/tools/DigSig/changes.html
        '1.2.840.113583.1.1.5': 'adobe_authentic_documents_trust',
        # https://www.idmanagement.gov/wp-content/uploads/sites/1171/uploads/fpki-pivi-cert-profiles.pdf
        '2.16.840.1.101.3.8.7': 'fpki_pivi_content_signing'
    }


class ExtKeyUsageSyntax(SequenceOf):
    _child_spec = KeyPurposeId


class AccessMethod(ObjectIdentifier):
    _map = {
        '1.3.6.1.5.5.7.48.1': 'ocsp',
        '1.3.6.1.5.5.7.48.2': 'ca_issuers',
        '1.3.6.1.5.5.7.48.3': 'time_stamping',
        '1.3.6.1.5.5.7.48.5': 'ca_repository',
    }


class AccessDescription(Sequence):
    _fields = [
        ('access_method', AccessMethod),
        ('access_location', GeneralName),
    ]


class AuthorityInfoAccessSyntax(SequenceOf):
    _child_spec = AccessDescription


class SubjectInfoAccessSyntax(SequenceOf):
    _child_spec = AccessDescription


# https://tools.ietf.org/html/rfc7633
class Features(SequenceOf):
    _child_spec = Integer


class EntrustVersionInfo(Sequence):
    _fields = [
        ('entrust_vers', GeneralString),
        ('entrust_info_flags', BitString)
    ]


class NetscapeCertificateType(BitString):
    _map = {
        0: 'ssl_client',
        1: 'ssl_server',
        2: 'email',
        3: 'object_signing',
        4: 'reserved',
        5: 'ssl_ca',
        6: 'email_ca',
        7: 'object_signing_ca',
    }


class Version(Integer):
    _map = {
        0: 'v1',
        1: 'v2',
        2: 'v3',
    }


class TPMSpecification(Sequence):
    _fields = [
        ('family', UTF8String),
        ('level', Integer),
        ('revision', Integer),
    ]


class SetOfTPMSpecification(SetOf):
    _child_spec = TPMSpecification


class TCGSpecificationVersion(Sequence):
    _fields = [
        ('major_version', Integer),
        ('minor_version', Integer),
        ('revision', Integer),
    ]


class TCGPlatformSpecification(Sequence):
    _fields = [
        ('version', TCGSpecificationVersion),
        ('platform_class', OctetString),
    ]


class SetOfTCGPlatformSpecification(SetOf):
    _child_spec = TCGPlatformSpecification


class EKGenerationType(Enumerated):
    _map = {
        0: 'internal',
        1: 'injected',
        2: 'internal_revocable',
        3: 'injected_revocable',
    }


class EKGenerationLocation(Enumerated):
    _map = {
        0: 'tpm_manufacturer',
        1: 'platform_manufacturer',
        2: 'ek_cert_signer',
    }


class EKCertificateGenerationLocation(Enumerated):
    _map = {
        0: 'tpm_manufacturer',
        1: 'platform_manufacturer',
        2: 'ek_cert_signer',
    }


class EvaluationAssuranceLevel(Enumerated):
    _map = {
        1: 'level1',
        2: 'level2',
        3: 'level3',
        4: 'level4',
        5: 'level5',
        6: 'level6',
        7: 'level7',
    }


class EvaluationStatus(Enumerated):
    _map = {
        0: 'designed_to_meet',
        1: 'evaluation_in_progress',
        2: 'evaluation_completed',
    }


class StrengthOfFunction(Enumerated):
    _map = {
        0: 'basic',
        1: 'medium',
        2: 'high',
    }


class URIReference(Sequence):
    _fields = [
        ('uniform_resource_identifier', IA5String),
        ('hash_algorithm', DigestAlgorithm, {'optional': True}),
        ('hash_value', BitString, {'optional': True}),
    ]


class CommonCriteriaMeasures(Sequence):
    _fields = [
        ('version', IA5String),
        ('assurance_level', EvaluationAssuranceLevel),
        ('evaluation_status', EvaluationStatus),
        ('plus', Boolean, {'default': False}),
        ('strengh_of_function', StrengthOfFunction, {'implicit': 0, 'optional': True}),
        ('profile_oid', ObjectIdentifier, {'implicit': 1, 'optional': True}),
        ('profile_url', URIReference, {'implicit': 2, 'optional': True}),
        ('target_oid', ObjectIdentifier, {'implicit': 3, 'optional': True}),
        ('target_uri', URIReference, {'implicit': 4, 'optional': True}),
    ]


class SecurityLevel(Enumerated):
    _map = {
        1: 'level1',
        2: 'level2',
        3: 'level3',
        4: 'level4',
    }


class FIPSLevel(Sequence):
    _fields = [
        ('version', IA5String),
        ('level', SecurityLevel),
        ('plus', Boolean, {'default': False}),
    ]


class TPMSecurityAssertions(Sequence):
    _fields = [
        ('version', Version, {'default': 'v1'}),
        ('field_upgradable', Boolean, {'default': False}),
        ('ek_generation_type', EKGenerationType, {'implicit': 0, 'optional': True}),
        ('ek_generation_location', EKGenerationLocation, {'implicit': 1, 'optional': True}),
        ('ek_certificate_generation_location', EKCertificateGenerationLocation, {'implicit': 2, 'optional': True}),
        ('cc_info', CommonCriteriaMeasures, {'implicit': 3, 'optional': True}),
        ('fips_level', FIPSLevel, {'implicit': 4, 'optional': True}),
        ('iso_9000_certified', Boolean, {'implicit': 5, 'default': False}),
        ('iso_9000_uri', IA5String, {'optional': True}),
    ]


class SetOfTPMSecurityAssertions(SetOf):
    _child_spec = TPMSecurityAssertions


class SubjectDirectoryAttributeId(ObjectIdentifier):
    _map = {
        # https://tools.ietf.org/html/rfc2256#page-11
        '2.5.4.52': 'supported_algorithms',
        # https://www.trustedcomputinggroup.org/wp-content/uploads/Credential_Profile_EK_V2.0_R14_published.pdf
        '2.23.133.2.16': 'tpm_specification',
        '2.23.133.2.17': 'tcg_platform_specification',
        '2.23.133.2.18': 'tpm_security_assertions',
        # https://tools.ietf.org/html/rfc3739#page-18
        '1.3.6.1.5.5.7.9.1': 'pda_date_of_birth',
        '1.3.6.1.5.5.7.9.2': 'pda_place_of_birth',
        '1.3.6.1.5.5.7.9.3': 'pda_gender',
        '1.3.6.1.5.5.7.9.4': 'pda_country_of_citizenship',
        '1.3.6.1.5.5.7.9.5': 'pda_country_of_residence',
        # https://holtstrom.com/michael/tools/asn1decoder.php
        '1.2.840.113533.7.68.29': 'entrust_user_role',
    }


class SetOfGeneralizedTime(SetOf):
    _child_spec = GeneralizedTime


class SetOfDirectoryString(SetOf):
    _child_spec = DirectoryString


class SetOfPrintableString(SetOf):
    _child_spec = PrintableString


class SupportedAlgorithm(Sequence):
    _fields = [
        ('algorithm_identifier', AnyAlgorithmIdentifier),
        ('intended_usage', KeyUsage, {'explicit': 0, 'optional': True}),
        ('intended_certificate_policies', CertificatePolicies, {'explicit': 1, 'optional': True}),
    ]


class SetOfSupportedAlgorithm(SetOf):
    _child_spec = SupportedAlgorithm


class SubjectDirectoryAttribute(Sequence):
    _fields = [
        ('type', SubjectDirectoryAttributeId),
        ('values', Any),
    ]

    _oid_pair = ('type', 'values')
    _oid_specs = {
        'supported_algorithms': SetOfSupportedAlgorithm,
        'tpm_specification': SetOfTPMSpecification,
        'tcg_platform_specification': SetOfTCGPlatformSpecification,
        'tpm_security_assertions': SetOfTPMSecurityAssertions,
        'pda_date_of_birth': SetOfGeneralizedTime,
        'pda_place_of_birth': SetOfDirectoryString,
        'pda_gender': SetOfPrintableString,
        'pda_country_of_citizenship': SetOfPrintableString,
        'pda_country_of_residence': SetOfPrintableString,
    }

    def _values_spec(self):
        pass

    _spec_callbacks = {
        'values': _values_spec
    }


class SubjectDirectoryAttributes(SequenceOf):
    _child_spec = SubjectDirectoryAttribute


class ExtensionId(ObjectIdentifier):
    _map = {
        '2.5.29.9': 'subject_directory_attributes',
        '2.5.29.14': 'key_identifier',
        '2.5.29.15': 'key_usage',
        '2.5.29.16': 'private_key_usage_period',
        '2.5.29.17': 'subject_alt_name',
        '2.5.29.18': 'issuer_alt_name',
        '2.5.29.19': 'basic_constraints',
        '2.5.29.30': 'name_constraints',
        '2.5.29.31': 'crl_distribution_points',
        '2.5.29.32': 'certificate_policies',
        '2.5.29.33': 'policy_mappings',
        '2.5.29.35': 'authority_key_identifier',
        '2.5.29.36': 'policy_constraints',
        '2.5.29.37': 'extended_key_usage',
        '2.5.29.46': 'freshest_crl',
        '2.5.29.54': 'inhibit_any_policy',
        '1.3.6.1.5.5.7.1.1': 'authority_information_access',
        '1.3.6.1.5.5.7.1.11': 'subject_information_access',
        # https://tools.ietf.org/html/rfc7633
        '1.3.6.1.5.5.7.1.24': 'tls_feature',
        '1.3.6.1.5.5.7.48.1.5': 'ocsp_no_check',
        '1.2.840.113533.7.65.0': 'entrust_version_extension',
        '2.16.840.1.113730.1.1': 'netscape_certificate_type',
        # https://tools.ietf.org/html/rfc6962.html#page-14
        '1.3.6.1.4.1.11129.2.4.2': 'signed_certificate_timestamp_list',
        # https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-wcce/3aec3e50-511a-42f9-a5d5-240af503e470
        '1.3.6.1.4.1.311.20.2': 'microsoft_enroll_certtype',
    }


class Extension(Sequence):
    _fields = [
        ('extn_id', ExtensionId),
        ('critical', Boolean, {'default': False}),
        ('extn_value', ParsableOctetString),
    ]

    _oid_pair = ('extn_id', 'extn_value')
    _oid_specs = {
        'subject_directory_attributes': SubjectDirectoryAttributes,
        'key_identifier': OctetString,
        'key_usage': KeyUsage,
        'private_key_usage_period': PrivateKeyUsagePeriod,
        'subject_alt_name': GeneralNames,
        'issuer_alt_name': GeneralNames,
        'basic_constraints': BasicConstraints,
        'name_constraints': NameConstraints,
        'crl_distribution_points': CRLDistributionPoints,
        'certificate_policies': CertificatePolicies,
        'policy_mappings': PolicyMappings,
        'authority_key_identifier': AuthorityKeyIdentifier,
        'policy_constraints': PolicyConstraints,
        'extended_key_usage': ExtKeyUsageSyntax,
        'freshest_crl': CRLDistributionPoints,
        'inhibit_any_policy': Integer,
        'authority_information_access': AuthorityInfoAccessSyntax,
        'subject_information_access': SubjectInfoAccessSyntax,
        'tls_feature': Features,
        'ocsp_no_check': Null,
        'entrust_version_extension': EntrustVersionInfo,
        'netscape_certificate_type': NetscapeCertificateType,
        'signed_certificate_timestamp_list': OctetString,
        # Not UTF8String as Microsofts docs claim, see:
        # https://www.alvestrand.no/objectid/1.3.6.1.4.1.311.20.2.html
        'microsoft_enroll_certtype': BMPString,
    }


class Extensions(SequenceOf):
    _child_spec = Extension


class TbsCertificate(Sequence):
    _fields = [
        ('version', Version, {'explicit': 0, 'default': 'v1'}),
        ('serial_number', Integer),
        ('signature', SignedDigestAlgorithm),
        ('issuer', Name),
        ('validity', Validity),
        ('subject', Name),
        ('subject_public_key_info', PublicKeyInfo),
        ('issuer_unique_id', OctetBitString, {'implicit': 1, 'optional': True}),
        ('subject_unique_id', OctetBitString, {'implicit': 2, 'optional': True}),
        ('extensions', Extensions, {'explicit': 3, 'optional': True}),
    ]


class Certificate(Sequence):
    _fields = [
        ('tbs_certificate', TbsCertificate),
        ('signature_algorithm', SignedDigestAlgorithm),
        ('signature_value', OctetBitString),
    ]

    _processed_extensions = False
    _critical_extensions = None
    _subject_directory_attributes_value = None
    _key_identifier_value = None
    _key_usage_value = None
    _subject_alt_name_value = None
    _issuer_alt_name_value = None
    _basic_constraints_value = None
    _name_constraints_value = None
    _crl_distribution_points_value = None
    _certificate_policies_value = None
    _policy_mappings_value = None
    _authority_key_identifier_value = None
    _policy_constraints_value = None
    _freshest_crl_value = None
    _inhibit_any_policy_value = None
    _extended_key_usage_value = None
    _authority_information_access_value = None
    _subject_information_access_value = None
    _private_key_usage_period_value = None
    _tls_feature_value = None
    _ocsp_no_check_value = None
    _issuer_serial = None
    _authority_issuer_serial = False
    _crl_distribution_points = None
    _delta_crl_distribution_points = None
    _valid_domains = None
    _valid_ips = None
    _self_issued = None
    _self_signed = None
    _sha1 = None
    _sha256 = None

    def _set_extensions(self):
        """
        Sets common named extensions to private attributes and creates a list
        of critical extensions
        """
        pass

    @property
    def critical_extensions(self):
        """
        Returns a set of the names (or OID if not a known extension) of the
        extensions marked as critical

        :return:
            A set of unicode strings
        """
        pass

    @property
    def private_key_usage_period_value(self):
        """
        This extension is used to constrain the period over which the subject
        private key may be used

        :return:
            None or a PrivateKeyUsagePeriod object
        """
        pass

    @property
    def subject_directory_attributes_value(self):
        """
        This extension is used to contain additional identification attributes
        about the subject.

        :return:
            None or a SubjectDirectoryAttributes object
        """
        pass

    @property
    def key_identifier_value(self):
        """
        This extension is used to help in creating certificate validation paths.
        It contains an identifier that should generally, but is not guaranteed
        to, be unique.

        :return:
            None or an OctetString object
        """
        pass

    @property
    def key_usage_value(self):
        """
        This extension is used to define the purpose of the public key
        contained within the certificate.

        :return:
            None or a KeyUsage
        """
        pass

    @property
    def subject_alt_name_value(self):
        """
        This extension allows for additional names to be associate with the
        subject of the certificate. While it may contain a whole host of
        possible names, it is usually used to allow certificates to be used
        with multiple different domain names.

        :return:
            None or a GeneralNames object
        """
        pass

    @property
    def issuer_alt_name_value(self):
        """
        This extension allows associating one or more alternative names with
        the issuer of the certificate.

        :return:
            None or an x509.GeneralNames object
        """
        pass

    @property
    def basic_constraints_value(self):
        """
        This extension is used to determine if the subject of the certificate
        is a CA, and if so, what the maximum number of intermediate CA certs
        after this are, before an end-entity certificate is found.

        :return:
            None or a BasicConstraints object
        """
        pass

    @property
    def name_constraints_value(self):
        """
        This extension is used in CA certificates, and is used to limit the
        possible names of certificates issued.

        :return:
            None or a NameConstraints object
        """
        pass

    @property
    def crl_distribution_points_value(self):
        """
        This extension is used to help in locating the CRL for this certificate.

        :return:
            None or a CRLDistributionPoints object
            extension
        """
        pass

    @property
    def certificate_policies_value(self):
        """
        This extension defines policies in CA certificates under which
        certificates may be issued. In end-entity certificates, the inclusion
        of a policy indicates the issuance of the certificate follows the
        policy.

        :return:
            None or a CertificatePolicies object
        """
        pass

    @property
    def policy_mappings_value(self):
        """
        This extension allows mapping policy OIDs to other OIDs. This is used
        to allow different policies to be treated as equivalent in the process
        of validation.

        :return:
            None or a PolicyMappings object
        """
        pass

    @property
    def authority_key_identifier_value(self):
        """
        This extension helps in identifying the public key with which to
        validate the authenticity of the certificate.

        :return:
            None or an AuthorityKeyIdentifier object
        """
        pass

    @property
    def policy_constraints_value(self):
        """
        This extension is used to control if policy mapping is allowed and
        when policies are required.

        :return:
            None or a PolicyConstraints object
        """
        pass

    @property
    def freshest_crl_value(self):
        """
        This extension is used to help locate any available delta CRLs

        :return:
            None or an CRLDistributionPoints object
        """
        pass

    @property
    def inhibit_any_policy_value(self):
        """
        This extension is used to prevent mapping of the any policy to
        specific requirements

        :return:
            None or a Integer object
        """
        pass

    @property
    def extended_key_usage_value(self):
        """
        This extension is used to define additional purposes for the public key
        beyond what is contained in the basic constraints.

        :return:
            None or an ExtKeyUsageSyntax object
        """
        pass

    @property
    def authority_information_access_value(self):
        """
        This extension is used to locate the CA certificate used to sign this
        certificate, or the OCSP responder for this certificate.

        :return:
            None or an AuthorityInfoAccessSyntax object
        """
        pass

    @property
    def subject_information_access_value(self):
        """
        This extension is used to access information about the subject of this
        certificate.

        :return:
            None or a SubjectInfoAccessSyntax object
        """
        pass

    @property
    def tls_feature_value(self):
        """
        This extension is used to list the TLS features a server must respond
        with if a client initiates a request supporting them.

        :return:
            None or a Features object
        """
        pass

    @property
    def ocsp_no_check_value(self):
        """
        This extension is used on certificates of OCSP responders, indicating
        that revocation information for the certificate should never need to
        be verified, thus preventing possible loops in path validation.

        :return:
            None or a Null object (if present)
        """
        pass

    @property
    def signature(self):
        """
        :return:
            A byte string of the signature
        """
        pass

    @property
    def signature_algo(self):
        """
        :return:
            A unicode string of "rsassa_pkcs1v15", "rsassa_pss", "dsa", "ecdsa"
        """
        pass

    @property
    def hash_algo(self):
        """
        :return:
            A unicode string of "md2", "md5", "sha1", "sha224", "sha256",
            "sha384", "sha512", "sha512_224", "sha512_256"
        """
        pass

    @property
    def public_key(self):
        """
        :return:
            The PublicKeyInfo object for this certificate
        """
        pass

    @property
    def subject(self):
        """
        :return:
            The Name object for the subject of this certificate
        """
        pass

    @property
    def issuer(self):
        """
        :return:
            The Name object for the issuer of this certificate
        """
        pass

    @property
    def serial_number(self):
        """
        :return:
            An integer of the certificate's serial number
        """
        pass

    @property
    def key_identifier(self):
        """
        :return:
            None or a byte string of the certificate's key identifier from the
            key identifier extension
        """
        pass

    @property
    def issuer_serial(self):
        """
        :return:
            A byte string of the SHA-256 hash of the issuer concatenated with
            the ascii character ":", concatenated with the serial number as
            an ascii string
        """
        pass

    @property
    def not_valid_after(self):
        """
        :return:
            A datetime of latest time when the certificate is still valid
        """
        pass

    @property
    def not_valid_before(self):
        """
        :return:
            A datetime of the earliest time when the certificate is valid
        """
        pass

    @property
    def authority_key_identifier(self):
        """
        :return:
            None or a byte string of the key_identifier from the authority key
            identifier extension
        """
        pass

    @property
    def authority_issuer_serial(self):
        """
        :return:
            None or a byte string of the SHA-256 hash of the isser from the
            authority key identifier extension concatenated with the ascii
            character ":", concatenated with the serial number from the
            authority key identifier extension as an ascii string
        """
        pass

    @property
    def crl_distribution_points(self):
        """
        Returns complete CRL URLs - does not include delta CRLs

        :return:
            A list of zero or more DistributionPoint objects
        """
        pass

    @property
    def delta_crl_distribution_points(self):
        """
        Returns delta CRL URLs - does not include complete CRLs

        :return:
            A list of zero or more DistributionPoint objects
        """
        pass

    def _get_http_crl_distribution_points(self, crl_distribution_points):
        """
        Fetches the DistributionPoint object for non-relative, HTTP CRLs
        referenced by the certificate

        :param crl_distribution_points:
            A CRLDistributionPoints object to grab the DistributionPoints from

        :return:
            A list of zero or more DistributionPoint objects
        """
        pass

    @property
    def ocsp_urls(self):
        """
        :return:
            A list of zero or more unicode strings of the OCSP URLs for this
            cert
        """
        pass

    @property
    def valid_domains(self):
        """
        :return:
            A list of unicode strings of valid domain names for the certificate.
            Wildcard certificates will have a domain in the form: *.example.com
        """
        pass

    @property
    def valid_ips(self):
        """
        :return:
            A list of unicode strings of valid IP addresses for the certificate
        """
        pass

    @property
    def ca(self):
        """
        :return;
            A boolean - if the certificate is marked as a CA
        """
        pass

    @property
    def max_path_length(self):
        """
        :return;
            None or an integer of the maximum path length
        """
        pass

    @property
    def self_issued(self):
        """
        :return:
            A boolean - if the certificate is self-issued, as defined by RFC
            5280
        """
        pass

    @property
    def self_signed(self):
        """
        :return:
            A unicode string of "no" or "maybe". The "maybe" result will
            be returned if the certificate issuer and subject are the same.
            If a key identifier and authority key identifier are present,
            they will need to match otherwise "no" will be returned.

            To verify is a certificate is truly self-signed, the signature
            will need to be verified. See the certvalidator package for
            one possible solution.
        """
        pass

    @property
    def sha1(self):
        """
        :return:
            The SHA-1 hash of the DER-encoded bytes of this complete certificate
        """
        pass

    @property
    def sha1_fingerprint(self):
        """
        :return:
            A unicode string of the SHA-1 hash, formatted using hex encoding
            with a space between each pair of characters, all uppercase
        """
        pass

    @property
    def sha256(self):
        """
        :return:
            The SHA-256 hash of the DER-encoded bytes of this complete
            certificate
        """
        pass

    @property
    def sha256_fingerprint(self):
        """
        :return:
            A unicode string of the SHA-256 hash, formatted using hex encoding
            with a space between each pair of characters, all uppercase
        """
        pass

    def is_valid_domain_ip(self, domain_ip):
        """
        Check if a domain name or IP address is valid according to the
        certificate

        :param domain_ip:
            A unicode string of a domain name or IP address

        :return:
            A boolean - if the domain or IP is valid for the certificate
        """
        pass

    def _is_wildcard_domain(self, domain):
        """
        Checks if a domain is a valid wildcard according to
        https://tools.ietf.org/html/rfc6125#section-6.4.3

        :param domain:
            A unicode string of the domain name, where any U-labels from an IDN
            have been converted to A-labels

        :return:
            A boolean - if the domain is a valid wildcard domain
        """
        pass

    def _is_wildcard_match(self, domain_labels, valid_domain_labels):
        """
        Determines if the labels in a domain are a match for labels from a
        wildcard valid domain name

        :param domain_labels:
            A list of unicode strings, with A-label form for IDNs, of the labels
            in the domain name to check

        :param valid_domain_labels:
            A list of unicode strings, with A-label form for IDNs, of the labels
            in a wildcard domain pattern

        :return:
            A boolean - if the domain matches the valid domain
        """
        pass


# The structures are taken from the OpenSSL source file x_x509a.c, and specify
# extra information that is added to X.509 certificates to store trust
# information about the certificate.

class KeyPurposeIdentifiers(SequenceOf):
    _child_spec = KeyPurposeId


class SequenceOfAlgorithmIdentifiers(SequenceOf):
    _child_spec = AlgorithmIdentifier


class CertificateAux(Sequence):
    _fields = [
        ('trust', KeyPurposeIdentifiers, {'optional': True}),
        ('reject', KeyPurposeIdentifiers, {'implicit': 0, 'optional': True}),
        ('alias', UTF8String, {'optional': True}),
        ('keyid', OctetString, {'optional': True}),
        ('other', SequenceOfAlgorithmIdentifiers, {'implicit': 1, 'optional': True}),
    ]


class TrustedCertificate(Concat):
    _child_specs = [Certificate, CertificateAux]
