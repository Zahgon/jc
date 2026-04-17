r"""jc - JSON Convert `needrestart -b` command output parser

Usage (cli):

    $ needrestart -b | jc --needrestart

or

    $ jc needrestart -b

Usage (module):

    import jc
    result = jc.parse('needrestart', needrestart_command_output)

Schema:

    {
      "version":                        string,
      "running_kernel_version":         string,
      "expected_kernel_version":        string,
      "kernel_status":                  integer,
      "container":                      string,
      "session": [
                                        string
      ],
      "service": [
                                        string
      ],
      "pid": [
                                        string
      ]
    }

Examples:

    $ needrestart -b | jc --needrestart -p
    {
      "version": "2.1",
      "running_kernel_version": "3.19.3-tl1+",
      "expected_kernel_version": "3.19.3-tl1+",
      "kernel_status": 1,
      "container": "LXC web1",
      "session": [
        "metabase @ user manager service",
        "root @ session #28017"
      ],
      "service": [
        "systemd-journald.service",
        "systemd-machined.service"
      ]
    }

    $ needrestart -b | jc --needrestart -p -r
    {
      "needrestart_ver": "2.1",
      "needrestart_kcur": "3.19.3-tl1+",
      "needrestart_kexp": "3.19.3-tl1+",
      "needrestart_ksta": "1",
      "needrestart_cont": "LXC web1",
      "needrestart_sess": [
        "metabase @ user manager service",
        "root @ session #28017"
      ],
      "needrestart_svc": [
        "systemd-journald.service",
        "systemd-machined.service"
      ]
    }
"""
from typing import List, Dict
from jc.jc_types import JSONDictType
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`needrestart -b` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    tags = ['command']
    magic_commands = ['needrestart -b']


__version__ = info.version


def _process(proc_data: JSONDictType) -> JSONDictType:
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
) -> JSONDictType:
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
