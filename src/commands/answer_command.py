""" Command that draws the answer as an SVG File"""

from src.commands.svg_command import SVGCommand
from src.items.box import Box
from src.items.cell import Cell
from src.items.column import Column
from src.items.item import Item
from src.items.known_cell import KnownCell
from src.items.row import Row
from src.items.solution import Solution


class AnswerCommand(SVGCommand):
    """ Display the answer """

    @staticmethod
    def selector(item: Item) -> bool:
        """ Just select the items that are needed to display the answer
        :param item: Is the item needed to display the answer?

        :return: True if the item is to be displayed
        """
        return item.__class__ in [Box, Cell, Column, Row, Solution, KnownCell]
