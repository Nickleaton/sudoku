# """ Frame Sudoku """
#
# from typing import List, Any, Dict
#
# from pulp import LpVariable, LpInteger
#
# from src.glyphs.glyph import Glyph, TextGlyph
# from src.items.board import Board
# from src.items.first_n import FirstN
# from src.items.item import Item
# from src.solvers.formulations import Formulations
# from src.solvers.pulp_solver import PulpSolver
# from src.utils.rule import Rule
# from src.utils.side import Side
#
#
# class MinMaxSum(FirstN):
#     """
#     Handle frame sudoku:
#         Numbers outside the frame equal the sum of the minimum and maximum values in the first three cells
#         corresponding row or column in the given direction
#     """
#
#     def __init__(self, board: Board, side: Side, index: int, total: int):
#         """
#         Construct
#         :param board: board being used
#         :param side: the side where the total is to go
#         :param index: the row or column of the total
#         :param total: the actual total
#         """
#         super().__init__(board, side, index)
#         self.total = total
#
#     def __repr__(self) -> str:
#         """
#         representation of the frame
#         :return: str
#         """
#         return (
#             f"{self.__class__.__name__}"
#             f"("
#             f"{self.board!r}, "
#             f"{self.side!r}, "
#             f"{self.total}"
#             f")"
#         )
#
#     @property
#     def rules(self) -> List[Rule]:
#         return [
#             Rule(
#                 'MinMaxSum',
#                 1,
#                 "Numbers outside the frame equal the sum of the minimum and maximum number in the "
#                 "corresponding row or column in the given direction"
#             )
#         ]
#
#     @property
#     def glyphs(self) -> List[Glyph]:
#         return [
#             TextGlyph(
#                 'MinMaxSumText',
#                 0,
#                 self.side.marker(self.board, self.index).center,
#                 str(self.total)
#             )
#         ]
#
#     @property
#     def tags(self) -> set[str]:
#         return super().tags.union({'Comparison', 'MinMaxSum', 'Minimum', 'Maximum'})
#
#     @classmethod
#     def extract(cls, board: Board, yaml: Dict) -> Any:
#         data = yaml[cls.__name__]
#         ref_str: str = data.split("=")[0]
#         total_str: str = data.split("=")[1]
#         side = Side.create(ref_str[0])
#         index = int(ref_str[1])
#         total = int(total_str)
#         return side, index, total
#
#     @classmethod
#     def create(cls, board: Board, yaml: Dict) -> Item:
#         side, index, total = MinMaxSum.extract(board, yaml)
#         return cls(board, side, index, total)
#
#     def add_constraint(self, solver: PulpSolver) -> None:
#         minimum = LpVariable(f"{self.name}_minimum", 1, self.board.maximum_digit, LpInteger)
#         maximum = LpVariable(f"{self.name}_maximum", 1, self.board.maximum_digit, LpInteger)
#         indicators = LpVariable.dicts(f"{self.name}_Indicators", (list(range(0, self.count()))), 0, 1, LpInteger)
#         variables = [solver.values[cell.row][cell.column] for cell in self.cells]
#         Formulations.minimum(solver, 1, self.board.maximum_digit, minimum, variables, indicators)
#         Formulations.maximum(solver, 1, self.board.maximum_digit, maximum, variables, indicators)
#         solver.model += minimum + maximum == self.total, self.name
#
#     def to_dict(self) -> Dict:
#         return {self.__class__.__name__: f"{self.side.value}{self.index}={self.total}"}
#
#     def css(self) -> Dict:
#         return {
#             ".MinMaxSumTextForeground": {
#                 "fill": "black",
#                 "font-size": "30px",
#                 "stroke": "black",
#                 "stroke-width": 1
#             },
#             ".MinMaxSumTextBackground": {
#                 "fill": "white",
#                 "font-size": "30px",
#                 "font-weight": "bolder",
#                 "stroke": "white",
#                 "stroke-width": 8
#             }
#         }
