from typing import List, Tuple, Optional, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.different_pair import DifferentPair
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class Anti(Composed):

    def __init__(self, board: Board, digits: List[int]):
        super().__init__(board, [])
        self.digits = digits
        for cell in Cell.cells():
            self.add_items(self.pairs(cell, digits))

    def offsets(self) -> List[Coord]:
        return []

    def pairs(self, c1: Cell, digits: List[int]) -> List[DifferentPair]:
        result = []
        for offset in self.offsets():
            if not self.board.is_valid(c1.row + offset.row, c1.column + offset.column):
                continue
            c2 = Cell.make(self.board, c1.row + offset.row, c1.column + offset.column)
            result.append(DifferentPair(self.board, c1, c2, digits))
        return result

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Chess', 'Anti'})

    @classmethod
    def create(cls, name: str, board: Board, yaml: Optional[Dict]) -> Item:
        return Anti(board, yaml)

    def __repr__(self) -> str:
        return f"{self.name}({self.board!r}, {self.digits!r})"


class AntiKnight(Anti):

    def __init__(self, board: Board):
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> List[Tuple[int, int]]:
        return \
            [
                Coord(-1, -2),
                Coord(1, -2),
                Coord(-2, -1),
                Coord(-2, 1),
                Coord(-1, 2),
                Coord(1, 2),
                Coord(2, 1),
                Coord(2, -1)
            ]

    @property
    def tags(self) -> List[str]:
        return super().tags.union({'Knight'})

    @classmethod
    def create(cls, name: str, board: Board, yaml: Optional[Dict]) -> Item:
        return AntiKnight(board)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule("AntiKnight", 1, "Identical digits cannot be separated by a knight's move")
        ]

    def __repr__(self) -> str:
        return f"{self.name}({self.board!r})"


class AntiMonkey(Anti):

    def __init__(self, board: Board):
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> List[Tuple[int, int]]:
        return \
            [
                Coord(-1, -3),
                Coord(1, -3),
                Coord(-3, -1),
                Coord(-3, 1),
                Coord(-1, 3),
                Coord(1, 3),
                Coord(3, 1),
                Coord(3, -1)
            ]

    @property
    def tags(self) -> List[str]:
        return super().tags.union({'Monkey'})

    @classmethod
    def create(cls, name: str, board: Board, yaml: Optional[Dict]) -> Item:
        return AntiMonkey(board)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule("AntiMonkey", 1, "Identical digits cannot be separated by a Monkey move [3 forward, 1 to the side]")
        ]

    def __repr__(self) -> str:
        return f"{self.name}({self.board!r})"


class AntiKing(Anti):

    def __init__(self, board: Board):
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> List[Tuple[int, int]]:
        return Direction.kings()

    @classmethod
    def create(cls, name: str, board: Board, yaml: Optional[Dict]) -> Item:
        return AntiKing(board)

    @property
    def tags(self) -> List[str]:
        return super().tags.union({'King'})

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule("AntiKing", 1, "Identical digits cannot be separated by a King's move")
        ]

    def __repr__(self) -> str:
        return f"{self.name}({self.board!r})"


class AntiQueen(Anti):

    def __init__(self, board: Board, digits: List[int]):
        super().__init__(board, digits)
        self.digits = digits

    def offsets(self) -> List[Tuple[int, int]]:
        results = []
        for distance in self.board.digit_range:
            results.append(Coord(-1, -1) * distance)
            results.append(Coord(1, -1) * distance)
            results.append(Coord(-1, 1) * distance)
            results.append(Coord(1, 1) * distance)
        return results

    @property
    def tags(self) -> List[str]:
        return super().tags.union({'Queen'})

    @classmethod
    def create(cls, name: str, board: Board, yaml: Optional[Dict]) -> Item:
        return AntiQueen(board, yaml)

    @property
    def rules(self) -> List[Rule]:
        digit_str = ' '.join([str(digit) for digit in self.digits])
        return [
            Rule("AntiQueen", 1, f"Digits [{digit_str}] cannot be separated by a Queen's move")
        ]

    def __repr__(self) -> str:
        return f"{self.name}({self.board!r}, {self.digits!r})"
