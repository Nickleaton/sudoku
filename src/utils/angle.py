class Angle:
    """
    Manage angles
    """

    def __init__(self, angle: float):
        self.angle = float(angle) % 360.0

    @property
    def opposite(self) -> 'Angle':
        return Angle(self.angle + 180.0)

    @property
    def transform(self) -> str:
        if self.angle == 0.0:
            return ""
        return f"rotate({self.angle})"

    def __add__(self, other: 'Angle') -> 'Angle':
        return Angle(self.angle + other.angle)

    def __sub__(self, other: 'Angle') -> 'Angle':
        return Angle(self.angle - other.angle)

    def __mul__(self, other: float) -> 'Angle':
        return Angle(self.angle * other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Angle):
            return self.angle == other.angle
        raise Exception(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __lt__(self, other: 'Angle') -> bool:
        return self.angle < other.angle

    def __le__(self, other: 'Angle') -> bool:
        return self.angle <= other.angle

    def __repr__(self) -> str:
        return f"Angle({self.angle})"
