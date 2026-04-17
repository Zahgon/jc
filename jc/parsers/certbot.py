r"""jc - JSON Convert `certbot` command output parser

Supports the following `certbot` commands:

- `certbot show_account`
- `certbot certificates`

Verbose options are not supported.

Usage (cli):

    $ certbot show_account | jc --certbot
    $ certbot certificates | jc --certbot

or

    $ jc certbot show_account
    $ jc certbot certificates

Usage (module):

    import jc
    result = jc.parse('certbot', certbot_command_output)

Schema:

    {
      "certificates": [
        {
          "name":                             string,
          "serial_number":                    string,
          "key_type":                         string,
          "domains": [
                                              string
          ],
          "expiration_date":                  string,
          "expiration_date_epoch":            integer,
          "expiration_date_epoch_utc":        integer,
          "expiration_date_iso":              string,
          "validity":                         string,
          "certificate_path":                 string,
          "private_key_path":                 string
        }
      ],
      "account": {
        "server":                             string,
        "url":                                string,
        "email":                              string
      }
    }

Examples:

    $ certbot certificates | jc --certbot -p
    {
      "certificates": [
        {
          "name": "example.com",
          "serial_number": "3f7axxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
          "key_type": "RSA",
          "domains": [
            "example.com",
            "www.example.com"
          ],
          "expiration_date": "2023-05-11 01:33:10+00:00",
          "validity": "63 days",
          "certificate_path": "/etc/letsencrypt/live/example.com/chain.pem",
          "private_key_path": "/etc/letsencrypt/live/example.com/priv.pem",
          "expiration_date_epoch": 1683793990,
          "expiration_date_epoch_utc": 1683768790,
          "expiration_date_iso": "2023-05-11T01:33:10+00:00"
        },
        {
          "name": "example.org",
          "serial_number": "3bcyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
          "key_type": "RSA",
          "domains": [
            "example.org",
            "www.example.org"
          ],
          "expiration_date": "2023-06-12 01:35:30+00:00",
          "validity": "63 days",
          "certificate_path": "/etc/letsencrypt/live/example.org/chain.pem",
          "private_key_path": "/etc/letsencrypt/live/example.org/key.pem",
          "expiration_date_epoch": 1686558930,
          "expiration_date_epoch_utc": 1686533730,
          "expiration_date_iso": "2023-06-12T01:35:30+00:00"
        }
      ]
    }

    $ certbot certificates | jc --certbot -p -r
    {
      "certificates": [
        {
          "name": "example.com",
          "serial_number": "3f7axxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
          "key_type": "RSA",
          "domains": [
            "example.com",
            "www.example.com"
          ],
          "expiration_date": "2023-05-11 01:33:10+00:00",
          "validity": "63 days",
          "certificate_path": "/etc/letsencrypt/live/example.com/chain.pem",
          "private_key_path": "/etc/letsencrypt/live/example.com/priv.pem"
        },
        {
          "name": "example.org",
          "serial_number": "3bcyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
          "key_type": "RSA",
          "domains": [
            "example.org",
            "www.example.org"
          ],
          "expiration_date": "2023-06-12 01:35:30+00:00",
          "validity": "63 days",
          "certificate_path": "/etc/letsencrypt/live/example.org/chain.pem",
          "private_key_path": "/etc/letsencrypt/live/example.org/key.pem"
        }
      ]
    }

    $ certbot show_account | jc --certbot -p
    {
      "account": {
        "server": "https://acme-staging-v02.api.letsencrypt.org/directory",
        "url": "https://acme-staging-v02.api.letsencrypt.org/acme/acct/123",
        "email": "some@example.com"
      }
    }
"""
import re
from typing import List, Dict
from jc.jc_types import JSONDictType
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = '`certbot` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['command']
    magic_commands = ['certbot']


__version__ = info.version


def _process(proc_data: JSONDictType) -> JSONDictType:
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
