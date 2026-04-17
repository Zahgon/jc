r"""jc - JSON Convert `update-alternatives --query` command output parser

Usage (cli):

    $ update-alternatives --query | jc --update-alt-q

or

    $ jc update-alternatives --query

Usage (module):

    import jc
    result = jc.parse('update_alt_q',
                      update_alternatives_query_command_output)

Schema:

    {
      "name":                 string,
      "link":                 string,
      "slaves": [
        {
          "name":             string,
          "path":             string
        }
      ],
      "status":               string,
      "best":                 string,
      "value":                string,   # (null if 'none')
      "alternatives": [
        {
          "alternative":      string,
          "priority":         integer,
          "slaves": [
            {
              "name":         string,
              "path":         string
            }
          ]
        }
      ]
    }

Examples:

    $ update-alternatives --query editor | jc --update-alt-q -p
    {
      "name": "editor",
      "link": "/usr/bin/editor",
      "slaves": [
        {
          "name": "editor.1.gz",
          "path": "/usr/share/man/man1/editor.1.gz"
        },
        {
          "name": "editor.da.1.gz",
          "path": "/usr/share/man/da/man1/editor.1.gz"
        }
      ],
      "status": "auto",
      "best": "/bin/nano",
      "value": "/bin/nano",
      "alternatives": [
        {
          "alternative": "/bin/ed",
          "priority": -100,
          "slaves": [
            {
              "name": "editor.1.gz",
              "path": "/usr/share/man/man1/ed.1.gz"
            }
          ]
        },
        {
          "alternative": "/bin/nano",
          "priority": 40,
          "slaves": [
            {
              "name": "editor.1.gz",
              "path": "/usr/share/man/man1/nano.1.gz"
            }
          ]
        }
      ]
    }

    $ update-alternatives --query | jc --update-alt-q -p -r
    {
      "name": "editor",
      "link": "/usr/bin/editor",
      "slaves": [
        {
          "name": "editor.1.gz",
          "path": "/usr/share/man/man1/editor.1.gz"
        },
        {
          "name": "editor.da.1.gz",
          "path": "/usr/share/man/da/man1/editor.1.gz"
        }
      ],
      "status": "auto",
      "best": "/bin/nano",
      "value": "/bin/nano",
      "alternatives": [
        {
          "alternative": "/bin/ed",
          "priority": "-100",
          "slaves": [
            {
              "name": "editor.1.gz",
              "path": "/usr/share/man/man1/ed.1.gz"
            }
          ]
        },
        {
          "alternative": "/bin/nano",
          "priority": "40",
          "slaves": [
            {
              "name": "editor.1.gz",
              "path": "/usr/share/man/man1/nano.1.gz"
            }
          ]
        }
      ]
    }
"""
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = '`update-alternatives --query` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['update-alternatives --query']
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
