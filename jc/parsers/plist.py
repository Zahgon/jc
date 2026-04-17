r"""jc - JSON Convert PLIST file parser

Converts binary, XML, and NeXTSTEP PLIST files.

Binary values are converted into an ASCII hex representation.

Datetime objects are converted into Unix epoch timestamps and ISO strings.
The timestamp and ISO string will maintain the same naive or timezone-aware
properties as the object in the original PLIST file.

Usage (cli):

    $ cat file.plist | jc --plist

Usage (module):

    import jc
    result = jc.parse('plist', plist_file_output)

Schema:

    {
      "<key>":            string/integer/float/boolean/object/array/null
    }

Examples:

    $ cat info.plist | jc --plist -p
    {
      "NSAppleScriptEnabled": true,
      "LSMultipleInstancesProhibited": true,
      "CFBundleInfoDictionaryVersion": "6.0",
      "DTPlatformVersion": "GM",
      "CFBundleIconFile": "GarageBand.icns",
      "CFBundleName": "GarageBand",
      "DTSDKName": "macosx10.13internal",
      "NSSupportsAutomaticGraphicsSwitching": true,
      "RevisionDate": "2018-12-03_14:10:56",
      "UTImportedTypeDeclarations": [
        {
          "UTTypeConformsTo": [
            "public.data",
            "public.content"
      pass
    }
"""
import sys

# ugly hack because I accidentally shadowed the xml module from the
# standard library with the xml parser. :(
sys.path = [x for x in sys.path if 'jc/jc/parsers' not in x]

from typing import Dict, Union
import plistlib
import binascii
from datetime import datetime
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.2'
    description = 'PLIST file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    details = 'Using the pbPlist library from https://github.com/samdmarshall/pbPlist/releases/tag/v1.0.4 for NeXTSTEP support'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'file', 'string', 'binary']


__version__ = info.version


def _process(proc_data: Dict) -> Dict:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured to conform to the schema.
    """
    pass


def _b2a(byte_string: bytes) -> str:
    """Convert a byte string to a colon-delimited hex ascii string"""
    pass


def _fix_objects(obj):
    """
    Recursively traverse the nested dictionary or list and convert objects
    into JSON serializable types.
    """
    pass


def parse(
    data: Union[str, bytes],
    raw: bool = False,
    quiet: bool = False
) -> Dict:
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
