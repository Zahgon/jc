"""jc - JSON Convert utils"""
import sys
import re
import locale
import shutil
from itertools import islice
from collections import namedtuple
from numbers import Number
from datetime import datetime, timezone
from textwrap import TextWrapper
from functools import lru_cache
from typing import Any, List, Dict, Iterable, Union, Optional, TextIO
from .jc_types import TimeStampFormatType

CLI_QUIET = False

def _asciify(string: str) -> str:
    """
    Return a string downgraded from Unicode to ASCII with some simple
    conversions.
    """
    pass


def _safe_print(
    string: str,
    sep: str = ' ',
    end: str = '\n',
    file: TextIO = sys.stdout,
    flush: bool = False
) -> None:
    """Output for both UTF-8 and ASCII encoding systems"""
    pass


def _safe_pager(string: str) -> None:
    """Pager output for both UTF-8 and ASCII encoding systems"""
    pass


def warning_message(message_lines: List[str]) -> None:
    """
    Prints warning message to `STDERR` for non-fatal issues. The first line
    is prepended with 'jc:  Warning - ' and subsequent lines are indented.
    Wraps text as needed based on the terminal width.

    Parameters:

        message:   (list) list of string lines

    Returns:

        None - just prints output to STDERR
    """
    pass


def error_message(message_lines: List[str]) -> None:
    """
    Prints an error message to `STDERR` for fatal issues. The first line is
    prepended with 'jc:  Error - ' and subsequent lines are indented.
    Wraps text as needed based on the terminal width.

    Parameters:

        message:   (list) list of string lines

    Returns:

        None - just prints output to `STDERR`
    """
    pass


def is_compatible(compatible: List[str]) -> bool:
    """
    Returns True if the parser is compatible with the running OS platform.
    """
    pass


def compatibility(mod_name: str, compatible: List[str], quiet: bool = False) -> None:
    """
    Checks for the parser's compatibility with the running OS platform and
    prints a warning message to `STDERR` if not compatible and
    `quiet=False.`

    Parameters:

        mod_name:     (string) __name__ of the calling module

        compatible:   (list) sys.platform name(s) compatible with
                      the parser. compatible options:
                      linux, darwin, cygwin, win32, aix, freebsd

        quiet:        (bool) suppress compatibility message if `True`

    Returns:

        None - just prints output to STDERR
    """
    pass


def has_data(data: Union[str, bytes]) -> bool:
    """
    Checks if the string input contains data. If there are any
    non-whitespace characters then return `True`, else return `False`.

    For bytes, returns `True` if there is any data.

    Parameters:

        data:        (string, bytes) input to check whether it contains data

    Returns:

        Boolean      `True` if input string (data) contains non-whitespace
                     characters, otherwise `False`. For bytes data, returns
                     `True` if there is any data, otherwise `False`.
    """
    pass


def remove_quotes(data: str) -> str:
    """
    Remove single or double quotes surrounding a string. If no quotes are
    found then the string is returned unmodified.

    Parameters:

        data:       (string) Input value

    Returns:

        string
    """
    pass


def normalize_key(data: str) -> str:
    r"""
    Normalize a key name by shifting to lower-case and converting special
    characters to underscores.

    Special characters are defined as `space` and the following:

        !"#$%&'()*+,-./:;<=>?@[\]^`{|}~

    This is a lossy algorithm. Repeating and trailing underscores are
    removed.

    Parameters:

        data:       (string) Input value

    Returns:

        string
    """
    pass


def convert_to_int(value: object) -> Optional[int]:
    """
    Converts string and float input to int. Strips all non-numeric
    characters from strings.

    Parameters:

        value:         (string/float) Input value

    Returns:

        integer/None   Integer if successful conversion, otherwise None
    """
    pass


def convert_to_float(value: object) -> Optional[float]:
    """
    Converts string and int input to float. Strips all non-numeric
    characters from strings.

    Parameters:

        value:         (string/integer) Input value

    Returns:

        float/None     Float if successful conversion, otherwise None
    """
    pass


def convert_to_bool(value: object) -> bool:
    """
    Converts string, integer, or float input to boolean by checking
    for 'truthy' values.

    Parameters:

        value:          (string/integer/float) Input value

    Returns:

        True/False      False unless a 'truthy' number or string is found
                        ('y', 'yes', 'true', '1', 1, -1, etc.)
    """
    pass


# convert_size_to_int from https://github.com/xolox/python-humanfriendly

# Copyright (c) 2021 Peter Odding

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
def convert_size_to_int(
    size: str,
    binary: bool = False,
    posix_mode: bool = False,
    decimal_bias: bool = False) -> Optional[int]:
    """
    Parse a human readable data size and return the number of bytes.

    Parameters:

        size:           (string) The human readable file size to parse.
        binary:         (boolean) `True` to use binary multiples of bytes
                        (base-2) for ambiguous unit symbols and names,
                        `False` to use decimal multiples of bytes (base-10).
        posix_mode:     (boolean) Treat one-letter units (k, m, g, etc.) as
                        binary.
        decimal_bias:   (boolean) `True` to treat slightly ambiguous two-
                        letter unit symbols ending in "i" (e.g. Ki, Gi) to
                        use decimal multiples of bytes (base-10). `False`
                        (default) to use binary multiples of bytes.
    Returns:

        integer/None    Integer if successful conversion, otherwise None

    This function knows how to parse sizes in bytes, kilobytes, megabytes,
    gigabytes, terabytes and petabytes. Some examples:

        >>> convert_size_to_int('42')
        42
        >>> convert_size_to_int('13b')
        13
        >>> convert_size_to_int('5 bytes')
        5
        >>> convert_size_to_int('1 KB')
        1000
        >>> convert_size_to_int('1 kilobyte')
        1000
        >>> convert_size_to_int('1 KiB')
        1024
        >>> convert_size_to_int('1 Ki')
        1024
        >>> convert_size_to_int('1 Ki', decimal_bias=True)
        1000
        >>> convert_size_to_int('1 KB', binary=True)
        1024
        >>> convert_size_to_int('1.5 GB')
        1500000000
        >>> convert_size_to_int('1.5 GB', binary=True)
        1610612736
    """
    pass


def input_type_check(data: object) -> None:
    """Ensure input data is a string. Raises `TypeError` if not."""
    pass


def _lazy_splitlines(text: str) -> Iterable[str]:
    pass


def line_slice(
        data: Union[str, Iterable[str], TextIO, bytes, None],
        slice_start: Optional[int] = None,
        slice_end: Optional[int] = None
) -> Union[str, Iterable[str], TextIO, bytes, None]:
    """
    Slice input data by lines - lazily, if possible.

    Accepts a string (for normal parsers) or an iterable (for streaming
    parsers). Uses normal start/stop slicing values, but will always slice
    on lines instead of characters. Positive slices will use less memory as
    the function will attempt to lazily iterate over the input. A negative
    slice parameter will force the function to read in all of the data and
    then slice, which will use more memory.

    Parameters:

        data:              (string or iterable) - input to slice by lines
        slice_start:       (int) - starting line
        slice_end:         (int) - ending line

    Returns:
        string if input is a string.
        iterable of strings if input is an iterable (for streaming parsers)
    """
    pass


class timestamp:
    __slots__ = ('string', 'format', 'naive', 'utc', 'iso')

    def __init__(self,
                 datetime_string: Optional[str],
                 format_hint: Optional[Iterable[int]] = None
    ) -> None:
        """
        Input a datetime text string of several formats and convert to a
        naive or timezone-aware epoch timestamp in UTC.

        Parameters:

            datetime_string  (str):  a string representation of a
                datetime in several supported formats

            format_hint  (iterable):  an optional iterable of format ID
                integers to instruct the timestamp object to try those
                formats first in the order given. Other formats will be
                tried after the format hint list is exhausted. This can
                speed up timestamp conversion so several different formats
                don't have to be tried in brute-force fashion.

        Returns a timestamp object with the following attributes:

            string  (str):  the input datetime string

            format  (int | None):  the format rule that was used to decode
                the datetime string. None if conversion fails.

            naive  (int | None):  timestamp based on locally configured
                timezone. None if conversion fails.

            utc  (int | None):  aware timestamp only if UTC timezone
                detected in datetime string. None if conversion fails.

            iso (str | None):  ISO string - timezone information is output
                only if UTC timezone is detected in the datetime string.
        """
        self.string = datetime_string

        if not format_hint:
            format_hint = tuple()
        else:
            format_hint = tuple(format_hint)

        dt = self._parse_dt(self.string, format_hint=format_hint)
        self.format = dt['format']
        self.naive = dt['timestamp_naive']
        self.utc = dt['timestamp_utc']
        self.iso = dt['iso']

    def __repr__(self) -> str:
        return f'timestamp(string={self.string!r}, format={self.format}, naive={self.naive}, utc={self.utc}, iso={self.iso!r})'

    @staticmethod
    @lru_cache(maxsize=2048)
    def _parse_dt(
        dt_string: Optional[str],
        format_hint: Optional[Iterable[int]] = None
    ) -> Dict[str, Any]:
        """
        Input a datetime text string of several formats and convert to
        a naive or timezone-aware epoch timestamp in UTC.

        Parameters:

            dt_string:    (string) a string representation of a date-time
                          in several supported formats

            format_hint:  (list | tuple) a list of format ID int's that
                          should be tried first. This can increase
                          performance since the function will not need to
                          try many incorrect formats before finding the
                          correct one.

        Returns:

            Dictionary of the following format:

                {
                    # for debugging purposes. None if conversion fails
                    "format":               int,

                    # timestamp based on locally configured timezone.
                    # None if conversion fails.
                    "timestamp_naive":      int,

                    # aware timestamp only if UTC timezone detected.
                    # None if conversion fails.
                    "timestamp_utc":        int

                    # ISO string. None if conversion fails.
                    "iso":                  str
                }

                The `format` integer denotes which date_time format
                conversion succeeded.

                The `timestamp_naive` integer is the converted date-time
                string to a naive epoch timestamp.

                The `timestamp_utc` integer is the converted date-time
                string to an aware epoch timestamp in the UTC timezone. If
                an aware conversion cannot be performed (e.g. the UTC
                timezone is not found in the date-time string), then this
                field will be None.

                The `iso` string will only have timezone information if the
                UTC timezone is detected in `dt_string`.

                If the conversion completely fails, all fields will be None.
        """
        pass
