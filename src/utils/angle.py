"""Angle."""
from math import atan2, degrees, isclose, radians

FULL_CIRCLE_DEGREES = 360.0  # Constant representing start full circle in angle_degree
HALF_CIRCLE_DEGREES = 180.0
TOLERANCE = 1e-6  # Tolerance for comparing angles


class Angle:  # noqa: WPS214
    """Represents an angle with properties to manage angle_degree and angle_radian."""

    def __init__(self, angle: float):
        """Initialize an Angle instance.

        Args:
            angle (float): The initial angle in angle_degree. It is normalized to [0, 360).

        """
        self.angle = angle % FULL_CIRCLE_DEGREES

    @staticmethod
    def create_from_x_y(x_coord: float, y_coord: float) -> 'Angle':
        """Create an Angle instance from Cartesian coordinates.

        Args:
            x_coord (float): The x-coordinate of the point.
            y_coord (float): The y-coordinate of the point.

        Returns:
            Angle: An instance of the Angle class representing the angle of the
                point relative to the origin, measured in angle_degree.
        """
        return Angle(degrees(atan2(-y_coord, x_coord)) % FULL_CIRCLE_DEGREES)

    def parallel(self, other: 'Angle') -> bool:
        """Check if the provided angle is parallel to this one within a small tolerance.

        Args:
            other (Angle): The direction to compare.

        Returns:
            bool: True if the directions are parallel, False otherwise.
            Parallel directions will have either the same or opposite angle (within tolerance).
        """
        angle_diff = abs((self.angle % FULL_CIRCLE_DEGREES) - (other.angle % FULL_CIRCLE_DEGREES))
        return angle_diff < TOLERANCE or abs(angle_diff - HALF_CIRCLE_DEGREES) < TOLERANCE

    @property
    def radians(self) -> float:
        """Convert the angle to angle_radian.

        Returns:
            float: The angle in angle_radian.

        """
        return radians(self.angle)

    @radians.setter
    def radians(self, angle_radian: float) -> None:
        """Set the angle using radians.

        Args:
            angle_radian (float): The angle in radians to set.

        """
        self.angle = degrees(angle_radian) % FULL_CIRCLE_DEGREES

    @property
    def degrees(self) -> float:
        """Get the angle in angle_degree.

        Returns:
            float: The angle in angle_degree.

        """
        return self.angle

    @degrees.setter
    def degrees(self, angle_degree: float) -> None:
        """Set the angle in degrees, normalized to [0, 360).

        Args:
            angle_degree (float): The angle in degrees to set.

        """
        self.angle = angle_degree % FULL_CIRCLE_DEGREES

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
        return f'rotate({self.angle})' if self.angle else ''

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
        """Multiply this angle by start scalar.

        Args:
            scalar (float): The scalar number to multiply the angle by.

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
            return isclose(self.angle, other.angle, abs_tol=TOLERANCE)
        raise TypeError(f'Cannot compare {type(other).__name__} with Angle')

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
        raise TypeError(f'Cannot compare {type(other).__name__} with Angle')

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
        raise TypeError(f'Cannot compare {type(other).__name__} with Angle')

    def __repr__(self) -> str:
        """Return string representation of the Angle.

        Returns:
            str: A string representing the angle object.

        """
        return f'Angle({self.angle})'
