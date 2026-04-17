"""
EDID helper
"""

from subprocess import CalledProcessError, check_output
from typing import List

__all__ = ["EdidHelper"]


class EdidHelper:
    """Class for working with EDID data"""

    @staticmethod
    def hex2bytes(hex_data: str) -> bytes:
        """Convert hex EDID string to bytes

        Args:
            hex_data (str): hex edid string

        Returns:
            bytes: edid byte string
        """
        pass

    @classmethod
    def get_edids(cls) -> List[bytes]:
        """Get edids from xrandr

        Raises:
            `RuntimeError`: if error with retrieving xrandr util data

        Returns:
            List[bytes]: list with edids
        """
        pass
