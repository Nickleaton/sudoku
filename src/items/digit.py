class Digit:
    """A class representing a digit range in a Sudoku puzzle.

    Attributes:
        minimum (int): The minimum possible value in the range.
        maximum (int): The maximum possible value in the range.
    """

    _instances: dict[tuple[int, int], 'Digit'] = {}

    def __new__(cls, minimum: int, maximum: int) -> 'Digit':
        """Creates a new instance or returns an existing instance if it already exists.

        Args:
            minimum (int): The minimum possible value for the digit range.
            maximum (int): The maximum possible value for the digit range.

        Returns:
            Digit: A new or existing instance of the Digit class.
        """
        key = (minimum, maximum)
        if key not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[key] = instance
        return cls._instances[key]

    def __init__(self, minimum: int, maximum: int) -> None:
        """Initializes a new instance of the Digit class.

        Args:
            minimum (int): The minimum possible value for the digit range.
            maximum (int): The maximum possible value for the digit range.

        Raises:
            TypeError: If minimum or maximum is not an integer.
            ValueError: If minimum is greater than maximum.
        """
        if not isinstance(minimum, int) or not isinstance(maximum, int):
            raise TypeError('Minimum and maximum must be integers.')
        if minimum > maximum:
            raise ValueError('Minimum must be less than or equal to maximum.')
        self.minimum: int = minimum
        self.maximum: int = maximum

    def is_valid(self, value: int) -> bool:
        """Checks if a value is within the digit range.

        Args:
            value (int): The value to validate.

        Returns:
            bool: True if the value is within the range, False otherwise.
        """
        return self.minimum <= value <= self.maximum

    def __len__(self) -> int:
        """Returns the number of possible digits in the range.

        Returns:
            int: The total number of digits in the range, inclusive.
        """
        return self.maximum - self.minimum + 1

    def __iter__(self) -> iter:
        """Iterates over all possible digits in the range.

        Returns:
            iter: An iterator over the range of digits.
        """
        return iter(range(self.minimum, self.maximum + 1))

    def __contains__(self, value: int) -> bool:
        """Checks if a value is within the range using the `in` operator.

        Args:
            value (int): The value to check.

        Returns:
            bool: True if the value is within the range, False otherwise.
        """
        return self.is_valid(value)

    def __repr__(self) -> str:
        """Returns a string representation of the instance.

        Returns:
            str: A string representation of the Digit instance.
        """
        return f'{self.__class__.__name__}(minimum={self.minimum}, maximum={self.maximum})'


digit_0_8 = Digit(0, 8)
digit_1_4 = Digit(1, 4)
digit_1_6 = Digit(1, 6)
digit_1_9 = Digit(1, 9)
digit_1_F = Digit(0x1, 0xF)
