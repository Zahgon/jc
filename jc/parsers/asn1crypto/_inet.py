# coding: utf-8
from __future__ import unicode_literals, division, absolute_import, print_function

import socket
import struct

from ._errors import unwrap
from ._types import type_name


def inet_ntop(address_family, packed_ip):
    """
    Windows compatibility shim for socket.inet_ntop().

    :param address_family:
        socket.AF_INET for IPv4 or socket.AF_INET6 for IPv6

    :param packed_ip:
        A byte string of the network form of an IP address

    :return:
        A unicode string of the IP address
    """
    pass


def inet_pton(address_family, ip_string):
    """
    Windows compatibility shim for socket.inet_ntop().

    :param address_family:
        socket.AF_INET for IPv4 or socket.AF_INET6 for IPv6

    :param ip_string:
        A unicode string of an IP address

    :return:
        A byte string of the network form of the IP address
    """
    pass
