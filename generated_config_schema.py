from strictyaml import Map, Seq, Optional, Str, Float, Int, Regex, NoneParser, Str, Regex

Map({'Board': Map({'Board': Str(), Optional("Box"): Str(), Optional("Video"): Str(), Optional("Reference"): Str(), Optional("Author"): Str(), Optional("Title"): Str()}), 'Constraints': Map({Optional("AntiBLTR"): NoneParser(), Optional("AntiKing"): NoneParser(), Optional("AntiKnight"): NoneParser(), Optional("AntiQueens"): <class 'src.parsers.digits_parser.DigitsParser'>, Optional("AntiRossini"): NoneParser(), Optional("AntiTLBR"): NoneParser(), Optional("Asterix"): NoneParser(), Optional("BLTR"): NoneParser(), Optional("Battenburg"): CellListParser(), Optional("Between"): Seq(CellListParser()), Optional("Boxes"): NoneParser(), Optional("CenterProduct"): Seq(VertexValueParser()), Optional("ColumnIndexer"): DigitsParser(), Optional("Columns"): NoneParser(), Optional("ConsecutivePair"): Seq(<class 'src.parsers.cell_pairs_parser.CellPairsParser'>), Optional("DisjointGroup"): NoneParser(), Optional("DutchWhisperLine"): Seq(CellListParser()), Optional("EntropicLine"): Seq(CellListParser()), Optional("EqualSumLine"): Seq(CellListParser()), Optional("EvenCellParser"): Seq(CellParser()), Optional("Exclusion"): Seq(VertexDigitParser()), Optional("FixedDifferencePair"): Seq(CellPairsParser()), Optional("FixedProductPair"): Seq(CellPairsParser()), Optional("FixedRatioPair"): Seq(CellPairsParser()), Optional("FixedSumPair"): Seq(CellPairsParser()), Optional("Frame"): Seq(OutsideArrowValueParser()), Optional("FrameProduct"): Seq(OutsideArrowValueParser()), Optional("FrozenThermometer"): Seq(CellListParser()), Optional("GermanWhisperLine"): Seq(CellListParser()), Optional("Girandola"): NoneParser(), Optional("Knight"): Seq(DigitParser()), Optional("Known"): Seq(KnownParser()), Optional("KropkiPair"): Seq(CellPairsParser()), Optional("LittleKiller"): Seq(LittleKillersParser()), Optional("MOTE"): Seq(CellListParser()), Optional("MagicSquare"): Seq(CellParser()), Optional("MaxArrowLine"): Seq(CellListParser()), Optional("MinMaxDifference"): Seq(OutsideArrowValueParser()), Optional("MinMaxSum"): Seq(OutsideArrowValueParser()), Optional("MountainLine"): Seq(CellListParser()), Optional("NegativeBattenburg"): NoneParser(), Optional("NumberedRoom"): Seq(OutsideArrowValueParser()), Optional("OddCellParser"): Seq(CellParser()), Optional("OrthogonalProduct"): Seq(CellValueParser()), Optional("OrthogonallyAdjacent"): NoneParser(), Optional("Outside"): Seq(OutsideArrowValueParser()), Optional("Palindrome"): Seq(CellListParser()), Optional("Quadro"): NoneParser(), Optional("Quadruple"): Seq(QuadruplesParser()), Optional("RenbanLine"): Seq(CellListParser()), Optional("Rossini"): Seq(RossiniParser()), Optional("Rows"): NoneParser(), Optional("Sandwich"): Seq(OutsideArrowValueParser()), Optional("SequenceLine"): Seq(CellListParser()), Optional("SimpleThermometer"): Seq(CellListParser()), Optional("SumArrowLine"): Seq(CellListParser()), Optional("SumArrowLine"): Seq(CellListParser()), Optional("TLBR"): NoneParser(), Optional("TLBRReflecting"): NoneParser(), Optional("VPair"): Seq(CellPairsParser()), Optional("Window"): Seq(CellParser()), Optional("XPair"): Seq(CellPairsParser())}), Optional("Solution"): Seq(SolutionParser())})