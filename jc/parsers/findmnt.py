r"""jc - JSON Convert `findmnt` command output parser

Supports `-a`, `-l`, or no `findmnt` options.

> Note: Newer versions of `findmnt` have a JSON output option.

Usage (cli):

    $ findmnt | jc --findmnt

or

    $ jc findmnt

Usage (module):

    import jc
    result = jc.parse('findmnt', findmnt_command_output)

Schema:

    [
      {
        "target":                   string,
        "source":                   string,
        "fstype":                   string,
        "options": [
                                    string
        ],
        "kv_options": {
          "<key_name>":             string
        }
    ]

Examples:

    $ findmnt | jc --findmnt -p
    [
      {
        "target": "/",
        "source": "/dev/mapper/centos-root",
        "fstype": "xfs",
        "options": [
          "rw",
          "relatime",
          "seclabel",
          "attr2",
          "inode64",
          "noquota"
        ]
      },
      {
        "target": "/sys/fs/cgroup",
        "source": "tmpfs",
        "fstype": "tmpfs",
        "options": [
          "ro",
          "nosuid",
          "nodev",
          "noexec",
          "seclabel"
        ],
        "kv_options": {
          "mode": "755"
        }
      },
      pass
    ]

    $ findmnt | jc --findmnt -p -r
    [
      {
        "target": "/",
        "source": "/dev/mapper/centos-root",
        "fstype": "xfs",
        "options": "rw,relatime,seclabel,attr2,inode64,noquota"
      },
      {
        "target": "/sys/fs/cgroup",
        "source": "tmpfs",
        "fstype": "tmpfs",
        "options": "ro,nosuid,nodev,noexec,seclabel,mode=755"
      },
      pass
    ]
"""
import re
from typing import List, Dict
from jc.jc_types import JSONDictType
from jc.parsers.universal import simple_table_parse
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.1'
    description = '`findmnt` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['findmnt']
    tags = ['command']


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


def _replace(matchobj):
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
