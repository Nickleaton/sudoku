"""Item."""

from typing import Type, Iterator

import strictyaml
from sortedcontainers import SortedDict

from src.glyphs.composed_glyph import ComposedGlyph
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.book_keeping_cell import BookKeepingCell
from src.parsers.none_parser import NoneParser
from src.parsers.parser import Parser
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException
from src.validators.validator import Validator


# pylint: disable=too-many-public-methods
class Item:
    """Top-level class for the Item hierarchy.

    Items generate the constraints, manage bookkeeping, and generate SVG for viewing problems and solutions.
    They are created via the create method.
    """

    # Class Variables
    classes: dict[str, Type['Item']] = SortedDict({})
    counter: int = 0

    # Creation Routines

    def __init_subclass__(cls, **kwargs):
        """Register the subclass to the `Item` class hierarchy.

        Args:
            cls (type): The class that is being initialized as a subclass of `Item`.
            **kwargs: Any additional keyword arguments passed to the method (not used).
        """
        super().__init_subclass__(**kwargs)
        Item.classes[cls.__name__] = cls
        Item.classes[Item.__name__] = Item

    def __init__(self, board: Board):
        """Initialize an Item with a given board.

        Args:
            board (Board): The board that this item belongs to.
        """
        super().__init__()

        self.board: Board = board
        self.parent: Item | None = None
        self.identity: int = Item.counter
        Item.counter += 1

    @classmethod
    def is_sequence(cls) -> bool:
        """Check if the item is a sequence.

        Returns:
            bool: True if this item is a sequence, otherwise False.
        """
        return False

    @classmethod
    def is_composite(cls) -> bool:
        """Check if the item is a composite.

        Returns:
            bool: True if this item is a composite, otherwise False.
        """
        return False

    @classmethod
    def parser(cls) -> Parser:
        """Return the parser for this item.

        Returns:
            Parser: The appropriate parser for this item.
        """
        return NoneParser()

    @classmethod
    def validator(cls) -> Validator:
        """Return the validator for this item.

        Returns:
            Validator: The appropriate validator for this item.
        """
        return Validator()

    @classmethod
    def schema(cls) -> strictyaml.Validator | strictyaml.Optional:
        """Return the schema for this item.

        Returns:
            Validator | Optional: The schema for this item, which may be a sequence or parser.
        """
        if cls.is_sequence():
            return strictyaml.Seq(cls.parser())
        return cls.parser()

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'Item':
        """Create an instance of the item from a YAML dictionary.

        Args:
            board (Board): The board this item belongs to.
            yaml (dict): The YAML data to create the item.

        Returns:
            Item: The created instance of the item.

        Raises:
            SudokuException: If the YAML data is invalid or the class cannot be found.
        """
        if isinstance(yaml, str):
            name = yaml
        else:
            name = next(iter(yaml.keys()))
        if name not in cls.classes:
            raise SudokuException(f"Unknown item class {name}")
        print(f"\n\nCreate {cls.__name__} {name} {yaml}\n\n")
        clazz = cls.classes[name]
        return clazz.create(board, yaml)

    @classmethod
    def create2(cls, board: Board, yaml: dict) -> 'Item':
        """Create an instance of the item from a YAML dictionary.

        Args:
            board (Board): The board this item belongs to.
            yaml (dict): The YAML data to create the item.

        Returns:
            Item: The created instance of the item.

        Raises:
            SudokuException: If the YAML data is invalid or the class cannot be found.
        """
        if isinstance(yaml, str):
            name = yaml
        else:
            name = next(iter(yaml.keys()))
        if name not in cls.classes:
            raise SudokuException(f"Unknown item class {name}")
        print(f"\n\nCreate {cls.__name__} {name} {yaml}\n\n")
        clazz = cls.classes[name]
        return clazz.create2(board, yaml)

    @property
    def top(self) -> 'Item':
        """Get the top-most item in the hierarchy.

        Returns:
            Item: The top-most item.
        """
        if self.parent is None:
            return self
        return self.parent.top

    def regions(self) -> set['Item']:
        """Get the set of items used in this item.

        Returns:
            Set[Item]: A set of items used by this item.
        """
        return {self}

    def svg(self) -> Glyph | None:
        """Return an SVG glyph to represent this item.

        Returns:
            Glyph | None: An SVG glyph for the item or None if not needed.
        """
        return None

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules that apply to this item.

        Returns:
            list[Rule]: A list of rules.
        """
        return []

    def flatten(self) -> list['Item']:
        """Flatten the item hierarchy into a list.

        Returns:
            list[Item]: A list of items in the hierarchy.
        """
        return [self]

    @property
    def sorted_unique_rules(self) -> list[Rule]:
        """Return unique, sorted rules that apply to this item.

        Returns:
            list[Rule]: A sorted list of unique rules.
        """
        return sorted(list(set(self.rules)))

    def glyphs(self) -> list[Glyph]:
        """Return a list of SVG glyphs for this item.

        Returns:
            list[Glyph]: A list of SVG glyphs.
        """
        return []

    def sorted_glyphs(self) -> Glyph:
        """Return a composed SVG glyph for this item.

        Returns:
            Glyph: A composed SVG glyph.
        """
        return ComposedGlyph('Composed', sorted(self.glyphs()))

    @property
    def name(self) -> str:
        """Return the name of the item, including its class name and identity.

        Returns:
            str: The name of the item.
        """
        return f"{self.__class__.__name__}_{self.identity}"

    @property
    def tags(self) -> set[str]:
        """Return a set of tags associated with this item.

        Returns:
            set[str]: A set of tags.
        """
        return set()

    def walk(self) -> Iterator['Item']:
        """Yield each item in the tree rooted at the current item.

        Yields:
            Item: The current item and recursively each item in the tree.
        """
        yield self

    @property
    def used_classes(self) -> set[Type['Item']]:
        """Return a set of classes used by this item.

        Returns:
            Set[Type[Item]]: A set of class types used by this item.
        """
        result = set(self.__class__.__mro__)
        for item in self.walk():
            result |= set(item.__class__.__mro__)
        return result.difference({object})

    @staticmethod
    def select_all(_: 'Item') -> bool:
        """Return True to select all items for inclusion in the model.

        Args:
            _: The item to be checked (not used in this method).

        Returns:
            bool: Always returns True, indicating all items are selected.
        """
        return True

    def __repr__(self) -> str:
        """Return a string representation of this item.

        Returns:
            str: A string representation of the item.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add a constraint to the solver.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """

    def bookkeeping(self) -> None:
        """Perform bookkeeping for this item."""

    def add_bookkeeping_constraint(self, solver: PulpSolver) -> None:
        """Add bookkeeping constraints for the item to the solver.

        Args:
            solver (PulpSolver): The solver to which bookkeeping constraints will be added.
        """
        for item in self.walk():
            if item.__class__.__name__ != 'Cell':
                continue
            item.add_bookkeeping_constraint(solver)

    def marked_book(self) -> BookKeepingCell | None:
        """Return the bookkeeping object for this item, or None.

        Returns:
            BookKeepingCell | None: The bookkeeping object, or None.
        """
        return None

    # pylint: disable=loop-invariant-statement
    def bookkeeping_unique(self) -> bool:
        """Check if all bookkeeping items in the hierarchy are unique.

        Returns:
            bool: True if all marked books are unique, False otherwise.
        """
        marked_books: list[BookKeepingCell] = []
        for item in self.walk():
            marked_book: BookKeepingCell | None = item.marked_book()
            if marked_book is not None:
                marked_books.append(marked_book)
        return all(marked_book.is_unique() for marked_book in marked_books)

    def to_dict(self) -> dict:
        """Convert the item to a dictionary for YAML dumping.

        Returns:
            dict: A dictionary representing the item.
        """
        return {self.__class__.__name__: None}

    def css(self) -> dict:
        """Return the CSS styles for this item.

        Returns:
            dict: A dictionary containing CSS styles.
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
    def css_text(data: dict, indent: int = 0) -> str:
        """Convert a dictionary of CSS rules to a string.

        Args:
            data (dict): A dictionary of CSS rules.
            indent (int, optional): The number of spaces to indent each line. Defaults to 0.

        Returns:
            str: A string representing the CSS rules.
        """
        tab = '    '
        result = ""
        spacer: str = tab * indent
        for k in sorted(data.keys()):
            v = data[k]
            if isinstance(v, dict):
                result += f"{spacer}{k} {{\n"
                result += Item.css_text(v, indent + 1)
                result += f"{spacer}}}\n\n"
            else:
                result += f"{spacer}{k}: {v};\n"
        return result
