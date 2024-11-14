import abc
from abc import ABC
from typing import Optional, List, Set, Type, Dict, Iterator

import strictyaml
from sortedcontainers import SortedDict

from src.glyphs.composed_glyph import ComposedGlyph
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.book_keeping import BookKeeping
from src.parsers.none_parser import NoneParser
from src.parsers.parser import Parser
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException


# pylint: disable=too-many-public-methods
class Item(ABC):
    """Top level of the Item hierarchy.
    Items generate the constraints
    Items generate the svg to view the problems and solutions
    Items manage bookkeeping to simplify problems

    They are created with the create method
    """

    # Class Variables

    # register of classes
    classes: Dict[str, Type['Item']] = SortedDict({})
    # Counter of instances created
    counter: int = 0

    # Creation Routines

    def __init_subclass__(cls, **kwargs):
        """Register the class so that it can be created from yaml.
        """
        super().__init_subclass__(**kwargs)
        # Register the class
        Item.classes[cls.__name__] = cls
        Item.classes[Item.__name__] = Item

    def __init__(self, board: Board):
        """Constructor.

        Args:
            board: The board this item belongs to.
        """
        super().__init__()

        # Board this item belongs to
        self.board: Board = board

        # Pointer back to parent
        self.parent: Optional[Item] = None
        # Allocation a new identity
        self.identity: int = Item.counter
        Item.counter += 1

    # Schema and creation

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if this item is a sequence"""
        return False

    @classmethod
    def is_composite(cls) -> bool:
        """Return True if this item is a composite"""
        return False

    @classmethod
    def parser(cls) -> Parser:
        return NoneParser()

    @classmethod
    def schema(cls) -> strictyaml.Validator | strictyaml.Optional:
        if cls.is_sequence():
            return strictyaml.Seq(cls.parser())
        return cls.parser()

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> 'Item':
        """Create an instance of an item from a YAML dictionary.

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
        if isinstance(yaml, str):
            name = yaml
        else:
            name = list(yaml.keys())[0]
        if name not in cls.classes:
            raise SudokuException(f"Unknown item class {name}")
        clazz = cls.classes[name]
        return clazz.create(board, yaml)

    @property
    def top(self) -> 'Item':
        """The top most item in the hierarchy this item belongs to.

        Returns:
            The top most item.
        """
        if self.parent is None:
            return self
        return self.parent.top

    def regions(self) -> Set['Item']:
        """Get the set of items used in this item.

        The default implementation returns a set containing just this item.
        Subclasses should override this method if they use other items.

        Returns:
            A set of items.
        """
        return {self}

    def svg(self) -> Optional[Glyph]:
        """Return an SVG glyph which can be used to display the item.
        The default implementation returns None, which means that the item
        should not be displayed.
        """
        return None

    @property
    def rules(self) -> List[Rule]:
        """Return a list of rules that apply to this item.

        The default implementation returns an empty list, which means that there
        are no rules that apply to this item.

        Returns:
            List[Rule]: A list of rules that apply to this item.
        """
        return []

    def flatten(self) -> List['Item']:
        """Return a list of all items in the hierarchy that this item belongs to.

        The default implementation returns a list containing just the current
        item. Subclasses should override this method if they contain other items.

        Returns:
            List[Self]: A list of all items in the hierarchy that this item
                belongs to.
        """
        return [self]

    @property
    def sorted_unique_rules(self) -> List[Rule]:
        """Return a list of unique rules that apply to this item, sorted in order.

        The rules are determined by recursively traversing the item tree and
        calling the `rules` property on each item. The resulting list of rules
        is de-duplicated and sorted in order.

        The ordering keeps the rules consistent between different puzzles

        Returns:
            List[Rule]: A list of unique rules that apply to this item, sorted
                in order.
        """
        return sorted(list(set(self.rules)))

    def glyphs(self) -> List[Glyph]:
        """Return a list of SVG glyphs for this item.

        The glyphs are determined by recursively traversing the item tree and
        calling the `svg` method on each item. The `selector` function is used to
        determine which items to include in the list of glyphs.

        So if we have answers in the tree, and we want the puzzle problem without
        the solution we can exclude it using a selector

        Returns:
            List[Glyph]: A list of glyphs.
        """
        return []

    def sorted_glyphs(self) -> Glyph:
        """Return a single glyph representing all the glyphs for this item.

        The glyphs are sorted by their `z_order` attribute.

        Returns:
            Glyph: A single glyph representing all the glyphs for this item.
        """
        return ComposedGlyph('Composed', sorted(self.glyphs()))

    @property
    def name(self) -> str:
        """Return a string identifying the item.

        The string is of the form `<class_name>_<identity>`, where `<class_name>`
        is the name of the class of the item and `<identity>` is an integer
        assigned to the item.

        Returns:
            str: A string identifying the item.
        """
        return f"{self.__class__.__name__}_{self.identity}"

    @property
    def tags(self) -> set[str]:
        """Return a set of strings associated with this item.

        The set of strings is used to identify items with certain properties,
        such as the type of item or the constraints it enforces.

        Returns:
            set[str]: A set of strings associated with this item.
        """
        return set()

    def walk(self) -> Iterator['Item']:
        """Yield each item in the tree of items rooted at the current item.

        The generator yields the current item, then recursively yields each item
        in the tree rooted at the current item. The order of the items is
        unspecified.

        Yields:
            Item: The current item, followed by each item in the tree rooted at
                the current item.
        """
        yield self

    @property
    def used_classes(self) -> Set[Type['Item']]:
        """Return a set of classes that this item uses.

        The set of classes is determined by traversing the method resolution
        order (MRO) of the item's class. The set contains all classes in the
        MRO, except for the abstract base class (`abc.ABC`) and the `object`
        class.

        Returns:
            Set[Type[Self]]: A set of classes that this item uses.
        """
        # Get the hierarchy of the class
        # handle the references
        result = set(self.__class__.__mro__)
        for item in self.walk():
            result |= set(item.__class__.__mro__)
        return result.difference({abc.ABC, object})

    @staticmethod
    def select_all(_: 'Item') -> bool:
        """The select method is used to select which items should be used when
        generating the lp model. The method should return True if the item
        should be used (i.e. included in the model) and False otherwise.

        Args:

        Returns:
            True
        """
        return True

    def __repr__(self) -> str:
        """Return a string representation of this item.

        The string representation is of the form `<class_name>(<board>)`, where
        `<class_name>` is the name of the class of the item and `<board>` is a
        string representation of the board associated with the item.

        Returns:
            str: A string representation of this item.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    # pylint: disable=unused-argument
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add a constraint to the given solver.

        This method is called when the given solver is solving the board
        associated with this item. The item is expected to add any constraints
        required to solve the board.

        Args:
            solver (PulpSolver): A solver that is solving the board associated
                with this item.
        """

    def bookkeeping(self) -> None:
        """Perform bookkeeping for this item.

        This method is called when the solver is adding constraints to the
        lp model. The method is expected to add any constraints required to
        ensure that the bookkeeping for this item is done correctly.
        """

    def add_bookkeeping_constraint(self, solver: PulpSolver) -> None:
        """Add a constraint to the given solver to keep track of the values chosen for all children of this item.

        In some cases we can completely eliminate choices. For example, if we have a cell with only one possible value
        in row 4 column 5, then we can eliminate that value from all other cells in that row and column.

        For thermometer constraints we can do similar.

        In practice this should be redundant as the presolve of the solver should take care of this.

        This method is called when the given solver is solving the board associated with this item. This method is
        expected to add any bookkeeping constraints required for this item.

        Args:
            solver (PulpSolver): A solver that is solving the board associated with this item.
        """
        # The following uses __class__.__name__ to avoid circular imports
        for item in self.walk():
            if item.__class__.__name__ != 'Cell':
                continue
            item.add_bookkeeping_constraint(solver)

    def marked_book(self) -> Optional[BookKeeping]:
        """Return the book for the cell or None.
        Enables Liskov Substitution Principle.
        """
        return None

    def bookkeeping_unique(self) -> bool:
        """Check if all bookkeeping items in the hierarchy are unique.

        This method traverses the tree of items rooted at the current item,
        calling the `marked_book` method for each item. It checks if each
        `marked_book` is not None and that it is unique by calling
        `is_unique()` on it.

        Returns:
            bool: True if all marked books are unique, False otherwise.
        """
        marked_books: List[BookKeeping] = []
        for item in self.walk():
            marked_book: Optional[BookKeeping] = item.marked_book()
            if marked_book is not None:
                marked_books.append(marked_book)
        return all(marked_book.is_unique() for marked_book in marked_books)

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for YAML dump.

        The dictionary has one key-value pair. The key is the name of the class
        of the item and the value is `None`.

        Returns:
            Dict: A dictionary with one key-value pair.
        """
        return {self.__class__.__name__: None}

    def css(self) -> Dict:
        # TODO Should we have this here?
        """Get the CSS for the item.

        This method returns a dictionary with CSS attributes for items of this class. The key is the class name of the
        item and the value is a dictionary with the CSS style for that class.

        Returns:
            Dict: A dictionary with CSS style for the class.
        """
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
        """TODO think if this is the wrong way. We could recurse the tree coming back with any
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
