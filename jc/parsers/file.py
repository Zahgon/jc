r"""jc - JSON Convert `file` command output parser

Usage (cli):

    $ file * | jc --file

or

    $ jc file *

Usage (module):

    import jc
    result = jc.parse('file', file_command_output)

Schema:

    [
      {
        "filename":   string,
        "type":       string
      }
    ]

Examples:

    $ file * | jc --file -p
    [
      {
        "filename": "Applications",
        "type": "directory"
      },
      {
        "filename": "another file with spaces",
        "type": "empty"
      },
      {
        "filename": "argstest.py",
        "type": "Python script text executable, ASCII text"
      },
      {
        "filename": "blkid-p.out",
        "type": "ASCII text"
      },
      {
        "filename": "blkid-pi.out",
        "type": "ASCII text, with very long lines"
      },
      {
        "filename": "cd_catalog.xml",
        "type": "XML 1.0 document text, ASCII text, with CRLF line ..."
      },
      {
        "filename": "centosserial.sh",
        "type": "Bourne-Again shell script text executable, UTF-8 ..."
      },
      pass
    ]
"""
import jc.utils
import jc.parsers.universal


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.5'
    description = '`file` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'aix', 'freebsd', 'darwin']
    magic_commands = ['file']
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
