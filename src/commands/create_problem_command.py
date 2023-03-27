""" Create Problem Command """
import logging

from src.commands.simple_command import SimpleCommand
from src.items.item import Item


class CreateProblemCommand(SimpleCommand):

    def __init__(self):
        super().__init__()
        self.problem = None

    def execute(self) -> None:
        """
        Create the problem
        """
        logging.info("Creating problem")
        self.problem = Item.create(self.parent.board.board, {'Constraints': self.parent.config.config['Constraints']})
