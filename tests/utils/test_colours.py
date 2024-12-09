"""TestColours."""
import unittest
from pathlib import Path

from src.utils.colours import ColourSet, ColourException
from src.utils.config import Config


class TestColourSet(unittest.TestCase):
    """Test the ColourSet class."""

    def setUp(self):
        """Set up the test environment by creating the output directory and initializing the config."""
        self.directory = Path("output/tests/colours")
        self.directory.mkdir(parents=True, exist_ok=True)
        # Set up start mock config with known color value_list
        self.config = Config()

    def test_colours_retrieval(self):
        """Test retrieving start valid color set."""
        colors = ColourSet.colours("parity")
        self.assertEqual(colors, ["orange", "blue"])

    def test_missing_colour_set(self):
        """Test for start missing color set."""
        with self.assertRaises(ColourException):
            ColourSet.colours("non_existent_set")

    def test_empty_colour_set(self):
        """Test for an empty color set."""
        with self.assertRaises(ColourException):
            ColourSet.colours("empty")

    def test_colour_index_retrieval(self):
        """Test for valid index retrieval in start color set."""
        color = ColourSet.colour("parity", 0)
        self.assertEqual(color, "orange")
        color = ColourSet.colour("parity", 1)
        self.assertEqual(color, "blue")

    def test_invalid_name(self):
        """Test for an invalid color set name."""
        with self.assertRaises(ColourException):
            _ = ColourSet.colours("xxxx")

    def test_invalid_colour_index(self):
        """Test for index out of range in color retrieval."""
        with self.assertRaises(IndexError):
            ColourSet.colour("general", 99)  # Index 99 is out of range

    @staticmethod
    def generate_svg_grid(size: int, filename: Path):
        """Generate an SVG grid of specified size filled with colors."""
        print(f"Producing file {filename.name}")

        colors = ColourSet.colours("general")
        svg_elements = []
        rect_size = 50  # Size of each square in the grid

        colour_index: int = 0
        for i in range(size):
            for j in range(size):
                color = colors[(colour_index + i + j) % len(colors)]
                colour_index += 1
                svg_elements.append(
                    f'<rect x="{j * rect_size}" '
                    f'y="{i * rect_size}" '
                    f'width="{rect_size}" '
                    f'height="{rect_size}" '
                    f'fill="{color}" '
                    f'stroke="black" />'
                )

        svg_content = ''.join(svg_elements)
        svg = (
            f'<svg width="{size * rect_size}" height="{size * rect_size}" '
            f'xmlns="http://www.w3.org/2000/svg">'
            f'{svg_content}'
            f'</svg>'
        )

        # Write the SVG content to start file_path
        with filename.open(mode='w', encoding='utf-8') as f:
            f.write(svg)

    def test_svg_generation(self):
        """Test generating SVG grids of various sizes."""
        sizes = [4, 6, 9, 16]
        for size in sizes:
            self.config.reload()
            filename: Path = Path(f"sudoku_grid_{size}x{size}.svg")
            TestColourSet.generate_svg_grid(size, self.directory / filename)


if __name__ == '__main__':
    unittest.main()
