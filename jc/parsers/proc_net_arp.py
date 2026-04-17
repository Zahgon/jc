r"""jc - JSON Convert `/proc/net/arp` file parser

Usage (cli):

    $ cat /proc/net/arp | jc --proc

or

    $ jc /proc/net/arp

or

    $ cat /proc/net/arp | jc --proc-net-arp

Usage (module):

    import jc
    result = jc.parse('proc', proc_net_arp_file)

or

    import jc
    result = jc.parse('proc_net_arp', proc_net_arp_file)

Schema:

    [
      {
        "IP_address":           string,
        "HW_type":              string,
        "Flags":                string,
        "HW_address":           string,
        "Mask":                 string,
        "Device":               string
      }
    ]

Examples:

    $ cat /proc/net/arp | jc --proc -p
    [
      {
        "IP_address": "192.168.71.254",
        "HW_type": "0x1",
        "Flags": "0x2",
        "HW_address": "00:50:56:f3:2f:ae",
        "Mask": "*",
        "Device": "ens33"
      },
      pass
    ]
"""
from typing import List, Dict
import jc.utils
from jc.parsers.universal import simple_table_parse


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/net/arp` file parser'
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
