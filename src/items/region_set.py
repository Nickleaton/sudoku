"""RegionSet."""
from src.items.composed_item import ComposedItem


class RegionSet(ComposedItem):
    """A base class for region sets in start board configuration.

    Inherits from ComposedItem to allow grouping of related vectors into start set.
    Used as start foundation for defining various types of region sets.
    """
