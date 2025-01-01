"""TestDifferencePair."""
# import unittest
# from typing import Type
#
# from src.vectors.board import Board
# from src.vectors.cell import Cell
# from src.vectors.composed_item import ComposedItem
# from src.vectors.difference_pair import DifferencePair
# from src.vectors.constraint import Item
# from src.vectors.pair import Pair
# from src.vectors.region import Region
# from tests.vectors.test_variable_pair import TestVariablePair
#
#
# class TestDifferencePair(TestVariablePair):
#
#     def setUp(self) -> None:
#         self.board = Board(9, 9, 3, 3, None)
#         self.constraint = DifferencePair(
#             self.board,
#             Cell.make(self.board, 1, 2),
#             Cell.make(self.board, 1, 3),
#             [1, 2]
#         )
#         self.size = 2
#
#     @property
#     def clazz(self):
#         return DifferencePair
#
#     @property
#     def config(self) -> str:
#         return "DifferencePair: 12-13"
#
#     @property
#     def has_rule(self) -> bool:
#         return True
#
#     @property
#     def representation(self) -> str:
#         return (
#             "DifferencePair"
#             "("
#             "Board(9, 9, 3, 3, None), "
#             "Cell(Board(9, 9, 3, 3, None), 1, 2), "
#             "Cell(Board(9, 9, 3, 3, None), 1, 3)"
#             ")"
#         )
#
#     @property
#     def expected_classes(self) -> set[Type[Item]]:
#         return {Cell, ComposedItem, DifferencePair, Item, Pair, Region}
#
#
# if __name__ == '__main__':  # pragma: no cover
#     unittest.main()
