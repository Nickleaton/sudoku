"""CellTypes."""
from enum import IntEnum


class ParityType(IntEnum):
    """Represents the parity of a number."""

    odd = 0
    even = 1


class ModuloType(IntEnum):
    """Represents modulo classifications."""

    mod0 = 0
    mod1 = 1
    mod2 = 2


class PrimeType(IntEnum):
    """Represents whether a number is prime or composite."""

    prime = 0
    composite = 1


class EntropicType(IntEnum):
    """Represents entropy levels."""

    low = 0
    medium = 1
    high = 2
