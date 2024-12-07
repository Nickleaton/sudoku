"""Angle."""
import math

FULL_CIRCLE_DEGREES = 360.0  # Constant representing a full circle in degrees
TOLERANCE = 1e-9  # Tolerance for comparing angles


class Angle:  # noqa: WPS214
    """Represents an angle with properties to manage degrees and radians."""

    def __init__(self, angle: float):
        """Initialize an Angle instance.

        Args:
            angle (float): The initial angle in degrees. It is normalized to [0, 360).

        """
        self.angle = angle % FULL_CIRCLE_DEGREES

    @property
    def radians(self) -> float:
        """Convert the angle to radians.

        Returns:
            float: The angle in radians.

        """
        return math.radians(self.angle)

    @radians.setter
    def radians(self, radians: float) -> None:
        """Set the angle using radians.

        Args:
            radians (float): The angle in radians to set.

        """
        self.angle = math.degrees(radians) % FULL_CIRCLE_DEGREES

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
            degrees (float): The angle in degrees to set.

        """
        self.angle = degrees % FULL_CIRCLE_DEGREES

    @property
    def opposite(self) -> 'Angle':
        """Calculate the angle opposite to this one.

        Returns:
            Angle: The opposite angle.

        """
        return Angle(self.angle + FULL_CIRCLE_DEGREES / 2)

    @property
    def transform(self) -> str:
        """Generate an SVG transform string for rotation by this angle.

        Returns:
            str: The SVG transform string.

        """
        return f"rotate({self.angle})" if self.angle else ""

    def __add__(self, other: 'Angle') -> 'Angle':
        """Add this angle to another angle.

        Args:
            other (Angle): The angle to add.

        Returns:
            Angle: The resulting angle after addition.

        """
        return Angle(self.angle + other.angle)

    def __sub__(self, other: 'Angle') -> 'Angle':
        """Subtract another angle from this angle.

        Args:
            other (Angle): The angle to subtract.

        Returns:
            Angle: The resulting angle after subtraction.

        """
        return Angle(self.angle - other.angle)

    def __mul__(self, scalar: float) -> 'Angle':
        """Multiply this angle by a scalar.

        Args:
            scalar (float): The scalar value to multiply the angle by.

        Returns:
            Angle: The resulting angle after multiplication.

        """
        return Angle(self.angle * scalar)

    def __eq__(self, other: object) -> bool:
        """Check if this angle is equal to another angle.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the angles are equal, otherwise False.

        Raises:
            TypeError: If `other` is not an instance of `Angle`.

        """
        if isinstance(other, Angle):
            return math.isclose(self.angle, other.angle, abs_tol=TOLERANCE)
        raise TypeError(f"Cannot compare {type(other).__name__} with Angle")

    def __lt__(self, other: object) -> bool:
        """Check if this angle is less than another angle.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if this angle is less than the other, otherwise False.

        Raises:
            TypeError: If `other` is not an instance of `Angle`.

        """
        if isinstance(other, Angle):
            return self.angle < other.angle
        raise TypeError(f"Cannot compare {type(other).__name__} with Angle")

    def __le__(self, other: object) -> bool:
        """Check if this angle is less than or equal to another angle.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if this angle is less than or equal to the other, otherwise False.

        Raises:
            TypeError: If `other` is not an instance of `Angle`.

        """
        if isinstance(other, Angle):
            return self.angle <= other.angle
        raise TypeError(f"Cannot compare {type(other).__name__} with Angle")

    def __repr__(self) -> str:
        """Return string representation of the Angle.

        Returns:
            str: A string representing the angle object.

        """
        return f"Angle({self.angle})"
