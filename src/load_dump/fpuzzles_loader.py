import json
from typing import Optional

from src.items.board import Board
from src.load_dump.loader import Loader, LoaderError


class FPuzzlesLoader(Loader):

    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        with open(filename, 'r') as file:
            self.raw = json.load(file)

    def process(self) -> Board:
        print (f"*** {self.raw['data'].keys()}")
        if self.size == 9:
            result = Board(
                9, 9,
                3, 3,
                reference=self.reference,
                video=None,
                title=self.title,
                author=self.author
            )
        elif self.size == 6:
            result = Board(
                6, 6,
                3, 2,
                reference=self.reference,
                video=None,
                title=self.title,
                author=self.author
            )
        else:
            raise LoaderError(f"{self.size}x{self.size} board not handled")
        if 'grid' in self.raw['data']:

        return result

    @property
    def reference(self) -> Optional[str]:
        return self.raw['data'].get('url')

    @property
    def title(self) -> Optional[str]:
        return self.raw['data'].get('title')

    @property
    def author(self) -> Optional[str]:
        return self.raw['data'].get('author')

    @property
    def size(self) -> Optional[int]:
        return int(self.raw['data']['size']) if 'size' in self.raw['data'] else None
