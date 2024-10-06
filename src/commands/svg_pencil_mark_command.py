""" Create an SVG drawing of the problem"""

# TODO - not used by default
# The idea is for the possible values, 1-9 as small numbers in each cell
# Will also need corner marks, and central marks

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution


class SVGPencilMarkCommand(SVGCommand):
    def select(self, item: Item) -> bool:
        """ Selector

        TODO

        :param item: Item to check if it's included in the output
        :return: True if the item is to be displayed
        """
        return not isinstance(item, Solution)
