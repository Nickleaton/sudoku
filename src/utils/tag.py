class Tag:

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Tag):
            return self.name == other.name
        raise Exception(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __lt__(self, other: 'Tag') -> bool:
        return self.name < other.name

    def __le__(self, other: 'Tag') -> bool:
        return self.name <= other.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"
