import math


class AngleException(Exception):
    pass


class Angle:
    # noinspection GrazieInspection
    """
        Manage angles.

        Args:
            angle (float): The initial angle value. It is normalized to the range [0, 360).
            and represents the angle in degrees.
        """

    def __init__(self, angle: float):
        self.angle = float(angle) % 360.0

    @property
    def radians(self) -> float:
        """
        Returns the angle in radians.

        Returns:
            float: The angle in radians.
        """
        return self.angle * math.pi / 180.0

    @radians.setter
    def radians(self, radians: float) -> None:
        """
        Sets the angle in radians.

        Args:
            radians (float): The angle in radians.
        """
        self.angle = radians * 180.0 / math.pi

    @property
    def degrees(self) -> float:
        """
        Returns the angle in degrees.

        Returns:
            float: The angle in degrees.
        """
        return self.angle

    @degrees.setter
    def degrees(self, degrees: float) -> None:
        """
        Sets the angle in degrees.

        Args:
            degrees (float): The angle in degrees.
        """
        self.angle = degrees % 360.0

    @property
    def opposite(self) -> 'Angle':
        """
        Returns the opposite of the current angle.

        Returns:
            Angle: A new angle that is 180 degrees away from the current one.
        """
        return Angle(self.angle + 180.0)

    @property
    def transform(self) -> str:
        """
        Returns a transform string for SVG that represents this angle.

        Returns:
            str: An SVG transform string. If the angle is 0, returns an empty string.
        """
        if self.angle == 0.0:
            return ""
        return f"rotate({self.angle})"

    def __add__(self, other: 'Angle') -> 'Angle':
        """
        Adds this angle to another angle.

        Args:
            other (Angle): The angle to add.

        Returns:
            Angle: The result of adding the two angles.
        """
        return Angle(self.angle + other.angle)

    def __sub__(self, other: 'Angle') -> 'Angle':
        """
        Subtracts another angle from this angle.

        Args:
            other (Angle): The angle to subtract.

        Returns:
            Angle: The result of subtracting the other angle from this one.
        """
        return Angle(self.angle - other.angle)

    def __mul__(self, other: float) -> 'Angle':
        """
        Multiplies this angle by a scalar.

        Args:
            other (float): The scalar value.

        Returns:
            Angle: The result of multiplying the angle by the scalar.
        """
        return Angle(self.angle * other)

    def __eq__(self, other: object) -> bool:
        """
        Checks if this angle is equal to another angle.

        Args:
            other (object): The object to compare to.

        Returns:
            bool: True if the angles are equal, otherwise False.

        Raises:
            AngleException: If `other` is not an instance of Angle.
        """
        if isinstance(other, Angle):
            return self.angle == other.angle
        raise AngleException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __lt__(self, other: object) -> bool:
        """
        Checks if this angle is less than another angle.

        Args:
            other (object): The object to compare to.

        Returns:
            bool: True if this angle is less than the other angle.

        Raises:
            AngleException: If `other` is not an instance of Angle.
        """
        if isinstance(other, Angle):
            return self.angle < other.angle
        raise AngleException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __le__(self, other: object) -> bool:
        """
        Checks if this angle is less than or equal to another angle.

        Args:
            other (object): The object to compare to.

        Returns:
            bool: True if this angle is less than or equal to the other angle.

        Raises:
            AngleException: If `other` is not an instance of Angle.
        """
        if isinstance(other, Angle):
            return self.angle <= other.angle
        raise AngleException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        """
        Returns a string representation of the Angle.

        Returns:
            str: The string representation of the angle.
        """
        return f"Angle({self.angle})"
