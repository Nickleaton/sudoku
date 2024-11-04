from typing import List

from src.utils.config import Config

# Initialize the configuration object to access color settings
config: Config = Config()


class ColourSet:
    """A utility class for managing and retrieving color sets."""

    @staticmethod
    def colours(set_name: str) -> List[str]:
        """Retrieve a list of colors associated with a specific set name.

        Args:
            set_name (str): The name of the color set to retrieve.

        Returns:
            List[str]: A list of color strings in the specified set.
        """
        return config.colours[set_name]

    @staticmethod
    def colour(set_name: str, index: int) -> str:
        """Retrieve a single color from a specified color set at a given index.

        Args:
            set_name (str): The name of the color set to retrieve from.
            index (int): The index of the color within the set.

        Returns:
            str: The color string at the specified index in the color set.
        """
        return ColourSet.colours(set_name)[index]
