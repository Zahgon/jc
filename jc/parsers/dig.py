r"""jc - JSON Convert `dig` command output parser

Options supported:
- `+noall +answer` options are supported in cases where only the answer
  information is desired.
- `+axfr` option is supported on its own
- `+nsid` option is supported

The `when_epoch` calculated timestamp field is naive. (i.e. based on the
local time of the system the parser is run on)

The `when_epoch_utc` calculated timestamp field is timezone-aware and is
only available if the timezone field is UTC.

Usage (cli):

    $ dig example.com | jc --dig

or

    $ jc dig example.com

Usage (module):

    import jc
    result = jc.parse('dig', dig_command_output)

Schema:

    [
      {
        "id":                   integer,
        "opcode":               string,
        "status":               string,
        "flags": [
                                string
        ],
        "query_num":            integer,
        "answer_num":           integer,
        "authority_num":        integer,
        "additional_num":       integer,
        "axfr": [
          {
            "name":             string,
            "class":            string,
            "type":             string,
            "ttl":              integer,
            "data":             string
          }
        ],
        "opt_pseudosection": {
          "edns": {
            "version":          integer,
            "flags": [
                                string
            ],
            "udp":              integer
          },
          "cookie":             string
        },
        "question": {
          "name":               string,
          "class":              string,
          "type":               string
        },
        "answer": [
          {
            "name":             string,
            "class":            string,
            "type":             string,
            "ttl":              integer,
            "data":             string
          }
        ],
        "additional": [
          {
            "name":             string,
            "class":            string,
            "type":             string,
            "ttl":              integer,
            "data":             string
          }
        ],
        "authority": [
          {
            "name":             string,
            "class":            string,
            "type":             string,
            "ttl":              integer,
            "data":             string
          }
        ],
        "query_size":           integer,
        "query_time":           integer,   # in msec
        "server":               string,
        "when":                 string,
        "when_epoch":           integer,   # [0]
        "when_epoch_utc":       integer,   # [1]
        "rcvd":                 integer
        "size":                 string
      }
    ]

    [0] naive timestamp if "when" field is parsable, else null
    [1] timezone aware timestamp available for UTC, else null

Examples:

    $ dig example.com | jc --dig -p
    [
      {
        "id": 2951,
        "opcode": "QUERY",
        "status": "NOERROR",
        "flags": [
          "qr",
          "rd",
          "ra"
        ],
        "query_num": 1,
        "answer_num": 1,
        "authority_num": 0,
        "additional_num": 1,
        "opt_pseudosection": {
          "edns": {
            "version": 0,
            "flags": [],
            "udp": 4096
          }
        },
        "question": {
          "name": "example.com.",
          "class": "IN",
          "type": "A"
        },
        "answer": [
          {
            "name": "example.com.",
            "class": "IN",
            "type": "A",
            "ttl": 39302,
            "data": "93.184.216.34"
          }
        ],
        "query_time": 49,
        "server": "2600:1700:bab0:d40::1#53(2600:1700:bab0:d40::1)",
        "when": "Fri Apr 16 16:05:10 PDT 2021",
        "rcvd": 56,
        "when_epoch": 1618614310,
        "when_epoch_utc": null
      }
    ]

    $ dig cnn.com www.cnn.com @205.251.194.64 | jc --dig -p -r
    [
      {
        "id": "46052",
        "opcode": "QUERY",
        "status": "NOERROR",
        "flags": [
          "qr",
          "rd",
          "ra"
        ],
        "query_num": "1",
        "answer_num": "1",
        "authority_num": "0",
        "additional_num": "1",
        "opt_pseudosection": {
          "edns": {
            "version": "0",
            "flags": [],
            "udp": "4096"
          }
        },
        "question": {
          "name": "example.com.",
          "class": "IN",
          "type": "A"
        },
        "answer": [
          {
            "name": "example.com.",
            "class": "IN",
            "type": "A",
            "ttl": "40426",
            "data": "93.184.216.34"
          }
        ],
        "query_time": "48 msec",
        "server": "2600:1700:bab0:d40::1#53(2600:1700:bab0:d40::1)",
        "when": "Fri Apr 16 16:06:12 PDT 2021",
        "rcvd": "56"
      }
    ]

    $ dig -x 1.1.1.1 | jc --dig -p
    [
      {
        "id": 20785,
        "opcode": "QUERY",
        "status": "NOERROR",
        "flags": [
          "qr",
          "rd",
          "ra"
        ],
        "query_num": 1,
        "answer_num": 1,
        "authority_num": 0,
        "additional_num": 1,
        "opt_pseudosection": {
          "edns": {
            "version": 0,
            "flags": [],
            "udp": 4096
          }
        },
        "question": {
          "name": "1.1.1.1.in-addr.arpa.",
          "class": "IN",
          "type": "PTR"
        },
        "answer": [
          {
            "name": "1.1.1.1.in-addr.arpa.",
            "class": "IN",
            "type": "PTR",
            "ttl": 1800,
            "data": "one.one.one.one."
          }
        ],
        "query_time": 40,
        "server": "2600:1700:bab0:d40::1#53(2600:1700:bab0:d40::1)",
        "when": "Sat Apr 17 14:50:50 PDT 2021",
        "rcvd": 78,
        "when_epoch": 1618696250,
        "when_epoch_utc": null
      }
    ]

    $ dig -x 1.1.1.1 | jc --dig -p -r
    [
      {
        "id": "32644",
        "opcode": "QUERY",
        "status": "NOERROR",
        "flags": [
          "qr",
          "rd",
          "ra"
        ],
        "query_num": "1",
        "answer_num": "1",
        "authority_num": "0",
        "additional_num": "1",
        "opt_pseudosection": {
          "edns": {
            "version": "0",
            "flags": [],
            "udp": "4096"
          }
        },
        "question": {
          "name": "1.1.1.1.in-addr.arpa.",
          "class": "IN",
          "type": "PTR"
        },
        "answer": [
          {
            "name": "1.1.1.1.in-addr.arpa.",
            "class": "IN",
            "type": "PTR",
            "ttl": "1800",
            "data": "one.one.one.one."
          }
        ],
        "query_time": "52 msec",
        "server": "2600:1700:bab0:d40::1#53(2600:1700:bab0:d40::1)",
        "when": "Sat Apr 17 14:51:46 PDT 2021",
        "rcvd": "78"
      }
    ]

    $ dig +noall +answer cnn.com | jc --dig -p
    [
      {
        "answer": [
          {
            "name": "cnn.com.",
            "class": "IN",
            "type": "A",
            "ttl": 60,
            "data": "151.101.193.67"
          },
          {
            "name": "cnn.com.",
            "class": "IN",
            "type": "A",
            "ttl": 60,
            "data": "151.101.65.67"
          },
          {
            "name": "cnn.com.",
            "class": "IN",
            "type": "A",
            "ttl": 60,
            "data": "151.101.1.67"
          },
          {
            "name": "cnn.com.",
            "class": "IN",
            "type": "A",
            "ttl": 60,
            "data": "151.101.129.67"
          }
        ]
      }
    ]
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '2.5'
    description = '`dig` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'aix', 'freebsd', 'darwin', 'win32', 'cygwin']
    magic_commands = ['dig']
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


def _parse_header(header):
    # ;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 6140
    pass


def _parse_flags_line(flagsline):
    # ;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1
    pass


def _parse_opt_pseudosection(optline):
    # ;; OPT PSEUDOSECTION:
    # ; EDNS: version: 0, flags:; udp: 4096
    # ; NSID: 67 70 64 6e 73 2d 73 66 6f ("gpdns-sfo")
    # ; COOKIE: 1cbc06703eaef210
    pass


def _parse_question(question):
    # ;www.cnn.com.           IN  A
    pass


def _parse_answer(answer):
    # www.cnn.com.        5   IN  CNAME   turner-tls.map.fastly.net.
    pass


def _parse_axfr(axfr):
    # ; <<>> DiG 9.11.14-3-Debian <<>> @81.4.108.41 axfr zonetransfer.me +nocookie
    # ; (1 server found)
    # ;; global options: +cmd
    # zonetransfer.me. 7200 IN A 5.196.105.14
    pass


def _parse_footer(footer):
    # footer consists of 4 lines
    # footer line 1
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
