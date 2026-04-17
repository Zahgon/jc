r"""jc - JSON Convert `asciitable-m` parser

This parser converts various styles of ASCII and Unicode text tables with
multi-line rows. Tables must have a header row and separator line between
rows.

For example:

    ╒══════════╤═════════╤════════╕
    │ foo      │ bar baz │ fiz    │
    │          │         │ buz    │
    ╞══════════╪═════════╪════════╡
    │ good day │ 12345   │        │
    │ mate     │         │        │
    ├──────────┼─────────┼────────┤
    │ hi there │ abc def │ 3.14   │
    │          │         │        │
    ╘══════════╧═════════╧════════╛

Cells with multiple lines within rows will be joined with a newline
character ('\\n').

Headers (keys) are converted to snake-case and newlines between multi-line
headers are joined with an underscore. All values are returned as strings,
except empty strings, which are converted to None/null.

> Note: To preserve the case of the keys use the `-r` cli option or
> `raw=True` argument in `parse()`.

> Note: table column separator characters (e.g. `|`) cannot be present
> inside the cell data. If detected, a warning message will be printed to
> `STDERR` and the line will be skipped. The warning message can be
> suppressed by using the `-q` command option or by setting `quiet=True` in
> `parse()`.

Usage (cli):

    $ cat table.txt | jc --asciitable-m

Usage (module):

    import jc
    result = jc.parse('asciitable_m', asciitable-string)

Schema:

    [
      {
        "column_name1":     string,    # empty string is null
        "column_name2":     string     # empty string is null
      }
    ]

Examples:

    $ echo '
    > +----------+---------+--------+
    > | foo      | bar     | baz    |
    > |          |         | buz    |
    > +==========+=========+========+
    > | good day | 12345   |        |
    > | mate     |         |        |
    > +----------+---------+--------+
    > | hi there | abc def | 3.14   |
    > |          |         |        |
    > +==========+=========+========+' | jc --asciitable-m -p
    [
      {
        "foo": "good day\\nmate",
        "bar": "12345",
        "baz_buz": null
      },
      {
        "foo": "hi there",
        "bar": "abc def",
        "baz_buz": "3.14"
      }
    ]

    $ echo '
    > ╒══════════╤═════════╤════════╕
    > │ foo      │ bar     │ baz    │
    > │          │         │ buz    │
    > ╞══════════╪═════════╪════════╡
    > │ good day │ 12345   │        │
    > │ mate     │         │        │
    > ├──────────┼─────────┼────────┤
    > │ hi there │ abc def │ 3.14   │
    > │          │         │        │
    > ╘══════════╧═════════╧════════╛' | jc --asciitable-m -p
    [
      {
        "foo": "good day\\nmate",
        "bar": "12345",
        "baz_buz": null
      },
      {
        "foo": "hi there",
        "bar": "abc def",
        "baz_buz": "3.14"
      }
    ]
"""
import re
from functools import lru_cache
from typing import Iterable, Tuple, List, Dict, Optional
import jc.utils
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = 'multi-line ASCII and Unicode table parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['generic', 'string']


__version__ = info.version


def _process(proc_data: List[Dict]) -> List[Dict]:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured to conform to the schema.
    """
    pass


def _remove_ansi(string: str) -> str:
    pass


def _lstrip(string: str) -> str:
    """find the leftmost non-whitespace character and lstrip to that index"""
    pass


def _rstrip(string: str) -> str:
    """find the rightmost non-whitespace character and rstrip and pad to that index"""
    pass


def _strip(string: str) -> str:
    pass


def _table_sniff(string: str) -> str:
    """find the table-type via heuristics"""
    pass

@lru_cache(maxsize=32)
def _is_separator(line: str) -> bool:
    """returns true if a table separator line is found"""
    pass


def _snake_case(line: str) -> str:
    """
    replace spaces between words and special characters with an underscore.
    """
    pass


def _fixup_separators(line: str) -> str:
    """normalize separators, and remove first and last separators"""
    pass


def _normalize_rows(table_lines: Iterable[str]) -> List[Tuple[int, List[str]]]:
    """return a List of tuples of row-counters and data lines."""
    pass


def _get_headers(table: Iterable[Tuple[int, List]]) -> List[List[str]]:
    """
    return a list of all of the header rows (which are lists of strings.
        [                            # headers
            ['str', 'str', 'str'],   # header rows
            ['str', 'str', 'str']
        ]
    """
    pass


def _get_data(table: Iterable[Tuple[int, List]]) -> List[List[List[str]]]:
    """
    return a list of rows, which are lists made up of lists of strings:
        [                                # data
            [                            # data rows
                ['str', 'str', 'str'],   # data lines
                ['str', 'str', 'str']
            ]
        ]
    """
    pass


def _collapse_headers(table: List[List[str]]) -> List[str]:
    """append each column string to return the full header list"""
    pass


def _collapse_data(table: List[List[List[str]]], quiet=False) -> List[List[str]]:
    """combine data rows to return a simple list of lists"""
    pass


def _create_table_dict(header: List[str], data: List[List[str]]) -> List[Dict[str, Optional[str]]]:
    """
    zip the headers and data to create a list of dictionaries. Also convert
    empty strings to None.
    """
    pass


def _parse_pretty(string: str, quiet: bool =False) -> List[Dict[str, Optional[str]]]:
    pass


def parse(
    data: str,
    raw: bool = False,
    quiet: bool = False
) -> List[Dict]:
    """
    Main text parsing function

    Parameters:

        data:        (string)  text data to parse
        raw:         (boolean) unprocessed output if True
        quiet:       (boolean) suppress warning messages if True

    Returns:

        List of Dictionaries. Raw or processed structured data.
    """
    pass
