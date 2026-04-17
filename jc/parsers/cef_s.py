r"""jc - JSON Convert CEF string output streaming parser

> This streaming parser outputs JSON Lines (cli) or returns an Iterable of
> Dictionaries (module)

This parser conforms to the Microfocus Arcsight CEF specification.

This parser will accept a single CEF string or multiple CEF string lines.
Any text before "CEF" will be ignored. Syslog and CEF escaped characters
(`\\`, `\\"`, `\\]`, `\\|`, `\\=`, `\\%`, `\\#`, `\\n`, and `\\r`) are
unescaped.

Extended fields, as defined in the CEF specification, are relabeled
and the values are converted to their respective types. Extra naive and
UTC epoch timestamps are added where appropriate per the CEF specification.

A warning message to `STDERR` will be printed if an unparsable line is found
unless `--quiet` or `quiet=True` is used.

To preserve escaping and original keynames and to prevent type conversions
use the `--raw` CLI option or `raw=True` param in the `parse()` function.

Usage (cli):

    $ echo 'CEF:0|Vendor|Product|3.2.0|1|SYSTEM|1|... | jc --cef-s

Usage (module):

    import jc

    result = jc.parse('cef_s', cef_command_output.splitlines())
    for item in result:
        # do something

Schema:

See: https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-8.3/cef-implementation-standard/Content/CEF/Chapter%201%20What%20is%20CEF.htm

> Note: Special characters in key names will be converted to underscores.

    {
      "deviceVendor":                   string,
      "deviceProduct":                  string,
      "deviceVersion":                  string,
      "deviceEventClassId":             string,
      "deviceEventClassIdNum":          integer/null,
      "name":                           string,
      "agentSeverity":                  string/integer,
      "agentSeverityString":            string,
      "agentSeverityNum":               integer/null,
      "CEFVersion":                     integer,
      <extended fields>                 string/integer/float,  # [0]
      <extended fields>"_epoch":        integer/null,  # [1]
      <extended fields>"_epoch_utc":    integer/null,  # [2]
      <custom fields>                   string,
      "unparsable":                     string  # [3]

      # below object only exists if using -qq or ignore_exceptions=True
      "_jc_meta": {
        "success":      boolean,     # false if error parsing
        "error":        string,      # exists if "success" is false
        "line":         string       # exists if "success" is false
      }
    }

    [0] Will attempt to convert extended fields to the type specified in the
        CEF specification. If conversion fails, then the field will remain
        a string.
    [1] Naive calculated epoch timestamp
    [2] Timezone-aware calculated epoch timestamp. (UTC only) This value
        will be null if a UTC timezone cannot be extracted from the original
        timestamp string value.
    [3] This field exists if the CEF line is not parsable. The value
        is the original syslog line.

Examples:

    $ cat cef.log | jc --cef-s
    {"deviceVendor":"Fortinet","deviceProduct":"FortiDeceptor","deviceV...}
    {"deviceVendor":"Trend Micro","deviceProduct":"Deep Security Agent"...}
    pass

    $ cat cef.log | jc --cef-s -r
    {"deviceVendor":"Fortinet","deviceProduct":"FortiDeceptor","deviceV...}
    {"deviceVendor":"Trend Micro","deviceProduct":"Deep Security Agent"...}
    pass
"""
from typing import Dict, Iterable, Union
import re
import jc.utils
from jc.streaming import (
    add_jc_meta, streaming_input_type_check, streaming_line_input_type_check, raise_or_yield
)
from jc.exceptions import ParseError
from jc.parsers.cef import _pycef_parse


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = 'CEF string streaming parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    details = 'Using the pycef library at https://github.com/DavidJBianco/pycef/releases/tag/v1.11-2'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'file', 'string']
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
