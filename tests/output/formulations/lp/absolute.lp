\* Sudoku *\
Minimize
OBJ: __dummy
Subject To
Abs_5_a: Abs_Difference_5 - x1 + x2 >= 0
Abs_5_b: Abs_Difference_5 + 18 Abs_Indicator_5 - x1 + x2 <= 18
Abs_5_c: Abs_Difference_5 + x1 - x2 >= 0
Abs_5_d: Abs_Difference_5 - 18 Abs_Indicator_5 + x1 - x2 <= 0
_C1: x1 = 1
_C2: x2 = 1
_C3: - Abs_Difference_5 + minimum = 0
Bounds
 0 <= Abs_Difference_5 <= 9
 __dummy = 0
 0 <= minimum <= 9
 1 <= x1 <= 9
 1 <= x2 <= 9
Generals
Abs_Difference_5
minimum
x1
x2
Binaries
Abs_Indicator_5
End
