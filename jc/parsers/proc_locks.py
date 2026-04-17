r"""jc - JSON Convert `/proc/locks` file parser

Usage (cli):

    $ cat /proc/locks | jc --proc

or

    $ jc /proc/locks

or

    $ cat /proc/locks | jc --proc-locks

Usage (module):

    import jc
    result = jc.parse('proc', proc_locks_file)

or

    import jc
    result = jc.parse('proc_locks', proc_locks_file)

Schema:

    [
      {
        "id":                   integer,
        "class":                string,
        "type":                 string,
        "access":               string,
        "pid":                  integer,
        "maj":                  string,
        "min":                  string,
        "inode":                integer,
        "start":                string,
        "end":                  string
      }
    ]

Examples:

    $ cat /proc/locks | jc --proc -p
    [
      {
        "id": 1,
        "class": "POSIX",
        "type": "ADVISORY",
        "access": "WRITE",
        "pid": 877,
        "maj": "00",
        "min": "19",
        "inode": 812,
        "start": "0",
        "end": "EOF"
      },
      {
        "id": 2,
        "class": "FLOCK",
        "type": "ADVISORY",
        "access": "WRITE",
        "pid": 854,
        "maj": "00",
        "min": "19",
        "inode": 805,
        "start": "0",
        "end": "EOF"
      },
      pass
    ]

    $ cat /proc/locks | jc --proc-locks -p -r
    [
      {
        "id": "1",
        "class": "POSIX",
        "type": "ADVISORY",
        "access": "WRITE",
        "pid": "877",
        "maj": "00",
        "min": "19",
        "inode": "812",
        "start": "0",
        "end": "EOF"
      },
      {
        "id": "2",
        "class": "FLOCK",
        "type": "ADVISORY",
        "access": "WRITE",
        "pid": "854",
        "maj": "00",
        "min": "19",
        "inode": "805",
        "start": "0",
        "end": "EOF"
      },
      pass
    ]
"""
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/locks` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    tags = ['file']
    hidden = True


__version__ = info.version


def _process(proc_data: List[Dict]) -> List[Dict]:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured to conform to the schema.
    """
    pass


def parse(
    data: str,
    raw: bool = False,
    quiet: bool = False
) -> List[Dict]:
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
