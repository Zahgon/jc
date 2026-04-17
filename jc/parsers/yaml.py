r"""jc - JSON Convert `YAML` file parser

> Note: `datetime` objects will be converted to strings.

Usage (cli):

    $ cat foo.yaml | jc --yaml

Usage (module):

    import jc
    result = jc.parse('yaml', yaml_file_output)

Schema:

YAML Document converted to a Dictionary.
See https://pypi.org/project/ruamel.yaml for details.

    [
      {
        "key1":     string/int/float/boolean/null/array/object,
        "key2":     string/int/float/boolean/null/array/object
      }
    ]

Examples:

    $ cat file.yaml
    apiVersion: "authentication.istio.io/v1alpha1"
    kind: "Policy"
    metadata:
      name: "default"
      namespace: "default"
    spec:
      peers:
      - mtls: {}
    ---
    apiVersion: "networking.istio.io/v1alpha3"
    kind: "DestinationRule"
    metadata:
      name: "default"
      namespace: "default"
    spec:
      host: "*.default.svc.cluster.local"
      trafficPolicy:
        tls:
          mode: ISTIO_MUTUAL

    $ cat file.yaml | jc --yaml -p
    [
      {
        "apiVersion": "authentication.istio.io/v1alpha1",
        "kind": "Policy",
        "metadata": {
          "name": "default",
          "namespace": "default"
        },
        "spec": {
          "peers": [
            {
              "mtls": {}
            }
          ]
        }
      },
      {
        "apiVersion": "networking.istio.io/v1alpha3",
        "kind": "DestinationRule",
        "metadata": {
          "name": "default",
          "namespace": "default"
        },
        "spec": {
          "host": "*.default.svc.cluster.local",
          "trafficPolicy": {
            "tls": {
              "mode": "ISTIO_MUTUAL"
            }
          }
        }
      }
    ]
"""
import jc.utils
from jc.exceptions import LibraryNotInstalled


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.8'
    description = 'YAML file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    details = 'Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
    tags = ['standard', 'file', 'string']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Each dictionary represents a YAML document.
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

        List of Dictionaries representing the YAML documents.
    """
    pass
