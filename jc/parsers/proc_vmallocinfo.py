r"""jc - JSON Convert `/proc/vmallocinfo` file parser

This parser will attempt to convert number values to integers. If that is
not desired, please use the `--raw` option (cli) or `raw=True` argument
(module).

Usage (cli):

    $ cat /proc/vmallocinfo | jc --proc

or

    $ jc /proc/vmallocinfo

or

    $ cat /proc/vmallocinfo | jc --proc-vmallocinfo

Usage (module):

    import jc
    result = jc.parse('proc', proc_vmallocinfo_file)

or

    import jc
    result = jc.parse('proc_vmallocinfo', proc_vmallocinfo_file)

Schema:

    [
      {
        "start":                  string,
        "end":                    string,
        "size":                   integer,
        "caller":                 string,
        "options": [
                                  string
        ],
        "phys":                   string
        "pages":                  integer,
        "N<id>":                  integer
      }
    ]

Examples:

    $ cat /proc/vmallocinfo | jc --proc -p
    [
      {
        "start": "0xffffb3c1c0000000",
        "end": "0xffffb3c1c0005000",
        "size": 20480,
        "caller": "map_irq_stack+0x93/0xe0",
        "options": [
          "vmap"
        ],
        "phys": "0x00000000bfefe000"
      },
      {
        "start": "0xffffb3c1c0005000",
        "end": "0xffffb3c1c0007000",
        "size": 8192,
        "caller": "acpi_os_map_iomem+0x1ac/0x1c0",
        "options": [
          "ioremap"
        ],
        "phys": "0x00000000bfeff000"
      },
      pass
    ]

    $ cat /proc/vmallocinfo | jc --proc-vmallocinfo -p -r
    [
      {
        "start": "0xffffb3c1c0000000",
        "end": "0xffffb3c1c0005000",
        "size": "20480",
        "caller": "map_irq_stack+0x93/0xe0",
        "options": [
          "vmap"
        ],
        "phys": "0x00000000bfefe000"
      },
      {
        "start": "0xffffb3c1c0005000",
        "end": "0xffffb3c1c0007000",
        "size": "8192",
        "caller": "acpi_os_map_iomem+0x1ac/0x1c0",
        "options": [
          "ioremap"
        ],
        "phys": "0x00000000bfeff000"
      },
      pass
    ]
"""
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/vmallocinfo` file parser'
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
