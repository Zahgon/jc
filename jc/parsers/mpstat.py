r"""jc - JSON Convert `mpstat` command output parser

> Note: Latest versions of `mpstat` support JSON output (v11.5.1+)

Usage (cli):

    $ mpstat | jc --mpstat

or

    $ jc mpstat

Usage (module):

    import jc
    result = jc.parse('mpstat', mpstat_command_output)

Schema:

    [
      {
        "type":               string,
        "time":               string,
        "cpu":                string,
        "node":               string,
        "average":            boolean,
        "percent_usr":        float,
        "percent_nice":       float,
        "percent_sys":        float,
        "percent_iowait":     float,
        "percent_irq":        float,
        "percent_soft":       float,
        "percent_steal":      float,
        "percent_guest":      float,
        "percent_gnice":      float,
        "percent_idle":       float,
        "intr_s":             float,
        "<x>_s":              float,      # <x> is an integer
        "nmi_s":              float,
        "loc_s":              float,
        "spu_s":              float,
        "pmi_s":              float,
        "iwi_s":              float,
        "rtr_s":              float,
        "res_s":              float,
        "cal_s":              float,
        "tlb_s":              float,
        "trm_s":              float,
        "thr_s":              float,
        "dfr_s":              float,
        "mce_s":              float,
        "mcp_s":              float,
        "err_s":              float,
        "mis_s":              float,
        "pin_s":              float,
        "npi_s":              float,
        "piw_s":              float,
        "hi_s":               float,
        "timer_s":            float,
        "net_tx_s":           float,
        "net_rx_s":           float,
        "block_s":            float,
        "irq_poll_s":         float,
        "block_iopoll_s":     float,
        "tasklet_s":          float,
        "sched_s":            float,
        "hrtimer_s":          float,
        "rcu_s":              float
      }
    ]

Examples:

    $ mpstat | jc --mpstat -p
    [
      {
        "cpu": "all",
        "percent_usr": 12.94,
        "percent_nice": 0.0,
        "percent_sys": 26.42,
        "percent_iowait": 0.43,
        "percent_irq": 0.0,
        "percent_soft": 0.16,
        "percent_steal": 0.0,
        "percent_guest": 0.0,
        "percent_gnice": 0.0,
        "percent_idle": 60.05,
        "type": "cpu",
        "time": "01:58:14 PM"
      }
    ]

    $ mpstat | jc --mpstat -p -r
    [
      {
        "cpu": "all",
        "percent_usr": "12.94",
        "percent_nice": "0.00",
        "percent_sys": "26.42",
        "percent_iowait": "0.43",
        "percent_irq": "0.00",
        "percent_soft": "0.16",
        "percent_steal": "0.00",
        "percent_guest": "0.00",
        "percent_gnice": "0.00",
        "percent_idle": "60.05",
        "type": "cpu",
        "time": "01:58:14 PM"
      }
    ]
"""
from typing import List, Dict
import jc.utils
from jc.parsers.universal import simple_table_parse


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.1'
    description = '`mpstat` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['mpstat']
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
