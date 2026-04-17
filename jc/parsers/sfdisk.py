r"""jc - JSON Convert `sfdisk` command output parser

Supports the following `sfdisk` options:
- `-l`
- `-F`
- `-d`   (deprecated - only for older versions of util-linux)
- `-uM`  (deprecated - only for older versions of util-linux)
- `-uC`  (deprecated - only for older versions of util-linux)
- `-uS`  (deprecated - only for older versions of util-linux)
- `-uB`  (deprecated - only for older versions of util-linux)

Usage (cli):

    # sfdisk -l | jc --sfdisk

or

    # jc sfdisk -l

Usage (module):

    import jc
    result = jc.parse('sfdisk', sfdisk_command_output)

Schema:

    [
      {
        "disk":                     string,
        "disk_size":                string,
        "free_disk_size":           string,
        "bytes":                    integer,
        "free_bytes":               integer,
        "sectors":                  integer,
        "free_sectors":             integer,
        "cylinders":                integer,
        "heads":                    integer,
        "sectors_per_track":        integer,
        "units":                    string,
        "logical_sector_size":      integer,
        "physical_sector_size":     integer,
        "min_io_size":              integer,
        "optimal_io_size":          integer,
        "disk_label_type":          string,
        "disk_identifier":          string,
        "disk_model":               string,
        "partitions": [
          {
            "device":               string,
            "boot":                 boolean,
            "start":                integer,
            "end":                  integer,
            "size":                 string,    # [0]
            "cyls":                 integer,
            "mib":                  integer,
            "blocks":               integer,
            "sectors":              integer,
            "id":                   string,
            "system":               string,
            "type":                 string
          }
        ]
      }
    ]

    [0] will be integer when using deprecated -d sfdisk option

Examples:

    # sfdisk -l | jc --sfdisk -p
    [
      {
        "disk": "/dev/sda",
        "cylinders": 2610,
        "heads": 255,
        "sectors_per_track": 63,
        "units": "cylinders of 8225280 bytes, blocks of 1024 bytes, ...",
        "partitions": [
          {
            "device": "/dev/sda1",
            "boot": true,
            "start": 0,
            "end": 130,
            "cyls": 131,
            "blocks": 1048576,
            "id": "83",
            "system": "Linux"
          },
          {
            "device": "/dev/sda2",
            "boot": false,
            "start": 130,
            "end": 2610,
            "cyls": 2481,
            "blocks": 19921920,
            "id": "8e",
            "system": "Linux LVM"
          },
          {
            "device": "/dev/sda3",
            "boot": false,
            "start": 0,
            "end": null,
            "cyls": 0,
            "blocks": 0,
            "id": "0",
            "system": "Empty"
          },
          {
            "device": "/dev/sda4",
            "boot": false,
            "start": 0,
            "end": null,
            "cyls": 0,
            "blocks": 0,
            "id": "0",
            "system": "Empty"
          }
        ]
      },
      {
        "disk": "/dev/mapper/centos-root",
        "cylinders": 2218,
        "heads": 255,
        "sectors_per_track": 63
      },
      {
        "disk": "/dev/mapper/centos-swap",
        "cylinders": 261,
        "heads": 255,
        "sectors_per_track": 63
      }
    ]

    # sfdisk -l | jc --sfdisk -p -r
    [
      {
        "disk": "/dev/sda",
        "cylinders": "2610",
        "heads": "255",
        "sectors_per_track": "63",
        "units": "cylinders of 8225280 bytes, blocks of 1024 bytes, co...",
        "partitions": [
          {
            "device": "/dev/sda1",
            "boot": "*",
            "start": "0+",
            "end": "130-",
            "cyls": "131-",
            "blocks": "1048576",
            "id": "83",
            "system": "Linux"
          },
          {
            "device": "/dev/sda2",
            "boot": null,
            "start": "130+",
            "end": "2610-",
            "cyls": "2481-",
            "blocks": "19921920",
            "id": "8e",
            "system": "Linux LVM"
          },
          {
            "device": "/dev/sda3",
            "boot": null,
            "start": "0",
            "end": "-",
            "cyls": "0",
            "blocks": "0",
            "id": "0",
            "system": "Empty"
          },
          {
            "device": "/dev/sda4",
            "boot": null,
            "start": "0",
            "end": "-",
            "cyls": "0",
            "blocks": "0",
            "id": "0",
            "system": "Empty"
          }
        ]
      },
      {
        "disk": "/dev/mapper/centos-root",
        "cylinders": "2218",
        "heads": "255",
        "sectors_per_track": "63"
      },
      {
        "disk": "/dev/mapper/centos-swap",
        "cylinders": "261",
        "heads": "255",
        "sectors_per_track": "63"
      }
    ]
"""
import jc.utils
import jc.parsers.universal


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.3'
    description = '`sfdisk` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['sfdisk']
    tags = ['command']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured to conform to the schema.
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
