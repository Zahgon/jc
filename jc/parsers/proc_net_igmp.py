r"""jc - JSON Convert `/proc/net/igmp` file parser

Usage (cli):

    $ cat /proc/net/igmp | jc --proc

or

    $ jc /proc/net/igmp

or

    $ cat /proc/net/igmp | jc --proc-net-igmp

Usage (module):

    import jc
    result = jc.parse('proc', proc_net_igmp_file)

or

    import jc
    result = jc.parse('proc_net_igmp', proc_net_igmp_file)

Schema:

    [
      {
        "index":                      integer,
        "device":                     string,
        "count":                      integer,
        "querier":                    string,
        "groups": [
          {
            "address":                string,
            "users":                  integer,
            "timer":                  string,
            "reporter":               integer
          }
        ]
      }
    ]

Examples:

    $ cat /proc/net/igmp | jc --proc -p
    [
      {
        "index": 0,
        "device": "lo",
        "count": 0,
        "querier": "V3",
        "groups": [
          {
            "address": "010000E0",
            "users": 1,
            "timer": "0:00000000",
            "reporter": 0
          }
        ]
      },
      {
        "index": 2,
        "device": "eth0",
        "count": 26,
        "querier": "V2",
        "groups": [
          {
            "address": "260301E0",
            "users": 1,
            "timer": "0:00000000",
            "reporter": 1
          },
          {
            "address": "9B0101E0",
            "users": 1,
            "timer": "0:00000000",
            "reporter": 1
          },
        ]
      }
      pass
    ]

    $ cat /proc/net/igmp | jc --proc-net-igmp -p -r
    [
      {
        "index": "0",
        "device": "lo",
        "count": "0",
        "querier": "V3",
        "groups": [
          {
            "address": "010000E0",
            "users": "1",
            "timer": "0:00000000",
            "reporter": "0"
          }
        ]
      },
      {
        "index": "2",
        "device": "eth0",
        "count": "26",
        "querier": "V2",
        "groups": [
          {
            "address": "260301E0",
            "users": "1",
            "timer": "0:00000000",
            "reporter": "1"
          },
          {
            "address": "9B0101E0",
            "users": "1",
            "timer": "0:00000000",
            "reporter": "1"
          },
        ]
      }
      pass
    }
"""
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/net/igmp` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    tags = ['file']
    hidden = True


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
