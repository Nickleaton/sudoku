""" Create an SVG drawing of the problem"""

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution
from src.solvers.answer import Answer


class SVGProblemCommand(SVGCommand):

    def __init__(self, problem_field: str = "problem_svg"):
        """
        Initialize the SVGProblemCommand

        Parameters:
            problem_field (str): The attribute of the problem that contains the root item to be drawn
        """
        super().__init__(problem_field)

    def select(self, item: Item) -> bool:
        """ Selector
        :param item: Item to check if it's included in the output
        :return: True if the item is to be displayed
        """
        return not isinstance(item, Solution) and not isinstance(item, Answer)
