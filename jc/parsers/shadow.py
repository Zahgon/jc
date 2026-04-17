r"""jc - JSON Convert `/etc/shadow` file parser

Usage (cli):

    $ sudo cat /etc/shadow | jc --shadow

Usage (module):

    import jc
    result = jc.parse('shadow', shadow_file_output)

Schema:

    [
      {
        "username":       string,
        "password":       string,
        "last_changed":   integer,
        "minimum":        integer,
        "maximum":        integer,
        "warn":           integer,
        "inactive":       integer,
        "expire":         integer
      }
    ]

Examples:

    $ sudo cat /etc/shadow | jc --shadow -p
    [
      {
        "username": "root",
        "password": "*",
        "last_changed": 18113,
        "minimum": 0,
        "maximum": 99999,
        "warn": 7,
        "inactive": null,
        "expire": null
      },
      {
        "username": "daemon",
        "password": "*",
        "last_changed": 18113,
        "minimum": 0,
        "maximum": 99999,
        "warn": 7,
        "inactive": null,
        "expire": null
      },
      {
        "username": "bin",
        "password": "*",
        "last_changed": 18113,
        "minimum": 0,
        "maximum": 99999,
        "warn": 7,
        "inactive": null,
        "expire": null
      },
      pass
    ]

    $ sudo cat /etc/shadow | jc --shadow -p -r
    [
      {
        "username": "root",
        "password": "*",
        "last_changed": "18113",
        "minimum": "0",
        "maximum": "99999",
        "warn": "7",
        "inactive": "",
        "expire": ""
      },
      {
        "username": "daemon",
        "password": "*",
        "last_changed": "18113",
        "minimum": "0",
        "maximum": "99999",
        "warn": "7",
        "inactive": "",
        "expire": ""
      },
      {
        "username": "bin",
        "password": "*",
        "last_changed": "18113",
        "minimum": "0",
        "maximum": "99999",
        "warn": "7",
        "inactive": "",
        "expire": ""
      },
      pass
    ]
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.5'
    description = '`/etc/shadow` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'aix', 'freebsd']
    tags = ['file']


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
