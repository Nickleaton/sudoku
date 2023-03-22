""" Create an SVG drawing of the problem"""

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution


class ProblemCommand(SVGCommand):

    @staticmethod
    def select(item: Item) -> bool:
        """ Ignore the solution
        :param item: Item to check if it's included in the output
        :return: True if the item is to be displayed
        """

        return not isinstance(item, Solution)
