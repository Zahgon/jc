r"""jc - JSON Convert Semantic Version string parser

This parser conforms to the specification at https://semver.org/

See Also: `ver` parser.

Usage (cli):

    $ echo 1.2.3-rc.1+44837 | jc --semver

Usage (module):

    import jc
    result = jc.parse('semver', semver_string)

Schema:

Strings that do not strictly conform to the specification will return an
empty object.

    {
      "major":                  integer,
      "minor":                  integer,
      "patch":                  integer,
      "prerelease":             string/null,
      "build":                  string/null
    }

Examples:

    $ echo 1.2.3-rc.1+44837 | jc --semver -p
    {
      "major": 1,
      "minor": 2,
      "patch": 3,
      "prerelease": "rc.1",
      "build": "44837"
    }

    $ echo 1.2.3-rc.1+44837 | jc --semver -p -r
    {
      "major": "1",
      "minor": "2",
      "patch": "3",
      "prerelease": "rc.1",
      "build": "44837"
    }
"""
import re
from typing import Set, Dict
from jc.jc_types import JSONDictType
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.1'
    description = 'Semantic Version string parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'string', 'slurpable']


__version__ = info.version


def _process(proc_data: JSONDictType) -> JSONDictType:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        Dictionary. Structured to conform to the schema.
    """
    pass


def parse(
    data: str,
    raw: bool = False,
    quiet: bool = False
) -> JSONDictType:
    """
    Main text parsing function

    Parameters:

        data:        (string)  text data to parse
        raw:         (boolean) unprocessed output if True
        quiet:       (boolean) suppress warning messages if True

    Returns:

        Dictionary. Raw or processed structured data.
    """
    pass
