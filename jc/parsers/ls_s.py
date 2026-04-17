r"""jc - JSON Convert `ls` and `vdir` command output streaming parser

> This streaming parser outputs JSON Lines (cli) or returns an Iterable of
> Dictionaries (module)

Requires the `-l` option to be used on `ls`. If there are newline characters
in the filename, then make sure to use the `-b` option on `ls`.

The `jc` `-qq` option can be used to ignore parsing errors. (e.g. filenames
with newline characters, but `-b` was not used)

The `epoch` calculated timestamp field is naive (i.e. based on the local
time of the system the parser is run on)

The `epoch_utc` calculated timestamp field is timezone-aware and is only
available if the timezone field is UTC.

Usage (cli):

    $ ls | jc --ls-s

Usage (module):

    import jc

    result = jc.parse('ls_s', ls_command_output.splitlines())
    for item in result:
        # do something

Schema:

    {
      "filename":       string,
      "flags":          string,
      "links":          integer,
      "parent":         string,
      "owner":          string,
      "group":          string,
      "size":           integer,
      "date":           string,
      "epoch":          integer,     # [0]
      "epoch_utc":      integer,     # [1]

      # below object only exists if using -qq or ignore_exceptions=True
      "_jc_meta": {
        "success":      boolean,     # false if error parsing
        "error":        string,      # exists if "success" is false
        "line":         string       # exists if "success" is false
      }
    }

    [0] naive timestamp if date field exists and can be converted.
    [1] timezone aware timestamp if date field is in UTC and can
        be converted

Examples:

    $ ls -l /usr/bin | jc --ls-s
    {"filename":"2to3-","flags":"-rwxr-xr-x","links":4,"owner":"root","...}
    {"filename":"2to3-2.7","link_to":"../../System/Library/Frameworks/P...}
    {"filename":"AssetCacheLocatorUtil","flags":"-rwxr-xr-x","links":1,...}
    pass

    $ ls -l /usr/bin | jc --ls-s -r
    {"filename":"2to3-","flags":"-rwxr-xr-x","links":"4","owner":"roo"..."}
    {"filename":"2to3-2.7","link_to":"../../System/Library/Frameworks/P...}
    {"filename":"AssetCacheLocatorUtil","flags":"-rwxr-xr-x","links":"1...}
    pass
"""
import re
import jc.utils
from jc.streaming import (
    add_jc_meta, streaming_input_type_check, streaming_line_input_type_check, raise_or_yield
)
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = '`ls` command streaming parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'aix', 'freebsd']
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
