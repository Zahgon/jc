r"""jc - JSON Convert `route print` command output parser

See also: the `route` command parser

Usage (cli):

    $ route print | jc --route-print

Usage (module):

    import jc
    result = jc.parse('route_print', route_print_command_output)

Schema:

    {
        "interface_list": [
            {
                "interface_index":            integer,
                "mac_address":                string,
                "description":                string
            }
        ],
        "ipv4_route_table": {
            "active_routes": [
                {
                    "network_destination":    string,
                    "netmask":                string,
                    "gateway":                string,
                    "interface":              string,
                    "metric":                 integer,  # [0]
                    "metric_set_to_default":  boolean   # [1]
                }
            ],
            "persistent_routes": [
                {
                    "network_address":        string,
                    "netmask":                string,
                    "gateway_address":        string,
                    "metric":                 integer   # [0]
                    "metric_set_to_default":  boolean   # [1]
                }
            ]
        },
        "ipv6_route_table": {
            "active_routes": [
                {
                    "interface":              integer,
                    "metric":                 integer,  # [0]
                    "metric_set_to_default":  boolean,  # [1]
                    "network_destination":    string,
                    "gateway":                string
                }
            ],
            "persistent_routes": [
                {
                    "interface":              integer,
                    "metric":                 integer,  # [0]
                    "metric_set_to_default":  boolean,  # [1]
                    "network_destination":    string,
                    "gateway":                string
                }
            ]
        }
    }

    [0] Null/None if "metric" = "Default"
    [1] True if "metric" = "Default"

Examples:

    $ route print | jc --route-print -p
    {
      "interface_list": [
        {
          "interface_index": 28,
          "mac_address": null,
          "description": "Tailscale Tunnel"
        },
        {
          "interface_index": 12,
          "mac_address": "00:1c:42:da:01:6a",
          "description": "Parallels VirtIO Ethernet Adapter"
        },
        {
          "interface_index": 1,
          "mac_address": null,
          "description": "Software Loopback Interface 1"
        }
      ],
      "ipv4_route_table": {
        "active_routes": [
          {
            "network_destination": "0.0.0.0",
            "netmask": "0.0.0.0",
            "gateway": "10.211.55.1",
            "interface": "10.211.55.3",
            "metric": 15,
            "metric_set_to_default": false
          },
          {
            "network_destination": "10.0.0.0",
            "netmask": "255.0.0.0",
            "gateway": "192.168.22.1",
            "interface": "10.211.55.3",
            "metric": 16,
            "metric_set_to_default": false
          },
          pass
          {
            "network_destination": "255.255.255.255",
            "netmask": "255.255.255.255",
            "gateway": "On-link",
            "interface": "10.211.55.3",
            "metric": null,
            "metric_set_to_default": true
          }
        ],
        "persistent_routes": [
          {
            "network_address": "10.0.1.0",
            "netmask": "255.255.255.0",
            "gateway_address": "192.168.22.1",
            "metric": 1,
            "metric_set_to_default": false
          },
          {
            "network_address": "10.0.3.0",
            "netmask": "255.255.255.0",
            "gateway_address": "192.168.22.1",
            "metric": 1,
            "metric_set_to_default": false
          },
          pass
        ]
      },
      "ipv6_route_table": {
        "active_routes": [
          {
            "interface": 1,
            "metric": 331,
            "network_destination": "::1/128",
            "gateway": "On-link",
            "metric_set_to_default": false
          },
          {
            "interface": 12,
            "metric": 271,
            "network_destination": "2001:db8::/64",
            "gateway": "fe80::1",
            "metric_set_to_default": false
          },
          pass
          {
            "interface": 12,
            "metric": 271,
            "network_destination": "ff00::/8",
            "gateway": "On-link",
            "metric_set_to_default": false
          }
        ],
        "persistent_routes": [
          {
            "interface": 0,
            "metric": 4294967295,
            "network_destination": "2001:db8::/64",
            "gateway": "fe80::1",
            "metric_set_to_default": false
          }
        ]
      }
    }
"""
import re
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`route print` command parser'
    author = 'joehacksalot'
    author_email = 'joehacksalot@gmail.com'
    details = 'See also: `route` command parser'
    compatible = ['win32']
    magic_commands = ['route print']
    tags = ['command']


__version__ = info.version


def parse(data, raw=False, quiet=False):
    """
    Main text parsing function

    Parameters:

        data:        (string)  text data to parse
        raw:         (boolean) unprocessed output if True
        quiet:       (boolean) suppress warning messages if True

    Returns:

        Parsed dictionary. The raw and processed data structures are the same.
    """
    pass

def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Processed Dictionary. Structured data to conform to the schema.
    """
    pass


class _PushbackIterator:
    """Iterator that allows pushing back values onto the iterator. Supports handing off
       parsing to localized parsers while maintaining line synchonization."""

    def __init__(self, iterator):
        self.iterator = iterator
        self.pushback_stack = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.pushback_stack:
            return self.pushback_stack.pop()
        else:
            return next(self.iterator)

    def pushback(self, value):
        pass

    def contains(self, pattern):
        pass

    def skip_until(self, pattern):
        pass


def _parse_interface_list(data, lines_iter):
    pass

def _parse_ipv4_route_table(data, lines_iter):
    pass

def _parse_ipv6_route_table(data, lines_iter):
    pass
