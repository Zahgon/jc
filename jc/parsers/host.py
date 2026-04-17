r"""jc - JSON Convert `host` command output parser

Supports parsing of the most commonly used RR types (A, AAAA, MX, TXT)

Usage (cli):

    $ host google.com | jc --host

or

    $ jc host google.com

Usage (module):

    import jc
    result = jc.parse('host', host_command_output)

Schema:

    [
      {
        "hostname":     string,
        "address": [
                        string
        ],
        "v6-address": [
                        string
        ],
        "mail": [
                        string
        ]
      }
    ]

    [
      {
        "nameserver":   string,
        "zone":         string,
        "mname":        string,
        "rname":        string,
        "serial":       integer,
        "refresh":      integer,
        "retry":        integer,
        "expire":       integer,
        "minimum":      integer
      }
    ]

Examples:

    $ host google.com | jc --host
    [
      {
        "hostname": "google.com",
        "address": [
          "142.251.39.110"
        ],
        "v6-address": [
          "2a00:1450:400e:811::200e"
        ],
        "mail": [
          "smtp.google.com."
        ]
      }
    ]

    $ jc host -C sunet.se
    [
      {
        "nameserver": "2001:6b0:7::2",
        "zone": "sunet.se",
        "mname": "sunic.sunet.se.",
        "rname": "hostmaster.sunet.se.",
        "serial": "2023090401",
        "refresh": "28800",
        "retry": "7200",
        "expire": "604800",
        "minimum": "300"
      },
      {
        pass
      }
    ]
"""
from typing import Dict, List
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`host` command parser'
    author = 'Pettai'
    author_email = 'pettai@sunet.se'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['command']
    magic_commands = ['host']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured to conform to the schema.
    """
    pass


def parse(data: str, raw: bool = False, quiet: bool = False):
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
