"""
Module for working with PNP ID REGISTRY
"""

import csv
import string
from html.parser import HTMLParser
from urllib import request

__all__ = ["Registry"]


class WebPnpIdParser(HTMLParser):
    """Parser pnp id from https://uefi.org/PNP_ID_List

    Examples:
        p = WebPnpIdParser()
        p.feed(html_data)
        p.result
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._find_table = False
        self._find_row = False
        # first -- company name, second -- pnp id, third -- approved date
        self._last_field = []
        # key -- pnp id, value -- tuple (company_name, approved_date)
        self.result = {}

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        # skip processing until table is found
        pass

    def error(self, message):
        pass


class Registry(dict):
    """Registry pnp id data dictionary

    key   -- pnp_id
    value -- company name
    """

    @classmethod
    def from_web(cls, filter_by_id: str = None):
        """Get registry from https://uefi.org/PNP_ID_List

        Args:
            filter_by_id (str), optional: filter registry by id

        Raises:

        Returns:

        """
        pass

    @classmethod
    def from_csv(cls, csv_path: str, filter_by_id: str = None):
        """Get registry by csv local file

        Args:
            csv_path (str): path to csv file
            filter_by_id (str), optional: filter registry by id

        Raises:

        Returns:

        """
        pass

    def to_csv(self, csv_path: str):
        """Dump registry to csv file"""
        pass

    def get_company_from_id(self, pnp_id: str) -> str:
        """Convert PNP id to company name"""
        pass

    def get_company_from_raw(self, raw: int) -> str:
        """Convert raw edid value to company name"""
        pass
