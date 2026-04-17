r"""jc - JSON Convert `net localgroup` command output parser

Usage (cli):

    $ net localgroup | jc --net-localgroup
    $ net localgroup /domain | jc --net-localgroup
    $ net localgroup Administrators | jc --net-localgroup
    $ net localgroup Administrators /domain | jc --net-localgroup

Usage (module):

    import jc
    result = jc.parse('net_localgroup', net_localgroup_command_output)

Schema:

    {
        "account_origin":     string,
        "domain":             string,
        "comment":            string,
        "groups": [
            {
                "name":       string
                "members": [
                              string
                ]
            }
        ],
    }

Examples:

    $ net localgroup | jc --net-localgroup -p
    {
        "account_origin": null,
        "comment": null,
        "domain": null,
        "groups": [
            {
                "name": "Administrators",
                "members": [
                    "Administrator",
                    "Operator",
                    "ansible",
                    "user1"
                ]
            }
        ]
    }
"""
import re
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`net localgroup` command parser'
    author = 'joehacksalot'
    author_email = 'joehacksalot@gmail.com'
    compatible = ['win32']
    magic_commands = ['net localgroup']
    tags = ['command']


__version__ = info.version


def parse(data, raw=False, quiet=False):
    """
    Main text parsing function

    Parameters:

        data:        (string)  text data to parse
        raw:         (boolean) unprocessed output if True
        quiet:       (boolean) suppress warning messages if True

    Returns:

        Parsed dictionary. The raw and processed data structures are the same.
    """
    pass

def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Processed Dictionary. Structured data to conform to the schema.
    """
    pass


class _PushbackIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.pushback_stack = []
    def __iter__(self):
        return self
    def __next__(self):
        if self.pushback_stack:
            return self.pushback_stack.pop()
        else:
            return next(self.iterator)
    def pushback(self, value):
        pass

def _parse_net_localgroup_list(line_iter, expect_asterisk):
    pass


def _parse(data):
    pass
