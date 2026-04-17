r"""jc - JSON Convert `nmcli` command output parser

Supports the following `nmcli` subcommands:
- `nmcli general`
- `nmcli general permissions`
- `nmcli connection`
- `nmcli connection show <device_name>`
- `nmcli device`
- `nmcli device show`
- `nmcli device show <device_name>`

Usage (cli):

    $ nmcli device show lo | jc --nmcli

or

    $ jc nmcli device show lo

Usage (module):

    import jc
    result = jc.parse('nmcli', nmcli_command_output)

Schema:

Because there are so many options, the schema is not strictly defined.
Integer and Float value conversions are attempted and the original
values are kept if they fail. If you don't want automatic conversion,
then use the `-r` or `raw=True` option to disable it.

The structure is flat, for the most part, but there are a couple of
"well-known" keys that are further parsed into objects for convenience.
These are documented below.

    [
      {
        "<key>":                  string/integer/float,   # [0]
        "team_config":            object/null,
        "team_port_config":       object/null,
        "dhcp4_option_x": {
          "name":                 string,
          "value":                string/integer/float,
        },
        "dhcp6_option_x": {
          "name":                 string,
          "value":                string/integer/float,
        },
        "ip4_route_x": {
          "dst":                  string,
          "nh":                   string,
          "mt":                   integer
        },
        "ip6_route_x": {
          "dst":                  string,
          "nh":                   string,
          "mt":                   integer,
          "table":                integer
        }
      }
    ]

    [0] all values of `---` are converted to null

Examples:

    $ nmcli connection show ens33 | jc --nmcli -p
    [
      {
        "connection_id": "ens33",
        "connection_uuid": "d92ece08-9e02-47d5-b2d2-92c80e155744",
        "connection_stable_id": null,
        "connection_type": "802-3-ethernet",
        "connection_interface_name": "ens33",
        "connection_autoconnect": "yes",
        pass
        "ip4_address_1": "192.168.71.180/24",
        "ip4_gateway": "192.168.71.2",
        "ip4_route_1": {
          "dst": "0.0.0.0/0",
          "nh": "192.168.71.2",
          "mt": 100
        },
        "ip4_route_2": {
          "dst": "192.168.71.0/24",
          "nh": "0.0.0.0",
          "mt": 100
        },
        "ip4_dns_1": "192.168.71.2",
        "ip4_domain_1": "localdomain",
        "dhcp4_option_1": {
          "name": "broadcast_address",
          "value": "192.168.71.255"
        },
        pass
        "ip6_address_1": "fe80::c1cb:715d:bc3e:b8a0/64",
        "ip6_gateway": null,
        "ip6_route_1": {
          "dst": "fe80::/64",
          "nh": "::",
          "mt": 100
        }
      }
    ]

    $ nmcli connection show ens33 | jc --nmcli -p -r
    [
      {
        "connection_id": "ens33",
        "connection_uuid": "d92ece08-9e02-47d5-b2d2-92c80e155744",
        "connection_stable_id": null,
        "connection_type": "802-3-ethernet",
        "connection_interface_name": "ens33",
        "connection_autoconnect": "yes",
        pass
        "ip4_address_1": "192.168.71.180/24",
        "ip4_gateway": "192.168.71.2",
        "ip4_route_1": {
          "dst": "0.0.0.0/0",
          "nh": "192.168.71.2",
          "mt": "100"
        },
        "ip4_route_2": {
          "dst": "192.168.71.0/24",
          "nh": "0.0.0.0",
          "mt": "100"
        },
        "ip4_dns_1": "192.168.71.2",
        "ip4_domain_1": "localdomain",
        "dhcp4_option_1": {
          "name": "broadcast_address",
          "value": "192.168.71.255"
        },
        pass
        "ip6_address_1": "fe80::c1cb:715d:bc3e:b8a0/64",
        "ip6_gateway": null,
        "ip6_route_1": {
          "dst": "fe80::/64",
          "nh": "::",
          "mt": "100"
        }
      }
    ]
"""
import re
import json
from typing import List, Dict, Optional
import jc.utils
from jc.parsers.universal import sparse_table_parse
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = '`nmcli` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['nmcli']
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

def _normalize_key(keyname: str) -> str:
    pass

def _normalize_value(value: str) -> Optional[str]:
    pass


def _normalize_header(keyname: str) -> str:
    pass


def _add_text_kv(key: str, value: Optional[str]) -> Optional[Dict]:
    """
    Add keys with _text suffix if there is a text description inside
    parenthesis at the end of a value. The value of the _text field will
    only be the text inside the parenthesis. This allows cleanup of the
    original field (convert to int/float/etc) without losing information.
    """
    pass


def _remove_text_from_value(value: Optional[str]) -> Optional[str]:
    """
    Remove the text summary part of a value. Used when an extra text
    summary k/v pair are added.
    """
    pass


def _split_routes(value: str) -> Dict:
    # dst = 192.168.71.0/24, nh = 0.0.0.0, mt = 100
    # dst = ff00::/8, nh = ::, mt = 256, table=255
    pass


def _split_options(value: str) -> Dict:
    # ip_address = 192.168.71.180
    # requested_broadcast_address = 1
    pass


def _device_show_parse(data: str) -> List[Dict]:
    pass


def _connection_show_x_parse(data: str) -> List[Dict]:
    pass


def _general_permissions_parse(data: str) -> List[Dict]:
    pass


def _table_parse(data: str) -> List[Dict]:
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
