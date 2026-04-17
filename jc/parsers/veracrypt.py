r"""jc - JSON Convert `veracrypt` command output parser

Supports the following `veracrypt` subcommands:
- `veracrypt --text --list`
- `veracrypt --text --list --verbose`
- `veracrypt --text --volume-properties <volume>`

Usage (cli):

    $ veracrypt --text --list | jc --veracrypt
or

    $ jc veracrypt --text --list

Usage (module):

    import jc
    result = jc.parse('veracrypt', veracrypt_command_output)

Schema:

    Volume:
    [
        {
            "slot":                 integer,
            "path":                 string,
            "device":               string,
            "mountpoint":           string,
            "size":                 string,
            "type":                 string,
            "readonly":             string,
            "hidden_protected":     string,
            "encryption_algo":      string,
            "pk_size":              string,
            "sk_size":              string,
            "block_size":           string,
            "mode":                 string,
            "prf":                  string,
            "format_version":       integer,
            "backup_header":        string
        }
    ]

Examples:

    $ veracrypt --text --list | jc --veracrypt -p
    [
        {
            "slot": 1,
            "path": "/dev/sdb1",
            "device": "/dev/mapper/veracrypt1",
            "mountpoint": "/home/bob/mount/encrypt/sdb1"
        }
    ]

    $ veracrypt --text --list --verbose | jc --veracrypt -p
    [
        {
            "slot": 1,
            "path": "/dev/sdb1",
            "device": "/dev/mapper/veracrypt1",
            "mountpoint": "/home/bob/mount/encrypt/sdb1",
            "size": "522 MiB",
            "type": "Normal",
            "readonly": "No",
            "hidden_protected": "No",
            "encryption_algo": "AES",
            "pk_size": "256 bits",
            "sk_size": "256 bits",
            "block_size": "128 bits",
            "mode": "XTS",
            "prf": "HMAC-SHA-512",
            "format_version": 2,
            "backup_header": "Yes"
        }
    ]
"""
import re
from typing import List, Dict, Optional, Any
from jc.jc_types import JSONDictType
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`veracrypt` command parser'
    author = 'Jake Ob'
    author_email = 'iakopap at gmail.com'
    compatible = ["linux"]
    magic_commands = ["veracrypt"]
    tags = ['command']


__version__ = info.version

try:
    from typing import TypedDict

    Volume = TypedDict(
        "Volume",
        {
            "slot": int,
            "path": str,
            "device": str,
            "mountpoint": str,
            "size": str,
            "type": str,
            "readonly": str,
            "hidden_protected": str,
            "encryption_algo": str,
            "pk_size": str,
            "sk_size": str,
            "block_size": str,
            "mode": str,
            "prf": str,
            "format_version": int,
            "backup_header": str
        },
    )
except ImportError:
    Volume = Dict[str, Any]  # type: ignore

_volume_line_pattern = r"(?P<slot>[0-9]+): (?P<path>.+?) (?P<device>.+?) (?P<mountpoint>.*)"

_volume_verbose_pattern = (
    r"(Slot:\s(?P<slot>.+)"
    + r"|Volume:\s(?P<path>.+)"
    + r"|Virtual\sDevice:\s(?P<device>.+)"
    + r"|Mount\sDirectory:\s(?P<mountpoint>.+)"
    + r"|Size:\s(?P<size>.+)"
    + r"|Type:\s(?P<type>.+)"
    + r"|Read-Only:\s(?P<readonly>.+)"
    + r"|Hidden\sVolume Protected:\s(?P<hidden_protected>.+)"
    + r"|Encryption\sAlgorithm:\s(?P<encryption_algo>.+)"
    + r"|Primary\sKey\sSize:\s(?P<pk_size>.+)"
    + r"|Secondary\sKey\sSize\s.*:\s(?P<sk_size>.+)"
    + r"|Block\sSize:\s(?P<block_size>.+)"
    + r"|Mode\sof\sOperation:\s(?P<mode>.+)"
    + r"|PKCS-5\sPRF:\s(?P<prf>.+)"
    + r"|Volume\sFormat\sVersion:\s(?P<format_version>.+)"
    + r"|Embedded\sBackup\sHeader:\s(?P<backup_header>.+))"
)

def _parse_volume(next_lines: List[str]) -> Optional[Volume]:
    pass

def parse(data: str, raw: bool = False, quiet: bool = False) -> List[JSONDictType]:
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
