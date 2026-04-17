r"""jc - JSON Convert `fstab` file parser

Usage (cli):

    $ cat /etc/fstab | jc --fstab

Usage (module):

    import jc
    result = jc.parse('fstab', fstab_command_output)

Schema:

    [
      {
        "fs_spec":      string,
        "fs_file":      string,
        "fs_vfstype":   string,
        "fs_mntops":    string,
        "fs_freq":      integer,
        "fs_passno":    integer
      }
    ]

Examples:

    $ cat /etc/fstab | jc --fstab -p
    [
      {
        "fs_spec": "/dev/mapper/centos-root",
        "fs_file": "/",
        "fs_vfstype": "xfs",
        "fs_mntops": "defaults",
        "fs_freq": 0,
        "fs_passno": 0
      },
      {
        "fs_spec": "UUID=05d927bb-5875-49e3-ada1-7f46cb31c932",
        "fs_file": "/boot",
        "fs_vfstype": "xfs",
        "fs_mntops": "defaults",
        "fs_freq": 0,
        "fs_passno": 0
      },
      {
        "fs_spec": "/dev/mapper/centos-swap",
        "fs_file": "swap",
        "fs_vfstype": "swap",
        "fs_mntops": "defaults",
        "fs_freq": 0,
        "fs_passno": 0
      }
    ]

    $ cat /etc/fstab | jc --fstab -p -r
    [
      {
        "fs_spec": "/dev/mapper/centos-root",
        "fs_file": "/",
        "fs_vfstype": "xfs",
        "fs_mntops": "defaults",
        "fs_freq": "0",
        "fs_passno": "0"
      },
      {
        "fs_spec": "UUID=05d927bb-5875-49e3-ada1-7f46cb31c932",
        "fs_file": "/boot",
        "fs_vfstype": "xfs",
        "fs_mntops": "defaults",
        "fs_freq": "0",
        "fs_passno": "0"
      },
      {
        "fs_spec": "/dev/mapper/centos-swap",
        "fs_file": "swap",
        "fs_vfstype": "swap",
        "fs_mntops": "defaults",
        "fs_freq": "0",
        "fs_passno": "0"
      }
    ]
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.7'
    description = '`/etc/fstab` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'freebsd']
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
