r"""jc - JSON Convert `zpool status` command output parser

Works with or without the `-v` option.

Usage (cli):

    $ zpool status | jc --zpool-status

or

    $ jc zpool status

Usage (module):

    import jc
    result = jc.parse('zpool_status', zpool_status_command_output)

Schema:

    [
      {
        "pool":                               string,
        "state":                              string,
        "status":                             string,
        "action":                             string,
        "see":                                string,
        "scan":                               string,
        "scrub":                              string,
        "config": [
          {
            "name":                           string,
            "state":                          string/null,
            "read":                           integer/null,
            "write":                          integer/null,
            "checksum":                       integer/null,
            "errors":                         string/null,
          }
        ],
        "errors":                             string
      }
    ]

Examples:

    $ zpool status -v | jc --zpool-status -p
    [
      {
        "pool": "tank",
        "state": "DEGRADED",
        "status": "One or more devices could not be opened.  Suffic...",
        "action": "Attach the missing device and online it using 'zpool...",
        "see": "http://www.sun.com/msg/ZFS-8000-2Q",
        "scrub": "none requested",
        "config": [
          {
            "name": "tank",
            "state": "DEGRADED",
            "read": 0,
            "write": 0,
            "checksum": 0
          },
          {
            "name": "mirror-0",
            "state": "DEGRADED",
            "read": 0,
            "write": 0,
            "checksum": 0
          },
          {
            "name": "c1t0d0",
            "state": "ONLINE",
            "read": 0,
            "write": 0,
            "checksum": 0
          },
          {
            "name": "c1t1d0",
            "state": "UNAVAIL",
            "read": 0,
            "write": 0,
            "checksum": 0,
            "errors": "cannot open"
          }
        ],
        "errors": "No known data errors"
      }
    ]

    $ zpool status -v | jc --zpool-status -p -r
    [
      {
        "pool": "tank",
        "state": "DEGRADED",
        "status": "One or more devices could not be opened.  Sufficient...",
        "action": "Attach the missing device and online it using 'zpool...",
        "see": "http://www.sun.com/msg/ZFS-8000-2Q",
        "scrub": "none requested",
        "config": [
          {
            "name": "tank",
            "state": "DEGRADED",
            "read": "0",
            "write": "0",
            "checksum": "0"
          },
          {
            "name": "mirror-0",
            "state": "DEGRADED",
            "read": "0",
            "write": "0",
            "checksum": "0"
          },
          {
            "name": "c1t0d0",
            "state": "ONLINE",
            "read": "0",
            "write": "0",
            "checksum": "0"
          },
          {
            "name": "c1t1d0",
            "state": "UNAVAIL",
            "read": "0",
            "write": "0",
            "checksum": "0",
            "errors": "cannot open"
          }
        ],
        "errors": "No known data errors"
      }
    ]
"""
from typing import List, Dict
from jc.jc_types import JSONDictType
import jc.utils
from jc.parsers.kv import parse as kv_parse


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = '`zpool status` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'freebsd']
    tags = ['command']
    magic_commands = ['zpool status']


__version__ = info.version


def _process(proc_data: List[JSONDictType]) -> List[JSONDictType]:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured to conform to the schema.
    """
    pass


def _build_config_list(string: str) -> List[Dict]:
    pass

def parse(
    data: str,
    raw: bool = False,
    quiet: bool = False
) -> List[JSONDictType]:
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
