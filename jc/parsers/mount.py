r"""jc - JSON Convert `mount` command output parser

Usage (cli):

    $ mount | jc --mount

or

    $ jc mount

Usage (module):

    import jc
    result = jc.parse('mount', mount_command_output)

Schema:

    [
      {
        "filesystem":       string,
        "mount_point":      string,
        "type":             string,
        "options": [
                            string
        ]
      }
    ]

Example:

    $ mount | jc --mount -p
    [
      {
        "filesystem": "sysfs",
        "mount_point": "/sys",
        "type": "sysfs",
        "options": [
          "rw",
          "nosuid",
          "nodev",
          "noexec",
          "relatime"
        ]
      },
      {
        "filesystem": "proc",
        "mount_point": "/proc",
        "type": "proc",
        "options": [
          "rw",
          "nosuid",
          "nodev",
          "noexec",
          "relatime"
        ]
      },
      {
        "filesystem": "udev",
        "mount_point": "/dev",
        "type": "devtmpfs",
        "options": [
          "rw",
          "nosuid",
          "relatime",
          "size=977500k",
          "nr_inodes=244375",
          "mode=755"
        ]
      },
      pass
    ]
"""
import re
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.11'
    description = '`mount` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'freebsd', 'aix']
    magic_commands = ['mount']
    tags = ['command']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured data to conform to the schema.
    """
    pass


def _osx_parse(data):
    pass


def _linux_parse(data):
    pass

def _aix_parse(data):
    pass


def parse(data, raw=False, quiet=False):
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
