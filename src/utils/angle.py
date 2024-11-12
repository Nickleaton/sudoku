"""Angle management for geometric operations."""
import math


class AngleException(Exception):
    """Exception raised for errors in Angle operations."""


class Angle:
    """Represents an angle with properties to manage degrees and radians.

    Attributes:
        angle (float): The angle value in degrees, normalized to the range [0, 360).
    """

    def __init__(self, angle: float):
        """Initialize an Angle instance.

        Args:
            angle (float): The initial angle in degrees. It is normalized to [0, 360).
        """
        self.angle = float(angle) % 360.0

    @property
    def radians(self) -> float:
        """Convert the angle to radians.

        Returns:
            float: The angle in radians.
        """
        return self.angle * math.pi / 180.0

    @radians.setter
    def radians(self, radians: float) -> None:
        """Set the angle using radians.

        Args:
            radians (float): The angle in radians.
        """
        self.angle = radians * 180.0 / math.pi

    @property
    def degrees(self) -> float:
        """Get the angle in degrees.

        Returns:
            float: The angle in degrees.
        """
        return self.angle

    @degrees.setter
    def degrees(self, degrees: float) -> None:
        """Set the angle in degrees, normalized to [0, 360).

        Args:
            degrees (float): The angle in degrees.
        """
        self.angle = degrees % 360.0

    @property
    def opposite(self) -> 'Angle':
        """Calculate the angle opposite to this one.

        Returns:
            Angle: A new angle that is 180 degrees from the current one.
        """
        return Angle(self.angle + 180.0)

    @property
    def transform(self) -> str:
        """Generate an SVG transform string for rotation by this angle.

        Returns:
            str: The SVG transform string, or an empty string if the angle is 0.
        """
        return "" if self.angle == 0.0 else f"rotate({self.angle})"

    def __add__(self, other: 'Angle') -> 'Angle':
        """Add this angle to another angle.

        Args:
            other (Angle): The angle to add.

        Returns:
            Angle: The resulting angle.
        """
        return Angle(self.angle + other.angle)

    def __sub__(self, other: 'Angle') -> 'Angle':
        """Subtract another angle from this angle.

        Args:
            other (Angle): The angle to subtract.

        Returns:
            Angle: The resulting angle.
        """
        return Angle(self.angle - other.angle)

    def __mul__(self, other: float) -> 'Angle':
        """Multiply this angle by a scalar.

        Args:
            other (float): The scalar to multiply by.

        Returns:
            Angle: The resulting angle.
        """
        return Angle(self.angle * other)

    def __eq__(self, other: object) -> bool:
        """Check if this angle is equal to another angle.

        Args:
            other (object): The angle to compare to.

        Returns:
            bool: True if angles are equal.

        Raises:
            AngleException: If `other` is not an Angle.
        """
        if isinstance(other, Angle):
            return self.angle == other.angle
        raise AngleException(f"Cannot compare {type(other).__name__} with {self.__class__.__name__}")

    def __lt__(self, other: object) -> bool:
        """Check if this angle is less than another angle.

        Args:
            other (object): The angle to compare to.

        Returns:
            bool: True if this angle is less.

        Raises:
            AngleException: If `other` is not an Angle.
        """
        if isinstance(other, Angle):
            return self.angle < other.angle
        raise AngleException(f"Cannot compare {type(other).__name__} with {self.__class__.__name__}")

    def __le__(self, other: object) -> bool:
        """Check if this angle is less than or equal to another angle.

        Args:
            other (object): The angle to compare to.

        Returns:
            bool: True if this angle is less than or equal.

        Raises:
            AngleException: If `other` is not an Angle.
        """
        if isinstance(other, Angle):
            return self.angle <= other.angle
        raise AngleException(f"Cannot compare {type(other).__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        """Return string representation of the Angle.

        Returns:
            str: The string representation of the angle.
        """
        return f"Angle({self.angle})"
