r"""jc - JSON Convert `systemctl list-unit-files` command output
parser

Usage (cli):

    $ systemctl list-unit-files | jc --systemctl-luf

or

    $ jc systemctl list-unit-files

Usage (module):

    import jc
    result = jc.parse('systemctl_luf', systemctl_luf_command_output)

Schema:

    [
      {
        "unit_file":   string,
        "state":       string
      }
    ]

Examples:

    $ systemctl list-unit-files | jc --systemctl-luf -p
    [
      {
        "unit_file": "proc-sys-fs-binfmt_misc.automount",
        "state": "static"
      },
      {
        "unit_file": "dev-hugepages.mount",
        "state": "static"
      },
      {
        "unit_file": "dev-mqueue.mount",
        "state": "static"
      },
      pass
    ]
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.5'
    description = '`systemctl list-unit-files` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['systemctl list-unit-files']
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
