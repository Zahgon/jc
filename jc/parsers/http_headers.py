r"""jc - JSON Convert HTTP headers parser

Converts HTTP request and response headers into a list of dictionaries.
Well-known headers are processed to allow multiple instances which are
aggregated into an array along with any comma-separated values. Integer,
float, and datetimes are converted where defined in the specifications.

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
https://datatracker.ietf.org/doc/html/rfc2616
https://datatracker.ietf.org/doc/html/rfc3229
https://datatracker.ietf.org/doc/html/rfc7089
https://datatracker.ietf.org/doc/html/rfc7231
https://datatracker.ietf.org/doc/html/rfc5789

If you are converting HTTP headers from `curl` verbose output, use the
`curl-head` parser which will strip the `>` and `<` characters and remove
non-header lines that begin with `*`.

Usage (cli):

    $ cat headers.txt | jc --http-headers

Usage (module):

    import jc
    result = jc.parse('http_headers', http_headers_output)

Schema:

    [
      {
        "_type":                                string,  # request or response
        "_request_method":                      string,
        "_request_uri":                         string,
        "_request_version":                     string,
        "_response_version":                    string,
        "_response_status":                     integer,
        "_response_reason":                     string or null,
        "<header>":                             string,

        # well-known headers:

        "accept": [
                                                string
        ],
        "accept-ch": [
                                                string
        ],
        "accept-ch-lifetime":                   integer,
        "accept-encoding": [
                                                string
        ],
        "accept-language": [
                                                string
        ],
        "accept-patch": [
                                                string
        ],
        "accept-post": [
                                                string
        ],
        "accept-ranges": [
                                                string
        ],
        "access-control-allow-headers": [
                                                string
        ],
        "access-control-allow-methods": [
                                                string
        ],
        "access-control-expose-headers": [
                                                string
        ],
        "access-control-max-age":               integer,
        "access-control-request-headers": [
                                                string
        ],
        "age":                                  integer,
        "allow": [
                                                string
        ],
        "alt-svc": [
                                                string
        ],
        "cache-control": [
                                                string
        ],
        "clear-site-data": [
                                                string
        ],
        "connection": [
                                                string
        ],
        "content-encoding": [
                                                string
        ],
        "content-dpr":                          integer,
        "content-language": [
                                                string
        ],
        "content-length":                       integer,
        "content-security-policy": [
                                                string
        ],
        "content-security-policy-report-only": [
                                                string
        ],
        "cookie": [
                                                string
        ],
        "critical-ch": [
                                                string
        ],
        "date":                                 string,
        "date_epoch_utc":                       integer,
        "expect-ct": [
                                                string
        ],
        "expires":                              string,
        "expires_epoch_utc":                    integer,
        "device-memory":                        integer,
        "downlink":                             integer,
        "dpr":                                  integer,
        "forwarded": [
                                                string
        ],
        "if-match": [
                                                string
        ],
        "if-modified-since":                    string,
        "if-modified-since_epoch_utc":          integer,
        "if-none-match": [
                                                string
        ],
        "if-range":                             string,
        "if-range_epoch_utc":                   integer,
        "if-unmodified-since":                  string,
        "if-unmodified-since_epoch_utc":        integer,
        "im": [
                                                string
        ],
        "keep-alive": [
                                                string
        ],
        "large-allocation":                     integer,
        "last-modified":                        string,
        "last-modified_epoch_utc":              integer,
        "link": [
                                                string
        ],
        "max-forwards":                         integer,
        "memento-datetime":                     string,
        "memento-datetime_epoch_utc":           integer,
        "permissions-policy": [
                                                string
        ],
        "permissions-policy-report-only": [
                                                string
        ],
        "pragma": [
                                                string
        ],
        "proxy-authenticate": [
                                                string
        ],
        "reporting-endpoints": [
                                                string
        ],
        "retry-after":                          string,
        "retry-after_epoch_utc":                integer,
        "rtt":                                  integer,
        "sec-ch-ua": [
                                                string
        ],
        "sec-ch-ua-full-version-list": [
                                                string
        ],
        "server": [
                                                string
        ],
        "server-timing": [
                                                string
        ],
        "set-cookie": [
                                                string
        ],
        "timing-allow-origin": [
                                                string
        ],
        "trailer": [
                                                string
        ],
        "transfer-encoding": [
                                                string
        ],
        "upgrade": [
                                                string
        ],
        "upgrade-insecure-requests":            integer,
        "vary": [
                                                string
        ],
        "via": [
                                                string
        ],
        "warning": [
                                                string
        ],
        "www-authenticate": [
                                                string
        ],
        "x-cache-hits": [
                                                integer
        ],
        "x-content-duration":                   float
      }
    ]

Examples:

    $ cat headers.txt | jc --http-headers -p
    [
      {
        "_type": "request",
        "_request_method": "HEAD",
        "_request_uri": "/",
        "_request_version": "HTTP/1.1",
        "host": "example.com",
        "user-agent": "curl/8.1.2",
        "accept": [
          "*/*"
        ]
      },
      {
        "_type": "response",
        "_response_version": "HTTP/1.1",
        "_response_status": 200,
        "_response_reason": [
          "OK"
        ],
        "accept-ranges": [
          "bytes"
        ],
        "age": 140203,
        "cache-control": [
          "max-age=604800"
        ],
        "content-type": "text/html; charset=UTF-8",
        "date": "Sun, 04 Feb 2024 02:25:07 GMT",
        "etag": "\"3147526947\"",
        "expires": "Sun, 11 Feb 2024 02:25:07 GMT",
        "last-modified": "Thu, 17 Oct 2019 07:18:26 GMT",
        "server": [
          "ECS (sac/252F)"
        ],
        "x-cache": "HIT",
        "content-length": 1256,
        "date_epoch_utc": 1707013507,
        "expires_epoch_utc": 1707618307,
        "last-modified_epoch_utc": 1571296706
      }
    ]

    $ cat headers.txt | jc --http-headers -p -r
    [
      {
        "_type": "request",
        "_request_method": "HEAD",
        "_request_uri": "/",
        "_request_version": "HTTP/1.1",
        "host": "example.com",
        "user-agent": "curl/8.1.2",
        "accept": [
          "*/*"
        ]
      },
      {
        "_type": "response",
        "_response_version": "HTTP/1.1",
        "_response_status": 200,
        "_response_reason": [
          "OK"
        ],
        "accept-ranges": [
          "bytes"
        ],
        "age": "140203",
        "cache-control": [
          "max-age=604800"
        ],
        "content-type": "text/html; charset=UTF-8",
        "date": "Sun, 04 Feb 2024 02:25:07 GMT",
        "etag": "\"3147526947\"",
        "expires": "Sun, 11 Feb 2024 02:25:07 GMT",
        "last-modified": "Thu, 17 Oct 2019 07:18:26 GMT",
        "server": [
          "ECS (sac/252F)"
        ],
        "x-cache": "HIT",
        "content-length": "1256"
      }
    ]
"""
from typing import List, Dict
from jc.jc_types import JSONDictType
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = 'HTTP headers parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'file']


__version__ = info.version

METHODS = {'connect', 'delete', 'get', 'head', 'options', 'patch', 'post', 'put', 'trace'}

INT_HEADERS = {
    'accept-ch-lifetime',
    'access-control-max-age',
    'age',
    'content-dpr',
    'content-length',
    'device-memory',
    'downlink',
    'dpr',
    'large-allocation',
    'max-forwards',
    'rtt',
    'upgrade-insecure-requests'
}

FLOAT_HEADERS = {
    'x-content-duration'
}

DT_HEADERS = {
    'date',
    'if-modified-since',
    'if-unmodified-since',
    'last-modified',
    'memento-datetime'
}

DT_OR_INT_HEADERS = {
    'expires',
    'retry-after'
}

DT_OR_STR_HEADERS = {
    'if-range'
}

MULTI_HEADERS = {
    'content-security-policy',
    'content-security-policy-report-only',
    'cookie',
    'set-cookie'
}

SPLIT_AND_MULTI_HEADERS = {
    'accept',
    'accept-ch',
    'accept-encoding',
    'accept-language',
    'accept-patch',
    'accept-post',
    'accept-ranges',
    'access-control-allow-headers',
    'access-control-allow-methods',
    'access-control-expose-headers',
    'access-control-request-headers',
    'allow',
    'alt-svc',
    'cache-control',
    'clear-site-data',
    'connection',
    'content-encoding',
    'content-language',
    'critical-ch',
    'expect-ct',
    'forwarded',
    'if-match',
    'if-none-match',
    'im',
    'keep-alive',
    'link',
    'permissions-policy',
    'permissions-policy-report-only',
    'pragma',
    'proxy-authenticate',
    'reporting-endpoints',
    'sec-ch-ua',
    'sec-ch-ua-full-version-list',
    'server',
    'server-timing',
    'timing-allow-origin',
    'trailer',
    'transfer-encoding',
    'upgrade',
    'vary',
    'via',
    'warning',
    'www-authenticate',
    'x-cache-hits'
}

def _process(proc_data: List[JSONDictType]) -> List[JSONDictType]:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured to conform to the schema.
    """
    pass


def parse(
    data: str,
    raw: bool = False,
    quiet: bool = False
) -> List[JSONDictType]:
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
