# coding: utf-8

"""
Functions for parsing and dumping using the ASN.1 DER encoding. Exports the
following items:

 - emit()
 - parse()
 - peek()

Other type classes are defined that help compose the types listed above.
"""

from __future__ import unicode_literals, division, absolute_import, print_function

import sys

from ._types import chr_cls, type_name
from .util import int_from_bytes, int_to_bytes

_INSUFFICIENT_DATA_MESSAGE = 'Insufficient data - %s bytes requested but only %s available'
_MAX_DEPTH = 10


def emit(class_, method, tag, contents):
    """
    Constructs a byte string of an ASN.1 DER-encoded value

    This is typically not useful. Instead, use one of the standard classes from
    asn1crypto.core, or construct a new class with specific fields, and call the
    .dump() method.

    :param class_:
        An integer ASN.1 class value: 0 (universal), 1 (application),
        2 (context), 3 (private)

    :param method:
        An integer ASN.1 method value: 0 (primitive), 1 (constructed)

    :param tag:
        An integer ASN.1 tag value

    :param contents:
        A byte string of the encoded byte contents

    :return:
        A byte string of the ASN.1 DER value (header and contents)
    """
    pass


def parse(contents, strict=False):
    """
    Parses a byte string of ASN.1 BER/DER-encoded data.

    This is typically not useful. Instead, use one of the standard classes from
    asn1crypto.core, or construct a new class with specific fields, and call the
    .load() class method.

    :param contents:
        A byte string of BER/DER-encoded data

    :param strict:
        A boolean indicating if trailing data should be forbidden - if so, a
        ValueError will be raised when trailing data exists

    :raises:
        ValueError - when the contents do not contain an ASN.1 header or are truncated in some way
        TypeError - when contents is not a byte string

    :return:
        A 6-element tuple:
         - 0: integer class (0 to 3)
         - 1: integer method
         - 2: integer tag
         - 3: byte string header
         - 4: byte string content
         - 5: byte string trailer
    """
    pass


def peek(contents):
    """
    Parses a byte string of ASN.1 BER/DER-encoded data to find the length

    This is typically used to look into an encoded value to see how long the
    next chunk of ASN.1-encoded data is. Primarily it is useful when a
    value is a concatenation of multiple values.

    :param contents:
        A byte string of BER/DER-encoded data

    :raises:
        ValueError - when the contents do not contain an ASN.1 header or are truncated in some way
        TypeError - when contents is not a byte string

    :return:
        An integer with the number of bytes occupied by the ASN.1 value
    """
    pass


def _parse(encoded_data, data_len, pointer=0, lengths_only=False, depth=0):
    """
    Parses a byte string into component parts

    :param encoded_data:
        A byte string that contains BER-encoded data

    :param data_len:
        The integer length of the encoded data

    :param pointer:
        The index in the byte string to parse from

    :param lengths_only:
        A boolean to cause the call to return a 2-element tuple of the integer
        number of bytes in the header and the integer number of bytes in the
        contents. Internal use only.

    :param depth:
        The recursion depth when evaluating indefinite-length encoding.

    :return:
        A 2-element tuple:
         - 0: A tuple of (class_, method, tag, header, content, trailer)
         - 1: An integer indicating how many bytes were consumed
    """
    pass


def _dump_header(class_, method, tag, contents):
    """
    Constructs the header bytes for an ASN.1 object

    :param class_:
        An integer ASN.1 class value: 0 (universal), 1 (application),
        2 (context), 3 (private)

    :param method:
        An integer ASN.1 method value: 0 (primitive), 1 (constructed)

    :param tag:
        An integer ASN.1 tag value

    :param contents:
        A byte string of the encoded byte contents

    :return:
        A byte string of the ASN.1 DER header
    """
    pass
