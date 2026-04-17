r"""jc - JSON Convert `hash` command output parser

Usage (cli):

    $ hash | jc --hash

Usage (module):

    import jc
    result = jc.parse('hash', hash_command_output)

Schema:

    [
      {
        "command":       string,
        "hits":          integer
      }
    ]

Examples:

    $ hash | jc --hash -p
    [
      {
        "hits": 2,
        "command": "/bin/cat"
      },
      {
        "hits": 1,
        "command": "/bin/ls"
      }
    ]
"""
import jc.utils
import jc.parsers.universal


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.4'
    description = '`hash` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'aix', 'freebsd']
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
