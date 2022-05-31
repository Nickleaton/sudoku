\* Sudoku *\
Minimize
OBJ: __dummy
Subject To
Minimum_11_0_a: Minimum_11 - x0 <= 0
Minimum_11_0_b: Minimum_11 - 8 Minimum_11_indicator_0 - x0 >= -8
Minimum_11_1_a: Minimum_11 - x1 <= 0
Minimum_11_1_b: Minimum_11 - 8 Minimum_11_indicator_1 - x1 >= -8
Minimum_11_2_a: Minimum_11 - x2 <= 0
Minimum_11_2_b: Minimum_11 - 8 Minimum_11_indicator_2 - x2 >= -8
Minimum_11_SOS: Minimum_11_indicator_0 + Minimum_11_indicator_1
 + Minimum_11_indicator_2 = 1
_C1: x0 = 3
_C2: x1 = 2
_C3: x2 = 1
Bounds
 1 <= Minimum_11 <= 9
 __dummy = 0
 1 <= x0 <= 9
 1 <= x1 <= 9
 1 <= x2 <= 9
Generals
Minimum_11
x0
x1
x2
Binaries
Minimum_11_indicator_0
Minimum_11_indicator_1
Minimum_11_indicator_2
End
