""" Produce an SVG just showing the pencil marks. The possible choices with all those eliminated not shown"""

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution


class PencilMarkCommand(SVGCommand):
    """ Draw pencil marks for a board """

    @staticmethod
    def select(item: Item) -> bool:
        return not isinstance(item, Solution)
