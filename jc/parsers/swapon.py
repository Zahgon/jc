r"""jc - JSON Convert `swapon` command output parser

Usage (cli):

    $ swapon | jc --swapon

or

    $ jc swapon

Usage (module):

    import jc
    result = jc.parse('swapon', swapon_command_output)

Schema:

    [
      {
        "name":             string,
        "type":             string,
        "size":             integer,
        "used":             integer,
        "priority":         integer
      }
    ]

Example:

    $ swapon | jc --swapon
    [
      {
        "name": "/swapfile",
        "type": "file",
        "size": 1073741824,
        "used": 0,
        "priority": -2
      }
    ]
"""
from enum import Enum
from jc.exceptions import ParseError
import jc.utils
from typing import List, Dict, Union


class info:
    """Provides parser metadata (version, author, etc.)"""
    version = "1.0"
    description = "`swapon` command parser"
    author = "Roey Darwish Dror"
    author_email = "roey.ghost@gmail.com"
    compatible = ["linux", "freebsd"]
    magic_commands = ["swapon"]
    tags = ["command"]


__version__ = info.version

_Value = Union[str, int]
_Entry = Dict[str, _Value]


class _Column(Enum):
    NAME = "name"
    TYPE = "type"
    SIZE = "size"
    USED = "used"
    PRIO = "priority"
    LABEL = "label"
    UUID = "uuid"

    @classmethod
    def from_header(cls, header: str) -> "_Column":
        pass


def _parse_size(size: str) -> int:
    pass


def _value(value: str, column: _Column) -> _Value:
    pass


def _process(proc_data: List[Dict]) -> List[Dict]:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured to conform to the schema.
    """
    pass


def parse(data: str, raw: bool = False, quiet: bool = False) -> List[_Entry]:
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
