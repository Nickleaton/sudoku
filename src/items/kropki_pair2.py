"""Kropki Dots
"""

from src.items.board import Board
from src.items.cell import Cell
from src.items.variable_product_pair import VariableProductPair


class KropkiPair2(VariableProductPair):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell):
        super().__init__(board, cell_1, cell_2, 2)
