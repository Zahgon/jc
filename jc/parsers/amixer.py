r"""jc - JSON Convert `amixer sget` command output parser

Usage (cli):

    $ amixer sget <control_name> | jc --amixer
    $ amixer sget Master | jc --amixer
    $ amixer sget Capture | jc --amixer
    $ amixer sget Speakers | jc --amixer

Usage (module):

    import jc
    result = jc.parse('amixer', <amixer_sget_command_output>)

Schema:

    {
        "control_name":                     string,
        "capabilities": [
                                            string
        ],
        "playback_channels": [
                                            string
        ],
        "limits": {
            "playback_min":                 integer,
            "playback_max":                 integer
        },
        "mono": {
            "playback_value":               integer,
            "percentage":                   integer,
            "db":                           float,
            "status":                       boolean
        }
    }

Examples:

    $ amixer sget Master | jc --amixer -p
    {
      "control_name": "Capture",
      "capabilities": [
        "cvolume",
        "cswitch"
      ],
      "playback_channels": [],
      "limits": {
        "playback_min": 0,
        "playback_max": 63
      },
      "front_left": {
        "playback_value": 63,
        "percentage": 100,
        "db": 30.0,
        "status": true
      },
      "front_right": {
        "playback_value": 63,
        "percentage": 100,
        "db": 30.0,
        "status": true
      }
    }

    $ amixer sget Master | jc --amixer -p -r
    {
        "control_name": "Master",
        "capabilities": [
            "pvolume",
            "pvolume-joined",
            "pswitch",
            "pswitch-joined"
        ],
        "playback_channels": [
            "Mono"
        ],
        "limits": {
            "playback_min": "0",
            "playback_max": "87"
        },
        "mono": {
            "playback_value": "87",
            "percentage": "100%",
            "db": "0.00db",
            "status": "on"
        }
    }
"""
from typing import Dict

import jc.utils
from jc.utils import convert_to_int
from jc.exceptions import ParseError

class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`amixer` command parser'
    author = 'Eden Refael'
    author_email = 'edenraf@hotmail.com'
    compatible = ['linux']
    magic_commands = ['amixer']
    tags = ['command']


__version__ = info.version


def _process(proc_data: Dict) -> Dict:
    """
    Processes raw structured data to match the schema requirements.

    Parameters:
        proc_data: (dict) raw structured data from the parser

    Returns:
        (dict) processed structured data adhering to the schema
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
