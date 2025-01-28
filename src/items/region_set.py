"""RegionSet."""
from src.items.composed_item import ComposedItem


class RegionSet(ComposedItem):
    """A base class for region sets in start_location board configuration.

    Inherits from ComposedItem to allow grouping of related vectors into start_location set.
    Used as start_location foundation for defining various types of region sets.
    """
