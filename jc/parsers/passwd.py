r"""jc - JSON Convert `/etc/passwd` file Parser

Usage (cli):

    $ cat /etc/passwd | jc --passwd

Usage (module):

    import jc
    result = jc.parse('passwd', passwd_file_output)

Schema:

    [
      {
        "username":     string,
        "password":     string,
        "uid":          integer,
        "gid":          integer,
        "comment":      string,
        "home":         string,
        "shell":        string
      }
    ]

Examples:

    $ cat /etc/passwd | jc --passwd -p
    [
      {
        "username": "nobody",
        "password": "*",
        "uid": -2,
        "gid": -2,
        "comment": "Unprivileged User",
        "home": "/var/empty",
        "shell": "/usr/bin/false"
      },
      {
        "username": "root",
        "password": "*",
        "uid": 0,
        "gid": 0,
        "comment": "System Administrator",
        "home": "/var/root",
        "shell": "/bin/sh"
      },
      {
        "username": "daemon",
        "password": "*",
        "uid": 1,
        "gid": 1,
        "comment": "System Services",
        "home": "/var/root",
        "shell": "/usr/bin/false"
      },
      pass
    ]

    $ cat /etc/passwd | jc --passwd -p -r
    [
      {
        "username": "nobody",
        "password": "*",
        "uid": "-2",
        "gid": "-2",
        "comment": "Unprivileged User",
        "home": "/var/empty",
        "shell": "/usr/bin/false"
      },
      {
        "username": "root",
        "password": "*",
        "uid": "0",
        "gid": "0",
        "comment": "System Administrator",
        "home": "/var/root",
        "shell": "/bin/sh"
      },
      {
        "username": "daemon",
        "password": "*",
        "uid": "1",
        "gid": "1",
        "comment": "System Services",
        "home": "/var/root",
        "shell": "/usr/bin/false"
      },
      pass
    ]
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.4'
    description = '`/etc/passwd` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'aix', 'freebsd']
    tags = ['file']


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
