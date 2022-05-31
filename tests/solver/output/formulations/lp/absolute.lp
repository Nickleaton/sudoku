\* Sudoku *\
Minimize
OBJ: __dummy
Subject To
Abs_2_a: Abs_Difference_2 - x1 + x2 >= 0
Abs_2_b: Abs_Difference_2 + 18 Abs_Indicator_2 - x1 + x2 <= 18
Abs_2_c: Abs_Difference_2 + x1 - x2 >= 0
Abs_2_d: Abs_Difference_2 - 18 Abs_Indicator_2 + x1 - x2 <= 0
_C1: x1 = 1
_C2: x2 = 1
_C3: - Abs_Difference_2 + minimum = 0
Bounds
 0 <= Abs_Difference_2 <= 9
 __dummy = 0
 0 <= minimum <= 9
 1 <= x1 <= 9
 1 <= x2 <= 9
Generals
Abs_Difference_2
minimum
x1
x2
Binaries
Abs_Indicator_2
End
