from typing import Optional, Dict

import oyaml as yaml

from src.utils.coord import Coord


class Board:

    # pylint: disable=too-many-arguments, too-many-instance-attributes
    def __init__(self,
                 board_rows: int,
                 board_columns: int,
                 box_rows: Optional[int] = None,
                 box_columns: Optional[int] = None,
                 reference: Optional[str] = None,
                 video: Optional[str] = None,
                 title: Optional[str] = None,
                 author: Optional[str] = None
                 ):
        # Rows
        self.board_rows = board_rows
        self.row_range = list(range(1, self.board_rows + 1))
        # Columns
        self.board_columns = board_columns
        self.column_range = list(range(1, self.board_columns + 1))
        # Digits
        self.minimum_digit = 1
        self.maximum_digit = max(self.board_rows, self.board_columns)
        self.digit_range = list(range(self.minimum_digit, self.maximum_digit + 1))
        self.digit_sum = sum(self.digit_range)
        # Boxes
        if box_rows is None:
            self.box_rows = None
            self.box_columns = None
            self.box_count = None
            self.box_range = None
        else:
            assert board_rows % box_rows == 0
            assert board_columns % box_columns == 0
            self.box_rows = box_rows
            self.box_columns = box_columns
            self.box_count = (board_rows // box_rows) * (board_columns // box_columns)
            self.box_range = list(range(1, self.box_count + 1))
        # meta data
        self.reference = reference
        self.video = video
        self.title = title
        self.author = author

    def is_valid(self, row: int, column: int) -> bool:
        return (row >= 1) and (row <= self.board_rows) and (column >= 1) and (column <= self.board_columns)

    def is_valid_coordinate(self, coord: Coord) -> bool:
        return self.is_valid(coord.row, coord.column)

    @classmethod
    def create(cls, name: str, yaml: Optional[Dict]) -> 'Board':
        y = yaml[name]
        board_rows = int(y['Board'].split("x")[0])
        board_columns = int(y['Board'].split("x")[1])
        box_rows = int(y['Boxes'].split("x")[0]) if 'Boxes' in y else None
        box_columns = int(y['Boxes'].split("x")[1]) if 'Boxes' in y else None
        reference = y['Reference'] if 'Reference' in y else None
        video = y['Video'] if 'Video' in y else None
        title = y['Title'] if 'Title' in y else None
        author = y['Author'] if 'Author' in y else None
        return Board(
            board_rows,
            board_columns,
            box_rows,
            box_columns,
            reference,
            video,
            title,
            author
        )

    def to_dict(self):
        result = {'Board': {}}
        result['Board']['Board'] = f"{self.board_rows}x{self.board_columns}"
        if self.box_rows is not None:
            result['Board']['Boxes'] = f"{self.box_rows}x{self.box_columns}"
        if self.reference is not None:
            result['Board']['Reference'] = self.reference
        if self.reference is not None:
            result['Board']['Video'] = self.video
        if self.reference is not None:
            result['Board']['Title'] = self.title
        if self.reference is not None:
            result['Board']['Author'] = self.author
        return result

    def to_yaml(self) -> str:
        return yaml.dump(self.to_dict())

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board_rows!r}, "
            f"{self.board_columns!r}, "
            f"{self.box_rows!r}, "
            f"{self.box_columns!r}, "
            f"{self.reference!r}, "
            f"{self.video!r}, "
            f"{self.title!r}, "
            f"{self.author!r}"
            f")"
        )
