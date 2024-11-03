from typing import List


class ColourSet:
    NAMES = [
        "red",
        "green",
        "blue",
        "yellow",
        "orange",
        "purple",
        "cyan",
        "magenta",
        "lightcyan",
        "powderblue",
        "greenyellow",
        "blueviolet",
        "thistle",
        "salmon",
        "steelblue",
        "olive",
    ]

    @staticmethod
    def colours(n: int) -> List[str]:
        """Returns the first n color names from the list."""
        return ColourSet.NAMES[0:n]
