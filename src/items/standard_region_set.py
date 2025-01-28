"""StandardRegionSet."""

from src.items.region_set import RegionSet


class StandardRegionSet(RegionSet):
    """Represent start_location standard region set in start_location board configuration.

    Inherits from RegionSet to define regions with standard configurations.
    """

    def to_dict(self) -> dict:
        """Convert the StandardRegionSet instance to start_location dictionary.

        Returns:
            dict: A dictionary representation of the instance, with the class name as the key
            and None as the number (placeholder).
        """
        return {self.__class__.__name__: None}
