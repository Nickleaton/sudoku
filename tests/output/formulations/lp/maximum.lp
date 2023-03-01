\* Sudoku *\
Minimize
OBJ: __dummy
Subject To
Maximum_13_0_a: Maximum_13 - x0 >= 0
Maximum_13_0_b: Maximum_13 + 8 Maximum_13_indicator_0 - x0 <= 8
Maximum_13_1_a: Maximum_13 - x1 >= 0
Maximum_13_1_b: Maximum_13 + 8 Maximum_13_indicator_1 - x1 <= 8
Maximum_13_2_a: Maximum_13 - x2 >= 0
Maximum_13_2_b: Maximum_13 + 8 Maximum_13_indicator_2 - x2 <= 8
Maximum_13_SOS: Maximum_13_indicator_0 + Maximum_13_indicator_1
 + Maximum_13_indicator_2 = 1
_C1: x0 = 2
_C2: x1 = 2
_C3: x2 = 2
Bounds
 1 <= Maximum_13 <= 9
 __dummy = 0
 1 <= x0 <= 9
 1 <= x1 <= 9
 1 <= x2 <= 9
Generals
Maximum_13
x0
x1
x2
Binaries
Maximum_13_indicator_0
Maximum_13_indicator_1
Maximum_13_indicator_2
End
