import unittest
from typing import Type

from svgwrite import Drawing

from src.glyphs.glyph import LineGlyph, PolyLineGlyph, \
    ThermometerGlyph, CircleGlyph, KropkiGlyph, \
    OddCellGlyph, ConsecutiveGlyph, Glyph, SquareGlyph, EvenCellGlyph, CellGlyph, BoxGlyph, \
    BattenburgGlyph, TextGlyph, SimpleTextGlyph, KnownGlyph, EdgeTextGlyph, \
    ArrowGlyph, StarGlyph, RectangleGlyph, Consecutive1Glyph, LittleArrowGlyph, LittleNumberGlyph, KillerTextGlyph, \
    LittleKillerGlyph, ComposedGlyph, FortressCellGlyph, RectGlyph, ArrowLineGlyph, KillerGlyph, BetweenGlyph, \
    SimpleThermometerGlyph, FrozenThermometerGlyph
from src.glyphs.glyph import QuadrupleGlyph
from src.utils.angle import Angle
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.point import Point

COLOURS = [
    "Red",
    "Orange",
    'Yellow',
    'Lime',
    'Green',
    'Cyan',
    'Blue',
    'Purple',
    'Magenta',
    'Grey'
]

a = Angle(0)  # Force imports for eval to work


class TestGlyph(unittest.TestCase):

    def setUp(self) -> None:
        self.canvas = Drawing(filename="test.svg", size=("100%", "100%"))
        self.glyph = Glyph('Style')
        self.maxDiff = None

    @property
    def representation(self) -> str:
        return "Glyph('Style')"

    @property
    def target(self) -> str:
        return ""  # pragma: no cover

    @property
    def start_marker(self) -> str:
        return ""

    @property
    def end_marker(self) -> str:
        return ""

    @property
    def symbol(self) -> str:
        return ""

    def test_draw(self) -> None:
        if not isinstance(self.glyph, Glyph):
            element = self.glyph.draw()
            if element is not None:
                self.assertEqual(self.target, element.tostring())

    def test_start_marker(self):
        marker = self.glyph.__class__.start_marker()
        if marker is None:
            self.assertEqual(self.start_marker, "", )
        else:
            self.assertEqual(self.start_marker, marker.tostring())

    def test_end_marker(self):
        marker = self.glyph.__class__.end_marker()
        if marker is None:
            self.assertEqual(self.end_marker, "")
        else:
            self.assertEqual(self.end_marker, marker.tostring())

    def test_symbol(self):
        symbol = self.glyph.__class__.symbol()
        if symbol is None:
            self.assertEqual(self.symbol, "")
        else:
            self.assertEqual(self.symbol, symbol.tostring())

    def test_priority(self):
        self.assertFalse(self.glyph < self.glyph)

    def test_repr(self):
        self.assertEqual(self.representation, str(self.glyph))

    def test_eval_repr(self):
        # pylint: disable=eval-used
        self.assertEqual(self.representation, repr(eval(self.representation)))

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph}

    def test_used_classes(self) -> None:
        # expected_names = sorted([cls.__name__ for cls in self.expected_classes])
        # used_names = sorted([cls.__name__ for cls in self.glyph.used_classes])
        # print(f"{{{', '.join(expected_names)}}}")
        # print(f"{{{', '.join(used_names)}}}")
        # print()
        self.assertEqual(self.expected_classes, self.glyph.used_classes)


class TestLineGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = LineGlyph("Style", Coord(0, 0), Coord(1, 2))

    @property
    def target(self) -> str:
        return '<line class="Style" x1="0" x2="200" y1="0" y2="100" />'

    @property
    def representation(self) -> str:
        return "LineGlyph('Style', Coord(0, 0), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, LineGlyph}


class TestPolyLineGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = PolyLineGlyph("Style", [Coord(0, 0), Coord(1, 2), Coord(2, 3)], False, False)

    @property
    def target(self):
        return '<polyline class="Style" points="50.0,50.0 250.0,150.0 350.0,250.0" />'

    @property
    def representation(self) -> str:
        return "PolyLineGlyph('Style', [Coord(0, 0), Coord(1, 2), Coord(2, 3)], False, False)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, PolyLineGlyph}


class TestArrowLineGlyph(TestPolyLineGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = ArrowLineGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        return (
            '<marker class="Arrow ArrowStart" '
            'id="Arrow-start" '
            'markerHeight="35" '
            'markerWidth="35" '
            'refX="50" '
            'refY="50" '
            'viewBox="0 0 100 100">'
            '<circle cx="50" cy="50" r="35" />'
            '</marker>'
        )

    @property
    def end_marker(self) -> str:
        return (
            '<marker class="Arrow ArrowEnd" id="Arrow-end" markerHeight="20" markerWidth="20" orient="auto" '
            'refX="20" refY="20" viewBox="0 0 50 50"><polyline points="0,0 20,20 0,40" /></marker>'
        )

    @property
    def target(self):
        return (
            '<polyline class="Style" '
            'marker-end="url(#Style-end)" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        return "ArrowLineGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {ArrowLineGlyph, Glyph, PolyLineGlyph}


class TestThermometerGlyph(TestPolyLineGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = ThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        return (
            '<marker class="Thermometer ThermometerStart" id="Thermometer-start" refX="50" refY="50" '
            'viewBox="0 0 100 100"><circle cx="50" cy="50" r="30" /></marker>'
        )

    @property
    def target(self):
        return (
            '<polyline class="Style" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        return "ThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, PolyLineGlyph, ThermometerGlyph}


class TestSimpleThermometerGlyph(TestThermometerGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = SimpleThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        return (
            '<marker class="SimpleThermometer SimpleThermometerStart" id="SimpleThermometer-start" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="30" /></marker>'
        )

    @property
    def target(self):
        return (
            '<polyline class="Style" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        return "SimpleThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, PolyLineGlyph, SimpleThermometerGlyph, ThermometerGlyph}


class TestFrozenThermometerGlyph(TestThermometerGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = FrozenThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        return (
            '<marker class="FrozenThermometer FrozenThermometerStart" id="FrozenThermometer-start" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="30" /></marker>'
        )

    @property
    def target(self):
        return (
            '<polyline class="Style" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        return "FrozenThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {FrozenThermometerGlyph, Glyph, PolyLineGlyph, ThermometerGlyph}


class TestBetweenLineGlyph(TestPolyLineGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = BetweenGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        return (
            '<marker class="Between BetweenStart" id="Between-start" markerHeight="35" markerWidth="35" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="35" /></marker>'
        )

    @property
    def end_marker(self) -> str:
        return (
            '<marker class="Between BetweenEnd" id="Between-end" markerHeight="35" markerWidth="35" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="35" /></marker>'
        )

    @property
    def target(self):
        return (
            '<polyline class="Style" '
            'marker-end="url(#Style-end)" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        return "BetweenGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {BetweenGlyph, Glyph, PolyLineGlyph}


class TestCircleGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = CircleGlyph('Style', Coord(1, 1), 0.5)

    @property
    def target(self):
        return '<circle class="Style" cx="0" cy="0" r="50.0" transform="translate(100, 100)" />'

    @property
    def representation(self) -> str:
        return "CircleGlyph('Style', Coord(1, 1), 0.5)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {CircleGlyph, Glyph}


class TestOddCellGlyph(TestCircleGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = OddCellGlyph('Style', Coord(1, 1))

    @property
    def symbol(self) -> str:
        return (
            '<symbol class="OddCell" id="OddCell-symbol" viewBox="0 0 100 100">'
            '<circle cx="50" cy="50" r="35" /></symbol>'
        )

    @property
    def target(self):
        return '<use class="OddCell" height="100" width="100" x="100" xlink:href="#OddCell-symbol" y="100" />'

    @property
    def representation(self) -> str:
        return "OddCellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, OddCellGlyph}


class TestKropkiGlyph(TestCircleGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = KropkiGlyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self):
        return '<circle class="Style" cx="0" cy="0" r="15.0" transform="translate(150.0, 100.0)" />'

    @property
    def representation(self) -> str:
        return "KropkiGlyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {CircleGlyph, Glyph, KropkiGlyph}


class TestConsecutiveGlyph(TestCircleGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = ConsecutiveGlyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self):
        return '<circle class="Style" cx="0" cy="0" r="15.0" transform="translate(150.0, 100.0)" />'

    @property
    def representation(self) -> str:
        return "ConsecutiveGlyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {CircleGlyph, ConsecutiveGlyph, Glyph}


class TestSquareGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = SquareGlyph('Style', position=Point(100, 100), size=50)

    @property
    def target(self):
        return '<rect class="Style" height="5000" transform="translate(100, 100)" width="5000" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "SquareGlyph('Style', Point(100, 100), 50)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, RectGlyph, SquareGlyph}


class TestRectGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = RectGlyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self):
        return '<rect class="Style" height="100" transform="translate(100, 100)" width="200" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "RectGlyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, RectGlyph}


class TestEvenCellGlyph(TestSquareGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = EvenCellGlyph('Style', Coord(1, 1))

    @property
    def target(self):
        return '<rect class="Style" height="70.0" transform="translate(115.0, 115.0)" width="70.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "EvenCellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {EvenCellGlyph, Glyph}


class TestCellGlyph(TestSquareGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = CellGlyph('Style', Coord(1, 1))

    @property
    def target(self):
        return '<rect class="Style" height="100" transform="translate(100, 100)" width="100" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "CellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {CellGlyph, Glyph, RectGlyph, SquareGlyph}


class TestFortressCellGlyph(TestSquareGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = FortressCellGlyph('Style', Coord(1, 1))

    @property
    def target(self):
        return (
            '<rect class="Style" height="100" '
            'transform="translate(100, 100)" width="100" x="0" y="0" />'
        )

    @property
    def representation(self) -> str:
        return "FortressCellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {FortressCellGlyph, Glyph, RectGlyph, SquareGlyph}


class TestBoxGlyph(TestSquareGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = BoxGlyph('Style', Coord(1, 1), Coord(3, 3))

    @property
    def target(self):
        return '<rect class="Style" height="300" transform="translate(100, 100)" width="300" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "BoxGlyph('Style', Coord(1, 1), Coord(3, 3))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {BoxGlyph, Glyph, RectGlyph}


class TestBattenburgGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = BattenburgGlyph('Style', Coord(3, 3))

    @property
    def symbol(self) -> str:
        return (
            '<symbol class="Battenberg" id="Battenberg-symbol" viewBox="0 0 100 100">'
            '<rect class="BattenbergPink" height="30.0" transform="translate(0.0, -30.0)" width="30.0" x="0" y="0" />'
            '<rect class="BattenbergYellow" height="30.0" transform="translate(30.0, 0.0)" width="30.0" x="0" y="0" />'
            '<rect class="BattenbergPink" height="30.0" transform="translate(0.0, 30.0)" width="30.0" x="0" y="0" />'
            '<rect class="BattenbergYellow" height="30.0" transform="translate(-30.0, 0.0)" width="30.0" x="0" y="0" />'
            '</symbol>'
        )

    @property
    def target(self):
        return '<use class="Battenberg" height="100" width="100" x="300" xlink:href="#Battenberg-symbol" y="300" />'

    @property
    def representation(self) -> str:
        return "BattenburgGlyph('Style', Coord(3, 3))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {BattenburgGlyph, Glyph}


class TestTextGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = TextGlyph('Style', 90, Point(100, 100), "abcd")

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(100, 100) rotate(90.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(100, 100) rotate(90.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "TextGlyph('Style', 90.0, Point(100, 100), 'abcd')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, TextGlyph}


class TestSimpleTextGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = SimpleTextGlyph('Style', 0, Coord(1, 1), "X")

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "SimpleTextGlyph('Style', 0.0, Coord(1, 1), 'X')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, SimpleTextGlyph, TextGlyph}


class TestEdgeTextGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = EdgeTextGlyph('Style', 0, Coord(1, 1), Coord(1, 2), 'X')

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(150.0, 100.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(150.0, 100.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "EdgeTextGlyph('Style', 0.0, Coord(1, 1), Coord(1, 2), 'X')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {EdgeTextGlyph, Glyph, TextGlyph}


class TestKnownGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = KnownGlyph('Style', Coord(1, 1), 1)

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(150.0, 150.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">1</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(150.0, 150.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">1</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "KnownGlyph('Style', Coord(1, 1), 1)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, KnownGlyph, SimpleTextGlyph, TextGlyph}


class TestArrowGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = ArrowGlyph('Style', 90.0, Coord(0, 0))

    @property
    def start_marker(self) -> str:
        return ""

    @property
    def end_marker(self) -> str:
        return ""

    @property
    def symbol(self) -> str:
        return ""

    @property
    def target(self):
        return (
            '<text class="Style" transform="translate(50.0, 50.0) rotate(90.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">↑</tspan></text>'
        )

    @property
    def representation(self) -> str:
        return "ArrowGlyph('Style', 90.0, Coord(0, 0))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {ArrowGlyph, Glyph}


class TestStarGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = StarGlyph('Style', Coord(1, 1))

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">✧</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">✧</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "StarGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, SimpleTextGlyph, StarGlyph, TextGlyph}


class TestRectangleGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = RectangleGlyph('Style', Coord(1, 1), Coord(1, 2), 0.25, 2, True)

    @property
    def target(self):
        return (
            '<rect class="Style" height="25.0" transform="translate(150.0, 100.0)" '
            'width="50.0" x="0" y="0" />'
        )

    @property
    def representation(self) -> str:
        return "RectangleGlyph('Style', Coord(1, 1), Coord(1, 2), 0.25, 2, True)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, RectangleGlyph}


class TestConsecutive1Glyph(TestRectangleGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = Consecutive1Glyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self):
        return (
            '<rect class="Style" height="50.0" transform="translate(150.0, 100.0)" '
            'width="25.0" x="0" y="0" />'
        )

    @property
    def representation(self) -> str:
        return "Consecutive1Glyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Consecutive1Glyph, Glyph, RectangleGlyph}


class TestLittleArrowGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = LittleArrowGlyph('Style', Coord(1, 1), 1)

    @property
    def target(self):
        return (
            '<text class="Style" transform="translate(140.0, 140.0) rotate(315.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">▲</tspan>'
            '</text>'
        )

    @property
    def representation(self) -> str:
        return "LittleArrowGlyph('Style', Coord(1, 1), 1)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, LittleArrowGlyph}


class TestLittleNumberGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = LittleNumberGlyph('Style', Coord(1, 1), 1)

    @property
    def target(self):
        return (
            '<text class="Style" transform="translate(135.0, 135.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">1</tspan>'
            '</text>'
        )

    @property
    def representation(self) -> str:
        return "LittleNumberGlyph('Style', Coord(1, 1), 1)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, LittleNumberGlyph}


class TestKillerTextGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = KillerTextGlyph('Style', 0, Coord(1, 1), 'abcd')

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(105.0, 105.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(105.0, 105.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "KillerTextGlyph('Style', 0.0, Coord(1, 1), 'abcd')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, KillerTextGlyph}


class TestLittleKillerGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = LittleKillerGlyph('Style', Coord(0, 0), Direction.DOWN_RIGHT.angle, 20)

    @property
    def target(self):
        return (
            '<g>'
            '<text class="Style" transform="translate(50.0, 50.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">20</tspan>'
            '</text>'
            '<text class="Style" transform="translate(50.0, 50.0) rotate(135.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">ꜛ</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "LittleKillerGlyph('Style', Coord(0, 0), Angle(135.0), 20)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, LittleKillerGlyph}


class TestComposedGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = ComposedGlyph('Style')

    @property
    def target(self):
        return '<g />'

    @property
    def representation(self) -> str:
        return (
            "ComposedGlyph("
            "'Style', "
            "["
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {ComposedGlyph, Glyph}


class TestKillerGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        cells = [
            Coord(1, 3),
            Coord(2, 3),
            Coord(3, 1),
            Coord(3, 2),
            Coord(3, 3),
            Coord(4, 2),
            Coord(4, 3),
            Coord(4, 4),
            Coord(5, 4)
        ]
        self.glyph = KillerGlyph('Style', cells)

    @property
    def target(self):
        return (
            '<g>'
            '<line class="Style" x1="300" x2="400" y1="100" y2="100" />'
            '<line class="Style" x1="100" x2="100" y1="300" y2="400" />'
            '<line class="Style" x1="300" x2="300" y1="300" y2="100" />'
            '<line class="Style" x1="300" x2="100" y1="300" y2="300" />'
            '<line class="Style" x1="100" x2="200" y1="400" y2="400" />'
            '<line class="Style" x1="200" x2="200" y1="400" y2="500" />'
            '<line class="Style" x1="400" x2="400" y1="400" y2="100" />'
            '<line class="Style" x1="400" x2="500" y1="400" y2="400" />'
            '<line class="Style" x1="400" x2="200" y1="500" y2="500" />'
            '<line class="Style" x1="400" x2="400" y1="500" y2="600" />'
            '<line class="Style" x1="400" x2="500" y1="600" y2="600" />'
            '<line class="Style" x1="500" x2="500" y1="600" y2="400" />'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return (
            "KillerGlyph('Style', "
            "["
            "Coord(1, 3), Coord(2, 3), Coord(3, 1), Coord(3, 2), Coord(3, 3), "
            "Coord(4, 2), Coord(4, 3), Coord(4, 4), Coord(5, 4)"
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, KillerGlyph}


class TestQuadrupleGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = QuadrupleGlyph("Style", Coord(2, 2), "1234")

    @property
    def target(self):
        return (
            '<g>'
            '<circle class="StyleCircle" cx="300" cy="300" r="35" />'
            '<text class="StyleText" transform="translate(300, 300)">'
            '<tspan alignment-baseline="central" text-anchor="middle">1234</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "QuadrupleGlyph('Style', Coord(2, 2), '1234')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, QuadrupleGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
