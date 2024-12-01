"""YamlLoader."""
from pathlib import Path

import oyaml as yaml

from src.items.board import Board
from src.load_dump.loader import Loader


class YamlLoader(Loader):
    """A Loader subclass that loads board data from a YAML file."""

    def __init__(self, file_path: Path) -> None:
        """Initialize the YamlLoader with the config_file to the YAML file and loads its contents.

        Args:
            file_path (Path): The config_file to the YAML file containing the board data.
        """
        super().__init__(file_path)
        with file_path.open(mode='r', encoding='utf-8') as file:
            self.raw = yaml.safe_load(file)

    def process(self) -> Board:
        """Process the loaded YAML data and creates a Board instance.

        This method takes the raw YAML data and uses it to create a Board instance.

        Returns:
            Board: The Board instance created from the YAML data.
        """
        return Board.create('Board', self.raw)
