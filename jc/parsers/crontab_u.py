r"""jc - JSON Convert `crontab -l` command output and crontab
file parser

This version of the `crontab -l` parser supports output that contains user
information for processes.

Usage (cli):

    $ crontab -l | jc --crontab-u

Usage (module):

    import jc
    result = jc.parse('crontab_u', crontab_u_output)

Schema:

    {
      "variables": [
        {
          "name":             string,
          "value":            string
        }
      ],
      "schedule": [
        {
          "minute": [
                              string
          ],
          "hour": [
                              string
          ],
          "day_of_month": [
                              string
          ],
          "month": [
                              string
          ],
          "day_of_week": [
                              string
          ],
          "occurrence":       string,
          "user":             string,
          "command":          string
        }
      ]
    }

Examples:

    $ cat /etc/crontab | jc --crontab-u -p
    {
      "variables": [
        {
          "name": "PATH",
          "value": "/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sb..."
        },
        {
          "name": "SHELL",
          "value": "/bin/sh"
        }
      ],
      "schedule": [
        {
          "minute": [
            "25"
          ],
          "hour": [
            "6"
          ],
          "day_of_month": [
            "*"
          ],
          "month": [
            "*"
          ],
          "day_of_week": [
            "*"
          ],
          "user": "root",
          "command": "test -x /usr/sbin/anacron || ( cd / && run-parts ..."
        },
        {
          "minute": [
            "47"
          ],
          "hour": [
            "6"
          ],
          "day_of_month": [
            "*"
          ],
          "month": [
            "*"
          ],
          "day_of_week": [
            "7"
          ],
          "user": "root",
          "command": "test -x /usr/sbin/anacron || ( cd / && run-parts ..."
        },
        {
          "minute": [
            "52"
          ],
          "hour": [
            "6"
          ],
          "day_of_month": [
            "1"
          ],
          "month": [
            "*"
          ],
          "day_of_week": [
            "*"
          ],
          "user": "root",
          "command": "test -x /usr/sbin/anacron || ( cd / && run-parts ..."
        }
      ]
    }

    $ cat /etc/crontab | jc --crontab-u -p -r
    {
      "variables": [
        {
          "name": "PATH",
          "value": "/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/..."
        },
        {
          "name": "SHELL",
          "value": "/bin/sh"
        }
      ],
      "schedule": [
        {
          "minute": "25",
          "hour": "6",
          "day_of_month": "*",
          "month": "*",
          "day_of_week": "*",
          "user": "root",
          "command": "test -x /usr/sbin/anacron || ( cd / && run-parts ..."
        },
        {
          "minute": "47",
          "hour": "6",
          "day_of_month": "*",
          "month": "*",
          "day_of_week": "7",
          "user": "root",
          "command": "test -x /usr/sbin/anacron || ( cd / && run-parts ..."
        },
        {
          "minute": "52",
          "hour": "6",
          "day_of_month": "1",
          "month": "*",
          "day_of_week": "*",
          "user": "root",
          "command": "test -x /usr/sbin/anacron || ( cd / && run-parts ..."
        }
      ]
    }
"""
import jc.utils
import jc.parsers.universal


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.10'
    description = '`crontab` file parser with user support'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'aix', 'freebsd']
    tags = ['file', 'command']


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
