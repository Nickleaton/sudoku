\* Sudoku *\
Minimize
OBJ: __dummy
Subject To
Logical_or_l_and_11_b: l_and_11 <= 1
Logical_or_l_and_11_x1_a: l_and_11 - x1 >= 0
Logical_or_l_and_11_x2_a: l_and_11 - x2 >= 0
_C1: x1 = 1
_C2: x2 = 1
Bounds
 __dummy = 0
Binaries
l_and_11
x1
x2
End
