r"""jc - JSON Convert `du` command output parser

The `du -h` option is not supported with the default output. If you
would like to use `du -h` or other options that change the output, be sure
to use `jc --raw` (cli) or `raw=True` (module).

Usage (cli):

    $ du | jc --du

or

    $ jc du

Usage (module):

    import jc
    result = jc.parse('du', du_command_output)

Schema:

    [
      {
        "size":     integer,
        "name":     string
      }
    ]

Examples:

    $ du /usr | jc --du -p
    [
      {
        "size": 104608,
        "name": "/usr/bin"
      },
      {
        "size": 56,
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      {
        "size": 0,
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      {
        "size": 0,
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      {
        "size": 0,
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      {
        "size": 1008,
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      pass
    ]

    $ du /usr | jc --du -p -r
    [
      {
        "size": "104608",
        "name": "/usr/bin"
      },
      {
        "size": "56",
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      {
        "size": "0",
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      {
        "size": "0",
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      {
        "size": "0",
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      {
        "size": "1008",
        "name": "/usr/standalone/firmware/iBridge1_1Customer.bundle/..."
      },
      pass
    ]
"""
import jc.utils
import jc.parsers.universal


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.6'
    description = '`du` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'aix', 'freebsd']
    magic_commands = ['du']
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
