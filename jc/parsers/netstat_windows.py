r"""
    jc - JSON Convert Windows `netstat` command output parser
"""


from typing import Dict, List

POSSIBLE_PROTOCOLS = ("TCP", "UDP", "TCPv6", "UDPv6")

def normalize_headers(headers: str):
    """
        Normalizes the headers to match the jc netstat parser style
        (local_address -> local_address, local_port...).
    """
    pass


def parse(cleandata: List[str]):
    """
    Main text parsing function for Windows netstat

    Parameters:

        cleandata:   (string)  text data to parse

    Returns:

        List of Dictionaries. Raw structured data.
    """
    pass
