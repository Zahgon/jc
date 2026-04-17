r"""jc - JSON Convert Syslog RFC 5424 string streaming parser

> This streaming parser outputs JSON Lines (cli) or returns an Iterable of
> Dictionaries (module)

This parser accepts a single syslog line string or multiple syslog lines
separated by newlines. A warning message to `STDERR` will be printed if an
unparsable line is found unless `--quiet` or `quiet=True` is used.

The `timestamp_epoch` calculated timestamp field is naive. (i.e. based on
the local time of the system the parser is run on)

The `timestamp_epoch_utc` calculated timestamp field is timezone-aware and
is only available if the timezone field is UTC.

Usage (cli):

    $ echo <165>1 2003-08-24T05:14:15.000003-07:00 192.0... | jc --syslog-s

Usage (module):

    import jc

    result = jc.parse('syslog_s', syslog_command_output.splitlines())
    for item in result:
        # do something

Schema:

Blank values converted to `null`/`None`.

    {
      "priority":                   integer,
      "version":                    integer,
      "timestamp":                  string,
      "timestamp_epoch":            integer,  # [0]
      "timestamp_epoch_utc":        integer,  # [1]
      "hostname":                   string,
      "appname":                    string,
      "proc_id":                    integer,
      "msg_id":                     string,
      "structured_data": [
        {
          "identity":               string,
          "parameters": {
            "<key>":                string
          }
        }
      ],
      "message":                    string,
      "unparsable":                 string  # [2]

      # below object only exists if using -qq or ignore_exceptions=True
      "_jc_meta": {
        "success":      boolean,     # false if error parsing
        "error":        string,      # exists if "success" is false
        "line":         string       # exists if "success" is false
      }
    }

    [0] naive timestamp if "timestamp" field is parsable, else null
    [1] timezone aware timestamp available for UTC, else null
    [2] this field exists if the syslog line is not parsable. The value
        is the original syslog line.

Examples:

    $ cat syslog.txt | jc --syslog-s -p
    {"priority":165,"version":1,"timestamp":"2003-08-24T05:14:15.000003-...}
    {"priority":165,"version":1,"timestamp":"2003-08-24T05:14:16.000003-...}
    pass

    $ cat syslog.txt | jc --syslog-s -p -r
    {"priority":"165","version":"1","timestamp":"2003-08-24T05:14:15.000...}
    {"priority":"165","version":"1","timestamp":"2003-08-24T05:15:15.000...}
    pass
"""
from typing import List, Dict, Iterable, Union, Optional
import re
import jc.utils
from jc.streaming import (
    add_jc_meta, streaming_input_type_check, streaming_line_input_type_check, raise_or_yield
)
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = 'Syslog RFC 5424 string streaming parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'file', 'string']
    streaming = True


__version__ = info.version


# fix escape chars specified in syslog RFC 5424
# https://www.rfc-editor.org/rfc/rfc5424.html#section-6
escape_map = {
    r'\\': '\\',
    r'\"': '"',
    r'\]': ']'
}


def _extract_structs(structs_string: str) -> List[str]:
    pass


def _extract_ident(struct_string) -> Optional[str]:
    pass


def _extract_kv(struct_string) -> List[Dict]:
    pass


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
