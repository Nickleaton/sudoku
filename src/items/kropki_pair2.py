"""
Kropki Dots
"""

from src.items.board import Board
from src.items.cell import Cell
from src.items.product_pair import ProductPair


class KropkiPair2(ProductPair):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell):
        super().__init__(board, cell_1, cell_2, 2)
