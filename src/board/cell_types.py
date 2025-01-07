"""CellTypes."""
from enum import IntEnum


class ParityType(IntEnum):
    """Represents the parity of a number."""

    odd: int = 0
    even: int = 1


class ModuloType(IntEnum):
    """Represents modulo classifications."""

    mod0: int = 0
    mod1: int = 1
    mod2: int = 2


class PrimeType(IntEnum):
    """Represents whether a number is prime or composite."""

    prime: int = 0
    composite: int = 1


class EntropicType(IntEnum):
    """Represents entropy levels."""

    low: int = 0
    medium: int = 1
    high: int = 2
