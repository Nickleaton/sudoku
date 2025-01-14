"""Item."""

from typing import Iterator, Type

import strictyaml

from src.board.board import Board
from src.board.book_keeping_cell import BookKeepingCell
from src.glyphs.composed_glyph import ComposedGlyph
from src.glyphs.glyph import Glyph
from src.parsers.none_parser import NoneParser
from src.parsers.parser import Parser
from src.solvers.pulp_solver import PulpSolver
from src.utils.config import Config
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException
from src.validators.validator import Validator

config = Config()


class Item:  # noqa: WPS110
    """Top-level class for the Item hierarchy.

    Items generate the constraints, manage bookkeeping, and generate SVG for viewing problems and solutions.
    They are created via the create method.
    """

    # Class Variables
    classes: dict[str, Type['Item']] = {}
    counter: int = 0

    # Creation Routines

    def __init_subclass__(cls, **kwargs):
        """Register the subclass to the `Item` class hierarchy.

        Args:
            kwargs: Any additional keyword arguments passed to the method (not used).
        """
        super().__init_subclass__(**kwargs)
        Item.classes[cls.__name__] = cls
        Item.classes['Item'] = Item

    def __init__(self, board: Board):
        """Initialize an Item with start given board.

        Args:
            board (Board): The board that this constraint belongs to.
        """
        super().__init__()
        if Item.__name__ not in Item.classes:
            Item.classes[Item.__name__] = Item

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
            yaml (dict): The YAML line to create the constraint.

        Returns:
            Item: The created instance of the constraint.

        Raises:
            SudokuException: If the YAML line is invalid or the class cannot be found.
        """
        if isinstance(yaml, str):
            name = yaml
        else:
            name = next(iter(yaml.keys()))
        if name not in cls.classes:
            raise SudokuException(f'Unknown constraint class {name}')
        clazz = cls.classes[name]
        return clazz.create(board, yaml)

    @classmethod
    def create2(cls, board: Board, yaml: dict) -> 'Item':
        """Create an instance of the constraint from start YAML dictionary.

        Args:
            board (Board): The board this constraint belongs to.
            yaml (dict): The YAML line to create the constraint.

        Returns:
            Item: The created instance of the constraint.

        Raises:
            SudokuException: If the YAML line is invalid or the class cannot be found.
        """
        if isinstance(yaml, str):
            name = yaml
        else:
            name = next(iter(yaml.keys()))
        if name not in cls.classes:
            raise SudokuException(f'Unknown constraint class {name}')
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
        return list(set(self.rules))

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
        return f'{self.__class__.__name__}_{self.identity}'

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
    def used_classes(self) -> set[type['Item']]:
        """Get the set of classes used by this constraint.

        Returns:
            set[type[Item]]: A set of class types used by this constraint.
        """
        class_hierarchy: set[type[Item]] = set(self.__class__.__mro__)  # Classes in the MRO of the current object
        for constraint in self.walk():
            class_hierarchy |= set(constraint.__class__.__mro__)  # Add MRO of each item
        return class_hierarchy.difference({object})  # Exclude the base 'object' class

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
        return f'{self.__class__.__name__}({self.board!r})'

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
        for constraint in self.walk():
            if constraint.__class__.__name__ != 'Cell':
                continue
            constraint.add_bookkeeping_constraint(solver)

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
        for constraint in self.walk():
            marked_book: BookKeepingCell | None = constraint.marked_book()
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
                'font-weight': 'bolder',
            },
            '.TextGlyphBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
            'LittleNumber': {
                'font-size': '20px',
                'stroke': 'black',
            },
        }

    @staticmethod
    def css_text(rules: dict[str, str | dict]) -> str:
        """Convert a dictionary of CSS rules to a formatted CSS string.

        Args:
            rules (dict[str, str | dict]): A dictionary of CSS rules where keys are selectors or properties
                                           and cell_values are either property cell_values or nested rule dictionaries.

        Returns:
            str: A formatted CSS string representation of the rules.
        """
        spacer: str = ' ' * config.css_indent_count
        css_lines: list[str] = []  # List to collect CSS lines

        sorted_rules = sorted(rules.items())  # Sort items upfront for clarity
        for key, rule_value in sorted_rules:
            if isinstance(rule_value, dict):
                css_lines.append(f'{spacer}{key} {{')
                css_lines.append(Item.css_text(rule_value))
                css_lines.append(f'{spacer}}}\n')
            else:
                css_lines.append(f'{spacer}{key}: {rule_value};')

        return '\n'.join(css_lines)
