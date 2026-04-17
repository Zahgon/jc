# coding: utf-8

"""
Encoding DER to PEM and decoding PEM to DER. Exports the following items:

 - armor()
 - detect()
 - unarmor()

"""

from __future__ import unicode_literals, division, absolute_import, print_function

from io import BytesIO
import base64
import re

from ._errors import unwrap
from ._types import type_name as _type_name



def detect(byte_string):
    """
    Detect if a byte string seems to contain a PEM-encoded block

    :param byte_string:
        A byte string to look through

    :return:
        A boolean, indicating if a PEM-encoded block is contained in the byte
        string
    """
    pass


def armor(type_name, der_bytes, headers=None):
    """
    Armors a DER-encoded byte string in PEM

    :param type_name:
        A unicode string that will be capitalized and placed in the header
        and footer of the block. E.g. "CERTIFICATE", "PRIVATE KEY", etc. This
        will appear as "-----BEGIN CERTIFICATE-----" and
        "-----END CERTIFICATE-----".

    :param der_bytes:
        A byte string to be armored

    :param headers:
        An OrderedDict of the header lines to write after the BEGIN line

    :return:
        A byte string of the PEM block
    """
    pass


def _unarmor(pem_bytes):
    """
    Convert a PEM-encoded byte string into one or more DER-encoded byte strings

    :param pem_bytes:
        A byte string of the PEM-encoded data

    :raises:
        ValueError - when the pem_bytes do not appear to be PEM-encoded bytes

    :return:
        A generator of 3-element tuples in the format: (object_type, headers,
        der_bytes). The object_type is a unicode string of what is between
        "-----BEGIN " and "-----". Examples include: "CERTIFICATE",
        "PUBLIC KEY", "PRIVATE KEY". The headers is a dict containing any lines
        in the form "Name: Value" that are right after the begin line.
    """
    pass


def unarmor(pem_bytes, multiple=False):
    """
    Convert a PEM-encoded byte string into a DER-encoded byte string

    :param pem_bytes:
        A byte string of the PEM-encoded data

    :param multiple:
        If True, function will return a generator

    :raises:
        ValueError - when the pem_bytes do not appear to be PEM-encoded bytes

    :return:
        A 3-element tuple (object_name, headers, der_bytes). The object_name is
        a unicode string of what is between "-----BEGIN " and "-----". Examples
        include: "CERTIFICATE", "PUBLIC KEY", "PRIVATE KEY". The headers is a
        dict containing any lines in the form "Name: Value" that are right
        after the begin line.
    """
    pass
