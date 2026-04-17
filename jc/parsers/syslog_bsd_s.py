r"""jc - JSON Convert Syslog RFC 3164 string streaming parser

> This streaming parser outputs JSON Lines (cli) or returns an Iterable of
> Dictionaries (module)

This parser accepts a single syslog line string or multiple syslog lines
separated by newlines. A warning message to `STDERR` will be printed if an
unparsable line is found unless `--quiet` or `quiet=True` is used.

Usage (cli):

    $ echo '<34>Oct 11 22:14:15 mymachine su: su ro...' | jc --syslog-bsd-s

Usage (module):

    import jc

    result = jc.parse('syslog_bsd_s', syslog_command_output.splitlines())
    for item in result:
        # do something

Schema:

    {
      "priority":                   integer/null,
      "date":                       string,
      "hostname":                   string,
      "tag":                        string/null,
      "content":                    string,
      "unparsable":                 string,  # [0]

      # below object only exists if using -qq or ignore_exceptions=True
      "_jc_meta": {
        "success":      boolean,     # false if error parsing
        "error":        string,      # exists if "success" is false
        "line":         string       # exists if "success" is false
      }
    }

    [0] this field exists if the syslog line is not parsable. The value
        is the original syslog line.

Examples:

    $ cat syslog.txt | jc --syslog-bsd-s -p
    {"priority":34,"date":"Oct 11 22:14:15","hostname":"mymachine","t...}
    {"priority":34,"date":"Oct 11 22:14:16","hostname":"mymachine","t...}
    pass

    $ cat syslog.txt | jc --syslog-bsd-s -p -r
    {"priority":"34","date":"Oct 11 22:14:15","hostname":"mymachine","...}
    {"priority":"34","date":"Oct 11 22:14:16","hostname":"mymachine","...}
    pass
"""
from typing import Dict, Iterable, Union
import re
import jc.utils
from jc.streaming import (
    add_jc_meta, streaming_input_type_check, streaming_line_input_type_check, raise_or_yield
)
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = 'Syslog RFC 3164 string streaming parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'file', 'string']
    streaming = True


__version__ = info.version


def _process(proc_data: Dict) -> Dict:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured data to conform to the schema.
    """
    pass


@add_jc_meta
def parse(
    data: Iterable[str],
    raw: bool = False,
    quiet: bool = False,
    ignore_exceptions: bool = False
) -> Union[Iterable[Dict], tuple]:
    """
    Main text parsing generator function. Returns an iterable object.

    Parameters:

        data:              (iterable)  line-based text data to parse
                                       (e.g. sys.stdin or str.splitlines())

        raw:               (boolean)   unprocessed output if True
        quiet:             (boolean)   suppress warning messages if True
        ignore_exceptions: (boolean)   ignore parsing exceptions if True


    Returns:

        Iterable of Dictionaries
    """
    pass
