r"""jc - JSON Convert `nsd-control` command output parser

Usage (cli):

    $ nsd-control | jc --nsd-control

or

    $ jc nsd-control

Usage (module):

    import jc
    result = jc.parse('nsd_control', nsd_control_command_output)

Schema:

    [
      {
        "version":              string,
        "verbosity":            integer,
        "ratelimit":            integer
      }
    ]

    [
      {
        "zone":                 string
        "status": {
          "state":              string,
          "pattern":            string,  # Additional
          "catalog-member-id":  string,  # Additional
          "served-serial":      string,
          "commit-serial":      string,
          "notified-serial":    string,  # Conditional
          "wait":               string,
          "transfer":           string	 # Conditional
        }
      }
    ]

Examples:

    $ nsd-control | jc --nsd-control status
    [
      {
        "version": "4.6.2",
        "verbosity": "2",
        "ratelimit": "0"
      }
    ]

    $ nsd-control | jc --nsd-control zonestatus sunet.se
    [
      {
        "zone": "sunet.se",
        "status": {
          "state": "ok",
          "served-serial": "2023090704 since 2023-09-07T16:34:27",
          "commit-serial": "2023090704 since 2023-09-07T16:34:27",
          "wait": "28684 sec between attempts"
        }
      }
    ]
"""
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = '`nsd-control` command parser'
    author = 'Pettai'
    author_email = 'pettai@sunet.se'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['command']
    magic_commands = ['nsd-control']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured to conform to the schema.
    """
    pass


def parse(data: str, raw: bool = False, quiet: bool = False):
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
