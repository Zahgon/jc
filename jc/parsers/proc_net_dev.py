r"""jc - JSON Convert `/proc/net/dev` file parser

Usage (cli):

    $ cat /proc/net/dev | jc --proc

or

    $ jc /proc/net/dev

or

    $ cat /proc/net/dev | jc --proc-net-dev

Usage (module):

    import jc
    result = jc.parse('proc', proc_net_dev_file)

or

    import jc
    result = jc.parse('proc_net_dev', proc_net_dev_file)

Schema:

    [
      {
        "interface":                  string,
        "r_bytes":                    integer,
        "r_packets":                  integer,
        "r_errs":                     integer,
        "r_drop":                     integer,
        "r_fifo":                     integer,
        "r_frame":                    integer,
        "r_compressed":               integer,
        "r_multicast":                integer,
        "t_bytes":                    integer,
        "t_packets":                  integer,
        "t_errs":                     integer,
        "t_drop":                     integer,
        "t_fifo":                     integer,
        "t_colls":                    integer,
        "t_carrier":                  integer,
        "t_compressed":               integer
      }
    ]

Examples:

    $ cat /proc/net/dev | jc --proc -p
    [
      {
        "interface": "lo",
        "r_bytes": 13222,
        "r_packets": 152,
        "r_errs": 0,
        "r_drop": 0,
        "r_fifo": 0,
        "r_frame": 0,
        "r_compressed": 0,
        "r_multicast": 0,
        "t_bytes": 13222,
        "t_packets": 152,
        "t_errs": 0,
        "t_drop": 0,
        "t_fifo": 0,
        "t_colls": 0,
        "t_carrier": 0,
        "t_compressed": 0
      },
      pass
    ]

    $ cat /proc/net/dev | jc --proc-net-dev -p -r
    [
      {
        "interface": "lo:",
        "r_bytes": "13222",
        "r_packets": "152",
        "r_errs": "0",
        "r_drop": "0",
        "r_fifo": "0",
        "r_frame": "0",
        "r_compressed": "0",
        "r_multicast": "0",
        "t_bytes": "13222",
        "t_packets": "152",
        "t_errs": "0",
        "t_drop": "0",
        "t_fifo": "0",
        "t_colls": "0",
        "t_carrier": "0",
        "t_compressed": "0"
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
    description = '`/proc/net/dev` file parser'
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
