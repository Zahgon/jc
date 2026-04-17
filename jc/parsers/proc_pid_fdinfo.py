r"""jc - JSON Convert `/proc/<pid>/fdinfo/<fd>` file parser

Usage (cli):

    $ cat /proc/1/fdinfo/5 | jc --proc

or

    $ jc /proc/1/fdinfo/5

or

    $ cat /proc/1/fdinfo/5 | jc --proc-pid-fdinfo

Usage (module):

    import jc
    result = jc.parse('proc', proc_pid_fdinfo_file)

or

    import jc
    result = jc.parse('proc_pid_fdinfo', proc_pid_fdinfo_file)

Schema:

Any unspecified fields are strings.

    {
      "pos":                        integer,
      "flags":                      integer,
      "mnt_id":                     integer,
      "scm_fds":                    string,
      "ino":                        integer,
      "lock":                       string,
      "epoll": {
        "tfd":                      integer,
        "events":                   string,
        "data":                     string,
        "pos":                      integer,
        "ino":                      string,
        "sdev":                     string
      },
      "inotify": {
        "wd":                       integer,
        "ino":                      string,
        "sdev":                     string,
        "mask":                     string,
        "ignored_mask":             string,
        "fhandle-bytes":            string,
        "fhandle-type":             string,
        "f_handle":                 string
      },
      "fanotify": {
        "flags":                    string,
        "event-flags":              string,
        "mnt_id":                   string,
        "mflags":                   string,
        "mask":                     string,
        "ignored_mask":             string,
        "ino":                      string,
        "sdev":                     string,
        "fhandle-bytes":            string,
        "fhandle-type":             string,
        "f_handle":                 string
      },
      "clockid":                    integer,
      "ticks":                      integer,
      "settime flags":              integer,
      "it_value": [
                                    integer
      ],
      "it_interval": [
                                    integer
      ]
    }

Examples:

    $ cat /proc/1/fdinfo/5 | jc --proc -p
    {
      "pos": 0,
      "flags": 2,
      "mnt_id": 9,
      "ino": 63107,
      "clockid": 0,
      "ticks": 0,
      "settime flags": 1,
      "it_value": [
        0,
        49406829
      ],
      "it_interval": [
        1,
        0
      ]
    }
"""
import re
from typing import Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/<pid>/fdinfo/<fd>` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    tags = ['file']
    hidden = True


__version__ = info.version


def _process(proc_data: Dict) -> Dict:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        Dictionary. Structured to conform to the schema.
    """
    pass


def parse(
    data: str,
    raw: bool = False,
    quiet: bool = False
) -> Dict:
    """
    Main text parsing function

    Parameters:

        data:        (string)  text data to parse
        raw:         (boolean) unprocessed output if True
        quiet:       (boolean) suppress warning messages if True

    Returns:

        Dictionary. Raw or processed structured data.
    """
    pass
