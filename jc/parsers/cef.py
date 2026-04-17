r"""jc - JSON Convert CEF string parser

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

    $ echo 'CEF:0|Vendor|Product|3.2.0|1|SYSTEM|1|... | jc --cef

Usage (module):

    import jc
    result = jc.parse('cef', cef_string_output)

Schema:

See: https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-8.3/cef-implementation-standard/Content/CEF/Chapter%201%20What%20is%20CEF.htm

> Note: Special characters in key names will be converted to underscores.

    [
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
      }
    ]

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

    $ cat cef.log | jc --cef -p
    [
      {
        "deviceVendor": "Trend Micro",
        "deviceProduct": "Deep Security Agent",
        "deviceVersion": "<DSA version>",
        "deviceEventClassId": "4000000",
        "name": "Eicar_test_file",
        "agentSeverity": 6,
        "CEFVersion": 0,
        "dvchost": "hostname",
        "string": "hello \"world\"!",
        "start": "Nov 08 2020 12:30:00.111 UTC",
        "start_epoch": 1604867400,
        "start_epoch_utc": 1604838600,
        "Host_ID": 1,
        "Quarantine": 205,
        "myDate": "Nov 08 2022 12:30:00.111",
        "myDate_epoch": 1667939400,
        "myDate_epoch_utc": null,
        "myFloat": 3.14,
        "deviceEventClassIdNum": 4000000,
        "agentSeverityString": "Medium",
        "agentSeverityNum": 6
      }
    ]

    $ cat cef.log | jc --cef -p -r
    [
      {
        "deviceVendor": "Trend Micro",
        "deviceProduct": "Deep Security Agent",
        "deviceVersion": "<DSA version>",
        "deviceEventClassId": "4000000",
        "name": "Eicar_test_file",
        "agentSeverity": "6",
        "CEFVersion": "0",
        "cn1": "1",
        "cn1Label": "Host ID",
        "dvchost": "hostname",
        "cn2": "205",
        "cn2Label": "Quarantine",
        "string": "hello \\\"world\\\"!",
        "start": "Nov 08 2020 12:30:00.111 UTC",
        "deviceCustomDate1": "Nov 08 2022 12:30:00.111",
        "deviceCustomDate1Label": "myDate",
        "cfp1": "3.14",
        "cfp1Label": "myFloat"
      }
    ]
"""
from typing import List, Dict
import re
import jc.utils
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = 'CEF string parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    details = 'Using the pycef library at https://github.com/DavidJBianco/pycef/releases/tag/v1.11-2'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'file', 'string']


__version__ = info.version


############################################################################
"""
The MIT License (MIT)

Copyright (c) 2016 DavidJBianco

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def _pycef_parse(str_input):
    """
    Parse a string in CEF format and return a dict with the header values
    and the extension data.
    """
    pass

############################################################################


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
