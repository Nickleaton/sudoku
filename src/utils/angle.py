""" Utility class to manage angles """


class AngleException(Exception):
    pass


class Angle:
    """
    Manage angles
    """

    def __init__(self, angle: float):
        self.angle = float(angle) % 360.0

    @property
    def opposite(self) -> 'Angle':
        """
        Return the opposite angle
        :return: Angle
        """
        return Angle(self.angle + 180.0)

    @property
    def transform(self) -> str:
        """
        return a svg transform string for the angle
        :return: str
        """
        if self.angle == 0.0:
            return ""
        return f"rotate({self.angle})"

    def __add__(self, other: 'Angle') -> 'Angle':
        """
        Add two angles
        :param other: Angle
        :return: Angle
        """
        return Angle(self.angle + other.angle)

    def __sub__(self, other: 'Angle') -> 'Angle':
        """
        Subtract two angles
        :param other: Angle
        :return: Angle
        """
        return Angle(self.angle - other.angle)

    def __mul__(self, other: float) -> 'Angle':
        """
        Multiply an angle by a scaler
        :param other: scalar as float
        :return: Angle
        """
        return Angle(self.angle * other)

    def __eq__(self, other: object) -> bool:
        """
        Compare two angles for equality
        :param other: Angle
        :return: Angle
        """
        if isinstance(other, Angle):
            return self.angle == other.angle
        raise AngleException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __lt__(self, other: object) -> bool:
        """
        Compare two angles for less than
        :param other: Angle
        :return: bool
        """
        if isinstance(other, Angle):
            return self.angle < other.angle
        raise AngleException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __le__(self, other: object) -> bool:
        """
        Compare two angles for less than or equal
        :param other: Angle
        :return: bool
        """
        if isinstance(other, Angle):
            return self.angle <= other.angle
        raise AngleException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        """
        Return representation of Angle
        :return: str
        """
        return f"Angle({self.angle})"
