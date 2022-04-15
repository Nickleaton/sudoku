import re


class Rule:

    def __init__(self, name: str, rank: int, text: str):
        self.name = name
        self.rank = rank
        self.text = text

    def __lt__(self, other: 'Rule') -> bool:
        return self.rank < other.rank

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rule):
            return self.name == other.name
        raise Exception(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.rank}, '{self.text}')"

    def __hash__(self) -> int:
        return hash(self.name)

    @property
    def human_name(self) -> str:
        return " ".join(re.findall('[A-Z][^A-Z]*', self.name))

    @property
    def html(self) -> str:
        if self.text is None:
            return ""
        else:
            return f"<h2>{self.text}</h2>"
