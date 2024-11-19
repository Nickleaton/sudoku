"""ColourSet."""
from src.utils.config import Config
from src.utils.sudoku_exception import SudokuException

# Initialize the configuration object to access color settings
config: Config = Config()


class ColourException(SudokuException):
    """An exception raised when an invalid colour is provided."""


class ColourSet:
    """A utility class for managing and retrieving color sets."""

    @staticmethod
    def colours(set_name: str) -> list[str]:
        """Retrieve a list of colors associated with a specific set name.

        Args:
            set_name (str): The name of the color set to retrieve.

        Returns:
            list[str]: A list of color strings in the specified set.
        """
        colour_set = config.colours
        if colour_set is None or set_name not in colour_set:
            raise ColourException(f"Colour set '{set_name}' not found in {config.config_file_path.name}")
        colors = colour_set[set_name]
        return [str(c) for c in colors]

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
