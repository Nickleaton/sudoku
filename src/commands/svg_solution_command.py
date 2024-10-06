""" Create an SVG drawing of the problem"""

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution


class SVGSolutionCommand(SVGCommand):

    def select(self, item: Item) -> bool:
        """ Selector
        :param item: Item to check if it's included in the output
        :return: True if the item is to be displayed
        """
        return isinstance(item, Solution)
