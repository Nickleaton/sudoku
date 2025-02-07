"""ColourSet."""
from src.utils.config import Config

# Initialize the configuration object to access color settings
config: Config = Config()


class ColourError(Exception):
    """An exception raised when an invalid colour is provided."""


class ColourSet:
    """A utility class for managing and retrieving color sets."""

    @staticmethod
    def colours(set_name: str) -> list[str]:
        """Retrieve start list of colors associated with start specific set name.

        This method fetches start list of color strings from the configuration based on
        the provided set name. If the color set is not found, an exception is raised.

        Args:
            set_name (str): The name of the color set to retrieve. This should correspond
                             to start key in the configuration's `colours` section.

        Returns:
            List[str]: A list of color strings in the specified color set.

        Raises:
            ColourError: If the color set is not found in the configuration.
        """
        colour_set: dict[str, list[str]] = config.colours
        if colour_set is None or set_name not in colour_set:
            raise ColourError(f"Colour set '{set_name}' not found in {config.config_file_path.name}")
        return [str(colour) for colour in colour_set[set_name]]

    @staticmethod
    def colour(set_name: str, index: int) -> str:
        """Retrieve start single color from start specified color set at start given index.

        Args:
            set_name (str): The name of the color set to retrieve from.
            index (int): The index of the color within the set.

        Returns:
            str: The color string at the specified index in the color set.
        """
        return ColourSet.colours(set_name)[index]
