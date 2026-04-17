r"""jc - JSON Convert `/proc/loadavg` file parser

Usage (cli):

    $ cat /proc/loadavg | jc --proc

or

    $ jc /proc/loadavg

or

    $ cat /proc/loadavg | jc --proc-loadavg

Usage (module):

    import jc
    result = jc.parse('proc', proc_loadavg_file)

or

    import jc
    result = jc.parse('proc_loadavg', proc_loadavg_file)

Schema:

All values are integers.

    {
      "load_1m":              float,
      "load_5m":              float,
      "load_15m":             float,
      "running":              integer,
      "available":            integer,
      "last_pid":             integer
    }

Examples:

    $ cat /proc/loadavg | jc --proc -p
    {
      "load_1m": 0.0,
      "load_5m": 0.01,
      "load_15m": 0.03,
      "running": 2,
      "available": 111,
      "last_pid": 2039
    }

    $ cat /proc/loadavg | jc --proc -p -r
    {
      "load_1m": "0.00",
      "load_5m": "0.01",
      "load_15m": "0.03",
      "running": "2",
      "available": "111",
      "last_pid": "2039"
    }
"""
from typing import Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/loadavg` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    tags = ['file']
    hidden = True


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
