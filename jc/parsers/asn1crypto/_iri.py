# coding: utf-8

"""
Functions to convert unicode IRIs into ASCII byte string URIs and back. Exports
the following items:

 - iri_to_uri()
 - uri_to_iri()
"""

from __future__ import unicode_literals, division, absolute_import, print_function

from encodings import idna  # noqa
import codecs
import re

from ._errors import unwrap
from ._types import type_name

from urllib.parse import (
    quote as urlquote,
    unquote_to_bytes,
    urlsplit,
    urlunsplit,
)


def iri_to_uri(value, normalize=False):
    """
    Encodes a unicode IRI into an ASCII byte string URI

    :param value:
        A unicode string of an IRI

    :param normalize:
        A bool that controls URI normalization

    :return:
        A byte string of the ASCII-encoded URI
    """
    pass


def uri_to_iri(value):
    """
    Converts an ASCII URI byte string into a unicode IRI

    :param value:
        An ASCII-encoded byte string of the URI

    :return:
        A unicode string of the IRI
    """
    pass


def _iri_utf8_errors_handler(exc):
    """
    Error handler for decoding UTF-8 parts of a URI into an IRI. Leaves byte
    sequences encoded in %XX format, but as part of a unicode string.

    :param exc:
        The UnicodeDecodeError exception

    :return:
        A 2-element tuple of (replacement unicode string, integer index to
        resume at)
    """
    pass


codecs.register_error('iriutf8', _iri_utf8_errors_handler)


def _urlquote(string, safe=''):
    """
    Quotes a unicode string for use in a URL

    :param string:
        A unicode string

    :param safe:
        A unicode string of character to not encode

    :return:
        None (if string is None) or an ASCII byte string of the quoted string
    """
    pass


def _urlunquote(byte_string, remap=None, preserve=None):
    """
    Unquotes a URI portion from a byte string into unicode using UTF-8

    :param byte_string:
        A byte string of the data to unquote

    :param remap:
        A list of characters (as unicode) that should be re-mapped to a
        %XX encoding. This is used when characters are not valid in part of a
        URL.

    :param preserve:
        A bool - indicates that the chars to be remapped if they occur in
        non-hex form, should be preserved. E.g. / for URL path.

    :return:
        A unicode string
    """
    pass
