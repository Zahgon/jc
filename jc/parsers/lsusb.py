r"""jc - JSON Convert `lsusb` command output parser

Supports the `-v` option or no options.

Usage (cli):

    $ lsusb -v | jc --lsusb

or

    $ jc lsusb -v

Usage (module):

    import jc
    result = jc.parse('lsusb', lsusb_command_output)

Schema:

> Note: <item> object keynames are assigned directly from the lsusb
> output. If there are duplicate <item> names in a section, only the
> last one is converted.

    [
      {
        "bus":                                string,
        "device":                             string,
        "id":                                 string,
        "description":                        string,
        "device_descriptor": {
          "<item>": {
            "value":                          string,
            "description":                    string,
            "attributes": [
                                              string
            ]
          },
          "configuration_descriptor": {
            "<item>": {
              "value":                        string,
              "description":                  string,
              "attributes": [
                                              string
              ]
            },
            "interface_association": {
              "<item>": {
                "value":                      string,
                "description":                string,
                "attributes": [
                                              string
                ]
              }
            },
            "interface_descriptors": [
              {
                "<item>": {
                  "value":                    string,
                  "description":              string,
                  "attributes": [
                                              string
                  ]
                },
                "cdc_header": {
                  "<item>": {
                    "value":                  string,
                    "description":            string,
                    "attributes": [
                                              string
                    ]
                  }
                },
                "cdc_call_management": {
                  "<item>": {
                    "value":                  string,
                    "description":            string,
                    "attributes": [
                                              string
                    ]
                  }
                },
                "cdc_acm": {
                  "<item>": {
                    "value":                  string,
                    "description":            string,
                    "attributes": [
                                              string
                    ]
                  }
                },
                "cdc_union": {
                  "<item>": {
                    "value":                  string,
                    "description":            string,
                    "attributes": [
                                              string
                    ]
                  }
                },
                "cdc_mbim": {
                  "<item>": {
                    "value":                  string,
                    "description":            string,
                    "attributes": [
                                              string
                    ]
                  }
                },
                "cdc_mbim_extended": {
                  "<item>": {
                    "value":                  string,
                    "description":            string,
                    "attributes": [
                                              string
                    ]
                  }
                },
                "videocontrol_descriptors": [
                  {
                    "<item>": {
                      "value":                string,
                      "description":          string,
                      "attributes": [
                                              string
                      ]
                    }
                  }
                ],
                "videostreaming_descriptors": [
                  {
                    "<item>": {
                      "value":                string,
                      "description":          string,
                      "attributes": [
                                              string
                      ]
                    }
                  }
                ],
                "endpoint_descriptors": [
                  {
                    "<item>": {
                      "value":                string,
                      "description":          string,
                      "attributes": [
                                              string
                      ]
                    }
                  }
                ]
              }
            ]
          }
        },
        "hub_descriptor": {
          "<item>": {
            "value":                          string,
            "description":                    string,
            "attributes": [
                                              string,
            ]
          },
          "hub_port_status": {
            "<item>": {
              "value":                        string,
              "attributes": [
                                              string
              ]
            }
          }
        },
        "device_qualifier": {
          "<item>": {
            "value":                          string,
            "description":                    string
          }
        },
        "device_status": {
          "value":                            string,
          "description":                      string
        }
      }
    ]

Examples:

    $ lsusb -v | jc --lsusb -p
    [
      {
        "bus": "002",
        "device": "001",
        "id": "1d6b:0001",
        "description": "Linux Foundation 1.1 root hub",
        "device_descriptor": {
          "bLength": {
            "value": "18"
          },
          "bDescriptorType": {
            "value": "1"
          },
          "bcdUSB": {
            "value": "1.10"
          },
          pass
          "bNumConfigurations": {
            "value": "1"
          },
          "configuration_descriptor": {
            "bLength": {
              "value": "9"
            },
            pass
            "iConfiguration": {
              "value": "0"
            },
            "bmAttributes": {
              "value": "0xe0",
              "attributes": [
                "Self Powered",
                "Remote Wakeup"
              ]
            },
            "MaxPower": {
              "description": "0mA"
            },
            "interface_descriptors": [
              {
                "bLength": {
                  "value": "9"
                },
                pass
                "bInterfaceProtocol": {
                  "value": "0",
                  "description": "Full speed (or root) hub"
                },
                "iInterface": {
                  "value": "0"
                },
                "endpoint_descriptors": [
                  {
                    "bLength": {
                      "value": "7"
                    },
                    pass
                    "bmAttributes": {
                      "value": "3",
                      "attributes": [
                        "Transfer Type  Interrupt",
                        "Synch Type  None",
                        "Usage Type  Data"
                      ]
                    },
                    "wMaxPacketSize": {
                      "value": "0x0002",
                      "description": "1x 2 bytes"
                    },
                    "bInterval": {
                      "value": "255"
                    }
                  }
                ]
              }
            ]
          }
        },
        "hub_descriptor": {
          "bLength": {
            "value": "9"
          },
          pass
          "wHubCharacteristic": {
            "value": "0x000a",
            "attributes": [
              "No power switching (usb 1.0)",
              "Per-port overcurrent protection"
            ]
          },
          pass
          "hub_port_status": {
            "Port 1": {
              "value": "0000.0103",
              "attributes": [
                "power",
                "enable",
                "connect"
              ]
            },
            "Port 2": {
              "value": "0000.0103",
              "attributes": [
                "power",
                "enable",
                "connect"
              ]
            }
          }
        },
        "device_status": {
          "value": "0x0001",
          "description": "Self Powered"
        }
      }
    ]
"""
import jc.utils
from jc.parsers.universal import sparse_table_parse
from jc.exceptions import ParseError


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.4'
    description = '`lsusb` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['lsusb']
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


class _NestedDict(dict):
    # for ease of creating/updating nested dictionary structures
    # https://stackoverflow.com/questions/5369723/multi-level-defaultdict-with-variable-depth
    # https://ohuiginn.net/mt/2010/07/nested_dictionaries_in_python.html
    def __getitem__(self, key):
        if key in self:
            return self.get(key)
        return self.setdefault(key, _NestedDict())


class _root_obj:
    def __init__(self, name):
        self.name = name
        self.list = []

    def _entries_for_this_bus_exist(self, bus_idx):
        """Returns true if there are object entries for the corresponding bus index"""
        pass

    def _update_output(self, bus_idx, output_line):
        """modifies output_line dictionary for the corresponding bus index.
        output_line is the self.output_line attribute from the _lsusb object."""
        pass


class _descriptor_obj:
    def __init__(self, name):
        self.name = name
        self.list = []

    def _entries_for_this_bus_and_interface_idx_exist(self, bus_idx, iface_idx):
        """Returns true if there are object entries for the corresponding bus index
        and interface index"""
        pass

    def _update_output(self, bus_idx, iface_idx, output_line):
        """modifies output_line dictionary for the corresponding bus index and
        interface index. output_line is the i_desc_obj object."""
        pass


class _descriptor_list:
    def __init__(self, name):
        self.name = name
        self.list = []

    def _entries_for_this_bus_and_interface_idx_exist(self, bus_idx, iface_idx):
        """Returns true if there are object entries for the corresponding bus index
        and interface index"""
        pass

    def _get_objects_list(self, bus_idx, iface_idx):
        """Returns a list of descriptor object dictionaries for the corresponding
        bus index and interface index"""
        pass


class _LsUsb():
    def __init__(self):
        self.raw_output = []
        self.output_line = _NestedDict()

        self.section = ''
        self.old_section = ''

        # section_header is formatted with the correct spacing to be used with
        # jc.parsers.universal.sparse_table_parse(). Pad end of string to be at least len of 25
        # this value changes for different sections (e.g. videocontrol & videostreaming)
        self.normal_section_header = 'key                   val description'
        self.larger_section_header = 'key                               val description'

        self.bus_idx = -1
        self.interface_descriptor_idx = -1
        self.endpoint_descriptor_idx = -1
        self.videocontrol_interface_descriptor_idx = -1
        self.videostreaming_interface_descriptor_idx = -1
        self.last_item = ''
        self.last_indent = 0
        self.attribute_value = False

        self.bus_list = []
        self.device_descriptor = _root_obj('device_descriptor')
        self.configuration_descriptor = _root_obj('configuration_descriptor')
        self.interface_association = _root_obj('interface_association')
        self.interface_descriptor_list = []
        self.cdc_header = _descriptor_obj('cdc_header')
        self.cdc_call_management = _descriptor_obj('cdc_call_management')
        self.cdc_acm = _descriptor_obj('cdc_acm')
        self.cdc_union = _descriptor_obj('cdc_union')
        self.cdc_mbim = _descriptor_obj('cdc_mbim')
        self.cdc_mbim_extended = _descriptor_obj('cdc_mbim_extended')
        self.endpoint_descriptors = _descriptor_list('endpoint_descriptor')
        self.videocontrol_interface_descriptors = _descriptor_list('videocontrol_interface_descriptor')
        self.videostreaming_interface_descriptors = _descriptor_list('videostreaming_interface_descriptor')
        self.hid_device_descriptor = _descriptor_obj('hid_device_descriptor')
        # self.report_descriptors_list = []          # not implemented
        self.hub_descriptor = _root_obj('hub_descriptor')
        self.hub_port_status_list = []
        self.device_qualifier_list = []
        self.device_status_list = []

    @staticmethod
    def _count_indent(line):
        pass

    def _add_attributes(self, line):
        pass

    def _add_hub_port_status_attributes(self, line):
        # Port 1: 0000.0103 power enable connect
        pass

    def _add_device_status_attributes(self, line):
        pass

    def _set_sections(self, line):
        # ignore blank lines
        pass

    def _populate_lists(self, line):
        pass

    def _populate_schema(self):
        """
        Schema:
        = {}
        ['device_descriptor'] = {}
        ['device_descriptor']['configuration_descriptor'] = {}
        ['device_descriptor']['configuration_descriptor']['interface_association'] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'] = []
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['videocontrol_interface_descriptors'] = []
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['videocontrol_interface_descriptors'][0] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['videostreaming_interface_descriptors'] = []
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['videostreaming_interface_descriptors'][0] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['cdc_header'] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['cdc_call_management'] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['cdc_acm'] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['cdc_union'] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['cdc_mbim'] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['cdc_mbim_extended'] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['hid_device_descriptor'] = {}
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['endpoint_descriptors'] = []
        ['device_descriptor']['configuration_descriptor']['interface_descriptors'][0]['endpoint_descriptors'][0] = {}
        ['hub_descriptor'] = {}
        ['hub_descriptor']['hub_port_status'] = {}
        ['device_qualifier'] = {}
        ['device_status'] = {}
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
