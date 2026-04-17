r"""jc - JSON Convert `tracepath` command output parser

Supports `tracepath` and `tracepath6` output.

Usage (cli):

    $ tracepath 1.2.3.4 | jc --tracepath

or

    $ jc tracepath 1.2.3.4

Usage (module):

    import jc
    result = jc.parse('tracepath', tracepath_command_output)

Schema:

    {
      "pmtu":                       integer,
      "forward_hops":               integer,
      "return_hops":                integer,
      "hops": [
        {
          "ttl":                    integer,
          "guess":                  boolean,
          "host":                   string,
          "reply_ms":               float,
          "pmtu":                   integer,
          "asymmetric_difference":  integer,
          "reached":                boolean
        }
      ]
    }

Examples:

    $ tracepath6 3ffe:2400:0:109::2 | jc --tracepath -p
    {
      "pmtu": 1480,
      "forward_hops": 2,
      "return_hops": 2,
      "hops": [
        {
          "ttl": 1,
          "guess": true,
          "host": "[LOCALHOST]",
          "reply_ms": null,
          "pmtu": 1500,
          "asymmetric_difference": null,
          "reached": false
        },
        {
          "ttl": 1,
          "guess": false,
          "host": "dust.inr.ac.ru",
          "reply_ms": 0.411,
          "pmtu": null,
          "asymmetric_difference": null,
          "reached": false
        },
        {
          "ttl": 2,
          "guess": false,
          "host": "dust.inr.ac.ru",
          "reply_ms": 0.39,
          "pmtu": 1480,
          "asymmetric_difference": 1,
          "reached": false
        },
        {
          "ttl": 2,
          "guess": false,
          "host": "3ffe:2400:0:109::2",
          "reply_ms": 463.514,
          "pmtu": null,
          "asymmetric_difference": null,
          "reached": true
        }
      ]
    }

    $ tracepath6 3ffe:2400:0:109::2 | jc --tracepath -p -r
    {
      "pmtu": "1480",
      "forward_hops": "2",
      "return_hops": "2",
      "hops": [
        {
          "ttl": "1",
          "guess": true,
          "host": "[LOCALHOST]",
          "reply_ms": null,
          "pmtu": "1500",
          "asymmetric_difference": null,
          "reached": false
        },
        {
          "ttl": "1",
          "guess": false,
          "host": "dust.inr.ac.ru",
          "reply_ms": "0.411",
          "pmtu": null,
          "asymmetric_difference": null,
          "reached": false
        },
        {
          "ttl": "2",
          "guess": false,
          "host": "dust.inr.ac.ru",
          "reply_ms": "0.390",
          "pmtu": "1480",
          "asymmetric_difference": "1",
          "reached": false
        },
        {
          "ttl": "2",
          "guess": false,
          "host": "3ffe:2400:0:109::2",
          "reply_ms": "463.514",
          "pmtu": null,
          "asymmetric_difference": null,
          "reached": true
        }
      ]
    }
"""
import re
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.4'
    description = '`tracepath` and `tracepath6` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['tracepath', 'tracepath6']
    tags = ['command']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured data to conform to the schema.
    """
    pass


def parse(data, raw=False, quiet=False):
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
