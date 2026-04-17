# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2021 Taneli Hukkinen
# Licensed to PSF under a Contributor Agreement.

# from __future__ import annotations

from collections import namedtuple
import string
# from types import MappingProxyType
# from typing import Any, BinaryIO, NamedTuple

from ._re import (
    RE_DATETIME,
    RE_LOCALTIME,
    RE_NUMBER,
    match_to_datetime,
    match_to_localtime,
    match_to_number,
)
# from ._types import Key, ParseFloat, Pos

ASCII_CTRL = frozenset(chr(i) for i in range(32)) | frozenset(chr(127))

# Neither of these sets include quotation mark or backslash. They are
# currently handled as separate cases in the parser functions.
ILLEGAL_BASIC_STR_CHARS = ASCII_CTRL - frozenset("\t")
ILLEGAL_MULTILINE_BASIC_STR_CHARS = ASCII_CTRL - frozenset("\t\n")

ILLEGAL_LITERAL_STR_CHARS = ILLEGAL_BASIC_STR_CHARS
ILLEGAL_MULTILINE_LITERAL_STR_CHARS = ILLEGAL_MULTILINE_BASIC_STR_CHARS

ILLEGAL_COMMENT_CHARS = ILLEGAL_BASIC_STR_CHARS

TOML_WS = frozenset(" \t")
TOML_WS_AND_NEWLINE = TOML_WS | frozenset("\n")
BARE_KEY_CHARS = frozenset(string.ascii_letters + string.digits + "-_")
KEY_INITIAL_CHARS = BARE_KEY_CHARS | frozenset("\"'")
HEXDIGIT_CHARS = frozenset(string.hexdigits)

BASIC_STR_ESCAPE_REPLACEMENTS = {
        "\\b": "\u0008",  # backspace
        "\\t": "\u0009",  # tab
        "\\n": "\u000A",  # linefeed
        "\\f": "\u000C",  # form feed
        "\\r": "\u000D",  # carriage return
        '\\"': "\u0022",  # quote
        "\\\\": "\u005C",  # backslash
}


class TOMLDecodeError(ValueError):
    """An error raised if a document is not valid TOML."""


def load(__fp, *, parse_float=float):
    """Parse TOML from a binary file object."""
    pass


def loads(__s, *, parse_float=float):
    """Parse TOML from a string."""
    pass


class Flags:
    """Flags that map to parsed keys/namespaces."""

    # Marks an immutable namespace (inline array or inline table).
    FROZEN = 0
    # Marks a nest that has been explicitly created and can no longer
    # be opened using the "[table]" syntax.
    EXPLICIT_NEST = 1

    def __init__(self):
        self._flags = {}
        self._pending_flags = set()

    def add_pending(self, key, flag):
        pass

    def finalize_pending(self):
        pass

    def unset_all(self, key):
        pass

    def set(self, key, flag, *, recursive):
        pass

    def is_(self, key, flag):
        pass


class NestedDict:
    def __init__(self):
        # The parsed content of the TOML document
        self.dict = {}

    def get_or_create_nest(
        self,
        key,
        *,
        access_lists: bool = True,
    ) -> dict:
        pass

    def append_nest_to_list(self, key):
        pass


# class Output(namedtuple):
#     data: NestedDict
#     flags: Flags

Output = namedtuple('Output', ['data', 'flags'])


def skip_chars(src: str, pos, chars):
    pass


def skip_until(
    src,
    pos,
    expect,
    *,
    error_on,
    error_on_eof,
):
    pass


def skip_comment(src, pos):
    pass


def skip_comments_and_array_ws(src, pos):
    pass


def create_dict_rule(src, pos, out):
    pass


def create_list_rule(src: str, pos, out):
    pass


def key_value_rule(
    src, pos, out, header, parse_float
):
    pass


def parse_key_value_pair(
    src, pos, parse_float
):
    pass


def parse_key(src, pos):
    pass


def parse_key_part(src, pos):
    pass


def parse_one_line_basic_str(src, pos):
    pass


def parse_array(src, pos, parse_float):
    pass


def parse_inline_table(src, pos, parse_float):
    pass


def parse_basic_str_escape(
    src, pos, *, multiline = False
):
    pass


def parse_basic_str_escape_multiline(src, pos):
    pass


def parse_hex_char(src, pos, hex_len):
    pass


def parse_literal_str(src, pos):
    pass


def parse_multiline_str(src, pos, *, literal):
    pass


def parse_basic_str(src, pos, *, multiline):
    pass


def parse_value(  # noqa: C901
    src, pos, parse_float
):
    pass


def suffixed_err(src, pos, msg):
    """Return a `TOMLDecodeError` where error message is suffixed with
    coordinates in source."""
    pass


def is_unicode_scalar_value(codepoint: int) -> bool:
    pass


def make_safe_parse_float(parse_float):
    """A decorator to make `parse_float` safe.

    `parse_float` must not return dicts or lists, because these types
    would be mixed with parsed TOML tables and arrays, thus confusing
    the parser. The returned decorated callable raises `ValueError`
    instead of returning illegal types.
    """
    pass
