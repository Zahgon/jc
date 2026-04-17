r"""jc - JSON Convert `finger` command output parser

Supports `-s` output option. Does not support the `-l` detail option.

Usage (cli):

    $ finger | jc --finger

or

    $ jc finger

Usage (module):

    import jc
    result = jc.parse('finger', finger_command_output)

Schema:

    [
      {
        "login":                string,
        "name":                 string,
        "tty":                  string,
        "idle":                 string,     # null if empty
        "login_time":           string,
        "details":              string,
        "tty_writeable":        boolean,
        "idle_minutes":         integer,
        "idle_hours":           integer,
        "idle_days":            integer,
        "total_idle_minutes":   integer
      }
    ]

Examples:

    $ finger | jc --finger -p
    [
      {
        "login": "jdoe",
        "name": "John Doe",
        "tty": "tty1",
        "idle": "14d",
        "login_time": "Mar 22 21:14",
        "tty_writeable": false,
        "idle_minutes": 0,
        "idle_hours": 0,
        "idle_days": 14,
        "total_idle_minutes": 20160
      },
      {
        "login": "jdoe",
        "name": "John Doe",
        "tty": "pts/0",
        "idle": null,
        "login_time": "Apr  5 15:33",
        "details": "(192.168.1.22)",
        "tty_writeable": true,
        "idle_minutes": 0,
        "idle_hours": 0,
        "idle_days": 0,
        "total_idle_minutes": 0
      },
      pass
    ]

    $ finger | jc --finger -p -r
    [
      {
        "login": "jdoe",
        "name": "John Doe",
        "tty": "*tty1",
        "idle": "14d",
        "login_time": "Mar 22 21:14"
      },
      {
        "login": "jdoe",
        "name": "John Doe",
        "tty": "pts/0",
        "idle": null,
        "login_time": "Apr  5 15:33",
        "details": "(192.168.1.22)"
      },
      pass
    ]
"""
import re
import jc.utils
import jc.parsers.universal


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = '`finger` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'freebsd']
    magic_commands = ['finger']
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
