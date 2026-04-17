r"""jc - JSON Convert `rsync` command output streaming parser

> This streaming parser outputs JSON Lines (cli) or returns an Iterable of
> Dictionaries (module)

Supports the `-i` or `--itemize-changes` options with all levels of
verbosity. This parser will process the `STDOUT` output or a log file
generated with the `--log-file` option.

Usage (cli):

    $ rsync -i -a source/ dest | jc --rsync-s

or

    $ cat rsync-backup.log | jc --rsync-s

Usage (module):

    import jc

    result = jc.parse('rsync_s', rsync_command_output.splitlines())
    for item in result:
        # do something

Schema:

    {
      "type":                           string,       # 'file' or 'summary'
      "date":                           string,
      "time":                           string,
      "process":                        integer,
      "sent":                           integer,
      "received":                       integer,
      "total_size":                     integer,
      "matches":                        integer,
      "hash_hits":                      integer,
      "false_alarms":                   integer,
      "data":                           integer,
      "bytes_sec":                      float,
      "speedup":                        float,
      "filename":                       string,
      "date":                           string,
      "time":                           string,
      "process":                        integer,
      "metadata":                       string,
      "update_type":                    string/null,  # [0]
      "file_type":                      string/null,  # [1]
      "checksum_or_value_different":    bool/null,
      "size_different":                 bool/null,
      "modification_time_different":    bool/null,
      "permissions_different":          bool/null,
      "owner_different":                bool/null,
      "group_different":                bool/null,
      "acl_different":                  bool/null,
      "extended_attribute_different":   bool/null,
      "epoch":                          integer,      # [2]

      # below object only exists if using -qq or ignore_exceptions=True
      "_jc_meta": {
        "success":      boolean,     # false if error parsing
        "error":        string,      # exists if "success" is false
        "line":         string       # exists if "success" is false
      }
    }

    [0] 'file sent', 'file received', 'local change or creation',
        'hard link', 'not updated', 'message'
    [1] 'file', 'directory', 'symlink', 'device', 'special file'
    [2] naive timestamp if time and date fields exist and can be converted.

Examples:

    $ rsync -i -a source/ dest | jc --rsync-s
    {"type":"file","filename":"./","metadata":".d..t......","update_...}
    pass

    $ cat rsync_backup.log | jc --rsync-s
    {"type":"file","filename":"./","date":"2022/01/28","time":"03:53...}
    pass
"""
import re
from typing import Dict, Iterable, Union
import jc.utils
from jc.streaming import (
    add_jc_meta, streaming_input_type_check, streaming_line_input_type_check, raise_or_yield
)

class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.3'
    description = '`rsync` command streaming parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'freebsd']
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
