from strictyaml import Map, Seq, Optional, Str, Regex

from src.parsers.cell_list_parser import CellListParser
from src.parsers.cell_pairs_parser import CellPairsParser
from src.parsers.cell_parser import CellParser
from src.parsers.cell_value_parser import CellValueParser
from src.parsers.digit_parser import DigitParser
from src.parsers.digits_parser import DigitsParser
from src.parsers.frame_parser import FrameParser
from src.parsers.known_parser import KnownParser
from src.parsers.little_killers_parser import LittleKillersParser
from src.parsers.none_parser import NoneParser
from src.parsers.quadruples_parser import QuadruplesParser
from src.parsers.rossini_parser import RossiniParser
from src.parsers.solution_parser import SolutionParser

problem_schema = Map(
    {
        "Board": Map(
            {
                "Board": Str(),
                Optional("Box"): Str(),
                Optional("Video"): Str(),
                Optional("Reference"): Str(),
                Optional("Author"): Str(),
                Optional("Title"): Str(),
            }
        ),
        "Constraints": Map(
            {
                Optional("Anti"): NoneParser(),
                Optional("AntiBLTR"): NoneParser(),
                Optional("AntiDiagonal"): NoneParser(),
                Optional("AntiKing"): NoneParser(),
                Optional("AntiKnight"): NoneParser(),
                Optional("AntiMonkey"): NoneParser(),
                Optional("AntiQueens"): DigitsParser(),
                Optional("AntiTLBR"): NoneParser(),
                Optional("Asterix"): NoneParser(),
                Optional("BLTR"): NoneParser(),
                Optional("Battenburg"): CellListParser(),
                Optional("BetweenLine"): Seq(CellListParser()),
                Optional("Box"): DigitParser(),
                Optional("Boxes"): NoneParser(),
                Optional("Cell"): NoneParser(),
                Optional("CellReference"): Seq(CellParser()),
                Optional("CenterProduct"): Seq(CellValueParser()),
                Optional("ClonedRegion"): NoneParser(),
                Optional("Column"): DigitParser(),
                Optional("ColumnIndexer"): DigitsParser(),
                Optional("Columns"): NoneParser(),
                Optional("ComposedItem"): NoneParser(),
                Optional("ConsecutivePair"): Seq(CellPairsParser()),
                Optional("Constraints"): NoneParser(),
                Optional("Diagonal"): NoneParser(),
                Optional("DifferenceLine"): Seq(CellListParser()),
                Optional("DifferencePair"): Seq(CellPairsParser()),
                Optional("DisjointGroup"): DigitParser(),
                Optional("DisjointGroups"): NoneParser(),
                Optional("DistinctRenbanLine"): Seq(CellListParser()),
                Optional("DutchWhisperLine"): Seq(CellListParser()),
                Optional("EntropicLine"): Seq(CellListParser()),
                Optional("EqualSumLine"): Seq(CellListParser()),
                Optional("EvenCell"): Seq(CellParser()),
                Optional("Exclusion"): Seq(CellValueParser()),
                Optional("FirstN"): Seq(FrameParser()),
                Optional("FixedDifferencePair"): Seq(CellPairsParser()),
                Optional("FixedPair"): Seq(CellPairsParser()),
                Optional("FixedProductPair"): Seq(CellPairsParser()),
                Optional("FixedRatioPair"): Seq(CellPairsParser()),
                Optional("FixedSumPair"): Seq(CellPairsParser()),
                Optional("FortressCell"): Seq(CellParser()),
                Optional("Frame"): Seq(FrameParser()),
                Optional("FrameProduct"): Seq(FrameParser()),
                Optional("FrozenThermometerLine"): Seq(CellListParser()),
                Optional("GermanWhisperLine"): Seq(CellListParser()),
                Optional("Girandola"): NoneParser(),
                Optional("GreaterThanEqualDifferenceLine"): Seq(CellListParser()),
                Optional("GreaterThanEqualDifferencePair"): Seq(CellPairsParser()),
                Optional("GreaterThanPair"): Seq(CellPairsParser()),
                Optional("HighCell"): Seq(CellParser()),
                Optional("Indexer"): DigitsParser(),
                Optional("Killer"): NoneParser(),
                Optional("Knight"): DigitsParser(),
                Optional("Known"): Seq(KnownParser()),
                Optional("KnownCell"): Seq(CellParser()),
                Optional("KropkiPair"): Seq(CellPairsParser()),
                Optional("LessThanEqualDifferenceLine"): Seq(CellListParser()),
                Optional("LessThanEqualDifferencePair"): Seq(CellPairsParser()),
                Optional("Line"): Seq(CellListParser()),
                Optional("LittleKiller"): Seq(LittleKillersParser()),
                Optional("LockOutLine"): Seq(CellListParser()),
                Optional("LowCell"): Seq(CellParser()),
                Optional("MagicSquare"): Seq(CellParser()),
                Optional("MaxArrowLine"): Seq(CellListParser()),
                Optional("MidCell"): Seq(CellParser()),
                Optional("MinMaxDifference"): Seq(FrameParser()),
                Optional("MinMaxSum"): Seq(FrameParser()),
                Optional("MountainLine"): Seq(CellListParser()),
                Optional("NumberedRoom"): Seq(FrameParser()),
                Optional("OddCell"): Seq(CellParser()),
                Optional("OrthogonalProduct"): Seq(CellValueParser()),
                Optional("OrthogonallyAdjacent"): NoneParser(),
                Optional("Outside"): Seq(FrameParser()),
                Optional("Pair"): Seq(CellPairsParser()),
                Optional("PalindromeLine"): Seq(CellListParser()),
                Optional("PencilMarkCell"): Seq(CellParser()),
                Optional("Product"): Seq(CellValueParser()),
                Optional("ProductArrowLine"): Seq(CellListParser()),
                Optional("Quadro"): NoneParser(),
                Optional("Quadruple"): Seq(QuadruplesParser()),
                Optional("Region"): NoneParser(),
                Optional("RegionSet"): NoneParser(),
                Optional("RenbanLine"): Seq(CellListParser()),
                Optional("Rossini"): Seq(RossiniParser()),
                Optional("Row"): DigitParser(),
                Optional("RowIndexer"): DigitsParser(),
                Optional("Rows"): NoneParser(),
                Optional("Sandwich"): Seq(FrameParser()),
                Optional("SequenceLine"): Seq(CellListParser()),
                Optional("SimpleCellReference"): Seq(CellParser()),
                Optional("SimpleThermometerLine"): Seq(CellListParser()),
                Optional("SpecialRegion"): NoneParser(),
                Optional("StandardDiagonal"): NoneParser(),
                Optional("StandardRegion"): NoneParser(),
                Optional("StandardRegionSet"): NoneParser(),
                Optional("SumArrowLine"): Seq(CellListParser()),
                Optional("SumPair"): Seq(CellPairsParser()),
                Optional("TLBR"): NoneParser(),
                Optional("TLBRReflecting"): NoneParser(),
                Optional("ThermometerLine"): Seq(CellListParser()),
                Optional("UniqueRegion"): NoneParser(),
                Optional("VIPair"): Seq(CellPairsParser()),
                Optional("VPair"): Seq(CellPairsParser()),
                Optional("VariableDifferencePair"): Seq(CellPairsParser()),
                Optional("VariablePair"): Seq(CellPairsParser()),
                Optional("VariableProductPair"): Seq(CellPairsParser()),
                Optional("VariableRatioPair"): Seq(CellPairsParser()),
                Optional("VariableSumPair"): Seq(CellPairsParser()),
                Optional("Window"): Seq(CellParser()),
                Optional("XIPair"): Seq(CellPairsParser()),
                Optional("XPair"): Seq(CellPairsParser()),
            }
        ),
        Optional("Solution"): Seq(SolutionParser()),
    }
)
