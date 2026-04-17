r"""jc - JSON Convert Linux netstat Parser"""
import string
import re


def normalize_headers(header):
    pass


def normalize_route_headers(header):
    pass


def normalize_interface_headers(header):
    pass


def parse_network(headers, entry):
    pass


def parse_socket(header_text, headers, entry):
    # get the column # of first letter of "state"
    pass


def parse_route(headers, entry):
    pass


def parse_interface(headers, entry):
    pass


def parse_post(raw_data):
    # clean up trailing whitespace on each item in each entry
    # flags --- = null
    # program_name - = null
    # split pid and program name and ip addresses and ports
    # create network and transport protocol fields

    pass


def parse(cleandata):
    """
    Main text parsing function for OSX netstat

    Parameters:

        cleandata:   (string)  text data to parse

    Returns:

        List of Dictionaries. Raw structured data.
    """
    pass
