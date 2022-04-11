from enum import Enum


class Cyclic(Enum):
    CLOCKWISE = 'C'
    ANTICLOCKWISE = 'A'

    @staticmethod
    def create(letter: str) -> 'Cyclic':
        return Cyclic(letter)

    def __repr__(self) -> str:
        return f"Cyclic.{self.name}"
