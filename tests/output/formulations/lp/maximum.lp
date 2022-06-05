\* Sudoku *\
Minimize
OBJ: __dummy
Subject To
Maximum_5_0_a: Maximum_5 - x0 >= 0
Maximum_5_0_b: Maximum_5 + 8 Maximum_5_indicator_0 - x0 <= 8
Maximum_5_1_a: Maximum_5 - x1 >= 0
Maximum_5_1_b: Maximum_5 + 8 Maximum_5_indicator_1 - x1 <= 8
Maximum_5_2_a: Maximum_5 - x2 >= 0
Maximum_5_2_b: Maximum_5 + 8 Maximum_5_indicator_2 - x2 <= 8
Maximum_5_SOS: Maximum_5_indicator_0 + Maximum_5_indicator_1
 + Maximum_5_indicator_2 = 1
_C1: x0 = 2
_C2: x1 = 2
_C3: x2 = 2
Bounds
 1 <= Maximum_5 <= 9
 __dummy = 0
 1 <= x0 <= 9
 1 <= x1 <= 9
 1 <= x2 <= 9
Generals
Maximum_5
x0
x1
x2
Binaries
Maximum_5_indicator_0
Maximum_5_indicator_1
Maximum_5_indicator_2
End
