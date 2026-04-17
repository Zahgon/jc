r"""jc - JSON Convert `find` command output parser

This parser returns a list of objects by default and a list of strings if
the `--raw` option is used.

Usage (cli):

    $ find | jc --find

Usage (module):

    import jc
    result = jc.parse('find', find_command_output)

Schema:

    [
      {
        "path":     string,
        "node":     string,
        "error":    string
      }
    ]

Examples:

    $ find | jc --find -p
    [
        {
          "path": "./directory"
          "node": "filename"
        },
        {
          "path": "./anotherdirectory"
          "node": "anotherfile"
        },
        {
          "path":   null
          "node":   null
          "error":  "find: './inaccessible': Permission denied"
        }
        pass
    ]

    $ find | jc --find -p -r
    [
      "./templates/readme_template",
      "./templates/manpage_template",
      "./.github/workflows/pythonapp.yml",
      pass
    ]
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`find` command parser'
    author = 'Solomon Leang'
    author_email = 'solomonleang@gmail.com'
    compatible = ['linux']
    tags = ['command']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data: (List of Strings) raw structured data to process

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

        List of raw strings or
        List of Dictionaries of processed structured data
    """
    pass
