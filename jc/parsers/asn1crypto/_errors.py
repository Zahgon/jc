# coding: utf-8

"""
Exports the following items:

 - unwrap()
 - APIException()
"""

from __future__ import unicode_literals, division, absolute_import, print_function

import re
import textwrap


class APIException(Exception):
    """
    An exception indicating an API has been removed from asn1crypto
    """

    pass


def unwrap(string, *params):
    """
    Takes a multi-line string and does the following:

     - dedents
     - converts newlines with text before and after into a single line
     - strips leading and trailing whitespace

    :param string:
        The string to format

    :param *params:
        Params to interpolate into the string

    :return:
        The formatted string
    """
    pass
