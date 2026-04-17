r"""jc - JSON Convert `/proc/stat` file parser

Usage (cli):

    $ cat /proc/stat | jc --proc

or

    $ jc /proc/stat

or

    $ cat /proc/stat | jc --proc-stat

Usage (module):

    import jc
    result = jc.parse('proc', proc_stat_file)

or

    import jc
    result = jc.parse('proc_stat', proc_stat_file)

Schema:

    {
      "cpu": {
        "user":                         integer,
        "nice":                         integer,
        "system":                       integer,
        "idle":                         integer,
        "iowait":                       integer,
        "irq":                          integer,
        "softirq":                      integer,
        "steal":                        integer,
        "guest":                        integer,
        "guest_nice":                   integer
      },
      "cpu<number>": {
        "user":                         integer,
        "nice":                         integer,
        "system":                       integer,
        "idle":                         integer,
        "iowait":                       integer,
        "irq":                          integer,
        "softirq":                      integer,
        "steal":                        integer,
        "guest":                        integer,
        "guest_nice":                   integer
      },
      "interrupts": [
                                        integer
      ],
      "context_switches":               integer,
      "boot_time":                      integer,
      "processes":                      integer,
      "processes_running":              integer,
      "processes_blocked":              integer,
      "softirq": [
                                        integer
      ]
    }

Examples:

    $ cat /proc/stat | jc --proc -p
    {
      "cpu": {
        "user": 6002,
        "nice": 152,
        "system": 8398,
        "idle": 3444436,
        "iowait": 448,
        "irq": 0,
        "softirq": 1174,
        "steal": 0,
        "guest": 0,
        "guest_nice": 0
      },
      "cpu0": {
        "user": 2784,
        "nice": 137,
        "system": 4367,
        "idle": 1732802,
        "iowait": 225,
        "irq": 0,
        "softirq": 221,
        "steal": 0,
        "guest": 0,
        "guest_nice": 0
      },
      "cpu1": {
        "user": 3218,
        "nice": 15,
        "system": 4031,
        "idle": 1711634,
        "iowait": 223,
        "irq": 0,
        "softirq": 953,
        "steal": 0,
        "guest": 0,
        "guest_nice": 0
      },
      "interrupts": [
        2496709,
        18,
        73,
        0,
        0,
        pass
      ],
      "context_switches": 4622716,
      "boot_time": 1662154781,
      "processes": 9831,
      "processes_running": 1,
      "processes_blocked": 0,
      "softirq": [
        3478985,
        35230,
        1252057,
        3467,
        128583,
        51014,
        0,
        171199,
        1241297,
        0,
        596138
      ]
    }
"""
from typing import Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/stat` file parser'
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
