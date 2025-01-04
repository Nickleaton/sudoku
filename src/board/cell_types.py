from enum import IntEnum


class ParityType(IntEnum):
    """Represents the parity of a number.

    Attributes:
        odd (int): Represents an odd number (0).
        even (int): Represents an even number (1).
    """
    odd: int = 0
    even: int = 1


class ModuloType(IntEnum):
    """Represents modulo classifications.

    Attributes:
        mod0 (int): Remainder of 0 in modulo operation (0).
        mod1 (int): Remainder of 1 in modulo operation (1).
        mod2 (int): Remainder of 2 in modulo operation (2).
    """
    mod0: int = 0
    mod1: int = 1
    mod2: int = 2


class PrimeType(IntEnum):
    """Represents whether a number is prime or composite.

    Attributes:
        prime (int): Represents a prime number (0).
        composite (int): Represents a composite number (1).
    """
    prime: int = 0
    composite: int = 1


class EntropicType(IntEnum):
    """Represents entropy levels.

    Attributes:
        low (int): Represents low entropy (0).
        medium (int): Represents medium entropy (1).
        high (int): Represents high entropy (2).
    """
    low: int = 0
    medium: int = 1
    high: int = 2
