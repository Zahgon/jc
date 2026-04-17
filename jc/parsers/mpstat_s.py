r"""jc - JSON Convert `mpstat` command output streaming parser

> This streaming parser outputs JSON Lines (cli) or returns an Iterable of
> Dictionaries (module)

> Note: Latest versions of `mpstat` support JSON output (v11.5.1+)

Usage (cli):

    $ mpstat | jc --mpstat-s

Usage (module):

    import jc

    result = jc.parse('mpstat_s', mpstat_command_output.splitlines())
    for item in result:
        # do something

Schema:

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
      "rcu_s":              float,

      # below object only exists if using -qq or ignore_exceptions=True
      "_jc_meta": {
        "success":          boolean,     # false if error parsing
        "error":            string,      # exists if "success" is false
        "line":             string       # exists if "success" is false
      }
    }

Examples:

    $ mpstat -A | jc --mpstat-s
    {"cpu":"all","percent_usr":0.22,"percent_nice":0.0,"percent_sys":...}
    {"cpu":"0","percent_usr":0.22,"percent_nice":0.0,"percent_sys":0....}
    {"cpu":"all","intr_s":37.61,"type":"interrupts","time":"03:15:06 PM"}
    pass

    $ mpstat -A | jc --mpstat-s -r
    {"cpu":"all","percent_usr":"0.22","percent_nice":"0.00","percent_...}
    {"cpu":"0","percent_usr":"0.22","percent_nice":"0.00","percent_sy...}
    {"cpu":"all","intr_s":"37.61","type":"interrupts","time":"03:15:06 PM"}
    pass
"""
from typing import Dict, Iterable, Union
import jc.utils
from jc.parsers.universal import simple_table_parse
from jc.streaming import (
    add_jc_meta, streaming_input_type_check, streaming_line_input_type_check, raise_or_yield
)
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.1'
    description = '`mpstat` command streaming parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    tags = ['command']
    streaming = True


__version__ = info.version


def _process(proc_data: Dict) -> Dict:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured data to conform to the schema.
    """
    pass


@add_jc_meta
def parse(
    data: Iterable[str],
    raw: bool = False,
    quiet: bool = False,
    ignore_exceptions: bool = False
) -> Union[Iterable[Dict], tuple]:
    """
    Main text parsing generator function. Returns an iterable object.

    Parameters:

        data:              (iterable)  line-based text data to parse
                                       (e.g. sys.stdin or str.splitlines())

        raw:               (boolean)   unprocessed output if True
        quiet:             (boolean)   suppress warning messages if True
        ignore_exceptions: (boolean)   ignore parsing exceptions if True

    Returns:

        Iterable of Dictionaries
    """
    pass
