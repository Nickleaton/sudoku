from config_schema import value
from src.parsers.parser import Parser, ParserError


class CellPairEqualValueParser(Parser):

    def __init__(self):
        super().__init__(pattern=f"^{Parser.CELL}-{Parser.CELL}={Parser.VALUE}$", example_format="r1c1-r2c2=dd")

    def parse(self, text: str) -> None:
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(
                f"{self.__class__.__name__} expects a cell pair equal value format like {self.example_format}")
        try:
            stripped_text: str = text.strip()
            lhs: str = stripped_text.split('=')[0]
            rhs: str = stripped_text.split('=')[1]
            cell1_str: str = lhs.split('-')[0]
            cell2_str: str = lhs.split('-')[1]
            r1: str = cell1_str[0]
            c1: str = cell1_str[1]
            r2: str = cell2_str[0]
            c2: str = cell2_str[1]
            self.result = [int(r1), int(c1), int(r2), int(c2), int(value)]
            self.answer = {
                "row1": r1,
                "column1": c1,
                "row2": r2,
                "column2": c2,
                "value": value
            }
        except ValueError:
            self.raise_error()
