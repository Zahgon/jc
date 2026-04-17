r"""jc - JSON Convert JWT string parser

> Note: `jc` will not check the integrity of the JWT payload.

Usage (cli):

    $ echo "eyJhbGciOiJIUzI1N..." | jc --jwt

Usage (module):

    import jc
    result = jc.parse('jwt', jwt_string)

Schema:

    {
      "header": {
        "alg":                    string,
        "typ":                    string
      },
      "payload": {
        <key name>:               string/integer/float/boolean/null
      },
      "signature":                string  # [0]
    }

    [0] in colon-delimited hex notation

Examples:

    % echo 'eyJhbGciOiJIUzI1N...' | jc --jwt -p
    {
      "header": {
        "alg": "HS256",
        "typ": "JWT"
      },
      "payload": {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": 1516239022
      },
      "signature": "49:f9:4a:c7:04:49:48:c7:8a:28:5d:90:4f:87:f0:a4:c7..."
    }
"""
from base64 import urlsafe_b64decode
import binascii
import json
from typing import Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.1'
    description = 'JWT string parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'string', 'slurpable']


__version__ = info.version


def _process(proc_data: Dict) -> Dict:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured to conform to the schema.
    """
    pass


def _b2a(byte_string: bytes) -> str:
    """Convert a byte string to a colon-delimited hex ascii string"""
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
