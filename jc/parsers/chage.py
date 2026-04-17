r"""jc - JSON Convert `chage --list` command output parser

Supports `chage -l <username>` or `chage --list <username>`

Usage (cli):

    $ chage -l johndoe | jc --chage

or

    $ jc chage -l johndoe

Usage (module):

    import jc
    result = jc.parse('chage', chage_command_output)

Schema:

    {
      "password_last_changed":                      string,
      "password_expires":                           string,
      "password_inactive":                          string,
      "account_expires":                            string,
      "min_days_between_password_change":           integer,
      "max_days_between_password_change":           integer,
      "warning_days_before_password_expires":       integer
    }

Examples:

    $ chage --list joeuser | jc --chage -p
    {
      "password_last_changed": "never",
      "password_expires": "never",
      "password_inactive": "never",
      "account_expires": "never",
      "min_days_between_password_change": 0,
      "max_days_between_password_change": 99999,
      "warning_days_before_password_expires": 7
    }

    $ chage --list joeuser | jc --chage -p -r
    {
      "password_last_changed": "never",
      "password_expires": "never",
      "password_inactive": "never",
      "account_expires": "never",
      "min_days_between_password_change": "0",
      "max_days_between_password_change": "99999",
      "warning_days_before_password_expires": "7"
    }
"""
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.1'
    description = '`chage --list` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['chage --list', 'chage -l']
    tags = ['command']


__version__ = info.version


def _process(proc_data: Dict) -> Dict:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured to conform to the schema.
    """
    pass


def parse(
    data: str,
    raw: bool = False,
    quiet: bool = False
) -> Dict:
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
