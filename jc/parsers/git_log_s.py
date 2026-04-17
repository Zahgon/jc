r"""jc - JSON Convert `git log` command output streaming parser

> This streaming parser outputs JSON Lines (cli) or returns an Iterable of
> Dictionaries (module)

Can be used with the following format options:
- `oneline`
- `short`
- `medium`
- `full`
- `fuller`

Additional options supported:
- `--stat`
- `--shortstat`

The `epoch` calculated timestamp field is naive. (i.e. based on the
local time of the system the parser is run on)

The `epoch_utc` calculated timestamp field is timezone-aware and is
only available if the timezone field is UTC.

Usage (cli):

    $ git log | jc --git-log-s

Usage (module):

    import jc

    result = jc.parse('git_log_s', git_log_command_output.splitlines())
    for item in result:
        # do something

Schema:

    {
      "commit":               string,
      "author":               string/null,
      "author_email":         string/null,
      "date":                 string,
      "epoch":                integer,  # [0]
      "epoch_utc":            integer,  # [1]
      "commit_by":            string/null,
      "commit_by_email":      string/null,
      "commit_by_date":       string,
      "message":              string,
      "stats" : {
        "files_changed":      integer,
        "insertions":         integer,
        "deletions":          integer,
        "files": [
                              string
        ],
        "file_stats": [
          {
            "name":           string,
            "lines_changed":  integer
          }
        ]
      }

      # below object only exists if using -qq or ignore_exceptions=True
      "_jc_meta": {
        "success":      boolean,     # false if error parsing
        "error":        string,      # exists if "success" is false
        "line":         string       # exists if "success" is false
      }
    }

    [0] naive timestamp if "date" field is parsable, else null
    [1] timezone aware timestamp available for UTC, else null

Examples:

    $ git log | jc --git-log-s
    {"commit":"a730ae18c8e81c5261db132df73cd74f272a0a26","author":"Kelly...}
    {"commit":"930bf439c06c48a952baec05a9896c8d92b7693e","author":"Kelly...}
    pass
"""
import re
from typing import List, Dict, Any, Iterable, Union
import jc.utils
from jc.parsers.git_log import _parse_name_email
from jc.streaming import (
    add_jc_meta, streaming_input_type_check, streaming_line_input_type_check, raise_or_yield
)
from jc.exceptions import ParseError


hash_pattern = re.compile(r'(?:[0-9]|[a-f]){40}')
changes_pattern = re.compile(r'\s(?P<files>\d+)\s+(files? changed)(?:,\s+(?P<insertions>\d+)\s+(insertions?\(\+\)))?(?:,\s+(?P<deletions>\d+)\s+(deletions?\(\-\)))?')


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.5'
    description = '`git log` command streaming parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
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


def _is_commit_hash(hash_string: str) -> bool:
    # 0c55240e9da30ac4293dc324f1094de2abd3da91
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
