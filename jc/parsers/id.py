r"""jc - JSON Convert `id` command output parser

Usage (cli):

    $ id | jc --id

or

    $ jc id

Usage (module):

    import jc
    result = jc.parse('id', id_command_output)

Schema:

    {
      "uid": {
        "id":       integer,
        "name":     string
      },
      "gid": {
        "id":       integer,
        "name":     string
      },
      "groups": [
        {
          "id":     integer,
          "name":   string
        },
        {
          "id":     integer,
          "name":   string
        }
      ],
      "context": {
        "user":     string,
        "role":     string,
        "type":     string,
        "level":    string
      }
    }

Examples:

    $ id | jc --id -p
    {
      "uid": {
        "id": 1000,
        "name": "joeuser"
      },
      "gid": {
        "id": 1000,
        "name": "joeuser"
      },
      "groups": [
        {
          "id": 1000,
          "name": "joeuser"
        },
        {
          "id": 10,
          "name": "wheel"
        }
      ],
      "context": {
        "user": "unconfined_u",
        "role": "unconfined_r",
        "type": "unconfined_t",
        "level": "s0-s0:c0.c1023"
      }
    }

    $ id | jc --id -p -r
    {
      "uid": {
        "id": "1000",
        "name": "joeuser"
      },
      "gid": {
        "id": "1000",
        "name": "joeuser"
      },
      "groups": [
        {
          "id": "1000",
          "name": "joeuser"
        },
        {
          "id": "10",
          "name": "wheel"
        }
      ],
      "context": {
        "user": "unconfined_u",
        "role": "unconfined_r",
        "type": "unconfined_t",
        "level": "s0-s0:c0.c1023"
      }
    }
"""
import re
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.7'
    description = '`id` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'aix', 'freebsd']
    magic_commands = ['id']
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


def _get_item(my_list, index, default=None):
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
