from pydotted import pydot


class Tags(pydot):
    def __init__(self, data: dict):
        super().__init__(data)

    def __eq__(self, other):
        if not isinstance(other, Tags):
            return NotImplemented
        return self.to_dict() == other.to_dict()

    def to_dict(self):
        """Convert the Tags object back to a dictionary for comparison."""
        return {key: self[key] for key in self.keys()}
