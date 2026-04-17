r"""jc - JSON Convert `pidstat -H` command output parser

Must use the `-H` (or `-h`, if `-H` is not available) option in `pidstat`.
All other `pidstat` options are supported in combination with this option.

Usage (cli):

    $ pidstat -H | jc --pidstat

or

    $ jc pidstat -H

Usage (module):

    import jc
    result = jc.parse('pidstat', pidstat_command_output)

Schema:

    [
      {
        "time":             integer,
        "uid":              integer,
        "pid":              integer,
        "percent_usr":      float,
        "percent_system":   float,
        "percent_guest":    float,
        "percent_cpu":      float,
        "cpu":              integer,
        "minflt_s":         float,
        "majflt_s":         float,
        "vsz":              integer,
        "rss":              integer,
        "percent_mem":      float,
        "stksize":          integer,
        "stkref":           integer,
        "kb_rd_s":          float,
        "kb_wr_s":          float,
        "kb_ccwr_s":        float,
        "cswch_s":          float,
        "nvcswch_s":        float,
        "usr_ms":           integer,
        "system_ms":        integer,
        "guest_ms":         integer,
        "command":          string
      }
    ]

Examples:

    $ pidstat -Hl | jc --pidstat -p
    [
      {
        "time": 1646859134,
        "uid": 0,
        "pid": 1,
        "percent_usr": 0.0,
        "percent_system": 0.03,
        "percent_guest": 0.0,
        "percent_cpu": 0.03,
        "cpu": 0,
        "command": "/usr/lib/systemd/systemd --switched-root --system..."
      },
      {
        "time": 1646859134,
        "uid": 0,
        "pid": 6,
        "percent_usr": 0.0,
        "percent_system": 0.0,
        "percent_guest": 0.0,
        "percent_cpu": 0.0,
        "cpu": 0,
        "command": "ksoftirqd/0"
      },
      {
        "time": 1646859134,
        "uid": 0,
        "pid": 2263,
        "percent_usr": 0.0,
        "percent_system": 0.0,
        "percent_guest": 0.0,
        "percent_cpu": 0.0,
        "cpu": 0,
        "command": "kworker/0:0"
      }
    ]

    $ pidstat -Hl | jc --pidstat -p -r
    [
      {
        "time": "1646859134",
        "uid": "0",
        "pid": "1",
        "percent_usr": "0.00",
        "percent_system": "0.03",
        "percent_guest": "0.00",
        "percent_cpu": "0.03",
        "cpu": "0",
        "command": "/usr/lib/systemd/systemd --switched-root --system..."
      },
      {
        "time": "1646859134",
        "uid": "0",
        "pid": "6",
        "percent_usr": "0.00",
        "percent_system": "0.00",
        "percent_guest": "0.00",
        "percent_cpu": "0.00",
        "cpu": "0",
        "command": "ksoftirqd/0"
      },
      {
        "time": "1646859134",
        "uid": "0",
        "pid": "2263",
        "percent_usr": "0.00",
        "percent_system": "0.00",
        "percent_guest": "0.00",
        "percent_cpu": "0.00",
        "cpu": "0",
        "command": "kworker/0:0"
      }
    ]
"""
from typing import List, Dict
import jc.utils
from jc.parsers.universal import simple_table_parse
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.3'
    description = '`pidstat -H` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['pidstat']
    tags = ['command']


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


def normalize_header(header: str) -> str:
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
