""" Build Board Command """
import logging

from src.commands.load_config_command import LoadConfigCommand
from src.commands.simple_command import SimpleCommand
from src.items.board import Board


class CreateBoardCommand(SimpleCommand):

    def __init__(self):
        super().__init__()
        self.board = None

    def execute(self) -> None:
        """
        Build the board
        """
        logging.info("Creating Board")
        self.board = Board.create('Board', self.parent.config.config)

