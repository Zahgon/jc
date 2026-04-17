r"""jc - JSON Convert `ping` command output streaming parser

> This streaming parser outputs JSON Lines (cli) or returns an Iterable of
> Dictionaries (module)

Supports `ping` and `ping6` output.

Usage (cli):

    $ ping 1.2.3.4 | jc --ping-s

> Note: When piping `jc` converted `ping` output to other processes it may
> appear the output is hanging due to the OS pipe buffers. This is because
> `ping` output is too small to quickly fill up the buffer. Use the `-u`
> option to unbuffer the `jc` output if you would like immediate output.
> See the [readme](https://github.com/kellyjonbrazil/jc/tree/master#unbuffering-output)
> for more information.

Usage (module):

    import jc

    result = jc.parse('ping_s', ping_command_output.splitlines())
    for item in result:
        # do something

Schema:

    {
      "type":                       string,   # [0]
      "source_ip":                  string,
      "destination_ip":             string,
      "sent_bytes":                 integer,
      "pattern":                    string,   # null if not set
      "destination":                string,
      "timestamp":                  float,
      "response_bytes":             integer,
      "response_ip":                string,
      "icmp_seq":                   integer,
      "ttl":                        integer,
      "time_ms":                    float,
      "duplicate":                  boolean,
      "packets_transmitted":        integer,
      "packets_received":           integer,
      "packet_loss_percent":        float,
      "duplicates":                 integer,
      "errors":                     integer,  # null if not set
      "corrupted":                  integer,  # null if not set
      "round_trip_ms_min":          float,    # null if not set
      "round_trip_ms_avg":          float,    # null if not set
      "round_trip_ms_max":          float,    # null if not set
      "round_trip_ms_stddev":       float,    # null if not set

      # below object only exists if using -qq or ignore_exceptions=True
      "_jc_meta": {
        "success":                  boolean,  # false if error parsing
        "error":                    string,   # exists if "success" is false
        "line":                     string    # exists if "success" is false
      }
    }

    [0] 'reply', 'timeout', 'summary', etc. See `_error_type.type_map`
        for all options.

Examples:

    $ ping 1.1.1.1 | jc --ping-s
    {"type":"reply","destination_ip":"1.1.1.1","sent_bytes":56,"patte...}
    {"type":"reply","destination_ip":"1.1.1.1","sent_bytes":56,"patte...}
    {"type":"reply","destination_ip":"1.1.1.1","sent_bytes":56,"patte...}
    pass

    $ ping 1.1.1.1 | jc --ping-s -r
    {"type":"reply","destination_ip":"1.1.1.1","sent_bytes":"56","patte...}
    {"type":"reply","destination_ip":"1.1.1.1","sent_bytes":"56","patte...}
    {"type":"reply","destination_ip":"1.1.1.1","sent_bytes":"56","patte...}
    pass
"""
import re
import string
import ipaddress
import jc.utils
from jc.streaming import (
    add_jc_meta, streaming_input_type_check, streaming_line_input_type_check, raise_or_yield
)
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.6'
    description = '`ping` and `ping6` command streaming parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'freebsd']
    tags = ['command']
    streaming = True


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured data to conform to the schema.
    """
    pass


class _state:
    os_detected = None
    linux = None
    bsd = None
    ipv4 = None
    source_ip = None
    hostname = None
    destination_ip = None
    sent_bytes = None
    pattern = None
    footer = False
    packets_transmitted = None
    packets_received = None
    packet_loss_percent = None
    time_ms = None
    duplicates = None
    corrupted = None
    errors = None
    round_trip_ms_min = None
    round_trip_ms_avg = None
    round_trip_ms_max = None
    round_trip_ms_stddev = None


def _ipv6_in(line):
    pass


def _error_type_v4(line):
    # from https://github.com/dgibson/iputils/blob/master/ping.c
    # https://android.googlesource.com/platform/external/ping/+/8fc3c91cf9e7f87bc20b9e6d3ea2982d87b70d9a/ping.c
    # https://opensource.apple.com/source/network_cmds/network_cmds-328/ping.tproj/ping.c
    pass


def _error_type_v6(line):
    pass


def _bsd_parse(line, s):
    pass


def _linux_parse(line, s):
    """
    Linux ping line parsing function.

    Parameters:

        line:        (string)        line of text data to parse
        s:           (state object)  global state

    Returns:

        Dictionary. Raw structured data.
    """
    pass


@add_jc_meta
def parse(data, raw=False, quiet=False, ignore_exceptions=False):
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
