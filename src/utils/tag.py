class TagException(Exception):
    pass


class Tag:

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Tag):
            return self.name == other.name
        raise TagException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Tag):
            return self.name < other.name
        raise TagException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __le__(self, other: object) -> bool:
        if isinstance(other, Tag):
            return self.name <= other.name
        raise TagException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"
