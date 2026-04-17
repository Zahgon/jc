r"""jc - JSON Convert `traceroute` command output parser

Supports `traceroute` and `traceroute6` output.

> Note: On some operating systems you will need to redirect `STDERR` to
> `STDOUT` for destination info since the header line is sent to
> `STDERR`. A warning message will be printed to `STDERR` if the
> header row is not found.
>
> e.g. `$ traceroute 8.8.8.8 2>&1 | jc --traceroute`

Usage (cli):

    $ traceroute 1.2.3.4 | jc --traceroute

or

    $ jc traceroute 1.2.3.4

Usage (module):

    import jc
    result = jc.parse('traceroute', traceroute_command_output)

Schema:

    {
      "destination_ip":         string,
      "destination_name":       string,
      "max_hops":               integer,
      "data_bytes":             integer,
      "hops": [
        {
          "hop":                integer,
          "probes": [
            {
              "annotation":     string,
              "asn":            integer,
              "ip":             string,
              "name":           string,
              "rtt":            float
            }
          ]
        }
      ]
    }

Examples:

    $ traceroute google.com | jc --traceroute -p
    {
      "destination_ip": "216.58.194.46",
      "destination_name": "google.com",
      "max_hops": 64,
      "data_bytes": 50,
      "hops": [
        {
          "hop": 1,
          "probes": [
            {
              "annotation": null,
              "asn": null,
              "ip": "216.230.231.141",
              "name": "216-230-231-141.static.houston.tx.oplink.net",
              "rtt": 198.574
            },
            {
              "annotation": null,
              "asn": null,
              "ip": "216.230.231.141",
              "name": "216-230-231-141.static.houston.tx.oplink.net",
              "rtt": null
            },
            {
              "annotation": null,
              "asn": null,
              "ip": "216.230.231.141",
              "name": "216-230-231-141.static.houston.tx.oplink.net",
              "rtt": 198.65
            }
          ]
        },
        pass
      ]
    }

    $ traceroute google.com  | jc --traceroute -p -r
    {
      "destination_ip": "216.58.194.46",
      "destination_name": "google.com",
      "max_hops": "64",
      "data_bytes": "50",
      "hops": [
        {
          "hop": "1",
          "probes": [
            {
              "annotation": null,
              "asn": null,
              "ip": "216.230.231.141",
              "name": "216-230-231-141.static.houston.tx.oplink.net",
              "rtt": "198.574"
            },
            {
              "annotation": null,
              "asn": null,
              "ip": "216.230.231.141",
              "name": "216-230-231-141.static.houston.tx.oplink.net",
              "rtt": null
            },
            {
              "annotation": null,
              "asn": null,
              "ip": "216.230.231.141",
              "name": "216-230-231-141.static.houston.tx.oplink.net",
              "rtt": "198.650"
            }
          ]
        },
        pass
      ]
    }
"""
import re
from decimal import Decimal
import jc.utils
from copy import deepcopy
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.9'
    description = '`traceroute` and `traceroute6` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    details = 'Using the trparse library by Luis Benitez at https://github.com/lbenitez000/trparse'
    compatible = ['linux', 'darwin', 'freebsd']
    magic_commands = ['traceroute', 'traceroute6']
    tags = ['command']


__version__ = info.version


'''
Copyright (C) 2015 Luis Benitez

Parses the output of a traceroute execution into an AST (Abstract Syntax Tree).

The MIT License (MIT)

Copyright (c) 2014 Luis Benitez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

RE_HEADER = re.compile(r'traceroute6? to (\S+)\s+\((\d+\.\d+\.\d+\.\d+|[0-9a-fA-F:]+)\)')
RE_HEADER_HOPS_BYTES = re.compile(r'(\d+) hops max, (\d+) byte packets')
RE_PROBE_NAME_IP = re.compile(r'(\S+)\s+\((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[0-9a-fA-F:]+)\)+')
RE_PROBE_IP_ONLY = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([^\(])')
RE_PROBE_IPV6_ONLY = re.compile(r'(([a-f0-9]*:)+[a-f0-9]+)')
RE_PROBE_BSD_IPV6 = re.compile(r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b')
RE_HOP = re.compile(r'^\s*(\d+)?\s+(.+)$')
RE_PROBE_ASN = re.compile(r'\[AS(\d+)\]')
RE_PROBE_RTT_ANNOTATION = re.compile(r'(?:(\d+(?:\.?\d+)?)\s+ms|(\s+\*\s+))\s*(!\S*)?')


class _Traceroute(object):
    def __init__(self, dest_name, dest_ip, max_hops=None, data_bytes=None):
        self.dest_name = dest_name
        self.dest_ip = dest_ip
        self.max_hops = max_hops
        self.data_bytes = data_bytes
        self.hops = []

    def add_hop(self, hop):
        pass

    def __str__(self):
        text = "Traceroute for %s (%s)\n\n" % (self.dest_name, self.dest_ip)
        for hop in self.hops:
            text += str(hop)
        return text


class _Hop(object):
    def __init__(self, idx):
        self.idx = idx  # Hop count, starting at 1 (usually)
        self.probes = []  # Series of Probe instances

    def add_probe(self, probe):
        """Adds a Probe instance to this hop's results."""
        pass

    def __str__(self):
        text = "{:>3d} ".format(self.idx)
        text_len = len(text)
        for n, probe in enumerate(self.probes):
            text_probe = str(probe)
            if n:
                text += (text_len * " ") + text_probe
            else:
                text += text_probe
        text += "\n"
        return text


class _Probe(object):
    def __init__(self, name=None, ip=None, asn=None, rtt=None, annotation=None):
        self.name = name
        self.ip = ip
        self.asn = asn  # Autonomous System number
        self.rtt = rtt  # RTT in ms
        self.annotation = annotation  # Annotation, such as !H, !N, !X, etc

    def __str__(self):
        text = ""
        if self.asn is not None:
            text += "[AS{:d}] ".format(self.asn)
        if self.rtt:
            text += "{:s} ({:s}) {:1.3f} ms".format(self.name, self.ip, self.rtt)
        else:
            text = "*"
        if self.annotation:
            text += " {:s}".format(self.annotation)
        text += "\n"
        return text


def _get_probes(hop_string: str):
    pass


def _loads(data: str, quiet: bool):
    pass


def _serialize_hop(hop: _Hop):
    pass


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured to conform to the schema.
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
