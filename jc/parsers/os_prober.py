r"""jc - JSON Convert `os-prober` command output parser

Usage (cli):

    $ os-prober | jc --os-prober

or

    $ jc os-prober

Usage (module):

    import jc
    result = jc.parse('os_prober', os_prober_command_output)

Schema:

    {
      "partition":              string,
      "efi_bootmgr":            string,  # [0]
      "name":                   string,
      "short_name":             string,
      "type":                   string
    }

    [0] only exists if an EFI boot manager is detected

Examples:

    $ os-prober | jc --os-prober -p
    {
      "partition": "/dev/sda1",
      "name": "Windows 10",
      "short_name": "Windows",
      "type": "chain"
    }
"""
from typing import Dict
from jc.jc_types import JSONDictType
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = '`os-prober` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['os-prober']
    tags = ['command', 'slurpable']


__version__ = info.version


def _process(proc_data: JSONDictType) -> JSONDictType:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

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
