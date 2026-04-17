# coding: utf-8

"""
ASN.1 type classes for various algorithms using in various aspects of public
key cryptography. Exports the following items:

 - AlgorithmIdentifier()
 - AnyAlgorithmIdentifier()
 - DigestAlgorithm()
 - DigestInfo()
 - DSASignature()
 - EncryptionAlgorithm()
 - HmacAlgorithm()
 - KdfAlgorithm()
 - Pkcs5MacAlgorithm()
 - SignedDigestAlgorithm()

Other type classes are defined that help compose the types listed above.
"""

from __future__ import unicode_literals, division, absolute_import, print_function

from ._errors import unwrap
from ._int import fill_width
from .util import int_from_bytes, int_to_bytes
from .core import (
    Any,
    Choice,
    Integer,
    Null,
    ObjectIdentifier,
    OctetString,
    Sequence,
    Void,
)


# Structures and OIDs in this file are pulled from
# https://tools.ietf.org/html/rfc3279, https://tools.ietf.org/html/rfc4055,
# https://tools.ietf.org/html/rfc5758, https://tools.ietf.org/html/rfc7292,
# http://www.emc.com/collateral/white-papers/h11302-pkcs5v2-1-password-based-cryptography-standard-wp.pdf

class AlgorithmIdentifier(Sequence):
    _fields = [
        ('algorithm', ObjectIdentifier),
        ('parameters', Any, {'optional': True}),
    ]


class _ForceNullParameters(object):
    """
    Various structures based on AlgorithmIdentifier require that the parameters
    field be core.Null() for certain OIDs. This mixin ensures that happens.
    """

    # The following attribute, plus the parameters spec callback and custom
    # __setitem__ are all to handle a situation where parameters should not be
    # optional and must be Null for certain OIDs. More info at
    # https://tools.ietf.org/html/rfc4055#page-15 and
    # https://tools.ietf.org/html/rfc4055#section-2.1
    _null_algos = set([
        '1.2.840.113549.1.1.1',    # rsassa_pkcs1v15 / rsaes_pkcs1v15 / rsa
        '1.2.840.113549.1.1.11',   # sha256_rsa
        '1.2.840.113549.1.1.12',   # sha384_rsa
        '1.2.840.113549.1.1.13',   # sha512_rsa
        '1.2.840.113549.1.1.14',   # sha224_rsa
        '1.3.14.3.2.26',           # sha1
        '2.16.840.1.101.3.4.2.4',  # sha224
        '2.16.840.1.101.3.4.2.1',  # sha256
        '2.16.840.1.101.3.4.2.2',  # sha384
        '2.16.840.1.101.3.4.2.3',  # sha512
    ])

    def _parameters_spec(self):
        pass

    _spec_callbacks = {
        'parameters': _parameters_spec
    }

    # We have to override this since the spec callback uses the value of
    # algorithm to determine the parameter spec, however default values are
    # assigned before setting a field, so a default value can't be based on
    # another field value (unless it is a default also). Thus we have to
    # manually check to see if the algorithm was set and parameters is unset,
    # and then fix the value as appropriate.
    def __setitem__(self, key, value):
        res = super(_ForceNullParameters, self).__setitem__(key, value)
        if key != 'algorithm':
            return res
        if self['algorithm'].dotted not in self._null_algos:
            return res
        if self['parameters'].__class__ != Void:
            return res
        self['parameters'] = Null()
        return res


class HmacAlgorithmId(ObjectIdentifier):
    _map = {
        '1.3.14.3.2.10': 'des_mac',
        '1.2.840.113549.2.7': 'sha1',
        '1.2.840.113549.2.8': 'sha224',
        '1.2.840.113549.2.9': 'sha256',
        '1.2.840.113549.2.10': 'sha384',
        '1.2.840.113549.2.11': 'sha512',
        '1.2.840.113549.2.12': 'sha512_224',
        '1.2.840.113549.2.13': 'sha512_256',
        '2.16.840.1.101.3.4.2.13': 'sha3_224',
        '2.16.840.1.101.3.4.2.14': 'sha3_256',
        '2.16.840.1.101.3.4.2.15': 'sha3_384',
        '2.16.840.1.101.3.4.2.16': 'sha3_512',
    }


class HmacAlgorithm(Sequence):
    _fields = [
        ('algorithm', HmacAlgorithmId),
        ('parameters', Any, {'optional': True}),
    ]


class DigestAlgorithmId(ObjectIdentifier):
    _map = {
        '1.2.840.113549.2.2': 'md2',
        '1.2.840.113549.2.5': 'md5',
        '1.3.14.3.2.26': 'sha1',
        '2.16.840.1.101.3.4.2.4': 'sha224',
        '2.16.840.1.101.3.4.2.1': 'sha256',
        '2.16.840.1.101.3.4.2.2': 'sha384',
        '2.16.840.1.101.3.4.2.3': 'sha512',
        '2.16.840.1.101.3.4.2.5': 'sha512_224',
        '2.16.840.1.101.3.4.2.6': 'sha512_256',
        '2.16.840.1.101.3.4.2.7': 'sha3_224',
        '2.16.840.1.101.3.4.2.8': 'sha3_256',
        '2.16.840.1.101.3.4.2.9': 'sha3_384',
        '2.16.840.1.101.3.4.2.10': 'sha3_512',
        '2.16.840.1.101.3.4.2.11': 'shake128',
        '2.16.840.1.101.3.4.2.12': 'shake256',
        '2.16.840.1.101.3.4.2.17': 'shake128_len',
        '2.16.840.1.101.3.4.2.18': 'shake256_len',
    }


class DigestAlgorithm(_ForceNullParameters, Sequence):
    _fields = [
        ('algorithm', DigestAlgorithmId),
        ('parameters', Any, {'optional': True}),
    ]


# This structure is what is signed with a SignedDigestAlgorithm
class DigestInfo(Sequence):
    _fields = [
        ('digest_algorithm', DigestAlgorithm),
        ('digest', OctetString),
    ]


class MaskGenAlgorithmId(ObjectIdentifier):
    _map = {
        '1.2.840.113549.1.1.8': 'mgf1',
    }


class MaskGenAlgorithm(Sequence):
    _fields = [
        ('algorithm', MaskGenAlgorithmId),
        ('parameters', Any, {'optional': True}),
    ]

    _oid_pair = ('algorithm', 'parameters')
    _oid_specs = {
        'mgf1': DigestAlgorithm
    }


class TrailerField(Integer):
    _map = {
        1: 'trailer_field_bc',
    }


class RSASSAPSSParams(Sequence):
    _fields = [
        (
            'hash_algorithm',
            DigestAlgorithm,
            {
                'explicit': 0,
                'default': {'algorithm': 'sha1'},
            }
        ),
        (
            'mask_gen_algorithm',
            MaskGenAlgorithm,
            {
                'explicit': 1,
                'default': {
                    'algorithm': 'mgf1',
                    'parameters': {'algorithm': 'sha1'},
                },
            }
        ),
        (
            'salt_length',
            Integer,
            {
                'explicit': 2,
                'default': 20,
            }
        ),
        (
            'trailer_field',
            TrailerField,
            {
                'explicit': 3,
                'default': 'trailer_field_bc',
            }
        ),
    ]


class SignedDigestAlgorithmId(ObjectIdentifier):
    _map = {
        '1.3.14.3.2.3': 'md5_rsa',
        '1.3.14.3.2.29': 'sha1_rsa',
        '1.3.14.7.2.3.1': 'md2_rsa',
        '1.2.840.113549.1.1.2': 'md2_rsa',
        '1.2.840.113549.1.1.4': 'md5_rsa',
        '1.2.840.113549.1.1.5': 'sha1_rsa',
        '1.2.840.113549.1.1.14': 'sha224_rsa',
        '1.2.840.113549.1.1.11': 'sha256_rsa',
        '1.2.840.113549.1.1.12': 'sha384_rsa',
        '1.2.840.113549.1.1.13': 'sha512_rsa',
        '1.2.840.113549.1.1.10': 'rsassa_pss',
        '1.2.840.10040.4.3': 'sha1_dsa',
        '1.3.14.3.2.13': 'sha1_dsa',
        '1.3.14.3.2.27': 'sha1_dsa',
        '2.16.840.1.101.3.4.3.1': 'sha224_dsa',
        '2.16.840.1.101.3.4.3.2': 'sha256_dsa',
        '1.2.840.10045.4.1': 'sha1_ecdsa',
        '1.2.840.10045.4.3.1': 'sha224_ecdsa',
        '1.2.840.10045.4.3.2': 'sha256_ecdsa',
        '1.2.840.10045.4.3.3': 'sha384_ecdsa',
        '1.2.840.10045.4.3.4': 'sha512_ecdsa',
        '2.16.840.1.101.3.4.3.9': 'sha3_224_ecdsa',
        '2.16.840.1.101.3.4.3.10': 'sha3_256_ecdsa',
        '2.16.840.1.101.3.4.3.11': 'sha3_384_ecdsa',
        '2.16.840.1.101.3.4.3.12': 'sha3_512_ecdsa',
        # For when the digest is specified elsewhere in a Sequence
        '1.2.840.113549.1.1.1': 'rsassa_pkcs1v15',
        '1.2.840.10040.4.1': 'dsa',
        '1.2.840.10045.4': 'ecdsa',
        # RFC 8410 -- https://tools.ietf.org/html/rfc8410
        '1.3.101.112': 'ed25519',
        '1.3.101.113': 'ed448',
    }

    _reverse_map = {
        'dsa': '1.2.840.10040.4.1',
        'ecdsa': '1.2.840.10045.4',
        'md2_rsa': '1.2.840.113549.1.1.2',
        'md5_rsa': '1.2.840.113549.1.1.4',
        'rsassa_pkcs1v15': '1.2.840.113549.1.1.1',
        'rsassa_pss': '1.2.840.113549.1.1.10',
        'sha1_dsa': '1.2.840.10040.4.3',
        'sha1_ecdsa': '1.2.840.10045.4.1',
        'sha1_rsa': '1.2.840.113549.1.1.5',
        'sha224_dsa': '2.16.840.1.101.3.4.3.1',
        'sha224_ecdsa': '1.2.840.10045.4.3.1',
        'sha224_rsa': '1.2.840.113549.1.1.14',
        'sha256_dsa': '2.16.840.1.101.3.4.3.2',
        'sha256_ecdsa': '1.2.840.10045.4.3.2',
        'sha256_rsa': '1.2.840.113549.1.1.11',
        'sha384_ecdsa': '1.2.840.10045.4.3.3',
        'sha384_rsa': '1.2.840.113549.1.1.12',
        'sha512_ecdsa': '1.2.840.10045.4.3.4',
        'sha512_rsa': '1.2.840.113549.1.1.13',
        'sha3_224_ecdsa': '2.16.840.1.101.3.4.3.9',
        'sha3_256_ecdsa': '2.16.840.1.101.3.4.3.10',
        'sha3_384_ecdsa': '2.16.840.1.101.3.4.3.11',
        'sha3_512_ecdsa': '2.16.840.1.101.3.4.3.12',
        'ed25519': '1.3.101.112',
        'ed448': '1.3.101.113',
    }


class SignedDigestAlgorithm(_ForceNullParameters, Sequence):
    _fields = [
        ('algorithm', SignedDigestAlgorithmId),
        ('parameters', Any, {'optional': True}),
    ]

    _oid_pair = ('algorithm', 'parameters')
    _oid_specs = {
        'rsassa_pss': RSASSAPSSParams,
    }

    @property
    def signature_algo(self):
        """
        :return:
            A unicode string of "rsassa_pkcs1v15", "rsassa_pss", "dsa",
            "ecdsa", "ed25519" or "ed448"
        """
        pass

    @property
    def hash_algo(self):
        """
        :return:
            A unicode string of "md2", "md5", "sha1", "sha224", "sha256",
            "sha384", "sha512", "sha512_224", "sha512_256" or "shake256"
        """
        pass


class Pbkdf2Salt(Choice):
    _alternatives = [
        ('specified', OctetString),
        ('other_source', AlgorithmIdentifier),
    ]


class Pbkdf2Params(Sequence):
    _fields = [
        ('salt', Pbkdf2Salt),
        ('iteration_count', Integer),
        ('key_length', Integer, {'optional': True}),
        ('prf', HmacAlgorithm, {'default': {'algorithm': 'sha1'}}),
    ]


class KdfAlgorithmId(ObjectIdentifier):
    _map = {
        '1.2.840.113549.1.5.12': 'pbkdf2'
    }


class KdfAlgorithm(Sequence):
    _fields = [
        ('algorithm', KdfAlgorithmId),
        ('parameters', Any, {'optional': True}),
    ]
    _oid_pair = ('algorithm', 'parameters')
    _oid_specs = {
        'pbkdf2': Pbkdf2Params
    }


class DHParameters(Sequence):
    """
    Original Name: DHParameter
    Source: ftp://ftp.rsasecurity.com/pub/pkcs/ascii/pkcs-3.asc section 9
    """

    _fields = [
        ('p', Integer),
        ('g', Integer),
        ('private_value_length', Integer, {'optional': True}),
    ]


class KeyExchangeAlgorithmId(ObjectIdentifier):
    _map = {
        '1.2.840.113549.1.3.1': 'dh',
    }


class KeyExchangeAlgorithm(Sequence):
    _fields = [
        ('algorithm', KeyExchangeAlgorithmId),
        ('parameters', Any, {'optional': True}),
    ]
    _oid_pair = ('algorithm', 'parameters')
    _oid_specs = {
        'dh': DHParameters,
    }


class Rc2Params(Sequence):
    _fields = [
        ('rc2_parameter_version', Integer, {'optional': True}),
        ('iv', OctetString),
    ]


class Rc5ParamVersion(Integer):
    _map = {
        16: 'v1-0'
    }


class Rc5Params(Sequence):
    _fields = [
        ('version', Rc5ParamVersion),
        ('rounds', Integer),
        ('block_size_in_bits', Integer),
        ('iv', OctetString, {'optional': True}),
    ]


class Pbes1Params(Sequence):
    _fields = [
        ('salt', OctetString),
        ('iterations', Integer),
    ]


class CcmParams(Sequence):
    # https://tools.ietf.org/html/rfc5084
    # aes_ICVlen: 4 | 6 | 8 | 10 | 12 | 14 | 16
    _fields = [
        ('aes_nonce', OctetString),
        ('aes_icvlen', Integer),
    ]


class PSourceAlgorithmId(ObjectIdentifier):
    _map = {
        '1.2.840.113549.1.1.9': 'p_specified',
    }


class PSourceAlgorithm(Sequence):
    _fields = [
        ('algorithm', PSourceAlgorithmId),
        ('parameters', Any, {'optional': True}),
    ]

    _oid_pair = ('algorithm', 'parameters')
    _oid_specs = {
        'p_specified': OctetString
    }


class RSAESOAEPParams(Sequence):
    _fields = [
        (
            'hash_algorithm',
            DigestAlgorithm,
            {
                'explicit': 0,
                'default': {'algorithm': 'sha1'}
            }
        ),
        (
            'mask_gen_algorithm',
            MaskGenAlgorithm,
            {
                'explicit': 1,
                'default': {
                    'algorithm': 'mgf1',
                    'parameters': {'algorithm': 'sha1'}
                }
            }
        ),
        (
            'p_source_algorithm',
            PSourceAlgorithm,
            {
                'explicit': 2,
                'default': {
                    'algorithm': 'p_specified',
                    'parameters': b''
                }
            }
        ),
    ]


class DSASignature(Sequence):
    """
    An ASN.1 class for translating between the OS crypto library's
    representation of an (EC)DSA signature and the ASN.1 structure that is part
    of various RFCs.

    Original Name: DSS-Sig-Value
    Source: https://tools.ietf.org/html/rfc3279#section-2.2.2
    """

    _fields = [
        ('r', Integer),
        ('s', Integer),
    ]

    @classmethod
    def from_p1363(cls, data):
        """
        Reads a signature from a byte string encoding according to IEEE P1363,
        which is used by Microsoft's BCryptSignHash() function.

        :param data:
            A byte string from BCryptSignHash()

        :return:
            A DSASignature object
        """
        pass

    def to_p1363(self):
        """
        Dumps a signature to a byte string compatible with Microsoft's
        BCryptVerifySignature() function.

        :return:
            A byte string compatible with BCryptVerifySignature()
        """
        pass


class EncryptionAlgorithmId(ObjectIdentifier):
    _map = {
        '1.3.14.3.2.7': 'des',
        '1.2.840.113549.3.7': 'tripledes_3key',
        '1.2.840.113549.3.2': 'rc2',
        '1.2.840.113549.3.4': 'rc4',
        '1.2.840.113549.3.9': 'rc5',
        # From http://csrc.nist.gov/groups/ST/crypto_apps_infra/csor/algorithms.html#AES
        '2.16.840.1.101.3.4.1.1': 'aes128_ecb',
        '2.16.840.1.101.3.4.1.2': 'aes128_cbc',
        '2.16.840.1.101.3.4.1.3': 'aes128_ofb',
        '2.16.840.1.101.3.4.1.4': 'aes128_cfb',
        '2.16.840.1.101.3.4.1.5': 'aes128_wrap',
        '2.16.840.1.101.3.4.1.6': 'aes128_gcm',
        '2.16.840.1.101.3.4.1.7': 'aes128_ccm',
        '2.16.840.1.101.3.4.1.8': 'aes128_wrap_pad',
        '2.16.840.1.101.3.4.1.21': 'aes192_ecb',
        '2.16.840.1.101.3.4.1.22': 'aes192_cbc',
        '2.16.840.1.101.3.4.1.23': 'aes192_ofb',
        '2.16.840.1.101.3.4.1.24': 'aes192_cfb',
        '2.16.840.1.101.3.4.1.25': 'aes192_wrap',
        '2.16.840.1.101.3.4.1.26': 'aes192_gcm',
        '2.16.840.1.101.3.4.1.27': 'aes192_ccm',
        '2.16.840.1.101.3.4.1.28': 'aes192_wrap_pad',
        '2.16.840.1.101.3.4.1.41': 'aes256_ecb',
        '2.16.840.1.101.3.4.1.42': 'aes256_cbc',
        '2.16.840.1.101.3.4.1.43': 'aes256_ofb',
        '2.16.840.1.101.3.4.1.44': 'aes256_cfb',
        '2.16.840.1.101.3.4.1.45': 'aes256_wrap',
        '2.16.840.1.101.3.4.1.46': 'aes256_gcm',
        '2.16.840.1.101.3.4.1.47': 'aes256_ccm',
        '2.16.840.1.101.3.4.1.48': 'aes256_wrap_pad',
        # From PKCS#5
        '1.2.840.113549.1.5.13': 'pbes2',
        '1.2.840.113549.1.5.1': 'pbes1_md2_des',
        '1.2.840.113549.1.5.3': 'pbes1_md5_des',
        '1.2.840.113549.1.5.4': 'pbes1_md2_rc2',
        '1.2.840.113549.1.5.6': 'pbes1_md5_rc2',
        '1.2.840.113549.1.5.10': 'pbes1_sha1_des',
        '1.2.840.113549.1.5.11': 'pbes1_sha1_rc2',
        # From PKCS#12
        '1.2.840.113549.1.12.1.1': 'pkcs12_sha1_rc4_128',
        '1.2.840.113549.1.12.1.2': 'pkcs12_sha1_rc4_40',
        '1.2.840.113549.1.12.1.3': 'pkcs12_sha1_tripledes_3key',
        '1.2.840.113549.1.12.1.4': 'pkcs12_sha1_tripledes_2key',
        '1.2.840.113549.1.12.1.5': 'pkcs12_sha1_rc2_128',
        '1.2.840.113549.1.12.1.6': 'pkcs12_sha1_rc2_40',
        # PKCS#1 v2.2
        '1.2.840.113549.1.1.1': 'rsaes_pkcs1v15',
        '1.2.840.113549.1.1.7': 'rsaes_oaep',
    }


class EncryptionAlgorithm(_ForceNullParameters, Sequence):
    _fields = [
        ('algorithm', EncryptionAlgorithmId),
        ('parameters', Any, {'optional': True}),
    ]

    _oid_pair = ('algorithm', 'parameters')
    _oid_specs = {
        'des': OctetString,
        'tripledes_3key': OctetString,
        'rc2': Rc2Params,
        'rc5': Rc5Params,
        'aes128_cbc': OctetString,
        'aes192_cbc': OctetString,
        'aes256_cbc': OctetString,
        'aes128_ofb': OctetString,
        'aes192_ofb': OctetString,
        'aes256_ofb': OctetString,
        # From RFC5084
        'aes128_ccm': CcmParams,
        'aes192_ccm': CcmParams,
        'aes256_ccm': CcmParams,
        # From PKCS#5
        'pbes1_md2_des': Pbes1Params,
        'pbes1_md5_des': Pbes1Params,
        'pbes1_md2_rc2': Pbes1Params,
        'pbes1_md5_rc2': Pbes1Params,
        'pbes1_sha1_des': Pbes1Params,
        'pbes1_sha1_rc2': Pbes1Params,
        # From PKCS#12
        'pkcs12_sha1_rc4_128': Pbes1Params,
        'pkcs12_sha1_rc4_40': Pbes1Params,
        'pkcs12_sha1_tripledes_3key': Pbes1Params,
        'pkcs12_sha1_tripledes_2key': Pbes1Params,
        'pkcs12_sha1_rc2_128': Pbes1Params,
        'pkcs12_sha1_rc2_40': Pbes1Params,
        # PKCS#1 v2.2
        'rsaes_oaep': RSAESOAEPParams,
    }

    @property
    def kdf(self):
        """
        Returns the name of the key derivation function to use.

        :return:
            A unicode from of one of the following: "pbkdf1", "pbkdf2",
            "pkcs12_kdf"
        """
        pass

    @property
    def kdf_hmac(self):
        """
        Returns the HMAC algorithm to use with the KDF.

        :return:
            A unicode string of one of the following: "md2", "md5", "sha1",
            "sha224", "sha256", "sha384", "sha512"
        """
        pass

    @property
    def kdf_salt(self):
        """
        Returns the byte string to use as the salt for the KDF.

        :return:
            A byte string
        """
        pass

    @property
    def kdf_iterations(self):
        """
        Returns the number of iterations that should be run via the KDF.

        :return:
            An integer
        """
        pass

    @property
    def key_length(self):
        """
        Returns the key length to pass to the cipher/kdf. The PKCS#5 spec does
        not specify a way to store the RC5 key length, however this tends not
        to be a problem since OpenSSL does not support RC5 in PKCS#8 and OS X
        does not provide an RC5 cipher for use in the Security Transforms
        library.

        :raises:
            ValueError - when the key length can not be determined

        :return:
            An integer representing the length in bytes
        """
        pass

    @property
    def encryption_mode(self):
        """
        Returns the name of the encryption mode to use.

        :return:
            A unicode string from one of the following: "cbc", "ecb", "ofb",
            "cfb", "wrap", "gcm", "ccm", "wrap_pad"
        """
        pass

    @property
    def encryption_cipher(self):
        """
        Returns the name of the symmetric encryption cipher to use. The key
        length can be retrieved via the .key_length property to disabiguate
        between different variations of TripleDES, AES, and the RC* ciphers.

        :return:
            A unicode string from one of the following: "rc2", "rc5", "des",
            "tripledes", "aes"
        """
        pass

    @property
    def encryption_block_size(self):
        """
        Returns the block size of the encryption cipher, in bytes.

        :return:
            An integer that is the block size in bytes
        """
        pass

    @property
    def encryption_iv(self):
        """
        Returns the byte string of the initialization vector for the encryption
        scheme. Only the PBES2 stores the IV in the params. For PBES1, the IV
        is derived from the KDF and this property will return None.

        :return:
            A byte string or None
        """
        pass


class Pbes2Params(Sequence):
    _fields = [
        ('key_derivation_func', KdfAlgorithm),
        ('encryption_scheme', EncryptionAlgorithm),
    ]


class Pbmac1Params(Sequence):
    _fields = [
        ('key_derivation_func', KdfAlgorithm),
        ('message_auth_scheme', HmacAlgorithm),
    ]


class Pkcs5MacId(ObjectIdentifier):
    _map = {
        '1.2.840.113549.1.5.14': 'pbmac1',
    }


class Pkcs5MacAlgorithm(Sequence):
    _fields = [
        ('algorithm', Pkcs5MacId),
        ('parameters', Any),
    ]

    _oid_pair = ('algorithm', 'parameters')
    _oid_specs = {
        'pbmac1': Pbmac1Params,
    }


EncryptionAlgorithm._oid_specs['pbes2'] = Pbes2Params


class AnyAlgorithmId(ObjectIdentifier):
    _map = {}

    def _setup(self):
        pass


class AnyAlgorithmIdentifier(_ForceNullParameters, Sequence):
    _fields = [
        ('algorithm', AnyAlgorithmId),
        ('parameters', Any, {'optional': True}),
    ]

    _oid_pair = ('algorithm', 'parameters')
    _oid_specs = {}

    def _setup(self):
        pass
