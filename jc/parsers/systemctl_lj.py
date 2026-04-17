r"""jc - JSON Convert `systemctl list-jobs` command output parser

Usage (cli):

    $ systemctl list-jobs | jc --systemctl-lj

or

    $ jc systemctl list-jobs

Usage (module):

    import jc
    result = jc.parse('systemctl_lj', systemctl_lj_command_output)

Schema:

    [
      {
        "job":      integer,
        "unit":     string,
        "type":     string,
        "state":    string
      }
    ]

Examples:

    $ systemctl list-jobs| jc --systemctl-lj -p
    [
      {
        "job": 3543,
        "unit": "nginxAfterGlusterfs.service",
        "type": "start",
        "state": "waiting"
      },
      {
        "job": 3545,
        "unit": "glusterReadyForLocalhostMount.service",
        "type": "start",
        "state": "running"
      },
      {
        "job": 3506,
        "unit": "nginx.service",
        "type": "start",
        "state": "waiting"
      }
    ]

    $ systemctl list-jobs| jc --systemctl-lj -p -r
    [
      {
        "job": "3543",
        "unit": "nginxAfterGlusterfs.service",
        "type": "start",
        "state": "waiting"
      },
      {
        "job": "3545",
        "unit": "glusterReadyForLocalhostMount.service",
        "type": "start",
        "state": "running"
      },
      {
        "job": "3506",
        "unit": "nginx.service",
        "type": "start",
        "state": "waiting"
      }
    ]
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.7'
    description = '`systemctl list-jobs` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['systemctl list-jobs']
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
