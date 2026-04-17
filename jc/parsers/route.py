r"""jc - JSON Convert `route` command output parser

Usage (cli):

    $ route | jc --route

or

    $ jc route

Usage (module):

    import jc
    result = jc.parse('route', route_command_output)

Schema:

    [
      {
        "interfaces": [
          {
            "id": string,
            "mac": string,
            "name": string,
          }
        ]
        "destination":        string,
        "gateway":            string,
        "genmask":            string,
        "flags":              string,
        "flags_pretty": [
                              string
        ]
        "metric":             integer,
        "ref":                integer,
        "use":                integer,
        "mss":                integer,
        "window":             integer,
        "irtt":               integer,
        "iface":              string
      }
    ]

Examples:

    $ route -ee | jc --route -p
    [
      {
        "destination": "default",
        "gateway": "_gateway",
        "genmask": "0.0.0.0",
        "flags": "UG",
        "metric": 202,
        "ref": 0,
        "use": 0,
        "iface": "ens33",
        "mss": 0,
        "window": 0,
        "irtt": 0,
        "flags_pretty": [
          "UP",
          "GATEWAY"
        ]
      },
      {
        "destination": "192.168.71.0",
        "gateway": "0.0.0.0",
        "genmask": "255.255.255.0",
        "flags": "U",
        "metric": 202,
        "ref": 0,
        "use": 0,
        "iface": "ens33",
        "mss": 0,
        "window": 0,
        "irtt": 0,
        "flags_pretty": [
          "UP"
        ]
      }
    ]

    $ route -ee | jc --route -p -r
    [
      {
        "destination": "default",
        "gateway": "_gateway",
        "genmask": "0.0.0.0",
        "flags": "UG",
        "metric": "202",
        "ref": "0",
        "use": "0",
        "iface": "ens33",
        "mss": "0",
        "window": "0",
        "irtt": "0"
      },
      {
        "destination": "192.168.71.0",
        "gateway": "0.0.0.0",
        "genmask": "255.255.255.0",
        "flags": "U",
        "metric": "202",
        "ref": "0",
        "use": "0",
        "iface": "ens33",
        "mss": "0",
        "window": "0",
        "irtt": "0"
      }
    ]
"""
import jc.utils

class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.9'
    description = '`route` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'win32']
    magic_commands = ['route']
    tags = ['command']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured data to conform to the schema.
    """
    pass

def normalize_headers(headers: str):
    # fixup header row for ipv6
    pass

def parse(data, raw=False, quiet=False):
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
