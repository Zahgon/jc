r"""jc - JSON Convert `df` command output parser

Values are normalized to bytes when using `df -h`.

Usage (cli):

    $ df | jc --df

or

    $ jc df

Usage (module):

    import jc
    result = jc.parse('df', df_command_output)

Schema:

    [
      {
        "filesystem":        string,
        "size":              integer,
        "1k_blocks":         integer,
        "512_blocks":        integer,
        "used":              integer,
        "available":         integer,
        "capacity_percent":  integer,
        "ifree":             integer,
        "iused":             integer,
        "use_percent":       integer,
        "iused_percent":     integer,
        "mounted_on":        string
      }
    ]

Examples:

    $ df | jc --df -p
    [
      {
        "filesystem": "devtmpfs",
        "1k_blocks": 1918820,
        "used": 0,
        "available": 1918820,
        "use_percent": 0,
        "mounted_on": "/dev"
      },
      {
        "filesystem": "tmpfs",
        "1k_blocks": 1930668,
        "used": 0,
        "available": 1930668,
        "use_percent": 0,
        "mounted_on": "/dev/shm"
      },
      {
        "filesystem": "tmpfs",
        "1k_blocks": 1930668,
        "used": 11800,
        "available": 1918868,
        "use_percent": 1,
        "mounted_on": "/run"
      },
      pass
    ]

    $ df | jc --df -p -r
    [
      {
        "filesystem": "devtmpfs",
        "1k_blocks": "1918820",
        "used": "0",
        "available": "1918820",
        "use_percent": "0%",
        "mounted_on": "/dev"
      },
      {
        "filesystem": "tmpfs",
        "1k_blocks": "1930668",
        "used": "0",
        "available": "1930668",
        "use_percent": "0%",
        "mounted_on": "/dev/shm"
      },
      {
        "filesystem": "tmpfs",
        "1k_blocks": "1930668",
        "used": "11800",
        "available": "1918868",
        "use_percent": "1%",
        "mounted_on": "/run"
      },
      pass
    ]
"""
import hashlib
import jc.utils
import jc.parsers.universal


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '2.1'
    description = '`df` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'freebsd']
    magic_commands = ['df']
    tags = ['command']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured data to conform to the schema:
    """
    pass


def _long_filesystem_hash(header, line):
    """
    Returns truncated hash and value of the filesystem field if it is too
    long for the column.
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
