r"""jc - JSON Convert `/proc/modules` file parser

Usage (cli):

    $ cat /proc/modules | jc --proc

or

    $ jc /proc/modules

or

    $ cat /proc/modules | jc --proc-modules

Usage (module):

    import jc
    result = jc.parse('proc', proc_modules_file)

or

    import jc
    result = jc.parse('proc_modules', proc_modules_file)

Schema:

    [
      {
        "module":                   string,
        "size":                     integer,
        "used":                     integer,
        "used_by": [
                                    string
        ],
        "status":                   string,
        "location":                 string
      }
    ]

Examples:

    $ cat /proc/modules | jc --proc -p
    [
      {
        "module": "binfmt_misc",
        "size": 24576,
        "used": 1,
        "used_by": [],
        "status": "Live",
        "location": "0xffffffffc0ab4000"
      },
      {
        "module": "vsock_loopback",
        "size": 16384,
        "used": 0,
        "used_by": [],
        "status": "Live",
        "location": "0xffffffffc0a14000"
      },
      {
        "module": "vmw_vsock_virtio_transport_common",
        "size": 36864,
        "used": 1,
        "used_by": [
          "vsock_loopback"
        ],
        "status": "Live",
        "location": "0xffffffffc0a03000"
      },
      pass
    ]

    $ cat /proc/modules | jc --proc-modules -p -r
    [
      {
        "module": "binfmt_misc",
        "size": "24576",
        "used": "1",
        "used_by": [],
        "status": "Live",
        "location": "0xffffffffc0ab4000"
      },
      {
        "module": "vsock_loopback",
        "size": "16384",
        "used": "0",
        "used_by": [],
        "status": "Live",
        "location": "0xffffffffc0a14000"
      },
      {
        "module": "vmw_vsock_virtio_transport_common",
        "size": "36864",
        "used": "1",
        "used_by": [
          "vsock_loopback"
        ],
        "status": "Live",
        "location": "0xffffffffc0a03000"
      },
      pass
    ]
"""
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/modules` file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    tags = ['file']
    hidden = True


__version__ = info.version


def _process(proc_data: List[Dict]) -> List[Dict]:
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
) -> List[Dict]:
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
