from abc import ABC, abstractmethod

from src.items.anti import AntiKnight, Anti, AntiKing, Item
from src.items.cell import Cell, Even, Odd, Fortress, Known
from src.items.composed import Composed
from src.items.diagonals import TLBR, BLTR
from src.items.knowns import Knowns
from src.items.line import Line, Palindromes, Thermometers
from src.items.palindrome import Palindrome
from src.items.thermometer import Thermometer, SimpleThermometer, FrozenThermometer
from src.items.arrow import Arrow
from src.items.renban import Renban
from src.items.little_killer import LittleKiller
from src.items.pair import Pair
from src.items.greater_than_pair import GreaterThanPair
from src.items.different_pair import DifferentPair
from src.items.xi_pair import XIPair
from src.items.vi_pair import VIPair
from src.items.consecutive_pair import ConsecutivePair
from src.items.v_pair import VPair
from src.items.x_pair import XPair
from src.items.difference_pair import DifferencePair
from src.items.kropki import KropkiPair
from src.items.board import Board
from src.items.region import Region, StandardRegion, Column, Row, Box, DisjointGroup, Window
from src.items.region_sets import RegionSet, StandardRegionSet, Columns, Rows, Boxes, DisjointGroups, Windows, \
    LittleKillers, Arrows
from src.items.solution import Solution


class Visitor(ABC):
    classes = {
        'Anti': 'anti',
        'AntiKing': 'anti_king',
        'AntiKnight': 'anti_knight',
        'Arrow': 'arrow',
        'BLTR': 'bltr',
        'Box': 'box',
        'Boxes': 'boxes',
        'Cell': 'cell',
        'Column': 'column',
        'Columns': 'columns',
        'Composed': 'composed',
        'ConsecutivePair': 'consecutive_pair',
        'DifferentPair': 'different_pair',
        'DisjointGroup': 'disjoint_group',
        'DisjointGroups': 'disjoint_groups',
        'Even': 'even',
        'FrozenThermo': 'frozen_thermo',
        'GreaterThanPair': 'greater_than_pair',
        'Item': 'item',
        'Known': 'known',
        'Knowns': 'knowns',
        'KropkiPair': 'kropki_pair',
        'Line': 'line',
        'LittleKiller': 'little_killer',
        'Odd': 'odd',
        'Pair': 'pair',
        'Palindrome': 'palindrome',
        'Problem': 'problem',
        'Region': 'region',
        'Renban': 'renban',
        'Row': 'row',
        'Rows': 'rows',
        'SimpleThermo': 'simple_thermo',
        'StandardRegion': 'standard_region',
        'TLBR': 'tlbr',
        'Thermo': 'thermo',
        'VIPair': 'vi_pair',
        'VPair': 'v_pair',
        'Window': 'window',
        'XIPair': 'xi_pair',
        'XPair': 'x_pair',
        'Palindromes': 'palindromes',
        'RegionSet': 'region_set',
        'Thermometers': 'thermometers',
        'Arrows': 'arrows',
        'Renbans': 'renbans',
        'Solution': 'solution',
        'Fortress': 'fortress',
        'Windows': 'windows',
        'DifferencePair': 'difference_pair',
        'LittleKillers': 'little_killers',
        'StandardRegionSet': 'standard_region_set'
    }

    @abstractmethod
    def region(self, item: Region) -> None:
        pass

    @abstractmethod
    def composed(self, item: Composed) -> None:
        pass

    @abstractmethod
    def thermo(self, item: Thermometer) -> None:
        pass

    @abstractmethod
    def pair(self, item: Pair) -> None:
        pass

    @abstractmethod
    def difference_pair(self, item: DifferencePair) -> None:
        pass

    @abstractmethod
    def line(self, item: Line) -> None:
        pass

    @abstractmethod
    def fortress(self, item: Fortress) -> None:
        pass

    @abstractmethod
    def greater_than_pair(self, item: GreaterThanPair) -> None:
        pass

    @abstractmethod
    def problem(self, item: Board) -> None:
        pass

    @abstractmethod
    def columns(self, item: Columns) -> None:
        pass

    @abstractmethod
    def rows(self, item: Rows) -> None:
        pass

    @abstractmethod
    def boxes(self, item: Boxes) -> None:
        pass

    @abstractmethod
    def row(self, item: Row) -> None:
        pass

    @abstractmethod
    def column(self, item: Column) -> None:
        pass

    @abstractmethod
    def box(self, item: Box) -> None:
        pass

    @abstractmethod
    def disjoint_group(self, item: DisjointGroup) -> None:
        pass

    @abstractmethod
    def disjoint_groups(self, item: DisjointGroups) -> None:
        pass

    @abstractmethod
    def knowns(self, item: Knowns) -> None:
        pass

    @abstractmethod
    def cell(self, item: Cell) -> None:
        pass

    @abstractmethod
    def even(self, item: Even) -> None:
        pass

    @abstractmethod
    def odd(self, item: Odd) -> None:
        pass

    @abstractmethod
    def known(self, item: Known) -> None:
        pass

    @abstractmethod
    def anti(self, item: Anti) -> None:
        pass

    @abstractmethod
    def anti_knight(self, item: AntiKnight) -> None:
        pass

    @abstractmethod
    def anti_king(self, item: AntiKing) -> None:
        pass

    @abstractmethod
    def different_pair(self, item: DifferentPair) -> None:
        pass

    @abstractmethod
    def tlbr(self, item: TLBR) -> None:
        pass

    @abstractmethod
    def bltr(self, item: BLTR) -> None:
        pass

    @abstractmethod
    def little_killer(self, item: LittleKiller) -> None:
        pass

    @abstractmethod
    def simple_thermo(self, item: SimpleThermometer) -> None:
        pass

    @abstractmethod
    def frozen_thermo(self, item: FrozenThermometer) -> None:
        pass

    @abstractmethod
    def arrow(self, item: Arrow) -> None:
        pass

    @abstractmethod
    def renban(self, item: Renban) -> None:
        pass

    @abstractmethod
    def palindrome(self, item: Palindrome) -> None:
        pass

    @abstractmethod
    def window(self, item: Window) -> None:
        pass

    @abstractmethod
    def greater_than_pair(self, item: GreaterThanPair) -> None:
        pass

    @abstractmethod
    def kropki_pair(self, item: KropkiPair) -> None:
        pass

    @abstractmethod
    def different_pair(self, item: DifferentPair) -> None:
        pass

    @abstractmethod
    def x_pair(self, item: XPair) -> None:
        pass

    @abstractmethod
    def xi_pair(self, item: XIPair) -> None:
        pass

    @abstractmethod
    def v_pair(self, item: VPair) -> None:
        pass

    @abstractmethod
    def vi_pair(self, item: VIPair) -> None:
        pass

    @abstractmethod
    def consecutive_pair(self, item: ConsecutivePair) -> None:
        pass

    @abstractmethod
    def item(self, item: Item) -> None:
        pass

    @abstractmethod
    def standard_region(self, item: StandardRegion) -> None:
        pass

    def palindromes(self, item: Palindromes) -> None:
        pass

    def region_set(self, item: RegionSet) -> None:
        pass

    def thermometers(self, item: Thermometers) -> None:
        pass

    def arrows(self, item: Arrows) -> None:
        pass

    def solution(self, item: Solution) -> None:
        pass

    def fortress(self, item: Fortress) -> None:
        pass

    def windows(self, item: Windows) -> None:
        pass

    def difference_pair(self, item: DifferencePair) -> None:
        pass

    def little_killers(self, item: LittleKillers) -> None:
        pass

    def standard_region_set(self, item: StandardRegionSet) -> None:
        pass
