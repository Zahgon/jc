r"""jc - JSON Convert `/etc/resolve.conf` file parser

This parser may be more forgiving than the system parser. For example, if
multiple `search` lists are defined, this parser will append all entries to
the `search` field, while the system parser may only use the list from the
last defined instance.

Usage (cli):

    $ cat /etc/resolve.conf | jc --resolve-conf

Usage (module):

    import jc
    result = jc.parse('resolve_conf', resolve_conf_output)

Schema:

    {
      "domain":             string,
      "search": [
                            string
      ],
      "nameservers": [
                            string
      ],
      "options": [
                            string
      ],
      "sortlist": [
                            string
      ]
    }


Examples:

    $ cat /etc/resolve.conf | jc --resolve-conf -p
    {
      "search": [
        "eng.myprime.com",
        "dev.eng.myprime.com",
        "labs.myprime.com",
        "qa.myprime.com"
      ],
      "nameservers": [
        "10.136.17.15"
      ],
      "options": [
        "rotate",
        "ndots:1"
      ]
    }
"""
import re
from typing import List, Dict
from jc.jc_types import JSONDictType
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/etc/resolve.conf` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['file']


__version__ = info.version


def _process(proc_data: JSONDictType) -> JSONDictType:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   Dictionary raw structured data to process

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
