r"""jc - JSON Convert Java `MANIFEST.MF` file parser

Usage (cli):

    $ cat MANIFEST.MF | jc --jar-manifest

Usage (module):

    import jc
    result = jc.parse('jar_manifest', jar_manifest_file_output)

Schema:

    [
      {
        "key1":     string,
        "key2":     string
      }
    ]

Examples:

    $ cat MANIFEST.MF | jc --jar-manifest -p
    $ unzip -c log4j-core-2.16.0.jar META-INF/MANIFEST.MF | \\
      jc --jar-manifest -p
    $ unzip -c 'apache-log4j-2.16.0-bin/*.jar' META-INF/MANIFEST.MF | \\
      jc --jar-manifest -p

    $ cat MANIFEST.MF | jc --jar-manifest -p
    [
      {
        "Import_Package": "com.conversantmedia.util.concurrent;resoluti...",
        "Export_Package": "org.apache.logging.log4j.core;uses:=\"org.ap...",
        "Manifest_Version": "1.0",
        "Bundle_License": "https://www.apache.org/licenses/LICENSE-2.0.txt",
        "Bundle_SymbolicName": "org.apache.logging.log4j.core",
        "Built_By": "matt",
        "Bnd_LastModified": "1639373735804",
        "Implementation_Vendor_Id": "org.apache.logging.log4j",
        "Specification_Title": "Apache Log4j Core",
        "Log4jReleaseManager": "Matt Sicker",
        pass
      }
    ]

    $ unzip -c 'apache-log4j-2.16.0-bin/*.jar' META-INF/MANIFEST.MF | \\
      jc --jar-manifest -p
    [
      pass
      {
        "Archive": "apache-log4j-2.16.0-bin/log4j-spring-boot-2.16.0-so...",
        "Manifest_Version": "1.0",
        "Built_By": "matt",
        "Created_By": "Apache Maven 3.8.4",
        "Build_Jdk": "1.8.0_312"
      },
      {
        "Archive": "apache-log4j-2.16.0-bin/log4j-spring-boot-2.16.0-ja...",
        "Manifest_Version": "1.0",
        "Built_By": "matt",
        "Created_By": "Apache Maven 3.8.4",
        "Build_Jdk": "1.8.0_312"
      },
      {
        "Bundle_SymbolicName": "org.apache.logging.log4j.spring-cloud-c...",
        "Export_Package": "org.apache.logging.log4j.spring.cloud.config...",
        "Archive": "apache-log4j-2.16.0-bin/log4j-spring-cloud-config-c...",
        "Manifest_Version": "1.0",
        "Bundle_License": "https://www.apache.org/licenses/LICENSE-2.0.txt",
        pass
      }
      pass
    ]
"""
import jc.utils
import re


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '0.01'
    description = 'Java MANIFEST.MF file parser'
    author = 'Matt J'
    author_email = 'https://github.com/listuser'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']
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
