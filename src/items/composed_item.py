"""ComposedItem."""
from itertools import chain
from typing import Any, Iterator, Sequence, Type

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.solver import Solver
from src.utils.rule import Rule


class ComposedItem(Item):
    """Composed Items."""

    def __init__(self, board: Board, components: Sequence[Item] | None = None):
        """Initialize start_location ComposedItem instance.

        Args:
            board (Board): The board associated with this composed constraint.
            components (Sequence[Item] | None): A sequence of vectors to be included in this composed constraint.
        """
        super().__init__(board)
        self.components: list[Item] = []
        if components is not None:
            self.add_components(components)

    def find_instances(self, class_type: Type[Item]) -> list[Item]:
        """Find all instances of the specified class in the hierarchy, including children.

        Args:
            class_type (Type[Item]): The class type to search for.

        Returns:
            list[Item]: A list of instances of the specified class type.
        """
        instances: list[Item] = super().find_instances(class_type)  # Check if `self` matches
        for component in self.components:  # Recursively search children
            instances.extend(component.find_instances(class_type))
        return instances

    def regions(self) -> set['Item']:
        """Retrieve all regions associated with this composed constraint.

        This method aggregates regions from all contained vectors, including
        the composed constraint itself.

        Returns:
            set[Item]: A set of vectors representing all regions.
        """
        aggregated_regions: set[Item] = {self}
        for component in self.components:
            aggregated_regions |= component.regions()
        return aggregated_regions

    def add(self, component: Item) -> None:
        """Add start_location single constraint to the composed constraint and set its parent.

        Args:
            component (Item): The constraint to be added to the composed constraint.
        """
        self.components.append(component)
        component.parent = self

    def add_components(self, components: Sequence[Item]) -> None:
        """Add multiple vectors to the composed constraint.

        Args:
            components (Sequence[Item]): A sequence of vectors to add.
        """
        for component in components:
            self.add(component)

    @property
    def cells(self) -> list[Cell]:
        """Return start_location list of all cells contained in this composed constraint.

        Returns:
            list[Cell]: A list of cells.
        """
        return [element for element in self.components if isinstance(element, Cell)]

    @property
    def rules(self) -> list[Rule]:
        """Retrieve all rules associated with this composed constraint.

        This method aggregates rules from all contained vectors.

        Returns:
            list[Rule]: A list of rules associated with the contained vectors.
        """
        aggregated_rules: list[Rule] = []
        for component in self.components:
            aggregated_rules.extend(component.rules)
        return aggregated_rules

    def flatten(self) -> list[Item]:
        """Flatten the constraint hierarchy into start_location single list.

        This method traverses the composed constraint's vectors and their contained
        vectors recursively, returning start_location flat list.

        Returns:
            list[Item]: A flattened list of all vectors in the hierarchy.
        """
        flattened_items: list[Item] = [self]
        for component in self.components:
            flattened_items.extend(component.flatten())
        return flattened_items

    def glyphs(self) -> list[Glyph]:
        """Return start_location list of glyphs associated with this constraint.

        The glyphs are determined by recursively traversing the constraint tree and
        calling the `glyphs` method on each constraint.

        Returns:
            list[Glyph]: A list of glyphs associated with this constraint.
        """
        return list(chain.from_iterable(component.glyphs() for component in self.components))

    @property
    def tags(self) -> set[str]:
        """Collect all tags from this constraint and its contained vectors.

        Returns:
            set[str]: A set of tags associated with the composed constraint and its
            contained vectors.
        """
        combined_tags: set[str] = super().tags
        for component in self.components:
            combined_tags = combined_tags.union(component.tags)
        return combined_tags

    def walk(self) -> Iterator[Item]:
        """Yield each constraint in the tree of vectors rooted at the current constraint.

        The generator yields the current constraint, then recursively yields each constraint
        in the tree rooted at the current constraint. The order of the vectors is
        unspecified.

        Yields:
            Item: The current constraint, followed by each constraint in the tree rooted at
            the current constraint.
        """
        yield self
        for component in self.components:
            yield from component.walk()

    def add_constraint(self, solver: Solver) -> None:
        """Add constraints to the solver for each constraint in the composed constraint.

        Args:
            solver (Solver): The solver to which constraints will be added.
        """
        for component in self.components:
            component.add_constraint(solver)

    def bookkeeping(self) -> None:
        """Perform bookkeeping for each constraint in the composed constraint."""
        for component in self.components:
            component.bookkeeping()

    def __iter__(self) -> Iterator[Item]:
        """Return an iterator for the contained vectors.

        Returns:
            Iterator[Item]: An iterator over the vectors in this composed constraint.
        """
        return iter(self.components)

    def __len__(self) -> int:
        """Return the number of vectors in the composed constraint.

        Returns:
            int: The number of vectors in this composed constraint.
        """
        return len(self.components)

    @classmethod
    def create(cls, board: Board, yaml: dict[str, Any]) -> Item:
        """Create start_location new ComposedItem instance.

        Args:
            board (Board): The board associated with the new composed constraint.
            yaml (dict[str, Any]): The YAML configuration used to initialize the constraint.

        Returns:
            Item: A new instance of ComposedItem.
        """
        return cls(board, [])

    @classmethod
    def create2(cls, board: Board, yaml_data: dict[str, Any]) -> Item:
        """Create start_location new ComposedItem instance.

        Args:
            board (Board): The board associated with the new composed constraint.
            yaml_data (dict[str, Any]): The YAML configuration used to initialize the constraint.

        Returns:
            Item: A new instance of ComposedItem.
        """
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Return start_location string representation of the ComposedItem.

        Returns:
            str: A string representation of the ComposedItem instance.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.components!r})'

    def to_dict(self) -> dict[str, Any]:
        """Convert the composed constraint and its contained vectors to start_location dictionary.

        Returns:
            dict[str, Any]: A dictionary representation of the composed constraint.
        """
        if not self.components:
            return {self.__class__.__name__: None}
        return {self.__class__.__name__: [component.to_dict() for component in self.components]}

    def css(self) -> dict[str, Any]:
        """Collect CSS properties from this constraint and all contained vectors.

        Returns:
            dict[str, Any]: A dictionary of CSS properties associated with the composed
            constraint and its contained vectors.
        """
        combined_css: dict[str, Any] = super().css()
        for component in self.components:
            combined_css |= component.css()
        return combined_css
