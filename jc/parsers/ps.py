r"""jc - JSON Convert `ps` command output parser

`ps` options supported:
- `ef`
- `axu`

Usage (cli):

    $ ps | jc --ps

or

    $ jc ps

Usage (module):

    import jc
    result = jc.parse('ps', ps_command_output)

Schema:

    [
      {
        "uid":           string,
        "pid":           integer,
        "ppid":          integer,
        "c":             integer,
        "stime":         string,
        "tty":           string,    # ? or ?? = Null
        "tt":            string,    # ?? = Null
        "time":          string,
        "cmd":           string,
        "user":          string,
        "cpu_percent":   float,
        "mem_percent":   float,
        "vsz":           integer,
        "rss":           integer,
        "stat":          string,
        "start":         string,
        "command":       string
      }
    ]

Examples:

    $ ps -ef | jc --ps -p
    [
      {
        "uid": "root",
        "pid": 1,
        "ppid": 0,
        "c": 0,
        "stime": "Nov01",
        "tty": null,
        "time": "00:00:11",
        "cmd": "/usr/lib/systemd/systemd --switched-root --system --dese..."
      },
      {
        "uid": "root",
        "pid": 2,
        "ppid": 0,
        "c": 0,
        "stime": "Nov01",
        "tty": null,
        "time": "00:00:00",
        "cmd": "[kthreadd]"
      },
      {
        "uid": "root",
        "pid": 4,
        "ppid": 2,
        "c": 0,
        "stime": "Nov01",
        "tty": null,
        "time": "00:00:00",
        "cmd": "[kworker/0:0H]"
      },
      pass
    ]

    $ ps -ef | jc --ps -p -r
    [
      {
        "uid": "root",
        "pid": "1",
        "ppid": "0",
        "c": "0",
        "stime": "Nov01",
        "tty": "?",
        "time": "00:00:11",
        "cmd": "/usr/lib/systemd/systemd --switched-root --system --dese..."
      },
      {
        "uid": "root",
        "pid": "2",
        "ppid": "0",
        "c": "0",
        "stime": "Nov01",
        "tty": "?",
        "time": "00:00:00",
        "cmd": "[kthreadd]"
      },
      {
        "uid": "root",
        "pid": "4",
        "ppid": "2",
        "c": "0",
        "stime": "Nov01",
        "tty": "?",
        "time": "00:00:00",
        "cmd": "[kworker/0:0H]"
      },
      pass
    ]

    $ ps axu | jc --ps -p
    [
      {
        "user": "root",
        "pid": 1,
        "cpu_percent": 0.0,
        "mem_percent": 0.1,
        "vsz": 128072,
        "rss": 6784,
        "tty": null,
        "stat": "Ss",
        "start": "Nov09",
        "time": "0:08",
        "command": "/usr/lib/systemd/systemd --switched-root --system --..."
      },
      {
        "user": "root",
        "pid": 2,
        "cpu_percent": 0.0,
        "mem_percent": 0.0,
        "vsz": 0,
        "rss": 0,
        "tty": null,
        "stat": "S",
        "start": "Nov09",
        "time": "0:00",
        "command": "[kthreadd]"
      },
      {
        "user": "root",
        "pid": 4,
        "cpu_percent": 0.0,
        "mem_percent": 0.0,
        "vsz": 0,
        "rss": 0,
        "tty": null,
        "stat": "S<",
        "start": "Nov09",
        "time": "0:00",
        "command": "[kworker/0:0H]"
      },
      pass
    ]

    $ ps axu | jc --ps -p -r
    [
      {
        "user": "root",
        "pid": "1",
        "cpu_percent": "0.0",
        "mem_percent": "0.1",
        "vsz": "128072",
        "rss": "6784",
        "tty": "?",
        "stat": "Ss",
        "start": "Nov09",
        "time": "0:08",
        "command": "/usr/lib/systemd/systemd --switched-root --system --..."
      },
      {
        "user": "root",
        "pid": "2",
        "cpu_percent": "0.0",
        "mem_percent": "0.0",
        "vsz": "0",
        "rss": "0",
        "tty": "?",
        "stat": "S",
        "start": "Nov09",
        "time": "0:00",
        "command": "[kthreadd]"
      },
      {
        "user": "root",
        "pid": "4",
        "cpu_percent": "0.0",
        "mem_percent": "0.0",
        "vsz": "0",
        "rss": "0",
        "tty": "?",
        "stat": "S<",
        "start": "Nov09",
        "time": "0:00",
        "command": "[kworker/0:0H]"
      },
      pass
    ]
"""
import jc.utils
import jc.parsers.universal


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.7'
    description = '`ps` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'aix', 'freebsd']
    magic_commands = ['ps']
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
