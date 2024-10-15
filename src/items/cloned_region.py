from typing import List, Tuple, Dict, Set, Type

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class ClonedRegion(Item):
    """
    In a cloned region, the cells in the first region are clones of the cells in the second region.
    """

    def __init__(self, board, cells_a: List[Cell], cells_b: List[Cell]):
        """
        Construct a ClonedRegion.

        :param board: The board with the two regions
        :param cells_a: The cells in the first region
        :param cells_b: The cells in the second region
        :raise AssertionError: If the two regions have different numbers of cells
        """
        super().__init__(board)
        assert len(cells_a) == len(cells_b)
        self.region_a: List[Cell] = cells_a
        self.region_b: List[Cell] = cells_b

    def __repr__(self) -> str:
        """
        Return a string representation of the ClonedRegion.

        The representation is a string that could be used to recreate the ClonedRegion.
        It is of the form:
        `ClonedRegion(board, cells_a, cells_b)`

        :return: A string representation of the ClonedRegion
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{repr(self.region_a)}, "
            f"{repr(self.region_b)}"
            f")"
        )

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple[List[Cell], List[Cell]]:
        # Force string conversion because yaml might convert to int which you don't want when just one cell is cloned
        part_a = str(yaml[cls.__name__].split('=')[0])
        part_b = str(yaml[cls.__name__].split('=')[1])
        cells_a = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in part_a.split(',')]
        cells_b = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in part_b.split(',')]
        return cells_a, cells_b

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """
        Create a ClonedRegion from a Board and a YAML dict.

        :param board: The board with the two regions
        :param yaml: A YAML dict with the two regions
        :return: A ClonedRegion
        """
        cells_a, cells_b = ClonedRegion.extract(board, yaml)
        return ClonedRegion(board, cells_a, cells_b)

    def glyphs(self) -> List[Glyph]:
        # TODO
        return []

    @property
    def used_classes(self) -> Set[Type[Item]]:
        """
        Return a set of classes that this item uses.

        The set of classes is determined by traversing the method resolution
        order (MRO) of the item's class. The set contains all classes in the
        MRO, except for the abstract base class (`abc.ABC`) and the `object`
        class.

        Returns:
            Set[Type[Self]]: A set of classes that this item uses.
        """
        result = super().used_classes
        for item in self.region_a:
            result |= item.used_classes
        for item in self.region_b:
            result |= item.used_classes
        return result

    @property
    def rules(self) -> List[Rule]:
        """
        Get the list of rules for this ClonedRegion.

        :return: A list of rules
        """
        return [
            Rule(
                "ClonedRegion",
                1,
                "The shaded areas are clones. They contain the same digits at the same locations."
            )
        ]

    @property
    def tags(self) -> set[str]:
        """
        Get the set of tags for this item.

        The tags are a set of strings that can be used to identify items with certain properties.
        The default tags are 'Item' and any tags that the item's classes have.
        :return: A set of strings
        """
        return super().tags.union({'ClonedRegion'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """
        Add the constraint that the two regions are clones of each other.

        The constraint is that for each pair of cells in the two regions, the values in the cells are the same.

        :param solver: The solver to add the constraint to
        :return: None
        """
        for cell_1, cell_2 in zip(self.region_a, self.region_b):
            name = f"{self.__class__.__name__}_{cell_1.row}{cell_1.column}_{cell_2.row}{cell_2.column}"
            value_1 = solver.values[cell_1.row][cell_1.column]
            value_2 = solver.values[cell_2.row][cell_2.column]
            solver.model += value_1 == value_2, name

    def to_dict(self) -> Dict:
        """
        Convert the ClonedRegion to a dictionary for YAML dump.

        The dictionary has one key-value pair. The key is the name of the class and the value is a string of the form:
        the first region and <cell_str_b> is a comma-separated string of the row and column of each cell in the second
        region.

        :return: A dictionary with one key-value pair
        """
        cell_str_a = ",".join([f"{cell.row}{cell.column}" for cell in self.region_a])
        cell_str_b = ",".join([f"{cell.row}{cell.column}" for cell in self.region_b])
        return {self.__class__.__name__: f"{cell_str_a}={cell_str_b}"}

    def css(self) -> Dict:
        """
        Get the CSS for the ClonedRegion.

        The CSS is a dictionary with three keys: 'ClonedRegion', 'ClonedRegionForeground', and 'ClonedRegionBackground'.
        The value for each key is a dictionary with the CSS style for that class.

        :return: A dictionary of CSS styles
        """
        return {
            '.ClonedRegion': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black'
            },
            '.ClonedRegionForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.ClonedRegionBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
