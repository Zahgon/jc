r"""jc - JSON Convert `systemctl` command output parser

Usage (cli):

    $ systemctl | jc --systemctl

or

    $ jc systemctl

Usage (module):

    import jc
    result = jc.parse('systemctl', systemctl_command_output)

Schema:

    [
      {
        "unit":          string,
        "load":          string,
        "active":        string,
        "sub":           string,
        "description":   string
      }
    ]

Examples:

    $ systemctl -a | jc --systemctl -p
    [
      {
        "unit": "proc-sys-fs-binfmt_misc.automount",
        "load": "loaded",
        "active": "active",
        "sub": "waiting",
        "description": "Arbitrary Executable File Formats File System ..."
      },
      {
        "unit": "dev-block-8:2.device",
        "load": "loaded",
        "active": "active",
        "sub": "plugged",
        "description": "LVM PV 3klkIj-w1qk-DkJi-0XBJ-y3o7-i2Ac-vHqWBM o..."
      },
      {
        "unit": "dev-cdrom.device",
        "load": "loaded",
        "active": "active",
        "sub": "plugged",
        "description": "VMware_Virtual_IDE_CDROM_Drive"
      },
      pass
    ]
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.5'
    description = '`systemctl` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['systemctl']
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
