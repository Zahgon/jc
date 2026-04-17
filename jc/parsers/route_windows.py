r"""
    jc - JSON Convert Windows `route` command output parser
"""


import re
from typing import List

SEPARATORS = (
    "===========================================================================",
    "  None"
)

# 22...00 50 56 c0 00 01 ......VMware Virtual Ethernet Adapter for VMnet1
# {"id": 22, "mac": "00 50 56 c0 00 01", "name": "VMware Virtual Ethernet Adapter for VMnet1"}
INTERFACE_REGEX = re.compile(
    r"^(?P<id>\d+)\.{3}(?P<mac>.{17})[\s+\.]+(?P<name>[^\n\r]+)$"
)

ROUTE_TABLES = ("IPv4 Route Table", "IPv6 Route Table")
ROUTE_TYPES = ("Active Routes:", "Persistent Routes:")


def get_lines_until_seperator(iterator):
    pass


def normalize_route_table(route_table: List[str]):
    pass


def parse(cleandata: List[str]):
    """
    Main text parsing function for Windows route

    Parameters:

        cleandata:   (string)  text data to parse

    Returns:

        List of Dictionaries. Raw structured data.
    """
    pass
