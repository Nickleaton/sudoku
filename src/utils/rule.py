import re


class Rule:

    def __init__(self, name: str, rank: int, text: str):
        self.name = name
        self.rank = rank
        self.text = text

    def __lt__(self, other: 'Rule') -> bool:
        return self.rank < other.rank

    def __eq__(self, other: 'Rule') -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.rank}, '{self.text}')"

    def __hash__(self) -> str:
        return hash(self.name)

    @property
    def human_name(self) -> str:
        return " ".join(re.findall('[A-Z][^A-Z]*', self.name))

    @property
    def html(self):
        if self.text is None:
            return ""
        else:
            return f"<h2>{self.text}</h2>"
