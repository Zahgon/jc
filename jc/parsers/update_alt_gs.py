r"""jc - JSON Convert `update-alternatives --get-selections` command output parser

Usage (cli):

    $ update-alternatives --get-selections | jc --update-alt-gs

or

    $ jc update-alternatives --get-selections

Usage (module):

    import jc
    result = jc.parse('update-alt-gs',
                      update_alternatives_get_selections_command_output)

Schema:

    [
      {
        "name":     string,
        "status":   string,
        "current":  string
      }
    ]

Examples:

    $ update-alternatives --get-selections | jc --update-alt-gs -p
    [
      {
        "name": "arptables",
        "status": "auto",
        "current": "/usr/sbin/arptables-nft"
      },
      {
        "name": "awk",
        "status": "auto",
        "current": "/usr/bin/gawk"
      }
    ]
"""
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`update-alternatives --get-selections` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['update-alternatives --get-selections']
    tags = ['command']


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
