\* Sudoku *\
Minimize
OBJ: __dummy
Subject To
Abs_4_a: Abs_Difference_4 - x1 + x2 >= 0
Abs_4_b: Abs_Difference_4 + 18 Abs_Indicator_4 - x1 + x2 <= 18
Abs_4_c: Abs_Difference_4 + x1 - x2 >= 0
Abs_4_d: Abs_Difference_4 - 18 Abs_Indicator_4 + x1 - x2 <= 0
_C1: x1 = 4.5
_C2: x2 = 2.8
_C3: - Abs_Difference_4 + minimum = 0
Bounds
 Abs_Difference_4 <= 9
 __dummy = 0
 minimum <= 9
 1 <= x1 <= 9
 1 <= x2 <= 9
Binaries
Abs_Indicator_4
End
