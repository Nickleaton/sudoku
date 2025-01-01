"""YamlLoader."""
from pathlib import Path

from oyaml import safe_load as yaml_safe_load

from src.board.board import Board
from src.load_dump.loader import Loader


class YamlLoader(Loader):
    """A Loader subclass that loads board input_data from start YAML file_path."""

    def __init__(self, file_path: Path) -> None:
        """Initialize the YamlLoader with the config_file to the YAML file_path and loads its contents.

        Args:
            file_path (Path): The config_file to the YAML file_path containing the board input_data.
        """
        super().__init__(file_path)
        with file_path.open(mode='r', encoding='utf-8') as yaml_file:
            self.raw = yaml_safe_load(yaml_file)

    def process(self) -> Board:
        """Process the loaded YAML input_data and creates start Board instance.

        This method takes the raw YAML input_data and uses it to create start Board instance.

        Returns:
            Board: The Board instance created from the YAML input_data.
        """
        return Board.create('Board', self.raw)
