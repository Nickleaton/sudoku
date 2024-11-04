import unittest
from pathlib import Path

from src.utils.colours import ColourSet


class TestColourSet(unittest.TestCase):

    def setUp(self):
        self.directory = Path("output/tests/colours")
        self.directory.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def generate_svg_grid(size: int, filename: Path):
        print(f"Producing file {filename.name}")

        """Generates an SVG grid of specified size filled with colors."""
        colors = ColourSet.colours("general")
        svg_elements = []
        rect_size = 50  # Size of each square in the grid

        colour_index: int = 0
        for i in range(size):
            for j in range(size):
                color = colors[(colour_index+i+j) % len(colors)]
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

        # Write the SVG content to a file
        with open(filename, 'w') as f:
            f.write(svg)

    def test_svg_generation(self):
        sizes = [4, 6, 9, 16]
        for size in sizes:
            filename:Path = Path(f"sudoku_grid_{size}x{size}.svg")
            TestColourSet.generate_svg_grid(size, self.directory / filename)


if __name__ == '__main__':
    unittest.main()