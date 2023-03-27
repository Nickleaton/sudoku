import abc
from abc import ABC
from typing import List, Type, Set, Optional

from svgwrite.base import BaseElement
from svgwrite.container import Use, Symbol, Marker, Group
from svgwrite.shapes import Line, Circle, Rect, Polyline
from svgwrite.text import Text, TSpan

from src.utils.angle import Angle
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.point import Point
from src.utils.vector import Vector
from src.utils.vector_list import VectorList

config = Config()


class Glyph(ABC):
    """
    Glyph
    """

    def __init__(self, class_name: str):
        self.class_name = class_name

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        return None

    @classmethod
    def end_marker(cls) -> Optional[Marker]:
        return None

    @classmethod
    def symbol(cls) -> Optional[Marker]:
        return None

    # pylint: disable=no-self-use
    def draw(self) -> Optional[BaseElement]:
        return None

    @property
    def priority(self) -> int:
        return 1

    def __lt__(self, other: 'Glyph') -> bool:
        return self.priority < other.priority

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}')"

    @property
    def used_classes(self) -> Set[Type['Glyph']]:
        return set(self.__class__.__mro__).difference({abc.ABC, object})


class ComposedGlyph(Glyph):
    """
    Standard Composed Pattern for Glyphs
    """

    def __init__(self, class_name: str, items: List[Glyph] = None):
        super().__init__(class_name)
        if items is None:
            self.items = []
        else:
            self.items = items

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"["
            f"{', '.join([str(item) for item in self.items])}"
            f"]"
            f")"
        )

    def add(self, item: Glyph):
        self.items.append(item)

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        for glyph in sorted(self.items):
            group.add(glyph.draw())
        return group

    @property
    def used_classes(self) -> Set[Type[Glyph]]:
        result = super().used_classes
        result = result.union({ComposedGlyph})
        for item in self.items:
            result = result.union(item.used_classes)
        return result


class LineGlyph(Glyph):
    """
    Straight line between two points
    """

    def __init__(self, class_name: str, start: Coord, end: Coord):
        super().__init__(class_name)
        self.start = start
        self.end = end

    def draw(self) -> Optional[BaseElement]:
        return Line(start=self.start.point.coordinates, end=self.end.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {str(self.start)}, {str(self.end)})"


class PolyLineGlyph(Glyph):
    """
    Polyline is a line through a list of coordinates
    """

    def __init__(self, class_name: str, coords: List[Coord], start: bool, end: bool):
        super().__init__(class_name)
        self.coords = coords
        self.start = start
        self.end = end

    def draw(self) -> Optional[BaseElement]:
        parameters = {
            'class_': self.class_name
        }
        if self.start:
            parameters['marker_start'] = f"url(#{self.class_name}-start)"
        if self.end:
            parameters['marker_end'] = f"url(#{self.class_name}-end)"
        return Polyline(points=[coord.center.point.coordinates for coord in self.coords], **parameters)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}], "
            f"{repr(self.start)}, "
            f"{repr(self.end)}"
            f")"
        )


class ThermometerGlyph(PolyLineGlyph):
    def __init__(self, class_name: str, coords: List[Coord]):
        super().__init__(class_name, coords, True, False)

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            viewBox="0 0 100 100",
            id_="Thermometer-start",
            class_="Thermometer ThermometerStart"
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )


class SimpleThermometerGlyph(ThermometerGlyph):

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            viewBox="0 0 100 100",
            id_="SimpleThermometer-start",
            class_="SimpleThermometer SimpleThermometerStart"
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )


class FrozenThermometerGlyph(ThermometerGlyph):

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            viewBox="0 0 100 100",
            id_="FrozenThermometer-start",
            class_="FrozenThermometer FrozenThermometerStart"
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )


class ArrowLineGlyph(PolyLineGlyph):
    """
    Arrow Line Glyph
    """

    def __init__(self, class_name: str, coords: List[Coord]):
        super().__init__(class_name, coords, True, True)

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            size=(35, 35),
            viewBox="0 0 100 100",
            id_="Arrow-start",
            class_="Arrow ArrowStart"
        )
        marker.add(Circle(center=(50, 50), r=35))
        return marker

    @classmethod
    def end_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(20, 20),
            size=(20, 20),
            viewBox="0 0 50 50",
            id_="Arrow-end",
            class_="Arrow ArrowEnd",
            orient="auto"
        )
        marker.add(Polyline(points=[(0, 0), (20, 20), (0, 40)]))
        return marker

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )


class BetweenGlyph(PolyLineGlyph):
    """
    Between line glyph
    """

    def __init__(self, class_name: str, coords: List[Coord]):
        super().__init__(class_name, coords, True, True)

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            size=(35, 35),
            viewBox="0 0 100 100",
            id_="Between-start",
            class_="Between BetweenStart"
        )
        marker.add(Circle(center=(50, 50), r=35))
        return marker

    @classmethod
    def end_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            size=(35, 35),
            viewBox="0 0 100 100",
            id_="Between-end",
            class_="Between BetweenEnd"
        )
        marker.add(Circle(center=(50, 50), r=35))
        return marker

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )


class CircleGlyph(Glyph):
    """
    Circle
    """

    def __init__(self, class_name: str, center: Coord, percentage: float):
        super().__init__(class_name)
        self.center = center
        self.percentage = percentage

    @property
    def priority(self) -> int:
        return 10

    def draw(self) -> Optional[BaseElement]:
        print(self.center.point.transform)
        print(self.percentage)
        print(config.drawing.cell_size)
        return Circle(transform=self.center.point.transform, r=self.percentage * config.drawing.cell_size,
                      class_=self.class_name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.center)}, {repr(self.percentage)})"


class OddCellGlyph(Glyph):

    def __init__(self, class_name: str, coord: Coord):
        super().__init__(class_name)
        self.coord = coord

    @classmethod
    def symbol(cls) -> Optional[Symbol]:
        result = Symbol(
            viewBox="0 0 100 100",
            id_="OddCell-symbol",
            class_="OddCell"
        )
        result.add(Circle(center=(50, 50), r=35))
        return result

    def draw(self) -> Optional[BaseElement]:
        return Use(href="#OddCell-symbol", insert=self.coord.point.coordinates, class_="OddCell", height=100, width=100)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.coord)})"


class LowCellGlyph(Glyph):

    def __init__(self, class_name: str, coord: Coord):
        super().__init__(class_name)
        self.coord = coord

    @classmethod
    def symbol(cls) -> Optional[Symbol]:
        result = Symbol(
            viewBox="0 0 100 100",
            id_="LowCell-symbol",
            class_="LowCell"
        )
        result.add(Circle(center=(50, 50), r=35))
        return result

    def draw(self) -> Optional[BaseElement]:
        return Use(href="#LowCell-symbol", insert=self.coord.point.coordinates, class_="LOwCell", height=100, width=100)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.coord)})"


class RectGlyph(Glyph):

    def __init__(self, class_name: str, position: Coord, size: Coord):
        super().__init__(class_name)
        self.position = position
        self.size = size

    def draw(self) -> Optional[BaseElement]:
        return Rect(transform=self.position.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, {repr(self.size)})"


class SquareGlyph(RectGlyph):

    def __init__(self, class_name: str, position: Coord, size: int):
        super().__init__(class_name, position, Coord(size, size))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, {repr(self.size.row)})"


class BoxGlyph(RectGlyph):

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, {repr(self.size)})"


class EvenCellGlyph(Glyph):

    def __init__(self, class_name: str, position: Coord):
        super().__init__(class_name)
        self.position = position
        self.percentage = 0.7
        self.size = Coord(1, 1) * self.percentage

    def draw(self) -> Optional[BaseElement]:
        top_left = self.position + Coord(1, 1) * (1.0 - self.percentage) / 2.0
        return Rect(transform=top_left.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)})"


class MidCellGlyph(Glyph):

    def __init__(self, class_name: str, position: Coord):
        super().__init__(class_name)
        self.position = position
        self.percentage = 0.7
        self.size = Coord(1, 1) * self.percentage

    def draw(self) -> Optional[BaseElement]:
        top_left = self.position + Coord(1, 1) * (1.0 - self.percentage) / 2.0
        return Rect(transform=top_left.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)})"


class FortressCellGlyph(SquareGlyph):

    def __init__(self, class_name: str, position: Coord):
        super().__init__(class_name, position, 1)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)})"


class CellGlyph(SquareGlyph):

    def __init__(self, class_name: str, position: Coord):
        super().__init__(class_name, position, 1)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)})"

    @property
    def priority(self) -> int:
        return 4


class BattenburgGlyph(Glyph):
    """
    Battenburg

    CSS classes are BattenburgGlyphPink and BattenburgGlyphYellow
    """

    def __init__(self, class_name: str, coord: Coord):
        super().__init__(class_name)
        self.coord = coord

    @classmethod
    def symbol(cls) -> Optional[Marker]:
        result = Symbol(
            viewBox="0 0 100 100",
            id_="Battenberg-symbol",
            class_="Battenberg"
        )
        percentage = 0.3
        for i, position in enumerate([(d * percentage).point for d in Direction.orthogonals()]):
            result.add(
                Rect(
                    transform=position.transform,
                    size=Coord(percentage, percentage).point.coordinates,
                    class_="Battenberg" + ("Pink" if i % 2 == 0 else "Yellow")
                )
            )
        return result

    def draw(self) -> Optional[BaseElement]:
        return Use(
            href="#Battenberg-symbol",
            insert=self.coord.point.coordinates,
            class_="Battenberg",
            height=100,
            width=100
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.coord)})"


class RectangleGlyph(Glyph):

    # pylint: disable=too-many-arguments
    def __init__(self,
                 class_name: str,
                 first: Coord,
                 second: Coord,
                 percentage: float,
                 ratio: float,
                 vertical: bool
                 ):
        super().__init__(class_name)
        self.first = first
        self.second = second
        self.percentage = percentage
        self.ratio = ratio
        self.vertical = vertical

    def draw(self) -> Optional[BaseElement]:
        if self.vertical:
            size = Point(config.drawing.cell_size * self.percentage * self.ratio,
                         config.drawing.cell_size * self.percentage)
        else:
            size = Point(config.drawing.cell_size * self.percentage,
                         config.drawing.cell_size * self.percentage * self.ratio)
        position = Coord.middle(self.first, self.second)
        return Rect(transform=position.transform, size=size.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"{repr(self.first)}, "
            f"{repr(self.second)}, "
            f"{repr(self.percentage)}, "
            f"{repr(self.ratio)}, "
            f"{repr(self.vertical)}"
            f")"
        )


class ConsecutiveGlyph(RectangleGlyph):

    def __init__(self, class_name: str, first: Coord, second: Coord):
        vertical = first.column > second.column if first.row == second.row else first.row < second.row
        super().__init__(class_name, first, second, 0.25, 2.0, vertical)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {str(self.first)}, {str(self.second)})"


class Consecutive1Glyph(RectangleGlyph):

    def __init__(self, class_name: str, first: Coord, second: Coord):
        vertical = first.column > second.column if first.row == second.row else first.row < second.row
        super().__init__(class_name, first, second, 0.25, 2.0, vertical)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {str(self.first)}, {str(self.second)})"


class KropkiGlyph(RectangleGlyph):

    def __init__(self, class_name: str, first: Coord, second: Coord):
        vertical = first.column > second.column if first.row == second.row else first.row < second.row
        super().__init__(class_name, first, second, 0.25, 2.0, vertical)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {str(self.first)}, {str(self.second)})"


class TextGlyph(Glyph):

    def __init__(self, class_name: str, angle: float, position: Coord, text: str) -> None:
        super().__init__(class_name)
        self.angle = Angle(angle)
        self.position = position
        self.text = text

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        text = Text("",
                    transform=self.position.transform + " " + self.angle.transform,
                    class_=self.class_name + "Background"
                    )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        text = Text("",
                    transform=self.position.transform + " " + self.angle.transform,
                    class_=self.class_name + "Foreground"
                    )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        return group

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}('{self.class_name}', {self.angle.angle}, {repr(self.position)}, '{self.text}')"
        )


class KillerTextGlyph(Glyph):

    def __init__(self, class_name: str, angle: float, position: Coord, text: str):
        super().__init__(class_name)
        self.angle = Angle(angle)
        self.position = position
        self.text = text

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        position = self.position.top_left + Coord(1, 1) * 0.05
        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name + "Background"
                    )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name + "Foreground"
                    )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        return group

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}('{self.class_name}', {self.angle.angle}, {repr(self.position)}, '{self.text}')"
        )


class SimpleTextGlyph(TextGlyph):
    pass


class EdgeTextGlyph(TextGlyph):

    # pylint: disable=too-many-arguments
    def __init__(self, class_name: str, angle: float, first: Coord, second: Coord, text: str):
        super().__init__(class_name, angle, Coord.middle(first, second), text)
        self.first = first
        self.second = second

    @property
    def priority(self) -> int:
        return 5

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"{self.angle.angle}, "
            f"{repr(self.first)}, "
            f"{repr(self.second)}, "
            f"'{self.text}'"
            f")"
        )


class KnownGlyph(SimpleTextGlyph):

    def __init__(self, class_name: str, position: Coord, number: int):
        super().__init__(
            class_name,
            0,
            position + Coord(0.5, 0.5),
            str(number))
        self.location = position
        self.number = number

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.location)}, {str(self.number)})"


class StarGlyph(SimpleTextGlyph):

    def __init__(self, class_name: str, position: Coord):
        super().__init__(class_name, 0, position, "✧")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)})"


class ArrowGlyph(Glyph):
    arrow = "\u2191"  # ↑

    def __init__(self, class_name: str, angle: float, position: Coord):
        super().__init__(class_name)
        self.angle = Angle(float(angle))
        self.position = position

    def draw(self) -> Optional[BaseElement]:
        text = Text("",
                    transform=self.position.transform + " " + self.angle.transform,
                    class_=self.class_name)
        span = TSpan(ArrowGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.angle.angle)}, {repr(self.position)})"


class LittleArrowGlyph(Glyph):
    arrow = "\u25B2"  # ▲

    def __init__(self, class_name: str, position: Coord, location: int):
        super().__init__(class_name)
        self.position = position
        self.location = location

    def draw(self) -> Optional[BaseElement]:
        direction = Direction.direction(self.location)
        size = Coord(0.4, 0.4)
        position = self.position + size
        text = Text("",
                    transform=position.transform + " " + direction.angle.transform,
                    class_=self.class_name
                    )
        span = TSpan(LittleArrowGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, {repr(self.location)})"


class LittleNumberGlyph(Glyph):

    def __init__(self, class_name: str, position: Coord, number: int):
        super().__init__(class_name)
        self.position = position
        self.number = number

    def draw(self) -> Optional[BaseElement]:
        size = Coord(0.35, 0.35)
        position = self.position + size
        text = Text("",
                    transform=position.transform,
                    class_=self.class_name
                    )
        span = TSpan(str(self.number), alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, {repr(self.number)})"


class LittleKillerGlyph(Glyph):
    arrow = "\uA71B"  # ꜛ

    def __init__(self, class_name: str, position: Coord, angle: Angle, value: int):
        super().__init__(class_name)
        self.position = position
        self.angle = angle
        self.value = value

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        position = (self.position + Coord(0.28, 0.28)).center
        text = Text("",
                    transform=position.transform,
                    class_=self.class_name
                    )
        span = TSpan(str(self.value), alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)

        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name
                    )
        span = TSpan(LittleKillerGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        return group

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"{repr(self.position)}, "
            f"{repr(self.angle)}, "
            f"{repr(self.value)}"
            f")"
        )


class KillerGlyph(Glyph):
    offset = 10

    size = config.drawing.cell_size / 2.0

    long_size = config.drawing.cell_size / 2.0 - offset

    long_lines = {
        2: Vector(Coord(0, 0), Coord(0, 1)),
        4: Vector(Coord(0, 0), Coord(1, 0)),
        6: Vector(Coord(0, 1), Coord(1, 1)),
        8: Vector(Coord(1, 0), Coord(1, 1))
    }

    short_lines = {
        12: (Point(-1, -1), Direction.UP),
        23: (Point(1, -1), Direction.UP),
        36: (Point(1, -1), Direction.RIGHT),
        69: (Point(1, 1), Direction.RIGHT),
        89: (Point(1, 1), Direction.DOWN),
        78: (Point(-1, 1), Direction.DOWN),
        47: (Point(-1, 1), Direction.LEFT),
        14: (Point(-1, -1), Direction.LEFT)
    }

    def __init__(self, class_name: str, cells: List[Coord]):
        super().__init__(class_name)
        self.cells = sorted(cells)

    def outside(self, cell: Coord) -> bool:
        for c in self.cells:
            if cell.row == c.row and cell.column == c.column:
                return False
        return True

    def cell_long_lines(self, cell: Coord) -> VectorList:
        vectors = []
        for location, vector in KillerGlyph.long_lines.items():
            if self.outside(cell + Direction(location).offset):
                vectors.append(vector + cell)
        return VectorList(vectors)

    def lines(self) -> VectorList:
        results = VectorList([])
        for cell in self.cells:
            results += self.cell_long_lines(cell)
        results.sort()
        return results

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        for vector in VectorList.merge_vectors(self.lines()):
            group.add(
                Line(
                    start=vector.start.point.coordinates,
                    end=vector.end.point.coordinates,
                    class_=self.class_name
                )
            )
        return group

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', [{', '.join([repr(cell) for cell in self.cells])}])"


class QuadrupleGlyph(Glyph):

    def __init__(self, class_name: str, position: Coord, numbers: str):
        super().__init__(class_name)
        self.position = position
        self.numbers = numbers

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        circle = Circle(class_=self.class_name + "Circle", center=self.position.bottom_right.point.coordinates, r=35)
        group.add(circle)
        text = Text(class_=self.class_name + "Text", text="", transform=self.position.bottom_right.transform)
        span = TSpan(self.numbers, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        return group

    @property
    def priority(self) -> int:
        return 20

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, '{self.numbers}')"
