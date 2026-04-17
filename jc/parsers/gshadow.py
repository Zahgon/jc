r"""jc - JSON Convert `/etc/gshadow` file parser

Usage (cli):

    $ cat /etc/gshadow | jc --gshadow

Usage (module):

    import jc
    result = jc.parse('gshadow', gshadow_file_output)

Schema:

    [
      {
        "group_name":       string,
        "password":         string,
        "administrators": [
                            string
        ],
        "members": [
                            string
        ]
      }
    ]

Examples:

    $ cat /etc/gshadow | jc --gshadow -p
    [
      {
        "group_name": "root",
        "password": "*",
        "administrators": [],
        "members": []
      },
      {
        "group_name": "adm",
        "password": "*",
        "administrators": [],
        "members": [
          "syslog",
          "joeuser"
        ]
      },
      pass
    ]

    $ cat /etc/gshadow | jc --gshadow -p -r
    [
      {
        "group_name": "root",
        "password": "*",
        "administrators": [
          ""
        ],
        "members": [
          ""
        ]
      },
      {
        "group_name": "adm",
        "password": "*",
        "administrators": [
          ""
        ],
        "members": [
          "syslog",
          "joeuser"
        ]
      },
      pass
    ]
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.3'
    description = '`/etc/gshadow` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'aix', 'freebsd']
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
