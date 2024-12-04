"""ComposedItem."""
from itertools import chain
from typing import Sequence, Iterator

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class ComposedItem(Item):
    """Composed Items."""

    def __init__(self, board: Board, items: Sequence[Item]):
        """Initialize a ComposedItem instance.

        Args:
            board (Board): The board associated with this composed item.
            items (Sequence[Item]): A sequence of items to be included in this composed item.
        """
        super().__init__(board)
        self.items: list[Item] = []
        self.add_items(items)

    def regions(self) -> set['Item']:
        """Retrieve all regions associated with this composed item.

        This method aggregates regions from all contained items, including
        the composed item itself.

        Returns:
            set[Item]: A set of items representing all regions.
        """
        result: set[Item] = {self}
        for item in self.items:
            result |= item.regions()
        return result

    def add(self, item: Item):
        """Add a single item to the composed item and set its parent.

        Args:
            item (Item): The item to be added to the composed item.
        """
        self.items.append(item)
        item.parent = self

    def add_items(self, items: Sequence[Item]):
        """Add multiple items to the composed item.

        Args:
            items (Sequence[Item]): A sequence of items to add.
        """
        for item in items:
            self.add(item)

    @property
    def cells(self) -> list[Cell]:
        """Return a list of all cells contained in this composed item.

        Returns:
            list[Cell]: A list of cells.
        """
        return [item for item in self.items if isinstance(item, Cell)]

    @property
    def rules(self) -> list[Rule]:
        """Retrieve all rules associated with this composed item.

        This method aggregates rules from all contained items.

        Returns:
            list[Rule]: A list of rules associated with the contained items.
        """
        result = []
        for item in self.items:
            result.extend(item.rules)
        return result

    def flatten(self) -> list[Item]:
        """Flatten the item hierarchy into a single list.

        This method traverses the composed item's items and their contained
        items recursively, returning a flat list.

        Returns:
            list[Item]: A flattened list of all items in the hierarchy.
        """
        result: list[Item] = [self]
        for item in self.items:
            result.extend(item.flatten())
        return result

    def glyphs(self) -> list[Glyph]:
        """Return a list of glyphs associated with this item.

        The glyphs are determined by recursively traversing the item tree and
        calling the `glyphs` method on each item.

        Returns:
            list[Glyph]: A list of glyphs associated with this item.
        """
        return list(chain.from_iterable(item.glyphs() for item in self.items))

    @property
    def tags(self) -> set[str]:
        """Collect all tags from this item and its contained items.

        Returns:
            set[str]: A set of tags associated with the composed item and its
            contained items.
        """
        result = super().tags
        for item in self.items:
            result = result.union(item.tags)
        return result

    def walk(self) -> Iterator[Item]:
        """Yield each item in the tree of items rooted at the current item.

        The generator yields the current item, then recursively yields each item
        in the tree rooted at the current item. The order of the items is
        unspecified.

        Yields:
            Item: The current item, followed by each item in the tree rooted at
            the current item.
        """
        yield self
        for item in self.items:
            yield from item.walk()

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for each item in the composed item.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
        """
        for item in self.items:
            item.add_constraint(solver)

    def bookkeeping(self) -> None:
        """Perform bookkeeping for each item in the composed item."""
        for item in self.items:
            item.bookkeeping()

    def __iter__(self):
        """Return an iterator for the contained items.

        Returns:
            Iterator[Item]: An iterator over the items in this composed item.
        """
        return iter(self.items)

    def __len__(self) -> int:
        """Return the number of items in the composed item.

        Returns:
            int: The number of items in this composed item.
        """
        return len(self.items)

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a new ComposedItem instance.

        Args:
            board (Board): The board associated with the new composed item.
            yaml (dict): The YAML configuration used to initialize the item.

        Returns:
            Item: A new instance of ComposedItem.
        """
        return cls(board, [])

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Return a string representation of the ComposedItem.

        Returns:
            str: A string representation of the ComposedItem instance.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.items!r})"

    def to_dict(self) -> dict:
        """Convert the composed item and its contained items to a dictionary.

        Returns:
            dict: A dictionary representation of the composed item.
        """
        if len(self.items) == 0:
            return {self.__class__.__name__: None}
        return {self.__class__.__name__: [item.to_dict() for item in self.items]}

    def css(self) -> dict:
        """Collect CSS properties from this item and all contained items.

        Returns:
            dict: A dictionary of CSS properties associated with the composed
            item and its contained items.
        """
        result = super().css()
        for item in self.items:
            result |= item.css()
        return result
