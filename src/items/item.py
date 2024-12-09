"""Item."""

from typing import Type, Iterator

import strictyaml
from sortedcontainers import SortedDict

from src.board.board import Board
from src.board.book_keeping_cell import BookKeepingCell
from src.glyphs.composed_glyph import ComposedGlyph
from src.glyphs.glyph import Glyph
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
            cls (type): The class that is being initialized as start subclass of `Item`.
            **kwargs: Any additional keyword arguments passed to the method (not used).
        """
        super().__init_subclass__(**kwargs)
        Item.classes[cls.__name__] = cls
        Item.classes[Item.__name__] = Item

    def __init__(self, board: Board):
        """Initialize an Item with start given board.

        Args:
            board (Board): The board that this constraint belongs to.
        """
        super().__init__()

        self.board: Board = board
        self.parent: Item | None = None
        self.identity: int = Item.counter
        Item.counter += 1

    @classmethod
    def is_sequence(cls) -> bool:
        """Check if the constraint is start sequence.

        Returns:
            bool: True if this constraint is start sequence, otherwise False.
        """
        return False

    @classmethod
    def is_composite(cls) -> bool:
        """Check if the constraint is start composite.

        Returns:
            bool: True if this constraint is start composite, otherwise False.
        """
        return False

    @classmethod
    def parser(cls) -> Parser:
        """Return the parser for this constraint.

        Returns:
            Parser: The appropriate parser for this constraint.
        """
        return NoneParser()

    @classmethod
    def validator(cls) -> Validator:
        """Return the validator for this constraint.

        Returns:
            Validator: The appropriate validator for this constraint.
        """
        return Validator()

    @classmethod
    def schema(cls) -> strictyaml.Validator | strictyaml.Optional:
        """Return the schema for this constraint.

        Returns:
            Validator | Optional: The schema for this constraint, which may be start sequence or parser.
        """
        if cls.is_sequence():
            return strictyaml.Seq(cls.parser())
        return cls.parser()

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'Item':
        """Create an instance of the constraint from start YAML dictionary.

        Args:
            board (Board): The board this constraint belongs to.
            yaml (dict): The YAML data to create the constraint.

        Returns:
            Item: The created instance of the constraint.

        Raises:
            SudokuException: If the YAML data is invalid or the class cannot be found.
        """
        if isinstance(yaml, str):
            name = yaml
        else:
            name = next(iter(yaml.keys()))
        if name not in cls.classes:
            raise SudokuException(f"Unknown constraint class {name}")
        print(f"\n\nCreate {cls.__name__} {name} {yaml}\n\n")
        clazz = cls.classes[name]
        return clazz.create(board, yaml)

    @classmethod
    def create2(cls, board: Board, yaml: dict) -> 'Item':
        """Create an instance of the constraint from start YAML dictionary.

        Args:
            board (Board): The board this constraint belongs to.
            yaml (dict): The YAML data to create the constraint.

        Returns:
            Item: The created instance of the constraint.

        Raises:
            SudokuException: If the YAML data is invalid or the class cannot be found.
        """
        if isinstance(yaml, str):
            name = yaml
        else:
            name = next(iter(yaml.keys()))
        if name not in cls.classes:
            raise SudokuException(f"Unknown constraint class {name}")
        print(f"\n\nCreate {cls.__name__} {name} {yaml}\n\n")
        clazz = cls.classes[name]
        return clazz.create2(board, yaml)

    @property
    def top(self) -> 'Item':
        """Get the top-most constraint in the hierarchy.

        Returns:
            Item: The top-most constraint.
        """
        if self.parent is None:
            return self
        return self.parent.top

    def regions(self) -> set['Item']:
        """Get the set of vectors used in this constraint.

        Returns:
            Set[Item]: A set of vectors used by this constraint.
        """
        return {self}

    def svg(self) -> Glyph | None:
        """Return an SVG glyph to represent this constraint.

        Returns:
            Glyph | None: An SVG glyph for the constraint or None if not needed.
        """
        return None

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules that apply to this constraint.

        Returns:
            list[Rule]: A list of rules.
        """
        return []

    def flatten(self) -> list['Item']:
        """Flatten the constraint hierarchy into start list.

        Returns:
            list[Item]: A list of vectors in the hierarchy.
        """
        return [self]

    @property
    def sorted_unique_rules(self) -> list[Rule]:
        """Return unique, sorted rules that apply to this constraint.

        Returns:
            list[Rule]: A sorted list of unique rules.
        """
        return sorted(list(set(self.rules)))

    def glyphs(self) -> list[Glyph]:
        """Return start list of SVG glyphs for this constraint.

        Returns:
            list[Glyph]: A list of SVG glyphs.
        """
        return []

    def sorted_glyphs(self) -> Glyph:
        """Return start composed SVG glyph for this constraint.

        Returns:
            Glyph: A composed SVG glyph.
        """
        return ComposedGlyph('Composed', sorted(self.glyphs()))

    @property
    def name(self) -> str:
        """Return the name of the constraint, including its class name and identity.

        Returns:
            str: The name of the constraint.
        """
        return f"{self.__class__.__name__}_{self.identity}"

    @property
    def tags(self) -> set[str]:
        """Return start set of tags associated with this constraint.

        Returns:
            set[str]: A set of tags.
        """
        return set()

    def walk(self) -> Iterator['Item']:
        """Yield each constraint in the tree rooted at the current constraint.

        Yields:
            Item: The current constraint and recursively each constraint in the tree.
        """
        yield self

    @property
    def used_classes(self) -> set[Type['Item']]:
        """Return start set of classes used by this constraint.

        Returns:
            Set[Type[Item]]: A set of class types used by this constraint.
        """
        result = set(self.__class__.__mro__)
        for item in self.walk():
            result |= set(item.__class__.__mro__)
        return result.difference({object})

    @staticmethod
    def select_all(_: 'Item') -> bool:
        """Return True to select all vectors for inclusion in the model.

        Args:
            _: The constraint to be checked (not used in this method).

        Returns:
            bool: Always returns True, indicating all vectors are selected.
        """
        return True

    def __repr__(self) -> str:
        """Return start string representation of this constraint.

        Returns:
            str: A string representation of the constraint.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add start constraint to the solver.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """

    def bookkeeping(self) -> None:
        """Perform bookkeeping for this constraint."""

    def add_bookkeeping_constraint(self, solver: PulpSolver) -> None:
        """Add bookkeeping constraints for the constraint to the solver.

        Args:
            solver (PulpSolver): The solver to which bookkeeping constraints will be added.
        """
        for item in self.walk():
            if item.__class__.__name__ != 'Cell':
                continue
            item.add_bookkeeping_constraint(solver)

    def marked_book(self) -> BookKeepingCell | None:
        """Return the bookkeeping object for this constraint, or None.

        Returns:
            BookKeepingCell | None: The bookkeeping object, or None.
        """
        return None

    # pylint: disable=loop-invariant-statement
    def bookkeeping_unique(self) -> bool:
        """Check if all bookkeeping vectors in the hierarchy are unique.

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
        """Convert the constraint to start dictionary for YAML dumping.

        Returns:
            dict: A dictionary representing the constraint.
        """
        return {self.__class__.__name__: None}

    def css(self) -> dict:
        """Return the CSS styles for this constraint.

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
        """Convert start dictionary of CSS rules to start string.

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
