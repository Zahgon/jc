r"""jc - JSON Convert Syslog RFC 3164 string parser

This parser accepts a single syslog line string or multiple syslog lines
separated by newlines. A warning message to `STDERR` will be printed if an
unparsable line is found unless `--quiet` or `quiet=True` is used.

Usage (cli):

    $ echo '<34>Oct 11 22:14:15 mymachine su: su root...' | jc --syslog-bsd

Usage (module):

    import jc
    result = jc.parse('syslog_bsd', syslog_command_output)

Schema:

    [
      {
        "priority":                   integer/null,
        "date":                       string,
        "hostname":                   string,
        "tag":                        string/null,
        "content":                    string,
        "unparsable":                 string,  # [0]
      }
    ]

    [0] this field exists if the syslog line is not parsable. The value
        is the original syslog line.

Examples:

    $ cat syslog.txt | jc --syslog-bsd -p
    [
      {
        "priority": 34,
        "date": "Oct 11 22:14:15",
        "hostname": "mymachine",
        "tag": "su",
        "content": "'su root' failed for lonvick on /dev/pts/8"
      }
    ]

    $ cat syslog.txt | jc --syslog-bsd -p -r
    [
      {
        "priority": "34",
        "date": "Oct 11 22:14:15",
        "hostname": "mymachine",
        "tag": "su",
        "content": "'su root' failed for lonvick on /dev/pts/8"
      }
    ]
"""
import re
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = 'Syslog RFC 3164 string parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'file', 'string']


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
