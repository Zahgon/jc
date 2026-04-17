r"""jc - JSON Convert `uname -a` command output parser

> Note: Must use `uname -a`

Usage (cli):

    $ uname -a | jc --uname

or

    $ jc uname -a

Usage (module):

    import jc
    result = jc.parse('uname', uname_command_output)

Schema:

    {
        "kernel_name":        string,
        "node_name":          string,
        "kernel_release":     string,
        "operating_system":   string,
        "hardware_platform":  string,
        "processor":          string,
        "machine":            string,
        "kernel_version":     string
    }

Example:

    $ uname -a | jc --uname -p
    {
      "kernel_name": "Linux",
      "node_name": "user-ubuntu",
      "kernel_release": "4.15.0-65-generic",
      "operating_system": "GNU/Linux",
      "hardware_platform": "x86_64",
      "processor": "x86_64",
      "machine": "x86_64",
      "kernel_version": "#74-Ubuntu SMP Tue Sep 17 17:06:04 UTC 2019"
    }
"""
import jc.utils
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.8'
    description = '`uname -a` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'freebsd']
    magic_commands = ['uname']
    tags = ['command', 'slurpable']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured data to conform to the schema.
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

        Dictionary. Raw or processed structured data.
    """
    pass
