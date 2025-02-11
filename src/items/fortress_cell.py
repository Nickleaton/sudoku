"""FortressCell."""

from src.glyphs.fortress_cell_glyph import FortressCellGlyph
from src.glyphs.glyph import Glyph
from src.items.simple_cell_reference import SimpleCellReference
from src.utils.coord import Coord


class FortressCell(SimpleCellReference):
    """Shared class for fortress cells."""

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs associated with this FortressCell.

        Returns:
            list[Glyph]: A list containing the FortressCellGlyph.
        """
        return [FortressCellGlyph('FortressCell', Coord(self.row, self.column))]

    def css(self) -> dict:
        """Return the CSS styling for the FortressCell.

        Returns:
            dict: A dictionary containing the CSS properties for the FortressCell.
        """
        return {
            '.FortressCell': {
                'stroke': 'black',
                'stroke-width': '3',
            },
        }

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this FortressCell.

        Returns:
            set[str]: A set of tags including 'Comparison'.
        """
        return super().tags.union({'Comparison'})

    def bookkeeping(self) -> None:
        """Update the bookkeeping for the FortressCell.

        Sets the impossibility of containing digits that cannot be valid for the fortress cell's constraints.
        """
