r"""jc - JSON Convert `git log` command output parser

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

    $ git log | jc --git-log

or

    $ jc git log

Usage (module):

    import jc
    result = jc.parse('git_log', git_log_command_output)

Schema:

    [
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
      }
    ]

    [0] naive timestamp if "date" field is parsable, else null
    [1] timezone aware timestamp available for UTC, else null

Examples:

    $ git log --stat | jc --git-log -p
    [
      {
        "commit": "728d882ed007b3c8b785018874a0eb06e1143b66",
        "author": "Kelly Brazil",
        "author_email": "kellyjonbrazil@gmail.com",
        "date": "Wed Apr 20 09:50:19 2022 -0400",
        "stats": {
          "files_changed": 2,
          "insertions": 90,
          "deletions": 12,
          "files": [
            "docs/parsers/git_log.md",
            "jc/parsers/git_log.py"
          ],
          "file_stats": [
            {
              "name": "docs/parsers/git_log.md",
              "lines_changed": 3
            },
            {
              "name": "jc/parsers/git_log.py",
              "lines_changed": 7
            }
          ]
        },
        "message": "add timestamp docs and examples",
        "epoch": 1650462619,
        "epoch_utc": null
      },
      {
        "commit": "b53e42aca623181aa9bc72194e6eeef1e9a3a237",
        "author": "Kelly Brazil",
        "author_email": "kellyjonbrazil@gmail.com",
        "date": "Wed Apr 20 09:44:42 2022 -0400",
        "stats": {
          "files_changed": 5,
          "insertions": 29,
          "deletions": 6,
          "files": [
            "docs/parsers/git_log.md",
            "docs/utils.md",
            "jc/parsers/git_log.py",
            "jc/utils.py",
            "man/jc.1"
          ],
          "file_stats": [
            {
              "name": "docs/parsers/git_log.md",
              "lines_changed": 3
            },
            {
              "name": "docs/utils.md",
              "lines_changed": 7
            },
            {
              "name": "jc/parsers/git_log.py",
              "lines_changed": 1
            },
            {
              "name": "jc/utils.py",
              "lines_changed": 12
            },
            {
              "name": "man/jc.1",
              "lines_changed": 14
            }
          ]
        },
        "message": "add calculated timestamp",
        "epoch": 1650462282,
        "epoch_utc": null
      },
      pass
    ]

    $ git log --stat | jc --git-log -p -r
    [
      {
        "commit": "728d882ed007b3c8b785018874a0eb06e1143b66",
        "author": "Kelly Brazil",
        "author_email": "kellyjonbrazil@gmail.com",
        "date": "Wed Apr 20 09:50:19 2022 -0400",
        "stats": {
          "files_changed": "2",
          "insertions": "90",
          "deletions": "12",
          "files": [
            "docs/parsers/git_log.md",
            "jc/parsers/git_log.py"
          ],
          "file_stats": [
            {
              "name": "docs/parsers/git_log.md",
              "lines_changed": "3"
            },
            {
              "name": "jc/parsers/git_log.py",
              "lines_changed": "7"
            }
          ]
        },
        "message": "add timestamp docs and examples"
      },
      {
        "commit": "b53e42aca623181aa9bc72194e6eeef1e9a3a237",
        "author": "Kelly Brazil",
        "author_email": "kellyjonbrazil@gmail.com",
        "date": "Wed Apr 20 09:44:42 2022 -0400",
        "stats": {
          "files_changed": "5",
          "insertions": "29",
          "deletions": "6",
          "files": [
            "docs/parsers/git_log.md",
            "docs/utils.md",
            "jc/parsers/git_log.py",
            "jc/utils.py",
            "man/jc.1"
          ],
          "file_stats": [
            {
              "name": "docs/parsers/git_log.md",
              "lines_changed": "3"
            },
            {
              "name": "docs/utils.md",
              "lines_changed": "7"
            },
            {
              "name": "jc/parsers/git_log.py",
              "lines_changed": "1"
            },
            {
              "name": "jc/utils.py",
              "lines_changed": "12"
            },
            {
              "name": "man/jc.1",
              "lines_changed": "14"
            }
          ]
        },
        "message": "add calculated timestamp"
      },
      pass
    ]
"""
import re
from typing import List, Dict, Any
import jc.utils

hash_pattern = re.compile(r'(?:[0-9]|[a-f]){40}')
changes_pattern = re.compile(r'\s(?P<files>\d+)\s+(files? changed)(?:,\s+(?P<insertions>\d+)\s+(insertions?\(\+\)))?(?:,\s+(?P<deletions>\d+)\s+(deletions?\(\-\)))?')

class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.5'
    description = '`git log` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    magic_commands = ['git log']
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


def _is_commit_hash(hash_string: str) -> bool:
    # 0c55240e9da30ac4293dc324f1094de2abd3da91
    pass

def _parse_name_email(line):
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
