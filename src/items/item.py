import abc
import logging
from abc import ABC
from typing import Optional, List, Set, Type, Dict, Callable, Self

from sortedcontainers import SortedDict

from src.glyphs.glyph import Glyph
from src.glyphs.composed_glyph import ComposedGlyph
from src.items.board import Board
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SudokuException(Exception):
    pass

class Item(ABC):
    """
    Top level of the Item hierarchy.
    Items generate the constraints
    Items generate the svg to view the problems and solutions
    Items manage bookkeeping to simplify problems

    They are created with the create method
    """
    classes: Dict[str, Type['Item']] = SortedDict({})
    counter = 0

    @staticmethod
    def select_all(_: 'Item') -> bool:
        return True

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Item.classes[cls.__name__] = cls

    def __init__(self, board: Board):
        """
        Constructor.

        Args:
            board: The board this item belongs to.
        """
        super().__init__()
        self.board: Board = board
        self.parent: Optional[Item] = None
        self.identity: int = Item.counter
        Item.counter += 1

    @property
    def top(self) -> Self:
        """
        The top most item in the hierarchy this item belongs to.

        Returns:
            The top most item.
        """
        if self.parent is None:
            return self
        return self.parent.top

    def regions(self) -> Set[Self]:
        return {self}

    # pylint: disable=no-self-use
    def svg(self) -> Optional[Glyph]:
        """
        Return an SVG glyph which can be used to display the item.
        The default implementation returns None, which means that the item
        should not be displayed.
        """
        return None

    @property
    def rules(self) -> List[Rule]:
        """
        Return a list of rules that apply to this item.

        The default implementation returns an empty list, which means that there
        are no rules that apply to this item.

        Returns:
            List[Rule]: A list of rules that apply to this item.
        """
        return []

    def flatten(self) -> List[Self]:
        return [self]

    @property
    def sorted_unique_rules(self) -> List[Rule]:
        """
        Return a list of unique rules that apply to this item, sorted in order.

        The rules are determined by recursively traversing the item tree and
        calling the `rules` property on each item. The resulting list of rules
        is de-duplicated and sorted in order.

        The ordering keeps the rules consistent between different puzzles

        Returns:
            List[Rule]: A list of unique rules that apply to this item, sorted
                in order.
        """
        return sorted(list(set(self.rules)))

    def glyphs(self, selector: Callable[[Self], bool]) -> List[Glyph]:
        """
        Return a list of SVG glyphs for this item.

        The glyphs are determined by recursively traversing the item tree and
        calling the `svg` method on each item. The `selector` function is used to
        determine which items to include in the list of glyphs.

        So if we have answers in the tree, and we want the puzzle problem without
        the solution we can exclude it using a selector

        Args:
            selector (Callable[[Item], bool]): A function that takes an item and
                returns a boolean indicating whether to include it in the list
                of glyphs.

        Returns:
            List[Glyph]: A list of glyphs.
        """
        return []

    def sorted_glyphs(self, selector: Callable[[Self], bool]) -> Glyph:
        """
        Return a single glyph representing all the glyphs for this item.

        The glyphs are sorted by their `z_order` attribute.

        Args:
            selector (Callable[[Item], bool]): A function that takes an item and
                returns a boolean indicating whether to include it in the list
                of glyphs.

        Returns:
            Glyph: A single glyph representing all the glyphs for this item.
        """
        return ComposedGlyph('Composed', sorted(self.glyphs(selector)))

    @property
    def name(self) -> str:
        """
        Return a string identifying the item.

        The string is of the form `<class_name>_<identity>`, where `<class_name>`
        is the name of the class of the item and `<identity>` is an integer
        assigned to the item.

        Returns:
            str: A string identifying the item.
        """
        return f"{self.__class__.__name__}_{self.identity}"

    @property
    def tags(self) -> set[str]:
        """
        Return a set of strings associated with this item.

        The set of strings is used to identify items with certain properties,
        such as the type of item or the constraints it enforces.

        Returns:
            set[str]: A set of strings associated with this item.
        """
        return set()

    @property
    def used_classes(self) -> Set[Type[Self]]:
        """
        Return a set of classes that this item uses.

        The set of classes is determined by traversing the method resolution
        order (MRO) of the item's class. The set contains all classes in the
        MRO, except for the abstract base class (`abc.ABC`) and the `object`
        class.

        Returns:
            Set[Type[Self]]: A set of classes that this item uses.
        """
        return set(self.__class__.__mro__).difference({abc.ABC, object})
    #

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Self:
        """
        Create an instance of an item from a YAML dictionary.

        The YAML dictionary must contain a single key-value pair, where the key
        is the name of the item class and the value is a dictionary of arguments
        to pass to the constructor of the item class.

        Args:
            board (Board): The board associated with this item.
            yaml (Dict): A YAML dictionary containing the key-value pair to
                create an item.

        Returns:
            Self: An instance of the item class associated with the YAML
                dictionary.

        Raises:
            SudokuException: If the YAML dictionary does not contain a single
                key-value pair.
        """
        if len(yaml) != 1:
            raise SudokuException(f"Yaml={str(yaml)}")
        name = list(yaml.keys())[0]
        if name not in cls.classes:
            logging.error(f"Cannot find item {name}")
        clazz = cls.classes[name]
        return clazz.create(board, yaml)

    def __repr__(self) -> str:
        """
        Return a string representation of this item.

        The string representation is of the form `<class_name>(<board>)`, where
        `<class_name>` is the name of the class of the item and `<board>` is a
        string representation of the board associated with the item.

        Returns:
            str: A string representation of this item.
        """
        return f"{self.__class__.__name__}(({self.board!r})"

    # pylint: disable=unused-argument
    def add_constraint(self, solver: PulpSolver) -> None:
        """
        Add a constraint to the given solver.

        This method is called when the given solver is solving the board
        associated with this item. The item is expected to add any constraints
        required to solve the board.

        Args:
            solver (PulpSolver): A solver that is solving the board associated
                with this item.
        """
        pass

    def bookkeeping(self) -> None:
        pass

    def children(self) -> Set[Self]:
        """
        Return a set of children items.

        This method returns a set of items that are children of this item. By
        default, this method returns a set containing only this item. Subclasses
        of `Item` can override this method to add additional items to the set.

        Returns:
            Set[Self]: A set of children items.
        """
        return {self}


    def add_bookkeeping_constraint(self, solver: PulpSolver) -> None:
        """
        Add a constraint to the given solver to keep track of the values chosen for all children of this item.

        In some cases we can completely eliminate choices. For example, if we have a cell with only one possible value
        in row 4 column 5, then we can eliminate that value from all other cells in that row and column.

        For thermometer constraints we can do similar.

        In practice this should be redundant as the presolve of the solver should take care of this.

        This method is called when the given solver is solving the board associated with this item. This method is
        expected to add any bookkeeping constraints required for this item.

        Args:
            solver (PulpSolver): A solver that is solving the board associated with this item.
        """
        cells = [i for i in self.children() if i.__class__.__name__ == 'Cell']
        for cell in cells:
            cell.add_bookkeeping_constraint(solver)

    def to_dict(self) -> Dict:
        """
        Convert the item to a dictionary for YAML dump.

        The dictionary has one key-value pair. The key is the name of the class
        of the item and the value is `None`.

        Returns:
            Dict: A dictionary with one key-value pair.
        """
        return {self.__class__.__name__: None}

    # pylint: disable=no-self-use
    def css(self) -> Dict:
        # TODO Should we have this here?
        return {
            '.TextGlyphForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 8,
                'fill': 'black',
                'font-weight': 'bolder'
            },
            '.TextGlyphBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            },
            'LittleNumber': {
                'font-size': '20px',
                'stroke': 'black',
            }
        }

    @staticmethod
    def css_text(data: Dict, indent: int = 0) -> str:
        """

        TODO think if this is the wrong way. We could recurse the tree coming back with any
        children's css building up a dictionary and returning it.

        Convert a dictionary of css rules to a string.

        The dictionary should have string keys and values that are either strings or
        dictionaries. The strings are directly used as css rules. The dictionaries
        are processed recursively.

        Args:
            data (Dict): The dictionary of css rules.
            indent (int, optional): The number of tabs to indent the output. Defaults to 0.

        Returns:
            str: The string of css rules.
        """
        tab = '    '
        result = ""
        for k in sorted(data.keys()):
            v = data[k]
            if isinstance(v, dict):
                result += f"{tab * indent}{k} {{\n"
                result += Item.css_text(v, indent + 1)
                result += f"{tab * indent}}}\n\n"
            else:
                result += f"{tab * indent}{k}: {v};\n"
        return result
