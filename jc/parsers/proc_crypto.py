r"""jc - JSON Convert `/proc/crypto` file parser

Usage (cli):

    $ cat /proc/crypto | jc --proc

or

    $ jc /proc/crypto

or

    $ cat /proc/crypto | jc --proc-crypto

Usage (module):

    import jc
    result = jc.parse('proc', proc_crypto_file)

or

    import jc
    result = jc.parse('proc_crypto', proc_crypto_file)

Schema:

"Well-known" keys like `priority` and `refcnt` are converted to integers.
Also, keynames ending in "size" are converted to integers.

If this is not desired, then use the `--raw` (CLI) or `raw=True` (Module)
option.

    [
      {
        "name":                   string,
        "driver":                 string,
        "module":                 string,
        "priority":               integer,
        "refcnt":                 integer,
        "selftest":               string,
        "internal":               string,
        "type":                   string,
        "*size":                  integer
      }
    ]

Examples:

    $ cat /proc/crypto | jc --proc -p
    [
      {
        "name": "ecdh",
        "driver": "ecdh-generic",
        "module": "ecdh_generic",
        "priority": 100,
        "refcnt": 1,
        "selftest": "passed",
        "internal": "no",
        "type": "kpp"
      },
      {
        "name": "blake2b-512",
        "driver": "blake2b-512-generic",
        "module": "blake2b_generic",
        "priority": 100,
        "refcnt": 1,
        "selftest": "passed",
        "internal": "no",
        "type": "shash",
        "blocksize": 128,
        "digestsize": 64
      },
      pass
    ]

    $ cat /proc/crypto | jc --proc_crypto -p -r
    [
      {
        "name": "ecdh",
        "driver": "ecdh-generic",
        "module": "ecdh_generic",
        "priority": "100",
        "refcnt": "1",
        "selftest": "passed",
        "internal": "no",
        "type": "kpp"
      },
      {
        "name": "blake2b-512",
        "driver": "blake2b-512-generic",
        "module": "blake2b_generic",
        "priority": "100",
        "refcnt": "1",
        "selftest": "passed",
        "internal": "no",
        "type": "shash",
        "blocksize": "128",
        "digestsize": "64"
      },
      {
        "name": "blake2b-384",
        "driver": "blake2b-384-generic",
        "module": "blake2b_generic",
        "priority": "100",
        "refcnt": "1",
        "selftest": "passed",
        "internal": "no",
        "type": "shash",
        "blocksize": "128",
        "digestsize": "48"
      },
      pass
    ]
"""
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`/proc/crypto` file parser'
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
