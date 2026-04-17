r"""jc - JSON Convert `top -b` command output streaming parser

> This streaming parser outputs JSON Lines (cli) or returns an Iterable of
> Dictionaries (module)

Requires batch mode (`-b`).

Warning messages will be printed to `STDERR` if truncated fields are
detected. These warnings can be suppressed with the `-q` or `quiet=True`
option.

Usage (cli):

    $ top -b | jc --top-s

Usage (module):

    import jc

    result = jc.parse('top_s', top_command_output.splitlines())
    for item in result:
        # do something

Schema:

    {
      "time":                                         string,
      "uptime":                                       integer,
      "users":                                        integer,
      "load_1m":                                      float,
      "load_5m":                                      float,
      "load_15m":                                     float,
      "tasks_total":                                  integer,
      "tasks_running":                                integer,
      "tasks_sleeping":                               integer,
      "tasks_stopped":                                integer,
      "tasks_zombie":                                 integer,
      "cpu_user":                                     float,
      "cpu_sys":                                      float,
      "cpu_nice":                                     float,
      "cpu_idle":                                     float,
      "cpu_wait":                                     float,
      "cpu_hardware":                                 float,
      "cpu_software":                                 float,
      "cpu_steal":                                    float,
      "mem_unit":                                     string,
      "swap_unit":                                    string,
      "mem_total":                                    float,
      "mem_total_bytes":                              integer,
      "mem_free":                                     float,
      "mem_free_bytes":                               integer,
      "mem_used":                                     float,
      "mem_used_bytes":                               integer,
      "mem_buff_cache":                               float,
      "mem_buff_cache_bytes":                         integer,
      "swap_total":                                   float,
      "swap_total_bytes":                             integer,
      "swap_free":                                    float,
      "swap_free_bytes":                              integer,
      "swap_used":                                    float,
      "swap_used_bytes":                              integer,
      "mem_available":                                float,
      "mem_available_bytes":                          integer,
      "processes": [
        {
          "pid":                                      integer,
          "user":                                     string,
          "priority":                                 integer,
          "nice":                                     integer,
          "virtual_mem":                              float,
          "virtual_mem_unit":                         string,
          "virtual_mem_bytes":                        integer,
          "resident_mem":                             float,
          "resident_mem_unit":                        string,
          "resident_mem_bytes":                       integer,
          "shared_mem":                               float,
          "shared_mem_unit":                          string,
          "shared_mem_bytes":                         integer,
          "status":                                   string,
          "percent_cpu":                              float,
          "percent_mem":                              float,
          "time_hundredths":                          string,
          "command":                                  string,
          "parent_pid":                               integer,
          "uid":                                      integer,
          "real_uid":                                 integer,
          "real_user":                                string,
          "saved_uid":                                integer,
          "saved_user":                               string,
          "gid":                                      integer,
          "group":                                    string,
          "pgrp":                                     integer,
          "tty":                                      string,
          "tty_process_gid":                          integer,
          "session_id":                               integer,
          "thread_count":                             integer,
          "last_used_processor":                      integer,
          "time":                                     string,
          "swap":                                     float,
          "swap_unit":                                string,
          "swap_bytes":                               integer,
          "code":                                     float,
          "code_unit":                                string,
          "code_bytes":                               integer
          "data":                                     float,
          "data_unit":                                string,
          "data_bytes":                               integer,
          "major_page_fault_count":                   integer,
          "minor_page_fault_count":                   integer,
          "dirty_pages_count":                        integer,
          "sleeping_in_function":                     string,
          "flags":                                    string,
          "cgroups":                                  string,
          "supplementary_gids": [
                                                      integer
          ],
          "supplementary_groups": [
                                                      string
          ],
          "thread_gid":                               integer,
          "environment_variables": [
                                                      string
          ]
          "major_page_fault_count_delta":             integer,
          "minor_page_fault_count_delta":             integer,
          "used":                                     float,
          "used_unit":                                string,
          "used_bytes":                               integer,
          "ipc_namespace_inode":                      integer,
          "mount_namespace_inode":                    integer,
          "net_namespace_inode":                      integer,
          "pid_namespace_inode":                      integer,
          "user_namespace_inode":                     integer,
          "nts_namespace_inode":                      integer,
          "control_group_name":                       string,
          "lxc_container_name":                       string,
          "numa_node":                                integer,
          "out_of_mem_adjustment":                    integer,
          "out_of_mem_score":                         integer,
          "resident_anon_mem":                        integer,
          "resident_file_backed_mem":                 integer,
          "resident_locked_mem":                      integer,
          "resident_shared_mem":                      integer
        }
      ],

      # below object only exists if using -qq or ignore_exceptions=True
      "_jc_meta": {
        "success":      boolean,     # false if error parsing
        "error":        string,      # exists if "success" is false
        "line":         string       # exists if "success" is false
      }
    }

Examples:

    $ top -b | jc --top-s
    {"time":"11:24:50","uptime":2,"users":2,"load_1m":0.23,"load_5m":...}
    pass

    $ top -b | jc --top-s -r
    {"time":"11:24:50","uptime":"2 min","users":"2","load_1m":"0.23","lo...}
    pass
"""
from typing import List, Dict, Set, Iterable, Union
import jc.utils
from jc.streaming import (
    add_jc_meta, streaming_input_type_check, streaming_line_input_type_check, raise_or_yield
)
from jc.exceptions import ParseError
from jc.parsers.uptime import parse as parse_uptime
from jc.parsers.universal import sparse_table_parse as parse_table


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.3'
    description = '`top -b` command streaming parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    tags = ['command']
    streaming = True


__version__ = info.version


def _safe_split(string: str, path: str, delim: str = ' ', quiet=False) -> List[str]:
    pass


def _process(proc_data: Dict, idx=0, quiet=False) -> Dict:
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
