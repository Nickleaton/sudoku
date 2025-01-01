"""ConfigSchema. Autogenerated."""

from strictyaml import Map, Optional, Seq, Str

from src.parsers.cell_list_parser import CellListParser
from src.parsers.cell_pair_equal_value_parser import CellPairEqualValueParser
from src.parsers.cell_pairs_parser import CellPairsParser
from src.parsers.cell_parser import CellParser
from src.parsers.cell_value_parser import CellValueParser
from src.parsers.digit_parser import DigitParser
from src.parsers.digits_parser import DigitsParser
from src.parsers.frame_parser import FrameParser
from src.parsers.known_parser import KnownParser
from src.parsers.little_killer_parser import LittleKillerParser
from src.parsers.none_parser import NoneParser
from src.parsers.quadruples_parser import QuadruplesParser
from src.parsers.rossini_parser import RossiniParser
from src.parsers.solution_parser import SolutionParser

problem_schema = Map(
    {
        'Board': Map(
            {
                'Board': Str(),
                Optional('Box'): Str(),
                Optional('Tags'): Map(
                    {
                        Optional('Title'): Str(),
                        Optional('Reference'): Str(),
                        Optional('Video'): Str(),
                        Optional('Author'): Str(),
                    }
                ),
            }
        ),
        'Constraints': Map(
            {
                Optional('Cell'): NoneParser(),
                Optional('Item'): NoneParser(),
                Optional('ComposedItem'): NoneParser(),
                Optional('Region'): NoneParser(),
                Optional('Pair'): Seq(CellPairsParser()),
                Optional('DifferencePair'): Seq(CellPairsParser()),
                Optional('Anti'): NoneParser(),
                Optional('Diagonal'): NoneParser(),
                Optional('AntiDiagonal'): NoneParser(),
                Optional('AntiBLTR'): NoneParser(),
                Optional('AntiKing'): NoneParser(),
                Optional('AntiKnight'): NoneParser(),
                Optional('AntiMonkey'): NoneParser(),
                Optional('AntiQueens'): DigitsParser(),
                Optional('FirstN'): Seq(FrameParser()),
                Optional('Rossini'): Seq(RossiniParser()),
                Optional('AntiRossini'): Seq(FrameParser()),
                Optional('AntiTLBR'): NoneParser(),
                Optional('SpecialRegion'): NoneParser(),
                Optional('Asterix'): NoneParser(),
                Optional('Battenburg'): CellListParser(),
                Optional('Line'): Seq(CellListParser()),
                Optional('BetweenLine'): Seq(CellListParser()),
                Optional('StandardDiagonal'): NoneParser(),
                Optional('BLTR'): NoneParser(),
                Optional('StandardRegion'): NoneParser(),
                Optional('Box'): DigitParser(),
                Optional('RegionSet'): NoneParser(),
                Optional('StandardRegionSet'): NoneParser(),
                Optional('Boxes'): NoneParser(),
                Optional('CellReference'): Seq(CellParser()),
                Optional('Product'): Seq(CellValueParser()),
                Optional('CenterProduct'): Seq(CellValueParser()),
                Optional('ClonedRegion'): NoneParser(),
                Optional('Column'): DigitParser(),
                Optional('Indexer'): DigitsParser(),
                Optional('ColumnIndexer'): DigitsParser(),
                Optional('Columns'): NoneParser(),
                Optional('LEDifferencePair'): Seq(CellPairsParser()),
                Optional('ConsecutivePair'): Seq(CellPairsParser()),
                Optional('Constraints'): NoneParser(),
                Optional('DifferenceLine'): Seq(CellListParser()),
                Optional('DisjointGroup'): DigitParser(),
                Optional('DisjointGroups'): NoneParser(),
                Optional('RenbanLine'): Seq(CellListParser()),
                Optional('DistinctRenbanLine'): Seq(CellListParser()),
                Optional('FixedPair'): Seq(CellPairEqualValueParser()),
                Optional('FixedDifferencePair'): Seq(CellPairEqualValueParser()),
                Optional('GEDifferencePair'): Seq(CellPairEqualValueParser()),
                Optional('Row'): DigitParser(),
                Optional('GEDifferenceLine'): Seq(CellListParser()),
                Optional('DutchWhisperLine'): Seq(CellListParser()),
                Optional('EntropicLine'): Seq(CellListParser()),
                Optional('EqualSumLine'): Seq(CellListParser()),
                Optional('SimpleCellReference'): Seq(CellParser()),
                Optional('EvenCell'): Seq(CellParser()),
                Optional('Exclusion'): Seq(CellValueParser()),
                Optional('FixedProductPair'): Seq(CellPairEqualValueParser()),
                Optional('VariablePair'): Seq(CellPairsParser()),
                Optional('FixedRatioPair'): Seq(CellPairsParser()),
                Optional('FortressCell'): Seq(CellParser()),
                Optional('Frame'): Seq(FrameParser()),
                Optional('FrameProduct'): Seq(FrameParser()),
                Optional('ThermometerLine'): Seq(CellListParser()),
                Optional('FrozenThermometerLine'): Seq(CellListParser()),
                Optional('GermanWhisperLine'): Seq(CellListParser()),
                Optional('Girandola'): NoneParser(),
                Optional('GreaterThanPair'): Seq(CellPairsParser()),
                Optional('HighCell'): Seq(CellParser()),
                Optional('Killer'): NoneParser(),
                Optional('Knight'): DigitsParser(),
                Optional('KnownCell'): Seq(CellParser()),
                Optional('LowCell'): Seq(CellParser()),
                Optional('MidCell'): Seq(CellParser()),
                Optional('OddCell'): Seq(CellParser()),
                Optional('Known'): Seq(KnownParser()),
                Optional('KropkiPair'): Seq(CellPairsParser()),
                Optional('LEDifferenceLine'): Seq(CellListParser()),
                Optional('LittleKiller'): Seq(LittleKillerParser()),
                Optional('LockOutLine'): Seq(CellListParser()),
                Optional('MagicSquare'): Seq(CellParser()),
                Optional('MaxArrowLine'): Seq(CellListParser()),
                Optional('MinMaxDifference'): Seq(FrameParser()),
                Optional('MinMaxSum'): Seq(FrameParser()),
                Optional('Mote'): NoneParser(),
                Optional('MountainLine'): Seq(CellListParser()),
                Optional('NumberedRoom'): Seq(FrameParser()),
                Optional('OrthogonalProduct'): Seq(CellValueParser()),
                Optional('OrthogonallyAdjacent'): NoneParser(),
                Optional('Outside'): Seq(FrameParser()),
                Optional('PalindromeLine'): Seq(CellListParser()),
                Optional('PencilMarkCell'): Seq(CellParser()),
                Optional('ProductArrowLine'): Seq(CellListParser()),
                Optional('Puzzle'): NoneParser(),
                Optional('Quadro'): NoneParser(),
                Optional('QuadrupleBase'): Seq(QuadruplesParser()),
                Optional('QuadrupleExclude'): Seq(QuadruplesParser()),
                Optional('QuadrupleInclude'): Seq(QuadruplesParser()),
                Optional('RowIndexer'): DigitsParser(),
                Optional('Rows'): NoneParser(),
                Optional('Sandwich'): Seq(FrameParser()),
                Optional('SequenceLine'): Seq(CellListParser()),
                Optional('SimpleThermometerLine'): Seq(CellListParser()),
                Optional('SumArrowLine'): Seq(CellListParser()),
                Optional('SumPair'): Seq(CellPairsParser()),
                Optional('TLBR'): NoneParser(),
                Optional('TLBRReflecting'): NoneParser(),
                Optional('UniqueRegion'): NoneParser(),
                Optional('VPair'): Seq(CellPairsParser()),
                Optional('VariableDifferencePair'): Seq(CellPairsParser()),
                Optional('VariableProductPair'): Seq(CellPairsParser()),
                Optional('VariableRatioPair'): Seq(CellPairsParser()),
                Optional('VariableSumPair'): Seq(CellPairsParser()),
                Optional('VIPair'): Seq(CellPairsParser()),
                Optional('Window'): Seq(CellParser()),
                Optional('XPair'): Seq(CellPairsParser()),
                Optional('XIPair'): Seq(CellPairsParser()),
            }
        ),
        Optional('Solution'): Seq(SolutionParser()),
    }
)
