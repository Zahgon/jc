"""
Edid module
"""

import struct
from collections import namedtuple

__all__ = ["Edid"]

# EDID:
#      00ffffffffffff004ca3523100000000
#      0014010380221378eac8959e57549226
#      0f505400000001010101010101010101
#      010101010101381d56d4500016303020
#      250058c2100000190000000f00000000
#      000000000025d9066a00000000fe0053
#      414d53554e470a204ca34154000000fe
#      004c544e313536415432343430310018


class Edid:
    """Edid class

    Raises:
        `ValueError`: if invalid edid data
    """

    _STRUCT_FORMAT = (
        "<"  # little-endian
        "8s"  # constant header (8 bytes)
        "H"  # manufacturer id (2 bytes)
        "H"  # product id (2 bytes)
        "I"  # serial number (4 bytes)
        "B"  # manufactoring week (1 byte)
        "B"  # manufactoring year (1 byte)
        "B"  # edid version (1 byte)
        "B"  # edid revision (1 byte)
        "B"  # video input type (1 byte)
        "B"  # horizontal size in cm (1 byte)
        "B"  # vertical size in cm (1 byte)
        "B"  # display gamma (1 byte)
        "B"  # supported features (1 byte)
        "10s"  # color characteristics (10 bytes)
        "H"  # supported timings (2 bytes)
        "B"  # reserved timing (1 byte)
        "16s"  # EDID supported timings (16 bytes)
        "18s"  # detailed timing block 1 (18 bytes)
        "18s"  # detailed timing block 2 (18 bytes)
        "18s"  # detailed timing block 3 (18 bytes)
        "18s"  # detailed timing block 4 (18 bytes)
        "B"  # extension flag (1 byte)
        "B"
    )  # checksum (1 byte)

    _TIMINGS = {
        0: (1280, 1024, 75.0),
        1: (1024, 768, 75.0),
        2: (1024, 768, 70.0),
        3: (1024, 768, 60.0),
        4: (1024, 768, 87.0),
        5: (832, 624, 75.0),
        6: (800, 600, 75.0),
        7: (800, 600, 72.0),
        8: (800, 600, 60.0),
        9: (800, 600, 56.0),
        10: (640, 480, 75.0),
        11: (640, 480, 72.0),
        12: (640, 480, 67.0),
        13: (640, 480, 60.0),
        14: (720, 400, 88.0),
        15: (720, 400, 70.0),
    }

    _ASPECT_RATIOS = {
        0b00: (16, 10),
        0b01: (4, 3),
        0b10: (5, 4),
        0b11: (16, 9),
    }

    _RawEdid = namedtuple(
        "RawEdid",
        (
            "header",
            "manu_id",
            "prod_id",
            "serial_no",
            "manu_week",
            "manu_year",
            "edid_version",
            "edid_revision",
            "input_type",
            "width",
            "height",
            "gamma",
            "features",
            "color",
            "timings_supported",
            "timings_reserved",
            "timings_edid",
            "timing_1",
            "timing_2",
            "timing_3",
            "timing_4",
            "extension",
            "checksum",
        ),
    )

    def __init__(self, edid: bytes):
        self._parse_edid(edid)

    def _parse_edid(self, edid: bytes):
        """Convert edid byte string to edid object"""
        pass

    def __repr__(self):
        clsname = self.__class__.__name__
        attributes = []
        for name in dir(self):
            if not name.startswith("_"):
                value = getattr(self, name)
                attributes.append("\t{}={}".format(name, value))
        return "{}(\n{}\n)".format(clsname, ", \n".join(attributes))
