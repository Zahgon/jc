r"""jc - JSON Convert `/proc/<pid>/mountinfo` file parser

Usage (cli):

    $ cat /proc/1/mountinfo | jc --proc

or

    $ jc /proc/1/mountinfo

or

    $ cat /proc/1/mountinfo | jc --proc-pid-mountinfo

Usage (module):

    import jc
    result = jc.parse('proc', proc_pid_mountinfo_file)

or

    import jc
    result = jc.parse('proc_pid_mountinfo', proc_pid_mountinfo_file)

Schema:

    [
      {
        "mount_id":                 integer,
        "parent_id":                integer,
        "maj":                      integer,
        "min":                      integer,
        "root":                     string,
        "mount_point":              string,
        "mount_options": [
                                    string
        ],
        "optional_fields": {                   # [0]
          "<key>":                  integer    # [1]
        },
        "fs_type":                  string,
        "mount_source":             string,
        "super_options": [
                                    integer    # [2]
        ],
        "super_options_fields": {
          "<key>":                  string
        }
      }
    ]

    [0] if empty, then private mount
    [1] unbindable will always have a value of 0
    [2] integer conversions are attempted. Use --raw or raw=True for
        original string values.

Examples:

    $ cat /proc/1/mountinfo | jc --proc -p
    [
      {
        "mount_id": 24,
        "parent_id": 30,
        "maj": 0,
        "min": 22,
        "root": "/",
        "mount_point": "/sys",
        "mount_options": [
          "rw",
          "nosuid",
          "nodev",
          "noexec",
          "relatime"
        ],
        "optional_fields": {
          "master": 1,
          "shared": 7
        },
        "fs_type": "sysfs",
        "mount_source": "sysfs",
        "super_options": [
          "rw"
        ]
      },
      {
        "mount_id": 25,
        "parent_id": 30,
        "maj": 0,
        "min": 23,
        "root": "/",
        "mount_point": "/proc",
        "mount_options": [
          "rw",
          "nosuid",
          "nodev",
          "noexec",
          "relatime"
        ],
        "optional_fields": {
          "shared": 14
        },
        "fs_type": "proc",
        "mount_source": "proc",
        "super_options": [
          "rw"
        ]
      },
      pass
    ]

    $ cat /proc/1/mountinfo | jc --proc-pid-mountinfo -p -r
    [
      {
        "mount_id": "24",
        "parent_id": "30",
        "maj": "0",
        "min": "22",
        "root": "/",
        "mount_point": "/sys",
        "mount_options": "rw,nosuid,nodev,noexec,relatime",
        "optional_fields": "master:1 shared:7 ",
        "fs_type": "sysfs",
        "mount_source": "sysfs",
        "super_options": "rw"
      },
      {
        "mount_id": "25",
        "parent_id": "30",
        "maj": "0",
        "min": "23",
        "root": "/",
        "mount_point": "/proc",
        "mount_options": "rw,nosuid,nodev,noexec,relatime",
        "optional_fields": "shared:14 ",
        "fs_type": "proc",
        "mount_source": "proc",
        "super_options": "rw"
      },
      pass
    ]
"""
import re
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/<pid>/mountinfo` file parser'
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
