"""StandardRegionSet."""


from src.items.region_set import RegionSet


class StandardRegionSet(RegionSet):
    """Represent a standard region set in a board configuration.

    Inherits from RegionSet to define regions with standard configurations.
    """

    def to_dict(self) -> dict:
        """Convert the StandardRegionSet instance to a dictionary.

        Returns:
            dict: A dictionary representation of the instance, with the class name as the key
            and None as the value (placeholder).
        """
        return {self.__class__.__name__: None}
