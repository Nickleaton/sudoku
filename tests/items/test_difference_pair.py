"""TestDifferencePair."""
# import unittest
# from typing import Type
#
# from src.items.board import Board
# from src.items.cell import Cell
# from src.items.composed_item import ComposedItem
# from src.items.difference_pair import DifferencePair
# from src.items.item import Item
# from src.items.pair import Pair
# from src.items.region import Region
# from tests.items.test_variable_pair import TestVariablePair
#
#
# class TestDifferencePair(TestVariablePair):
#
#     def setUp(self) -> None:
#         self.board = Board(9, 9, 3, 3, None, None, None, None)
#         self.item = DifferencePair(
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
#             "Board(9, 9, 3, 3, None, None, None, None), "
#             "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
#             "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
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

