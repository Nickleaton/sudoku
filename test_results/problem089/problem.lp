\* Sudoku *\
Minimize
Objective: __dummy
Subject To
Abs_0_a: Abs_Difference_0 - Log10_2_5 + Log10_2_6 >= 0
Abs_0_b: Abs_Difference_0 + 4 Abs_Indicator_0 - Log10_2_5 + Log10_2_6 <= 4
Abs_0_c: Abs_Difference_0 + Log10_2_5 - Log10_2_6 >= 0
Abs_0_d: Abs_Difference_0 - 4 Abs_Indicator_0 + Log10_2_5 - Log10_2_6 <= 0
Abs_1_a: Abs_Difference_1 - Values_1_2 + Values_2_2 >= 0
Abs_1_b: Abs_Difference_1 + 20 Abs_Indicator_1 - Values_1_2 + Values_2_2 <= 20
Abs_1_c: Abs_Difference_1 + Values_1_2 - Values_2_2 >= 0
Abs_1_d: Abs_Difference_1 - 20 Abs_Indicator_1 + Values_1_2 - Values_2_2 <= 0
Abs_2_a: Abs_Difference_2 - Values_2_5 + Values_3_5 >= 0
Abs_2_b: Abs_Difference_2 + 20 Abs_Indicator_2 - Values_2_5 + Values_3_5 <= 20
Abs_2_c: Abs_Difference_2 + Values_2_5 - Values_3_5 >= 0
Abs_2_d: Abs_Difference_2 - 20 Abs_Indicator_2 + Values_2_5 - Values_3_5 <= 0
Abs_3_a: Abs_Difference_3 - Values_3_5 + Values_3_6 >= 0
Abs_3_b: Abs_Difference_3 + 20 Abs_Indicator_3 - Values_3_5 + Values_3_6 <= 20
Abs_3_c: Abs_Difference_3 + Values_3_5 - Values_3_6 >= 0
Abs_3_d: Abs_Difference_3 - 20 Abs_Indicator_3 + Values_3_5 - Values_3_6 <= 0
Abs_4_a: Abs_Difference_4 + Values_2_6 - Values_3_6 >= 0
Abs_4_b: Abs_Difference_4 + 20 Abs_Indicator_4 + Values_2_6 - Values_3_6 <= 20
Abs_4_c: Abs_Difference_4 - Values_2_6 + Values_3_6 >= 0
Abs_4_d: Abs_Difference_4 - 20 Abs_Indicator_4 - Values_2_6 + Values_3_6 <= 0
Abs_5_a: Abs_Difference_5 - Values_3_7 + Values_4_7 >= 0
Abs_5_b: Abs_Difference_5 + 20 Abs_Indicator_5 - Values_3_7 + Values_4_7 <= 20
Abs_5_c: Abs_Difference_5 + Values_3_7 - Values_4_7 >= 0
Abs_5_d: Abs_Difference_5 - 20 Abs_Indicator_5 + Values_3_7 - Values_4_7 <= 0
Abs_6_a: Abs_Difference_6 - Values_1_9 + Values_2_9 >= 0
Abs_6_b: Abs_Difference_6 + 20 Abs_Indicator_6 - Values_1_9 + Values_2_9 <= 20
Abs_6_c: Abs_Difference_6 + Values_1_9 - Values_2_9 >= 0
Abs_6_d: Abs_Difference_6 - 20 Abs_Indicator_6 + Values_1_9 - Values_2_9 <= 0
Abs_7_a: Abs_Difference_7 - Values_3_8 + Values_3_9 >= 0
Abs_7_b: Abs_Difference_7 + 20 Abs_Indicator_7 - Values_3_8 + Values_3_9 <= 20
Abs_7_c: Abs_Difference_7 + Values_3_8 - Values_3_9 >= 0
Abs_7_d: Abs_Difference_7 - 20 Abs_Indicator_7 + Values_3_8 - Values_3_9 <= 0
Abs_8_a: Abs_Difference_8 - Values_5_5 + Values_5_6 >= 0
Abs_8_b: Abs_Difference_8 + 20 Abs_Indicator_8 - Values_5_5 + Values_5_6 <= 20
Abs_8_c: Abs_Difference_8 + Values_5_5 - Values_5_6 >= 0
Abs_8_d: Abs_Difference_8 - 20 Abs_Indicator_8 + Values_5_5 - Values_5_6 <= 0
Abs_9_a: Abs_Difference_9 - Values_8_8 + Values_9_8 >= 0
Abs_9_b: Abs_Difference_9 + 20 Abs_Indicator_9 - Values_8_8 + Values_9_8 <= 20
Abs_9_c: Abs_Difference_9 + Values_8_8 - Values_9_8 >= 0
Abs_9_d: Abs_Difference_9 - 20 Abs_Indicator_9 + Values_8_8 - Values_9_8 <= 0
Box_634_Unique_1: Choice_1_1_1 + Choice_1_1_2 + Choice_1_1_3 + Choice_1_2_1
 + Choice_1_2_2 + Choice_1_2_3 + Choice_1_3_1 + Choice_1_3_2 + Choice_1_3_3
 = 1
Box_634_Unique_2: Choice_2_1_1 + Choice_2_1_2 + Choice_2_1_3 + Choice_2_2_1
 + Choice_2_2_2 + Choice_2_2_3 + Choice_2_3_1 + Choice_2_3_2 + Choice_2_3_3
 = 1
Box_634_Unique_3: Choice_3_1_1 + Choice_3_1_2 + Choice_3_1_3 + Choice_3_2_1
 + Choice_3_2_2 + Choice_3_2_3 + Choice_3_3_1 + Choice_3_3_2 + Choice_3_3_3
 = 1
Box_634_Unique_4: Choice_4_1_1 + Choice_4_1_2 + Choice_4_1_3 + Choice_4_2_1
 + Choice_4_2_2 + Choice_4_2_3 + Choice_4_3_1 + Choice_4_3_2 + Choice_4_3_3
 = 1
Box_634_Unique_5: Choice_5_1_1 + Choice_5_1_2 + Choice_5_1_3 + Choice_5_2_1
 + Choice_5_2_2 + Choice_5_2_3 + Choice_5_3_1 + Choice_5_3_2 + Choice_5_3_3
 = 1
Box_634_Unique_6: Choice_6_1_1 + Choice_6_1_2 + Choice_6_1_3 + Choice_6_2_1
 + Choice_6_2_2 + Choice_6_2_3 + Choice_6_3_1 + Choice_6_3_2 + Choice_6_3_3
 = 1
Box_634_Unique_7: Choice_7_1_1 + Choice_7_1_2 + Choice_7_1_3 + Choice_7_2_1
 + Choice_7_2_2 + Choice_7_2_3 + Choice_7_3_1 + Choice_7_3_2 + Choice_7_3_3
 = 1
Box_634_Unique_8: Choice_8_1_1 + Choice_8_1_2 + Choice_8_1_3 + Choice_8_2_1
 + Choice_8_2_2 + Choice_8_2_3 + Choice_8_3_1 + Choice_8_3_2 + Choice_8_3_3
 = 1
Box_634_Unique_9: Choice_9_1_1 + Choice_9_1_2 + Choice_9_1_3 + Choice_9_2_1
 + Choice_9_2_2 + Choice_9_2_3 + Choice_9_3_1 + Choice_9_3_2 + Choice_9_3_3
 = 1
Box_635_Unique_1: Choice_1_4_1 + Choice_1_4_2 + Choice_1_4_3 + Choice_1_5_1
 + Choice_1_5_2 + Choice_1_5_3 + Choice_1_6_1 + Choice_1_6_2 + Choice_1_6_3
 = 1
Box_635_Unique_2: Choice_2_4_1 + Choice_2_4_2 + Choice_2_4_3 + Choice_2_5_1
 + Choice_2_5_2 + Choice_2_5_3 + Choice_2_6_1 + Choice_2_6_2 + Choice_2_6_3
 = 1
Box_635_Unique_3: Choice_3_4_1 + Choice_3_4_2 + Choice_3_4_3 + Choice_3_5_1
 + Choice_3_5_2 + Choice_3_5_3 + Choice_3_6_1 + Choice_3_6_2 + Choice_3_6_3
 = 1
Box_635_Unique_4: Choice_4_4_1 + Choice_4_4_2 + Choice_4_4_3 + Choice_4_5_1
 + Choice_4_5_2 + Choice_4_5_3 + Choice_4_6_1 + Choice_4_6_2 + Choice_4_6_3
 = 1
Box_635_Unique_5: Choice_5_4_1 + Choice_5_4_2 + Choice_5_4_3 + Choice_5_5_1
 + Choice_5_5_2 + Choice_5_5_3 + Choice_5_6_1 + Choice_5_6_2 + Choice_5_6_3
 = 1
Box_635_Unique_6: Choice_6_4_1 + Choice_6_4_2 + Choice_6_4_3 + Choice_6_5_1
 + Choice_6_5_2 + Choice_6_5_3 + Choice_6_6_1 + Choice_6_6_2 + Choice_6_6_3
 = 1
Box_635_Unique_7: Choice_7_4_1 + Choice_7_4_2 + Choice_7_4_3 + Choice_7_5_1
 + Choice_7_5_2 + Choice_7_5_3 + Choice_7_6_1 + Choice_7_6_2 + Choice_7_6_3
 = 1
Box_635_Unique_8: Choice_8_4_1 + Choice_8_4_2 + Choice_8_4_3 + Choice_8_5_1
 + Choice_8_5_2 + Choice_8_5_3 + Choice_8_6_1 + Choice_8_6_2 + Choice_8_6_3
 = 1
Box_635_Unique_9: Choice_9_4_1 + Choice_9_4_2 + Choice_9_4_3 + Choice_9_5_1
 + Choice_9_5_2 + Choice_9_5_3 + Choice_9_6_1 + Choice_9_6_2 + Choice_9_6_3
 = 1
Box_636_Unique_1: Choice_1_7_1 + Choice_1_7_2 + Choice_1_7_3 + Choice_1_8_1
 + Choice_1_8_2 + Choice_1_8_3 + Choice_1_9_1 + Choice_1_9_2 + Choice_1_9_3
 = 1
Box_636_Unique_2: Choice_2_7_1 + Choice_2_7_2 + Choice_2_7_3 + Choice_2_8_1
 + Choice_2_8_2 + Choice_2_8_3 + Choice_2_9_1 + Choice_2_9_2 + Choice_2_9_3
 = 1
Box_636_Unique_3: Choice_3_7_1 + Choice_3_7_2 + Choice_3_7_3 + Choice_3_8_1
 + Choice_3_8_2 + Choice_3_8_3 + Choice_3_9_1 + Choice_3_9_2 + Choice_3_9_3
 = 1
Box_636_Unique_4: Choice_4_7_1 + Choice_4_7_2 + Choice_4_7_3 + Choice_4_8_1
 + Choice_4_8_2 + Choice_4_8_3 + Choice_4_9_1 + Choice_4_9_2 + Choice_4_9_3
 = 1
Box_636_Unique_5: Choice_5_7_1 + Choice_5_7_2 + Choice_5_7_3 + Choice_5_8_1
 + Choice_5_8_2 + Choice_5_8_3 + Choice_5_9_1 + Choice_5_9_2 + Choice_5_9_3
 = 1
Box_636_Unique_6: Choice_6_7_1 + Choice_6_7_2 + Choice_6_7_3 + Choice_6_8_1
 + Choice_6_8_2 + Choice_6_8_3 + Choice_6_9_1 + Choice_6_9_2 + Choice_6_9_3
 = 1
Box_636_Unique_7: Choice_7_7_1 + Choice_7_7_2 + Choice_7_7_3 + Choice_7_8_1
 + Choice_7_8_2 + Choice_7_8_3 + Choice_7_9_1 + Choice_7_9_2 + Choice_7_9_3
 = 1
Box_636_Unique_8: Choice_8_7_1 + Choice_8_7_2 + Choice_8_7_3 + Choice_8_8_1
 + Choice_8_8_2 + Choice_8_8_3 + Choice_8_9_1 + Choice_8_9_2 + Choice_8_9_3
 = 1
Box_636_Unique_9: Choice_9_7_1 + Choice_9_7_2 + Choice_9_7_3 + Choice_9_8_1
 + Choice_9_8_2 + Choice_9_8_3 + Choice_9_9_1 + Choice_9_9_2 + Choice_9_9_3
 = 1
Box_637_Unique_1: Choice_1_1_4 + Choice_1_1_5 + Choice_1_1_6 + Choice_1_2_4
 + Choice_1_2_5 + Choice_1_2_6 + Choice_1_3_4 + Choice_1_3_5 + Choice_1_3_6
 = 1
Box_637_Unique_2: Choice_2_1_4 + Choice_2_1_5 + Choice_2_1_6 + Choice_2_2_4
 + Choice_2_2_5 + Choice_2_2_6 + Choice_2_3_4 + Choice_2_3_5 + Choice_2_3_6
 = 1
Box_637_Unique_3: Choice_3_1_4 + Choice_3_1_5 + Choice_3_1_6 + Choice_3_2_4
 + Choice_3_2_5 + Choice_3_2_6 + Choice_3_3_4 + Choice_3_3_5 + Choice_3_3_6
 = 1
Box_637_Unique_4: Choice_4_1_4 + Choice_4_1_5 + Choice_4_1_6 + Choice_4_2_4
 + Choice_4_2_5 + Choice_4_2_6 + Choice_4_3_4 + Choice_4_3_5 + Choice_4_3_6
 = 1
Box_637_Unique_5: Choice_5_1_4 + Choice_5_1_5 + Choice_5_1_6 + Choice_5_2_4
 + Choice_5_2_5 + Choice_5_2_6 + Choice_5_3_4 + Choice_5_3_5 + Choice_5_3_6
 = 1
Box_637_Unique_6: Choice_6_1_4 + Choice_6_1_5 + Choice_6_1_6 + Choice_6_2_4
 + Choice_6_2_5 + Choice_6_2_6 + Choice_6_3_4 + Choice_6_3_5 + Choice_6_3_6
 = 1
Box_637_Unique_7: Choice_7_1_4 + Choice_7_1_5 + Choice_7_1_6 + Choice_7_2_4
 + Choice_7_2_5 + Choice_7_2_6 + Choice_7_3_4 + Choice_7_3_5 + Choice_7_3_6
 = 1
Box_637_Unique_8: Choice_8_1_4 + Choice_8_1_5 + Choice_8_1_6 + Choice_8_2_4
 + Choice_8_2_5 + Choice_8_2_6 + Choice_8_3_4 + Choice_8_3_5 + Choice_8_3_6
 = 1
Box_637_Unique_9: Choice_9_1_4 + Choice_9_1_5 + Choice_9_1_6 + Choice_9_2_4
 + Choice_9_2_5 + Choice_9_2_6 + Choice_9_3_4 + Choice_9_3_5 + Choice_9_3_6
 = 1
Box_638_Unique_1: Choice_1_4_4 + Choice_1_4_5 + Choice_1_4_6 + Choice_1_5_4
 + Choice_1_5_5 + Choice_1_5_6 + Choice_1_6_4 + Choice_1_6_5 + Choice_1_6_6
 = 1
Box_638_Unique_2: Choice_2_4_4 + Choice_2_4_5 + Choice_2_4_6 + Choice_2_5_4
 + Choice_2_5_5 + Choice_2_5_6 + Choice_2_6_4 + Choice_2_6_5 + Choice_2_6_6
 = 1
Box_638_Unique_3: Choice_3_4_4 + Choice_3_4_5 + Choice_3_4_6 + Choice_3_5_4
 + Choice_3_5_5 + Choice_3_5_6 + Choice_3_6_4 + Choice_3_6_5 + Choice_3_6_6
 = 1
Box_638_Unique_4: Choice_4_4_4 + Choice_4_4_5 + Choice_4_4_6 + Choice_4_5_4
 + Choice_4_5_5 + Choice_4_5_6 + Choice_4_6_4 + Choice_4_6_5 + Choice_4_6_6
 = 1
Box_638_Unique_5: Choice_5_4_4 + Choice_5_4_5 + Choice_5_4_6 + Choice_5_5_4
 + Choice_5_5_5 + Choice_5_5_6 + Choice_5_6_4 + Choice_5_6_5 + Choice_5_6_6
 = 1
Box_638_Unique_6: Choice_6_4_4 + Choice_6_4_5 + Choice_6_4_6 + Choice_6_5_4
 + Choice_6_5_5 + Choice_6_5_6 + Choice_6_6_4 + Choice_6_6_5 + Choice_6_6_6
 = 1
Box_638_Unique_7: Choice_7_4_4 + Choice_7_4_5 + Choice_7_4_6 + Choice_7_5_4
 + Choice_7_5_5 + Choice_7_5_6 + Choice_7_6_4 + Choice_7_6_5 + Choice_7_6_6
 = 1
Box_638_Unique_8: Choice_8_4_4 + Choice_8_4_5 + Choice_8_4_6 + Choice_8_5_4
 + Choice_8_5_5 + Choice_8_5_6 + Choice_8_6_4 + Choice_8_6_5 + Choice_8_6_6
 = 1
Box_638_Unique_9: Choice_9_4_4 + Choice_9_4_5 + Choice_9_4_6 + Choice_9_5_4
 + Choice_9_5_5 + Choice_9_5_6 + Choice_9_6_4 + Choice_9_6_5 + Choice_9_6_6
 = 1
Box_639_Unique_1: Choice_1_7_4 + Choice_1_7_5 + Choice_1_7_6 + Choice_1_8_4
 + Choice_1_8_5 + Choice_1_8_6 + Choice_1_9_4 + Choice_1_9_5 + Choice_1_9_6
 = 1
Box_639_Unique_2: Choice_2_7_4 + Choice_2_7_5 + Choice_2_7_6 + Choice_2_8_4
 + Choice_2_8_5 + Choice_2_8_6 + Choice_2_9_4 + Choice_2_9_5 + Choice_2_9_6
 = 1
Box_639_Unique_3: Choice_3_7_4 + Choice_3_7_5 + Choice_3_7_6 + Choice_3_8_4
 + Choice_3_8_5 + Choice_3_8_6 + Choice_3_9_4 + Choice_3_9_5 + Choice_3_9_6
 = 1
Box_639_Unique_4: Choice_4_7_4 + Choice_4_7_5 + Choice_4_7_6 + Choice_4_8_4
 + Choice_4_8_5 + Choice_4_8_6 + Choice_4_9_4 + Choice_4_9_5 + Choice_4_9_6
 = 1
Box_639_Unique_5: Choice_5_7_4 + Choice_5_7_5 + Choice_5_7_6 + Choice_5_8_4
 + Choice_5_8_5 + Choice_5_8_6 + Choice_5_9_4 + Choice_5_9_5 + Choice_5_9_6
 = 1
Box_639_Unique_6: Choice_6_7_4 + Choice_6_7_5 + Choice_6_7_6 + Choice_6_8_4
 + Choice_6_8_5 + Choice_6_8_6 + Choice_6_9_4 + Choice_6_9_5 + Choice_6_9_6
 = 1
Box_639_Unique_7: Choice_7_7_4 + Choice_7_7_5 + Choice_7_7_6 + Choice_7_8_4
 + Choice_7_8_5 + Choice_7_8_6 + Choice_7_9_4 + Choice_7_9_5 + Choice_7_9_6
 = 1
Box_639_Unique_8: Choice_8_7_4 + Choice_8_7_5 + Choice_8_7_6 + Choice_8_8_4
 + Choice_8_8_5 + Choice_8_8_6 + Choice_8_9_4 + Choice_8_9_5 + Choice_8_9_6
 = 1
Box_639_Unique_9: Choice_9_7_4 + Choice_9_7_5 + Choice_9_7_6 + Choice_9_8_4
 + Choice_9_8_5 + Choice_9_8_6 + Choice_9_9_4 + Choice_9_9_5 + Choice_9_9_6
 = 1
Box_640_Unique_1: Choice_1_1_7 + Choice_1_1_8 + Choice_1_1_9 + Choice_1_2_7
 + Choice_1_2_8 + Choice_1_2_9 + Choice_1_3_7 + Choice_1_3_8 + Choice_1_3_9
 = 1
Box_640_Unique_2: Choice_2_1_7 + Choice_2_1_8 + Choice_2_1_9 + Choice_2_2_7
 + Choice_2_2_8 + Choice_2_2_9 + Choice_2_3_7 + Choice_2_3_8 + Choice_2_3_9
 = 1
Box_640_Unique_3: Choice_3_1_7 + Choice_3_1_8 + Choice_3_1_9 + Choice_3_2_7
 + Choice_3_2_8 + Choice_3_2_9 + Choice_3_3_7 + Choice_3_3_8 + Choice_3_3_9
 = 1
Box_640_Unique_4: Choice_4_1_7 + Choice_4_1_8 + Choice_4_1_9 + Choice_4_2_7
 + Choice_4_2_8 + Choice_4_2_9 + Choice_4_3_7 + Choice_4_3_8 + Choice_4_3_9
 = 1
Box_640_Unique_5: Choice_5_1_7 + Choice_5_1_8 + Choice_5_1_9 + Choice_5_2_7
 + Choice_5_2_8 + Choice_5_2_9 + Choice_5_3_7 + Choice_5_3_8 + Choice_5_3_9
 = 1
Box_640_Unique_6: Choice_6_1_7 + Choice_6_1_8 + Choice_6_1_9 + Choice_6_2_7
 + Choice_6_2_8 + Choice_6_2_9 + Choice_6_3_7 + Choice_6_3_8 + Choice_6_3_9
 = 1
Box_640_Unique_7: Choice_7_1_7 + Choice_7_1_8 + Choice_7_1_9 + Choice_7_2_7
 + Choice_7_2_8 + Choice_7_2_9 + Choice_7_3_7 + Choice_7_3_8 + Choice_7_3_9
 = 1
Box_640_Unique_8: Choice_8_1_7 + Choice_8_1_8 + Choice_8_1_9 + Choice_8_2_7
 + Choice_8_2_8 + Choice_8_2_9 + Choice_8_3_7 + Choice_8_3_8 + Choice_8_3_9
 = 1
Box_640_Unique_9: Choice_9_1_7 + Choice_9_1_8 + Choice_9_1_9 + Choice_9_2_7
 + Choice_9_2_8 + Choice_9_2_9 + Choice_9_3_7 + Choice_9_3_8 + Choice_9_3_9
 = 1
Box_641_Unique_1: Choice_1_4_7 + Choice_1_4_8 + Choice_1_4_9 + Choice_1_5_7
 + Choice_1_5_8 + Choice_1_5_9 + Choice_1_6_7 + Choice_1_6_8 + Choice_1_6_9
 = 1
Box_641_Unique_2: Choice_2_4_7 + Choice_2_4_8 + Choice_2_4_9 + Choice_2_5_7
 + Choice_2_5_8 + Choice_2_5_9 + Choice_2_6_7 + Choice_2_6_8 + Choice_2_6_9
 = 1
Box_641_Unique_3: Choice_3_4_7 + Choice_3_4_8 + Choice_3_4_9 + Choice_3_5_7
 + Choice_3_5_8 + Choice_3_5_9 + Choice_3_6_7 + Choice_3_6_8 + Choice_3_6_9
 = 1
Box_641_Unique_4: Choice_4_4_7 + Choice_4_4_8 + Choice_4_4_9 + Choice_4_5_7
 + Choice_4_5_8 + Choice_4_5_9 + Choice_4_6_7 + Choice_4_6_8 + Choice_4_6_9
 = 1
Box_641_Unique_5: Choice_5_4_7 + Choice_5_4_8 + Choice_5_4_9 + Choice_5_5_7
 + Choice_5_5_8 + Choice_5_5_9 + Choice_5_6_7 + Choice_5_6_8 + Choice_5_6_9
 = 1
Box_641_Unique_6: Choice_6_4_7 + Choice_6_4_8 + Choice_6_4_9 + Choice_6_5_7
 + Choice_6_5_8 + Choice_6_5_9 + Choice_6_6_7 + Choice_6_6_8 + Choice_6_6_9
 = 1
Box_641_Unique_7: Choice_7_4_7 + Choice_7_4_8 + Choice_7_4_9 + Choice_7_5_7
 + Choice_7_5_8 + Choice_7_5_9 + Choice_7_6_7 + Choice_7_6_8 + Choice_7_6_9
 = 1
Box_641_Unique_8: Choice_8_4_7 + Choice_8_4_8 + Choice_8_4_9 + Choice_8_5_7
 + Choice_8_5_8 + Choice_8_5_9 + Choice_8_6_7 + Choice_8_6_8 + Choice_8_6_9
 = 1
Box_641_Unique_9: Choice_9_4_7 + Choice_9_4_8 + Choice_9_4_9 + Choice_9_5_7
 + Choice_9_5_8 + Choice_9_5_9 + Choice_9_6_7 + Choice_9_6_8 + Choice_9_6_9
 = 1
Box_642_Unique_1: Choice_1_7_7 + Choice_1_7_8 + Choice_1_7_9 + Choice_1_8_7
 + Choice_1_8_8 + Choice_1_8_9 + Choice_1_9_7 + Choice_1_9_8 + Choice_1_9_9
 = 1
Box_642_Unique_2: Choice_2_7_7 + Choice_2_7_8 + Choice_2_7_9 + Choice_2_8_7
 + Choice_2_8_8 + Choice_2_8_9 + Choice_2_9_7 + Choice_2_9_8 + Choice_2_9_9
 = 1
Box_642_Unique_3: Choice_3_7_7 + Choice_3_7_8 + Choice_3_7_9 + Choice_3_8_7
 + Choice_3_8_8 + Choice_3_8_9 + Choice_3_9_7 + Choice_3_9_8 + Choice_3_9_9
 = 1
Box_642_Unique_4: Choice_4_7_7 + Choice_4_7_8 + Choice_4_7_9 + Choice_4_8_7
 + Choice_4_8_8 + Choice_4_8_9 + Choice_4_9_7 + Choice_4_9_8 + Choice_4_9_9
 = 1
Box_642_Unique_5: Choice_5_7_7 + Choice_5_7_8 + Choice_5_7_9 + Choice_5_8_7
 + Choice_5_8_8 + Choice_5_8_9 + Choice_5_9_7 + Choice_5_9_8 + Choice_5_9_9
 = 1
Box_642_Unique_6: Choice_6_7_7 + Choice_6_7_8 + Choice_6_7_9 + Choice_6_8_7
 + Choice_6_8_8 + Choice_6_8_9 + Choice_6_9_7 + Choice_6_9_8 + Choice_6_9_9
 = 1
Box_642_Unique_7: Choice_7_7_7 + Choice_7_7_8 + Choice_7_7_9 + Choice_7_8_7
 + Choice_7_8_8 + Choice_7_8_9 + Choice_7_9_7 + Choice_7_9_8 + Choice_7_9_9
 = 1
Box_642_Unique_8: Choice_8_7_7 + Choice_8_7_8 + Choice_8_7_9 + Choice_8_8_7
 + Choice_8_8_8 + Choice_8_8_9 + Choice_8_9_7 + Choice_8_9_8 + Choice_8_9_9
 = 1
Box_642_Unique_9: Choice_9_7_7 + Choice_9_7_8 + Choice_9_7_9 + Choice_9_8_7
 + Choice_9_8_8 + Choice_9_8_9 + Choice_9_9_7 + Choice_9_9_8 + Choice_9_9_9
 = 1
Column_614_Unique_1: Choice_1_1_1 + Choice_1_2_1 + Choice_1_3_1 + Choice_1_4_1
 + Choice_1_5_1 + Choice_1_6_1 + Choice_1_7_1 + Choice_1_8_1 + Choice_1_9_1
 = 1
Column_614_Unique_2: Choice_2_1_1 + Choice_2_2_1 + Choice_2_3_1 + Choice_2_4_1
 + Choice_2_5_1 + Choice_2_6_1 + Choice_2_7_1 + Choice_2_8_1 + Choice_2_9_1
 = 1
Column_614_Unique_3: Choice_3_1_1 + Choice_3_2_1 + Choice_3_3_1 + Choice_3_4_1
 + Choice_3_5_1 + Choice_3_6_1 + Choice_3_7_1 + Choice_3_8_1 + Choice_3_9_1
 = 1
Column_614_Unique_4: Choice_4_1_1 + Choice_4_2_1 + Choice_4_3_1 + Choice_4_4_1
 + Choice_4_5_1 + Choice_4_6_1 + Choice_4_7_1 + Choice_4_8_1 + Choice_4_9_1
 = 1
Column_614_Unique_5: Choice_5_1_1 + Choice_5_2_1 + Choice_5_3_1 + Choice_5_4_1
 + Choice_5_5_1 + Choice_5_6_1 + Choice_5_7_1 + Choice_5_8_1 + Choice_5_9_1
 = 1
Column_614_Unique_6: Choice_6_1_1 + Choice_6_2_1 + Choice_6_3_1 + Choice_6_4_1
 + Choice_6_5_1 + Choice_6_6_1 + Choice_6_7_1 + Choice_6_8_1 + Choice_6_9_1
 = 1
Column_614_Unique_7: Choice_7_1_1 + Choice_7_2_1 + Choice_7_3_1 + Choice_7_4_1
 + Choice_7_5_1 + Choice_7_6_1 + Choice_7_7_1 + Choice_7_8_1 + Choice_7_9_1
 = 1
Column_614_Unique_8: Choice_8_1_1 + Choice_8_2_1 + Choice_8_3_1 + Choice_8_4_1
 + Choice_8_5_1 + Choice_8_6_1 + Choice_8_7_1 + Choice_8_8_1 + Choice_8_9_1
 = 1
Column_614_Unique_9: Choice_9_1_1 + Choice_9_2_1 + Choice_9_3_1 + Choice_9_4_1
 + Choice_9_5_1 + Choice_9_6_1 + Choice_9_7_1 + Choice_9_8_1 + Choice_9_9_1
 = 1
Column_615_Unique_1: Choice_1_1_2 + Choice_1_2_2 + Choice_1_3_2 + Choice_1_4_2
 + Choice_1_5_2 + Choice_1_6_2 + Choice_1_7_2 + Choice_1_8_2 + Choice_1_9_2
 = 1
Column_615_Unique_2: Choice_2_1_2 + Choice_2_2_2 + Choice_2_3_2 + Choice_2_4_2
 + Choice_2_5_2 + Choice_2_6_2 + Choice_2_7_2 + Choice_2_8_2 + Choice_2_9_2
 = 1
Column_615_Unique_3: Choice_3_1_2 + Choice_3_2_2 + Choice_3_3_2 + Choice_3_4_2
 + Choice_3_5_2 + Choice_3_6_2 + Choice_3_7_2 + Choice_3_8_2 + Choice_3_9_2
 = 1
Column_615_Unique_4: Choice_4_1_2 + Choice_4_2_2 + Choice_4_3_2 + Choice_4_4_2
 + Choice_4_5_2 + Choice_4_6_2 + Choice_4_7_2 + Choice_4_8_2 + Choice_4_9_2
 = 1
Column_615_Unique_5: Choice_5_1_2 + Choice_5_2_2 + Choice_5_3_2 + Choice_5_4_2
 + Choice_5_5_2 + Choice_5_6_2 + Choice_5_7_2 + Choice_5_8_2 + Choice_5_9_2
 = 1
Column_615_Unique_6: Choice_6_1_2 + Choice_6_2_2 + Choice_6_3_2 + Choice_6_4_2
 + Choice_6_5_2 + Choice_6_6_2 + Choice_6_7_2 + Choice_6_8_2 + Choice_6_9_2
 = 1
Column_615_Unique_7: Choice_7_1_2 + Choice_7_2_2 + Choice_7_3_2 + Choice_7_4_2
 + Choice_7_5_2 + Choice_7_6_2 + Choice_7_7_2 + Choice_7_8_2 + Choice_7_9_2
 = 1
Column_615_Unique_8: Choice_8_1_2 + Choice_8_2_2 + Choice_8_3_2 + Choice_8_4_2
 + Choice_8_5_2 + Choice_8_6_2 + Choice_8_7_2 + Choice_8_8_2 + Choice_8_9_2
 = 1
Column_615_Unique_9: Choice_9_1_2 + Choice_9_2_2 + Choice_9_3_2 + Choice_9_4_2
 + Choice_9_5_2 + Choice_9_6_2 + Choice_9_7_2 + Choice_9_8_2 + Choice_9_9_2
 = 1
Column_616_Unique_1: Choice_1_1_3 + Choice_1_2_3 + Choice_1_3_3 + Choice_1_4_3
 + Choice_1_5_3 + Choice_1_6_3 + Choice_1_7_3 + Choice_1_8_3 + Choice_1_9_3
 = 1
Column_616_Unique_2: Choice_2_1_3 + Choice_2_2_3 + Choice_2_3_3 + Choice_2_4_3
 + Choice_2_5_3 + Choice_2_6_3 + Choice_2_7_3 + Choice_2_8_3 + Choice_2_9_3
 = 1
Column_616_Unique_3: Choice_3_1_3 + Choice_3_2_3 + Choice_3_3_3 + Choice_3_4_3
 + Choice_3_5_3 + Choice_3_6_3 + Choice_3_7_3 + Choice_3_8_3 + Choice_3_9_3
 = 1
Column_616_Unique_4: Choice_4_1_3 + Choice_4_2_3 + Choice_4_3_3 + Choice_4_4_3
 + Choice_4_5_3 + Choice_4_6_3 + Choice_4_7_3 + Choice_4_8_3 + Choice_4_9_3
 = 1
Column_616_Unique_5: Choice_5_1_3 + Choice_5_2_3 + Choice_5_3_3 + Choice_5_4_3
 + Choice_5_5_3 + Choice_5_6_3 + Choice_5_7_3 + Choice_5_8_3 + Choice_5_9_3
 = 1
Column_616_Unique_6: Choice_6_1_3 + Choice_6_2_3 + Choice_6_3_3 + Choice_6_4_3
 + Choice_6_5_3 + Choice_6_6_3 + Choice_6_7_3 + Choice_6_8_3 + Choice_6_9_3
 = 1
Column_616_Unique_7: Choice_7_1_3 + Choice_7_2_3 + Choice_7_3_3 + Choice_7_4_3
 + Choice_7_5_3 + Choice_7_6_3 + Choice_7_7_3 + Choice_7_8_3 + Choice_7_9_3
 = 1
Column_616_Unique_8: Choice_8_1_3 + Choice_8_2_3 + Choice_8_3_3 + Choice_8_4_3
 + Choice_8_5_3 + Choice_8_6_3 + Choice_8_7_3 + Choice_8_8_3 + Choice_8_9_3
 = 1
Column_616_Unique_9: Choice_9_1_3 + Choice_9_2_3 + Choice_9_3_3 + Choice_9_4_3
 + Choice_9_5_3 + Choice_9_6_3 + Choice_9_7_3 + Choice_9_8_3 + Choice_9_9_3
 = 1
Column_617_Unique_1: Choice_1_1_4 + Choice_1_2_4 + Choice_1_3_4 + Choice_1_4_4
 + Choice_1_5_4 + Choice_1_6_4 + Choice_1_7_4 + Choice_1_8_4 + Choice_1_9_4
 = 1
Column_617_Unique_2: Choice_2_1_4 + Choice_2_2_4 + Choice_2_3_4 + Choice_2_4_4
 + Choice_2_5_4 + Choice_2_6_4 + Choice_2_7_4 + Choice_2_8_4 + Choice_2_9_4
 = 1
Column_617_Unique_3: Choice_3_1_4 + Choice_3_2_4 + Choice_3_3_4 + Choice_3_4_4
 + Choice_3_5_4 + Choice_3_6_4 + Choice_3_7_4 + Choice_3_8_4 + Choice_3_9_4
 = 1
Column_617_Unique_4: Choice_4_1_4 + Choice_4_2_4 + Choice_4_3_4 + Choice_4_4_4
 + Choice_4_5_4 + Choice_4_6_4 + Choice_4_7_4 + Choice_4_8_4 + Choice_4_9_4
 = 1
Column_617_Unique_5: Choice_5_1_4 + Choice_5_2_4 + Choice_5_3_4 + Choice_5_4_4
 + Choice_5_5_4 + Choice_5_6_4 + Choice_5_7_4 + Choice_5_8_4 + Choice_5_9_4
 = 1
Column_617_Unique_6: Choice_6_1_4 + Choice_6_2_4 + Choice_6_3_4 + Choice_6_4_4
 + Choice_6_5_4 + Choice_6_6_4 + Choice_6_7_4 + Choice_6_8_4 + Choice_6_9_4
 = 1
Column_617_Unique_7: Choice_7_1_4 + Choice_7_2_4 + Choice_7_3_4 + Choice_7_4_4
 + Choice_7_5_4 + Choice_7_6_4 + Choice_7_7_4 + Choice_7_8_4 + Choice_7_9_4
 = 1
Column_617_Unique_8: Choice_8_1_4 + Choice_8_2_4 + Choice_8_3_4 + Choice_8_4_4
 + Choice_8_5_4 + Choice_8_6_4 + Choice_8_7_4 + Choice_8_8_4 + Choice_8_9_4
 = 1
Column_617_Unique_9: Choice_9_1_4 + Choice_9_2_4 + Choice_9_3_4 + Choice_9_4_4
 + Choice_9_5_4 + Choice_9_6_4 + Choice_9_7_4 + Choice_9_8_4 + Choice_9_9_4
 = 1
Column_618_Unique_1: Choice_1_1_5 + Choice_1_2_5 + Choice_1_3_5 + Choice_1_4_5
 + Choice_1_5_5 + Choice_1_6_5 + Choice_1_7_5 + Choice_1_8_5 + Choice_1_9_5
 = 1
Column_618_Unique_2: Choice_2_1_5 + Choice_2_2_5 + Choice_2_3_5 + Choice_2_4_5
 + Choice_2_5_5 + Choice_2_6_5 + Choice_2_7_5 + Choice_2_8_5 + Choice_2_9_5
 = 1
Column_618_Unique_3: Choice_3_1_5 + Choice_3_2_5 + Choice_3_3_5 + Choice_3_4_5
 + Choice_3_5_5 + Choice_3_6_5 + Choice_3_7_5 + Choice_3_8_5 + Choice_3_9_5
 = 1
Column_618_Unique_4: Choice_4_1_5 + Choice_4_2_5 + Choice_4_3_5 + Choice_4_4_5
 + Choice_4_5_5 + Choice_4_6_5 + Choice_4_7_5 + Choice_4_8_5 + Choice_4_9_5
 = 1
Column_618_Unique_5: Choice_5_1_5 + Choice_5_2_5 + Choice_5_3_5 + Choice_5_4_5
 + Choice_5_5_5 + Choice_5_6_5 + Choice_5_7_5 + Choice_5_8_5 + Choice_5_9_5
 = 1
Column_618_Unique_6: Choice_6_1_5 + Choice_6_2_5 + Choice_6_3_5 + Choice_6_4_5
 + Choice_6_5_5 + Choice_6_6_5 + Choice_6_7_5 + Choice_6_8_5 + Choice_6_9_5
 = 1
Column_618_Unique_7: Choice_7_1_5 + Choice_7_2_5 + Choice_7_3_5 + Choice_7_4_5
 + Choice_7_5_5 + Choice_7_6_5 + Choice_7_7_5 + Choice_7_8_5 + Choice_7_9_5
 = 1
Column_618_Unique_8: Choice_8_1_5 + Choice_8_2_5 + Choice_8_3_5 + Choice_8_4_5
 + Choice_8_5_5 + Choice_8_6_5 + Choice_8_7_5 + Choice_8_8_5 + Choice_8_9_5
 = 1
Column_618_Unique_9: Choice_9_1_5 + Choice_9_2_5 + Choice_9_3_5 + Choice_9_4_5
 + Choice_9_5_5 + Choice_9_6_5 + Choice_9_7_5 + Choice_9_8_5 + Choice_9_9_5
 = 1
Column_619_Unique_1: Choice_1_1_6 + Choice_1_2_6 + Choice_1_3_6 + Choice_1_4_6
 + Choice_1_5_6 + Choice_1_6_6 + Choice_1_7_6 + Choice_1_8_6 + Choice_1_9_6
 = 1
Column_619_Unique_2: Choice_2_1_6 + Choice_2_2_6 + Choice_2_3_6 + Choice_2_4_6
 + Choice_2_5_6 + Choice_2_6_6 + Choice_2_7_6 + Choice_2_8_6 + Choice_2_9_6
 = 1
Column_619_Unique_3: Choice_3_1_6 + Choice_3_2_6 + Choice_3_3_6 + Choice_3_4_6
 + Choice_3_5_6 + Choice_3_6_6 + Choice_3_7_6 + Choice_3_8_6 + Choice_3_9_6
 = 1
Column_619_Unique_4: Choice_4_1_6 + Choice_4_2_6 + Choice_4_3_6 + Choice_4_4_6
 + Choice_4_5_6 + Choice_4_6_6 + Choice_4_7_6 + Choice_4_8_6 + Choice_4_9_6
 = 1
Column_619_Unique_5: Choice_5_1_6 + Choice_5_2_6 + Choice_5_3_6 + Choice_5_4_6
 + Choice_5_5_6 + Choice_5_6_6 + Choice_5_7_6 + Choice_5_8_6 + Choice_5_9_6
 = 1
Column_619_Unique_6: Choice_6_1_6 + Choice_6_2_6 + Choice_6_3_6 + Choice_6_4_6
 + Choice_6_5_6 + Choice_6_6_6 + Choice_6_7_6 + Choice_6_8_6 + Choice_6_9_6
 = 1
Column_619_Unique_7: Choice_7_1_6 + Choice_7_2_6 + Choice_7_3_6 + Choice_7_4_6
 + Choice_7_5_6 + Choice_7_6_6 + Choice_7_7_6 + Choice_7_8_6 + Choice_7_9_6
 = 1
Column_619_Unique_8: Choice_8_1_6 + Choice_8_2_6 + Choice_8_3_6 + Choice_8_4_6
 + Choice_8_5_6 + Choice_8_6_6 + Choice_8_7_6 + Choice_8_8_6 + Choice_8_9_6
 = 1
Column_619_Unique_9: Choice_9_1_6 + Choice_9_2_6 + Choice_9_3_6 + Choice_9_4_6
 + Choice_9_5_6 + Choice_9_6_6 + Choice_9_7_6 + Choice_9_8_6 + Choice_9_9_6
 = 1
Column_620_Unique_1: Choice_1_1_7 + Choice_1_2_7 + Choice_1_3_7 + Choice_1_4_7
 + Choice_1_5_7 + Choice_1_6_7 + Choice_1_7_7 + Choice_1_8_7 + Choice_1_9_7
 = 1
Column_620_Unique_2: Choice_2_1_7 + Choice_2_2_7 + Choice_2_3_7 + Choice_2_4_7
 + Choice_2_5_7 + Choice_2_6_7 + Choice_2_7_7 + Choice_2_8_7 + Choice_2_9_7
 = 1
Column_620_Unique_3: Choice_3_1_7 + Choice_3_2_7 + Choice_3_3_7 + Choice_3_4_7
 + Choice_3_5_7 + Choice_3_6_7 + Choice_3_7_7 + Choice_3_8_7 + Choice_3_9_7
 = 1
Column_620_Unique_4: Choice_4_1_7 + Choice_4_2_7 + Choice_4_3_7 + Choice_4_4_7
 + Choice_4_5_7 + Choice_4_6_7 + Choice_4_7_7 + Choice_4_8_7 + Choice_4_9_7
 = 1
Column_620_Unique_5: Choice_5_1_7 + Choice_5_2_7 + Choice_5_3_7 + Choice_5_4_7
 + Choice_5_5_7 + Choice_5_6_7 + Choice_5_7_7 + Choice_5_8_7 + Choice_5_9_7
 = 1
Column_620_Unique_6: Choice_6_1_7 + Choice_6_2_7 + Choice_6_3_7 + Choice_6_4_7
 + Choice_6_5_7 + Choice_6_6_7 + Choice_6_7_7 + Choice_6_8_7 + Choice_6_9_7
 = 1
Column_620_Unique_7: Choice_7_1_7 + Choice_7_2_7 + Choice_7_3_7 + Choice_7_4_7
 + Choice_7_5_7 + Choice_7_6_7 + Choice_7_7_7 + Choice_7_8_7 + Choice_7_9_7
 = 1
Column_620_Unique_8: Choice_8_1_7 + Choice_8_2_7 + Choice_8_3_7 + Choice_8_4_7
 + Choice_8_5_7 + Choice_8_6_7 + Choice_8_7_7 + Choice_8_8_7 + Choice_8_9_7
 = 1
Column_620_Unique_9: Choice_9_1_7 + Choice_9_2_7 + Choice_9_3_7 + Choice_9_4_7
 + Choice_9_5_7 + Choice_9_6_7 + Choice_9_7_7 + Choice_9_8_7 + Choice_9_9_7
 = 1
Column_621_Unique_1: Choice_1_1_8 + Choice_1_2_8 + Choice_1_3_8 + Choice_1_4_8
 + Choice_1_5_8 + Choice_1_6_8 + Choice_1_7_8 + Choice_1_8_8 + Choice_1_9_8
 = 1
Column_621_Unique_2: Choice_2_1_8 + Choice_2_2_8 + Choice_2_3_8 + Choice_2_4_8
 + Choice_2_5_8 + Choice_2_6_8 + Choice_2_7_8 + Choice_2_8_8 + Choice_2_9_8
 = 1
Column_621_Unique_3: Choice_3_1_8 + Choice_3_2_8 + Choice_3_3_8 + Choice_3_4_8
 + Choice_3_5_8 + Choice_3_6_8 + Choice_3_7_8 + Choice_3_8_8 + Choice_3_9_8
 = 1
Column_621_Unique_4: Choice_4_1_8 + Choice_4_2_8 + Choice_4_3_8 + Choice_4_4_8
 + Choice_4_5_8 + Choice_4_6_8 + Choice_4_7_8 + Choice_4_8_8 + Choice_4_9_8
 = 1
Column_621_Unique_5: Choice_5_1_8 + Choice_5_2_8 + Choice_5_3_8 + Choice_5_4_8
 + Choice_5_5_8 + Choice_5_6_8 + Choice_5_7_8 + Choice_5_8_8 + Choice_5_9_8
 = 1
Column_621_Unique_6: Choice_6_1_8 + Choice_6_2_8 + Choice_6_3_8 + Choice_6_4_8
 + Choice_6_5_8 + Choice_6_6_8 + Choice_6_7_8 + Choice_6_8_8 + Choice_6_9_8
 = 1
Column_621_Unique_7: Choice_7_1_8 + Choice_7_2_8 + Choice_7_3_8 + Choice_7_4_8
 + Choice_7_5_8 + Choice_7_6_8 + Choice_7_7_8 + Choice_7_8_8 + Choice_7_9_8
 = 1
Column_621_Unique_8: Choice_8_1_8 + Choice_8_2_8 + Choice_8_3_8 + Choice_8_4_8
 + Choice_8_5_8 + Choice_8_6_8 + Choice_8_7_8 + Choice_8_8_8 + Choice_8_9_8
 = 1
Column_621_Unique_9: Choice_9_1_8 + Choice_9_2_8 + Choice_9_3_8 + Choice_9_4_8
 + Choice_9_5_8 + Choice_9_6_8 + Choice_9_7_8 + Choice_9_8_8 + Choice_9_9_8
 = 1
Column_622_Unique_1: Choice_1_1_9 + Choice_1_2_9 + Choice_1_3_9 + Choice_1_4_9
 + Choice_1_5_9 + Choice_1_6_9 + Choice_1_7_9 + Choice_1_8_9 + Choice_1_9_9
 = 1
Column_622_Unique_2: Choice_2_1_9 + Choice_2_2_9 + Choice_2_3_9 + Choice_2_4_9
 + Choice_2_5_9 + Choice_2_6_9 + Choice_2_7_9 + Choice_2_8_9 + Choice_2_9_9
 = 1
Column_622_Unique_3: Choice_3_1_9 + Choice_3_2_9 + Choice_3_3_9 + Choice_3_4_9
 + Choice_3_5_9 + Choice_3_6_9 + Choice_3_7_9 + Choice_3_8_9 + Choice_3_9_9
 = 1
Column_622_Unique_4: Choice_4_1_9 + Choice_4_2_9 + Choice_4_3_9 + Choice_4_4_9
 + Choice_4_5_9 + Choice_4_6_9 + Choice_4_7_9 + Choice_4_8_9 + Choice_4_9_9
 = 1
Column_622_Unique_5: Choice_5_1_9 + Choice_5_2_9 + Choice_5_3_9 + Choice_5_4_9
 + Choice_5_5_9 + Choice_5_6_9 + Choice_5_7_9 + Choice_5_8_9 + Choice_5_9_9
 = 1
Column_622_Unique_6: Choice_6_1_9 + Choice_6_2_9 + Choice_6_3_9 + Choice_6_4_9
 + Choice_6_5_9 + Choice_6_6_9 + Choice_6_7_9 + Choice_6_8_9 + Choice_6_9_9
 = 1
Column_622_Unique_7: Choice_7_1_9 + Choice_7_2_9 + Choice_7_3_9 + Choice_7_4_9
 + Choice_7_5_9 + Choice_7_6_9 + Choice_7_7_9 + Choice_7_8_9 + Choice_7_9_9
 = 1
Column_622_Unique_8: Choice_8_1_9 + Choice_8_2_9 + Choice_8_3_9 + Choice_8_4_9
 + Choice_8_5_9 + Choice_8_6_9 + Choice_8_7_9 + Choice_8_8_9 + Choice_8_9_9
 = 1
Column_622_Unique_9: Choice_9_1_9 + Choice_9_2_9 + Choice_9_3_9 + Choice_9_4_9
 + Choice_9_5_9 + Choice_9_6_9 + Choice_9_7_9 + Choice_9_8_9 + Choice_9_9_9
 = 1
FixedDifferencePair_655: Abs_Difference_1 - FixedDifferencePair = 0
FixedDifferencePair_656: Abs_Difference_2 - FixedDifferencePair = 0
FixedDifferencePair_657: Abs_Difference_3 - FixedDifferencePair = 0
FixedDifferencePair_658: Abs_Difference_4 - FixedDifferencePair = 0
FixedDifferencePair_659: Abs_Difference_5 - FixedDifferencePair = 0
FixedDifferencePair_660: Abs_Difference_6 - FixedDifferencePair = 0
FixedDifferencePair_661: Abs_Difference_7 - FixedDifferencePair = 0
FixedDifferencePair_662: Abs_Difference_8 - FixedDifferencePair = 0
FixedDifferencePair_663: Abs_Difference_9 - FixedDifferencePair = 0
FixedProductPair_644: - FixedProductPair + Log10_1_5 + Log10_1_6 = 0
FixedProductPair_645: - FixedProductPair + Log10_6_3 + Log10_7_3 = 0
FixedProductPair_646: - FixedProductPair + Log10_6_2 + Log10_7_2 = 0
FixedRatioPair_647: Abs_Difference_0 - FixedRatioPair = 0
FixedSumPair_648: - FixedSumPair + Values_4_2 + Values_5_2 = 0
FixedSumPair_649: - FixedSumPair + Values_6_2 + Values_6_3 = 0
FixedSumPair_650: - FixedSumPair + Values_4_7 + Values_5_7 = 0
FixedSumPair_651: - FixedSumPair + Values_4_8 + Values_4_9 = 0
FixedSumPair_652: - FixedSumPair + Values_5_8 + Values_5_9 = 0
FixedSumPair_653: - FixedSumPair + Values_6_7 + Values_6_8 = 0
FixedSumPair_654: - FixedSumPair + Values_9_1 + Values_9_2 = 0
Imposible_1_1_1: Choice_1_1_1 = 0
Imposible_1_1_2: Choice_1_1_2 = 0
Imposible_1_1_3: Choice_1_1_3 = 0
Imposible_1_1_5: Choice_1_1_5 = 0
Imposible_1_1_6: Choice_1_1_6 = 0
Imposible_1_1_7: Choice_1_1_7 = 0
Imposible_1_1_8: Choice_1_1_8 = 0
Imposible_1_1_9: Choice_1_1_9 = 0
Imposible_1_2_1: Choice_1_2_1 = 0
Imposible_1_2_2: Choice_1_2_2 = 0
Imposible_1_2_3: Choice_1_2_3 = 0
Imposible_1_2_4: Choice_1_2_4 = 0
Imposible_1_2_5: Choice_1_2_5 = 0
Imposible_1_2_6: Choice_1_2_6 = 0
Imposible_1_2_8: Choice_1_2_8 = 0
Imposible_1_2_9: Choice_1_2_9 = 0
Imposible_1_3_1: Choice_1_3_1 = 0
Imposible_1_3_2: Choice_1_3_2 = 0
Imposible_1_3_4: Choice_1_3_4 = 0
Imposible_1_3_5: Choice_1_3_5 = 0
Imposible_1_3_6: Choice_1_3_6 = 0
Imposible_1_3_7: Choice_1_3_7 = 0
Imposible_1_3_8: Choice_1_3_8 = 0
Imposible_1_3_9: Choice_1_3_9 = 0
Imposible_1_4_1: Choice_1_4_1 = 0
Imposible_1_4_2: Choice_1_4_2 = 0
Imposible_1_4_3: Choice_1_4_3 = 0
Imposible_1_4_4: Choice_1_4_4 = 0
Imposible_1_4_5: Choice_1_4_5 = 0
Imposible_1_4_6: Choice_1_4_6 = 0
Imposible_1_4_7: Choice_1_4_7 = 0
Imposible_1_4_8: Choice_1_4_8 = 0
Imposible_1_5_1: Choice_1_5_1 = 0
Imposible_1_5_2: Choice_1_5_2 = 0
Imposible_1_5_3: Choice_1_5_3 = 0
Imposible_1_5_4: Choice_1_5_4 = 0
Imposible_1_5_5: Choice_1_5_5 = 0
Imposible_1_5_7: Choice_1_5_7 = 0
Imposible_1_5_8: Choice_1_5_8 = 0
Imposible_1_5_9: Choice_1_5_9 = 0
Imposible_1_6_2: Choice_1_6_2 = 0
Imposible_1_6_3: Choice_1_6_3 = 0
Imposible_1_6_4: Choice_1_6_4 = 0
Imposible_1_6_5: Choice_1_6_5 = 0
Imposible_1_6_6: Choice_1_6_6 = 0
Imposible_1_6_7: Choice_1_6_7 = 0
Imposible_1_6_8: Choice_1_6_8 = 0
Imposible_1_6_9: Choice_1_6_9 = 0
Imposible_1_7_1: Choice_1_7_1 = 0
Imposible_1_7_2: Choice_1_7_2 = 0
Imposible_1_7_3: Choice_1_7_3 = 0
Imposible_1_7_4: Choice_1_7_4 = 0
Imposible_1_7_5: Choice_1_7_5 = 0
Imposible_1_7_6: Choice_1_7_6 = 0
Imposible_1_7_7: Choice_1_7_7 = 0
Imposible_1_7_9: Choice_1_7_9 = 0
Imposible_1_8_1: Choice_1_8_1 = 0
Imposible_1_8_2: Choice_1_8_2 = 0
Imposible_1_8_3: Choice_1_8_3 = 0
Imposible_1_8_4: Choice_1_8_4 = 0
Imposible_1_8_6: Choice_1_8_6 = 0
Imposible_1_8_7: Choice_1_8_7 = 0
Imposible_1_8_8: Choice_1_8_8 = 0
Imposible_1_8_9: Choice_1_8_9 = 0
Imposible_1_9_1: Choice_1_9_1 = 0
Imposible_1_9_3: Choice_1_9_3 = 0
Imposible_1_9_4: Choice_1_9_4 = 0
Imposible_1_9_5: Choice_1_9_5 = 0
Imposible_1_9_6: Choice_1_9_6 = 0
Imposible_1_9_7: Choice_1_9_7 = 0
Imposible_1_9_8: Choice_1_9_8 = 0
Imposible_1_9_9: Choice_1_9_9 = 0
Imposible_2_1_1: Choice_2_1_1 = 0
Imposible_2_1_2: Choice_2_1_2 = 0
Imposible_2_1_3: Choice_2_1_3 = 0
Imposible_2_1_4: Choice_2_1_4 = 0
Imposible_2_1_5: Choice_2_1_5 = 0
Imposible_2_1_6: Choice_2_1_6 = 0
Imposible_2_1_7: Choice_2_1_7 = 0
Imposible_2_1_9: Choice_2_1_9 = 0
Imposible_2_2_2: Choice_2_2_2 = 0
Imposible_2_2_3: Choice_2_2_3 = 0
Imposible_2_2_4: Choice_2_2_4 = 0
Imposible_2_2_5: Choice_2_2_5 = 0
Imposible_2_2_6: Choice_2_2_6 = 0
Imposible_2_2_7: Choice_2_2_7 = 0
Imposible_2_2_8: Choice_2_2_8 = 0
Imposible_2_2_9: Choice_2_2_9 = 0
Imposible_2_3_1: Choice_2_3_1 = 0
Imposible_2_3_2: Choice_2_3_2 = 0
Imposible_2_3_3: Choice_2_3_3 = 0
Imposible_2_3_5: Choice_2_3_5 = 0
Imposible_2_3_6: Choice_2_3_6 = 0
Imposible_2_3_7: Choice_2_3_7 = 0
Imposible_2_3_8: Choice_2_3_8 = 0
Imposible_2_3_9: Choice_2_3_9 = 0
Imposible_2_4_1: Choice_2_4_1 = 0
Imposible_2_4_3: Choice_2_4_3 = 0
Imposible_2_4_4: Choice_2_4_4 = 0
Imposible_2_4_5: Choice_2_4_5 = 0
Imposible_2_4_6: Choice_2_4_6 = 0
Imposible_2_4_7: Choice_2_4_7 = 0
Imposible_2_4_8: Choice_2_4_8 = 0
Imposible_2_4_9: Choice_2_4_9 = 0
Imposible_2_5_1: Choice_2_5_1 = 0
Imposible_2_5_2: Choice_2_5_2 = 0
Imposible_2_5_3: Choice_2_5_3 = 0
Imposible_2_5_4: Choice_2_5_4 = 0
Imposible_2_5_6: Choice_2_5_6 = 0
Imposible_2_5_7: Choice_2_5_7 = 0
Imposible_2_5_8: Choice_2_5_8 = 0
Imposible_2_5_9: Choice_2_5_9 = 0
Imposible_2_6_1: Choice_2_6_1 = 0
Imposible_2_6_2: Choice_2_6_2 = 0
Imposible_2_6_3: Choice_2_6_3 = 0
Imposible_2_6_4: Choice_2_6_4 = 0
Imposible_2_6_5: Choice_2_6_5 = 0
Imposible_2_6_6: Choice_2_6_6 = 0
Imposible_2_6_8: Choice_2_6_8 = 0
Imposible_2_6_9: Choice_2_6_9 = 0
Imposible_2_7_1: Choice_2_7_1 = 0
Imposible_2_7_2: Choice_2_7_2 = 0
Imposible_2_7_4: Choice_2_7_4 = 0
Imposible_2_7_5: Choice_2_7_5 = 0
Imposible_2_7_6: Choice_2_7_6 = 0
Imposible_2_7_7: Choice_2_7_7 = 0
Imposible_2_7_8: Choice_2_7_8 = 0
Imposible_2_7_9: Choice_2_7_9 = 0
Imposible_2_8_1: Choice_2_8_1 = 0
Imposible_2_8_2: Choice_2_8_2 = 0
Imposible_2_8_3: Choice_2_8_3 = 0
Imposible_2_8_4: Choice_2_8_4 = 0
Imposible_2_8_5: Choice_2_8_5 = 0
Imposible_2_8_6: Choice_2_8_6 = 0
Imposible_2_8_7: Choice_2_8_7 = 0
Imposible_2_8_8: Choice_2_8_8 = 0
Imposible_2_9_1: Choice_2_9_1 = 0
Imposible_2_9_2: Choice_2_9_2 = 0
Imposible_2_9_3: Choice_2_9_3 = 0
Imposible_2_9_4: Choice_2_9_4 = 0
Imposible_2_9_5: Choice_2_9_5 = 0
Imposible_2_9_7: Choice_2_9_7 = 0
Imposible_2_9_8: Choice_2_9_8 = 0
Imposible_2_9_9: Choice_2_9_9 = 0
Imposible_3_1_1: Choice_3_1_1 = 0
Imposible_3_1_2: Choice_3_1_2 = 0
Imposible_3_1_3: Choice_3_1_3 = 0
Imposible_3_1_4: Choice_3_1_4 = 0
Imposible_3_1_5: Choice_3_1_5 = 0
Imposible_3_1_7: Choice_3_1_7 = 0
Imposible_3_1_8: Choice_3_1_8 = 0
Imposible_3_1_9: Choice_3_1_9 = 0
Imposible_3_2_1: Choice_3_2_1 = 0
Imposible_3_2_2: Choice_3_2_2 = 0
Imposible_3_2_4: Choice_3_2_4 = 0
Imposible_3_2_5: Choice_3_2_5 = 0
Imposible_3_2_6: Choice_3_2_6 = 0
Imposible_3_2_7: Choice_3_2_7 = 0
Imposible_3_2_8: Choice_3_2_8 = 0
Imposible_3_2_9: Choice_3_2_9 = 0
Imposible_3_3_1: Choice_3_3_1 = 0
Imposible_3_3_2: Choice_3_3_2 = 0
Imposible_3_3_3: Choice_3_3_3 = 0
Imposible_3_3_4: Choice_3_3_4 = 0
Imposible_3_3_5: Choice_3_3_5 = 0
Imposible_3_3_6: Choice_3_3_6 = 0
Imposible_3_3_8: Choice_3_3_8 = 0
Imposible_3_3_9: Choice_3_3_9 = 0
Imposible_3_4_2: Choice_3_4_2 = 0
Imposible_3_4_3: Choice_3_4_3 = 0
Imposible_3_4_4: Choice_3_4_4 = 0
Imposible_3_4_5: Choice_3_4_5 = 0
Imposible_3_4_6: Choice_3_4_6 = 0
Imposible_3_4_7: Choice_3_4_7 = 0
Imposible_3_4_8: Choice_3_4_8 = 0
Imposible_3_4_9: Choice_3_4_9 = 0
Imposible_3_5_1: Choice_3_5_1 = 0
Imposible_3_5_2: Choice_3_5_2 = 0
Imposible_3_5_3: Choice_3_5_3 = 0
Imposible_3_5_4: Choice_3_5_4 = 0
Imposible_3_5_5: Choice_3_5_5 = 0
Imposible_3_5_6: Choice_3_5_6 = 0
Imposible_3_5_7: Choice_3_5_7 = 0
Imposible_3_5_9: Choice_3_5_9 = 0
Imposible_3_6_1: Choice_3_6_1 = 0
Imposible_3_6_2: Choice_3_6_2 = 0
Imposible_3_6_3: Choice_3_6_3 = 0
Imposible_3_6_4: Choice_3_6_4 = 0
Imposible_3_6_6: Choice_3_6_6 = 0
Imposible_3_6_7: Choice_3_6_7 = 0
Imposible_3_6_8: Choice_3_6_8 = 0
Imposible_3_6_9: Choice_3_6_9 = 0
Imposible_3_7_1: Choice_3_7_1 = 0
Imposible_3_7_3: Choice_3_7_3 = 0
Imposible_3_7_4: Choice_3_7_4 = 0
Imposible_3_7_5: Choice_3_7_5 = 0
Imposible_3_7_6: Choice_3_7_6 = 0
Imposible_3_7_7: Choice_3_7_7 = 0
Imposible_3_7_8: Choice_3_7_8 = 0
Imposible_3_7_9: Choice_3_7_9 = 0
Imposible_3_8_1: Choice_3_8_1 = 0
Imposible_3_8_2: Choice_3_8_2 = 0
Imposible_3_8_3: Choice_3_8_3 = 0
Imposible_3_8_5: Choice_3_8_5 = 0
Imposible_3_8_6: Choice_3_8_6 = 0
Imposible_3_8_7: Choice_3_8_7 = 0
Imposible_3_8_8: Choice_3_8_8 = 0
Imposible_3_8_9: Choice_3_8_9 = 0
Imposible_3_9_1: Choice_3_9_1 = 0
Imposible_3_9_2: Choice_3_9_2 = 0
Imposible_3_9_3: Choice_3_9_3 = 0
Imposible_3_9_4: Choice_3_9_4 = 0
Imposible_3_9_5: Choice_3_9_5 = 0
Imposible_3_9_6: Choice_3_9_6 = 0
Imposible_3_9_7: Choice_3_9_7 = 0
Imposible_3_9_8: Choice_3_9_8 = 0
Imposible_4_1_1: Choice_4_1_1 = 0
Imposible_4_1_2: Choice_4_1_2 = 0
Imposible_4_1_3: Choice_4_1_3 = 0
Imposible_4_1_4: Choice_4_1_4 = 0
Imposible_4_1_6: Choice_4_1_6 = 0
Imposible_4_1_7: Choice_4_1_7 = 0
Imposible_4_1_8: Choice_4_1_8 = 0
Imposible_4_1_9: Choice_4_1_9 = 0
Imposible_4_2_1: Choice_4_2_1 = 0
Imposible_4_2_2: Choice_4_2_2 = 0
Imposible_4_2_3: Choice_4_2_3 = 0
Imposible_4_2_4: Choice_4_2_4 = 0
Imposible_4_2_5: Choice_4_2_5 = 0
Imposible_4_2_6: Choice_4_2_6 = 0
Imposible_4_2_7: Choice_4_2_7 = 0
Imposible_4_2_9: Choice_4_2_9 = 0
Imposible_4_3_2: Choice_4_3_2 = 0
Imposible_4_3_3: Choice_4_3_3 = 0
Imposible_4_3_4: Choice_4_3_4 = 0
Imposible_4_3_5: Choice_4_3_5 = 0
Imposible_4_3_6: Choice_4_3_6 = 0
Imposible_4_3_7: Choice_4_3_7 = 0
Imposible_4_3_8: Choice_4_3_8 = 0
Imposible_4_3_9: Choice_4_3_9 = 0
Imposible_4_4_1: Choice_4_4_1 = 0
Imposible_4_4_2: Choice_4_4_2 = 0
Imposible_4_4_3: Choice_4_4_3 = 0
Imposible_4_4_4: Choice_4_4_4 = 0
Imposible_4_4_5: Choice_4_4_5 = 0
Imposible_4_4_6: Choice_4_4_6 = 0
Imposible_4_4_8: Choice_4_4_8 = 0
Imposible_4_4_9: Choice_4_4_9 = 0
Imposible_4_5_1: Choice_4_5_1 = 0
Imposible_4_5_2: Choice_4_5_2 = 0
Imposible_4_5_3: Choice_4_5_3 = 0
Imposible_4_5_5: Choice_4_5_5 = 0
Imposible_4_5_6: Choice_4_5_6 = 0
Imposible_4_5_7: Choice_4_5_7 = 0
Imposible_4_5_8: Choice_4_5_8 = 0
Imposible_4_5_9: Choice_4_5_9 = 0
Imposible_4_6_1: Choice_4_6_1 = 0
Imposible_4_6_3: Choice_4_6_3 = 0
Imposible_4_6_4: Choice_4_6_4 = 0
Imposible_4_6_5: Choice_4_6_5 = 0
Imposible_4_6_6: Choice_4_6_6 = 0
Imposible_4_6_7: Choice_4_6_7 = 0
Imposible_4_6_8: Choice_4_6_8 = 0
Imposible_4_6_9: Choice_4_6_9 = 0
Imposible_4_7_1: Choice_4_7_1 = 0
Imposible_4_7_2: Choice_4_7_2 = 0
Imposible_4_7_3: Choice_4_7_3 = 0
Imposible_4_7_4: Choice_4_7_4 = 0
Imposible_4_7_5: Choice_4_7_5 = 0
Imposible_4_7_6: Choice_4_7_6 = 0
Imposible_4_7_7: Choice_4_7_7 = 0
Imposible_4_7_8: Choice_4_7_8 = 0
Imposible_4_8_1: Choice_4_8_1 = 0
Imposible_4_8_2: Choice_4_8_2 = 0
Imposible_4_8_3: Choice_4_8_3 = 0
Imposible_4_8_4: Choice_4_8_4 = 0
Imposible_4_8_5: Choice_4_8_5 = 0
Imposible_4_8_7: Choice_4_8_7 = 0
Imposible_4_8_8: Choice_4_8_8 = 0
Imposible_4_8_9: Choice_4_8_9 = 0
Imposible_4_9_1: Choice_4_9_1 = 0
Imposible_4_9_2: Choice_4_9_2 = 0
Imposible_4_9_4: Choice_4_9_4 = 0
Imposible_4_9_5: Choice_4_9_5 = 0
Imposible_4_9_6: Choice_4_9_6 = 0
Imposible_4_9_7: Choice_4_9_7 = 0
Imposible_4_9_8: Choice_4_9_8 = 0
Imposible_4_9_9: Choice_4_9_9 = 0
Imposible_5_1_1: Choice_5_1_1 = 0
Imposible_5_1_2: Choice_5_1_2 = 0
Imposible_5_1_4: Choice_5_1_4 = 0
Imposible_5_1_5: Choice_5_1_5 = 0
Imposible_5_1_6: Choice_5_1_6 = 0
Imposible_5_1_7: Choice_5_1_7 = 0
Imposible_5_1_8: Choice_5_1_8 = 0
Imposible_5_1_9: Choice_5_1_9 = 0
Imposible_5_2_1: Choice_5_2_1 = 0
Imposible_5_2_2: Choice_5_2_2 = 0
Imposible_5_2_3: Choice_5_2_3 = 0
Imposible_5_2_5: Choice_5_2_5 = 0
Imposible_5_2_6: Choice_5_2_6 = 0
Imposible_5_2_7: Choice_5_2_7 = 0
Imposible_5_2_8: Choice_5_2_8 = 0
Imposible_5_2_9: Choice_5_2_9 = 0
Imposible_5_3_1: Choice_5_3_1 = 0
Imposible_5_3_2: Choice_5_3_2 = 0
Imposible_5_3_3: Choice_5_3_3 = 0
Imposible_5_3_4: Choice_5_3_4 = 0
Imposible_5_3_5: Choice_5_3_5 = 0
Imposible_5_3_6: Choice_5_3_6 = 0
Imposible_5_3_7: Choice_5_3_7 = 0
Imposible_5_3_9: Choice_5_3_9 = 0
Imposible_5_4_1: Choice_5_4_1 = 0
Imposible_5_4_2: Choice_5_4_2 = 0
Imposible_5_4_3: Choice_5_4_3 = 0
Imposible_5_4_4: Choice_5_4_4 = 0
Imposible_5_4_5: Choice_5_4_5 = 0
Imposible_5_4_7: Choice_5_4_7 = 0
Imposible_5_4_8: Choice_5_4_8 = 0
Imposible_5_4_9: Choice_5_4_9 = 0
Imposible_5_5_2: Choice_5_5_2 = 0
Imposible_5_5_3: Choice_5_5_3 = 0
Imposible_5_5_4: Choice_5_5_4 = 0
Imposible_5_5_5: Choice_5_5_5 = 0
Imposible_5_5_6: Choice_5_5_6 = 0
Imposible_5_5_7: Choice_5_5_7 = 0
Imposible_5_5_8: Choice_5_5_8 = 0
Imposible_5_5_9: Choice_5_5_9 = 0
Imposible_5_6_1: Choice_5_6_1 = 0
Imposible_5_6_2: Choice_5_6_2 = 0
Imposible_5_6_3: Choice_5_6_3 = 0
Imposible_5_6_4: Choice_5_6_4 = 0
Imposible_5_6_5: Choice_5_6_5 = 0
Imposible_5_6_6: Choice_5_6_6 = 0
Imposible_5_6_7: Choice_5_6_7 = 0
Imposible_5_6_8: Choice_5_6_8 = 0
Imposible_5_7_1: Choice_5_7_1 = 0
Imposible_5_7_2: Choice_5_7_2 = 0
Imposible_5_7_3: Choice_5_7_3 = 0
Imposible_5_7_4: Choice_5_7_4 = 0
Imposible_5_7_5: Choice_5_7_5 = 0
Imposible_5_7_6: Choice_5_7_6 = 0
Imposible_5_7_8: Choice_5_7_8 = 0
Imposible_5_7_9: Choice_5_7_9 = 0
Imposible_5_8_1: Choice_5_8_1 = 0
Imposible_5_8_3: Choice_5_8_3 = 0
Imposible_5_8_4: Choice_5_8_4 = 0
Imposible_5_8_5: Choice_5_8_5 = 0
Imposible_5_8_6: Choice_5_8_6 = 0
Imposible_5_8_7: Choice_5_8_7 = 0
Imposible_5_8_8: Choice_5_8_8 = 0
Imposible_5_8_9: Choice_5_8_9 = 0
Imposible_5_9_1: Choice_5_9_1 = 0
Imposible_5_9_2: Choice_5_9_2 = 0
Imposible_5_9_3: Choice_5_9_3 = 0
Imposible_5_9_4: Choice_5_9_4 = 0
Imposible_5_9_6: Choice_5_9_6 = 0
Imposible_5_9_7: Choice_5_9_7 = 0
Imposible_5_9_8: Choice_5_9_8 = 0
Imposible_5_9_9: Choice_5_9_9 = 0
Imposible_6_1_1: Choice_6_1_1 = 0
Imposible_6_1_3: Choice_6_1_3 = 0
Imposible_6_1_4: Choice_6_1_4 = 0
Imposible_6_1_5: Choice_6_1_5 = 0
Imposible_6_1_6: Choice_6_1_6 = 0
Imposible_6_1_7: Choice_6_1_7 = 0
Imposible_6_1_8: Choice_6_1_8 = 0
Imposible_6_1_9: Choice_6_1_9 = 0
Imposible_6_2_1: Choice_6_2_1 = 0
Imposible_6_2_2: Choice_6_2_2 = 0
Imposible_6_2_3: Choice_6_2_3 = 0
Imposible_6_2_4: Choice_6_2_4 = 0
Imposible_6_2_6: Choice_6_2_6 = 0
Imposible_6_2_7: Choice_6_2_7 = 0
Imposible_6_2_8: Choice_6_2_8 = 0
Imposible_6_2_9: Choice_6_2_9 = 0
Imposible_6_3_1: Choice_6_3_1 = 0
Imposible_6_3_2: Choice_6_3_2 = 0
Imposible_6_3_3: Choice_6_3_3 = 0
Imposible_6_3_4: Choice_6_3_4 = 0
Imposible_6_3_5: Choice_6_3_5 = 0
Imposible_6_3_6: Choice_6_3_6 = 0
Imposible_6_3_7: Choice_6_3_7 = 0
Imposible_6_3_8: Choice_6_3_8 = 0
Imposible_6_4_1: Choice_6_4_1 = 0
Imposible_6_4_2: Choice_6_4_2 = 0
Imposible_6_4_3: Choice_6_4_3 = 0
Imposible_6_4_5: Choice_6_4_5 = 0
Imposible_6_4_6: Choice_6_4_6 = 0
Imposible_6_4_7: Choice_6_4_7 = 0
Imposible_6_4_8: Choice_6_4_8 = 0
Imposible_6_4_9: Choice_6_4_9 = 0
Imposible_6_5_1: Choice_6_5_1 = 0
Imposible_6_5_2: Choice_6_5_2 = 0
Imposible_6_5_3: Choice_6_5_3 = 0
Imposible_6_5_4: Choice_6_5_4 = 0
Imposible_6_5_5: Choice_6_5_5 = 0
Imposible_6_5_6: Choice_6_5_6 = 0
Imposible_6_5_8: Choice_6_5_8 = 0
Imposible_6_5_9: Choice_6_5_9 = 0
Imposible_6_6_1: Choice_6_6_1 = 0
Imposible_6_6_2: Choice_6_6_2 = 0
Imposible_6_6_4: Choice_6_6_4 = 0
Imposible_6_6_5: Choice_6_6_5 = 0
Imposible_6_6_6: Choice_6_6_6 = 0
Imposible_6_6_7: Choice_6_6_7 = 0
Imposible_6_6_8: Choice_6_6_8 = 0
Imposible_6_6_9: Choice_6_6_9 = 0
Imposible_6_7_1: Choice_6_7_1 = 0
Imposible_6_7_2: Choice_6_7_2 = 0
Imposible_6_7_3: Choice_6_7_3 = 0
Imposible_6_7_4: Choice_6_7_4 = 0
Imposible_6_7_5: Choice_6_7_5 = 0
Imposible_6_7_7: Choice_6_7_7 = 0
Imposible_6_7_8: Choice_6_7_8 = 0
Imposible_6_7_9: Choice_6_7_9 = 0
Imposible_6_8_2: Choice_6_8_2 = 0
Imposible_6_8_3: Choice_6_8_3 = 0
Imposible_6_8_4: Choice_6_8_4 = 0
Imposible_6_8_5: Choice_6_8_5 = 0
Imposible_6_8_6: Choice_6_8_6 = 0
Imposible_6_8_7: Choice_6_8_7 = 0
Imposible_6_8_8: Choice_6_8_8 = 0
Imposible_6_8_9: Choice_6_8_9 = 0
Imposible_6_9_1: Choice_6_9_1 = 0
Imposible_6_9_2: Choice_6_9_2 = 0
Imposible_6_9_3: Choice_6_9_3 = 0
Imposible_6_9_4: Choice_6_9_4 = 0
Imposible_6_9_5: Choice_6_9_5 = 0
Imposible_6_9_6: Choice_6_9_6 = 0
Imposible_6_9_7: Choice_6_9_7 = 0
Imposible_6_9_9: Choice_6_9_9 = 0
Imposible_7_1_1: Choice_7_1_1 = 0
Imposible_7_1_2: Choice_7_1_2 = 0
Imposible_7_1_3: Choice_7_1_3 = 0
Imposible_7_1_4: Choice_7_1_4 = 0
Imposible_7_1_5: Choice_7_1_5 = 0
Imposible_7_1_6: Choice_7_1_6 = 0
Imposible_7_1_8: Choice_7_1_8 = 0
Imposible_7_1_9: Choice_7_1_9 = 0
Imposible_7_2_1: Choice_7_2_1 = 0
Imposible_7_2_3: Choice_7_2_3 = 0
Imposible_7_2_4: Choice_7_2_4 = 0
Imposible_7_2_5: Choice_7_2_5 = 0
Imposible_7_2_6: Choice_7_2_6 = 0
Imposible_7_2_7: Choice_7_2_7 = 0
Imposible_7_2_8: Choice_7_2_8 = 0
Imposible_7_2_9: Choice_7_2_9 = 0
Imposible_7_3_1: Choice_7_3_1 = 0
Imposible_7_3_2: Choice_7_3_2 = 0
Imposible_7_3_3: Choice_7_3_3 = 0
Imposible_7_3_4: Choice_7_3_4 = 0
Imposible_7_3_6: Choice_7_3_6 = 0
Imposible_7_3_7: Choice_7_3_7 = 0
Imposible_7_3_8: Choice_7_3_8 = 0
Imposible_7_3_9: Choice_7_3_9 = 0
Imposible_7_4_1: Choice_7_4_1 = 0
Imposible_7_4_2: Choice_7_4_2 = 0
Imposible_7_4_4: Choice_7_4_4 = 0
Imposible_7_4_5: Choice_7_4_5 = 0
Imposible_7_4_6: Choice_7_4_6 = 0
Imposible_7_4_7: Choice_7_4_7 = 0
Imposible_7_4_8: Choice_7_4_8 = 0
Imposible_7_4_9: Choice_7_4_9 = 0
Imposible_7_5_1: Choice_7_5_1 = 0
Imposible_7_5_2: Choice_7_5_2 = 0
Imposible_7_5_3: Choice_7_5_3 = 0
Imposible_7_5_4: Choice_7_5_4 = 0
Imposible_7_5_5: Choice_7_5_5 = 0
Imposible_7_5_6: Choice_7_5_6 = 0
Imposible_7_5_7: Choice_7_5_7 = 0
Imposible_7_5_8: Choice_7_5_8 = 0
Imposible_7_6_1: Choice_7_6_1 = 0
Imposible_7_6_2: Choice_7_6_2 = 0
Imposible_7_6_3: Choice_7_6_3 = 0
Imposible_7_6_4: Choice_7_6_4 = 0
Imposible_7_6_5: Choice_7_6_5 = 0
Imposible_7_6_7: Choice_7_6_7 = 0
Imposible_7_6_8: Choice_7_6_8 = 0
Imposible_7_6_9: Choice_7_6_9 = 0
Imposible_7_7_2: Choice_7_7_2 = 0
Imposible_7_7_3: Choice_7_7_3 = 0
Imposible_7_7_4: Choice_7_7_4 = 0
Imposible_7_7_5: Choice_7_7_5 = 0
Imposible_7_7_6: Choice_7_7_6 = 0
Imposible_7_7_7: Choice_7_7_7 = 0
Imposible_7_7_8: Choice_7_7_8 = 0
Imposible_7_7_9: Choice_7_7_9 = 0
Imposible_7_8_1: Choice_7_8_1 = 0
Imposible_7_8_2: Choice_7_8_2 = 0
Imposible_7_8_3: Choice_7_8_3 = 0
Imposible_7_8_4: Choice_7_8_4 = 0
Imposible_7_8_5: Choice_7_8_5 = 0
Imposible_7_8_6: Choice_7_8_6 = 0
Imposible_7_8_7: Choice_7_8_7 = 0
Imposible_7_8_9: Choice_7_8_9 = 0
Imposible_7_9_1: Choice_7_9_1 = 0
Imposible_7_9_2: Choice_7_9_2 = 0
Imposible_7_9_3: Choice_7_9_3 = 0
Imposible_7_9_5: Choice_7_9_5 = 0
Imposible_7_9_6: Choice_7_9_6 = 0
Imposible_7_9_7: Choice_7_9_7 = 0
Imposible_7_9_8: Choice_7_9_8 = 0
Imposible_7_9_9: Choice_7_9_9 = 0
Imposible_8_1_2: Choice_8_1_2 = 0
Imposible_8_1_3: Choice_8_1_3 = 0
Imposible_8_1_4: Choice_8_1_4 = 0
Imposible_8_1_5: Choice_8_1_5 = 0
Imposible_8_1_6: Choice_8_1_6 = 0
Imposible_8_1_7: Choice_8_1_7 = 0
Imposible_8_1_8: Choice_8_1_8 = 0
Imposible_8_1_9: Choice_8_1_9 = 0
Imposible_8_2_1: Choice_8_2_1 = 0
Imposible_8_2_2: Choice_8_2_2 = 0
Imposible_8_2_3: Choice_8_2_3 = 0
Imposible_8_2_4: Choice_8_2_4 = 0
Imposible_8_2_5: Choice_8_2_5 = 0
Imposible_8_2_6: Choice_8_2_6 = 0
Imposible_8_2_7: Choice_8_2_7 = 0
Imposible_8_2_8: Choice_8_2_8 = 0
Imposible_8_3_1: Choice_8_3_1 = 0
Imposible_8_3_2: Choice_8_3_2 = 0
Imposible_8_3_3: Choice_8_3_3 = 0
Imposible_8_3_4: Choice_8_3_4 = 0
Imposible_8_3_5: Choice_8_3_5 = 0
Imposible_8_3_7: Choice_8_3_7 = 0
Imposible_8_3_8: Choice_8_3_8 = 0
Imposible_8_3_9: Choice_8_3_9 = 0
Imposible_8_4_1: Choice_8_4_1 = 0
Imposible_8_4_2: Choice_8_4_2 = 0
Imposible_8_4_3: Choice_8_4_3 = 0
Imposible_8_4_4: Choice_8_4_4 = 0
Imposible_8_4_6: Choice_8_4_6 = 0
Imposible_8_4_7: Choice_8_4_7 = 0
Imposible_8_4_8: Choice_8_4_8 = 0
Imposible_8_4_9: Choice_8_4_9 = 0
Imposible_8_5_1: Choice_8_5_1 = 0
Imposible_8_5_3: Choice_8_5_3 = 0
Imposible_8_5_4: Choice_8_5_4 = 0
Imposible_8_5_5: Choice_8_5_5 = 0
Imposible_8_5_6: Choice_8_5_6 = 0
Imposible_8_5_7: Choice_8_5_7 = 0
Imposible_8_5_8: Choice_8_5_8 = 0
Imposible_8_5_9: Choice_8_5_9 = 0
Imposible_8_6_1: Choice_8_6_1 = 0
Imposible_8_6_2: Choice_8_6_2 = 0
Imposible_8_6_3: Choice_8_6_3 = 0
Imposible_8_6_4: Choice_8_6_4 = 0
Imposible_8_6_5: Choice_8_6_5 = 0
Imposible_8_6_6: Choice_8_6_6 = 0
Imposible_8_6_7: Choice_8_6_7 = 0
Imposible_8_6_9: Choice_8_6_9 = 0
Imposible_8_7_1: Choice_8_7_1 = 0
Imposible_8_7_2: Choice_8_7_2 = 0
Imposible_8_7_3: Choice_8_7_3 = 0
Imposible_8_7_5: Choice_8_7_5 = 0
Imposible_8_7_6: Choice_8_7_6 = 0
Imposible_8_7_7: Choice_8_7_7 = 0
Imposible_8_7_8: Choice_8_7_8 = 0
Imposible_8_7_9: Choice_8_7_9 = 0
Imposible_8_8_1: Choice_8_8_1 = 0
Imposible_8_8_2: Choice_8_8_2 = 0
Imposible_8_8_4: Choice_8_8_4 = 0
Imposible_8_8_5: Choice_8_8_5 = 0
Imposible_8_8_6: Choice_8_8_6 = 0
Imposible_8_8_7: Choice_8_8_7 = 0
Imposible_8_8_8: Choice_8_8_8 = 0
Imposible_8_8_9: Choice_8_8_9 = 0
Imposible_8_9_1: Choice_8_9_1 = 0
Imposible_8_9_2: Choice_8_9_2 = 0
Imposible_8_9_3: Choice_8_9_3 = 0
Imposible_8_9_4: Choice_8_9_4 = 0
Imposible_8_9_5: Choice_8_9_5 = 0
Imposible_8_9_6: Choice_8_9_6 = 0
Imposible_8_9_8: Choice_8_9_8 = 0
Imposible_8_9_9: Choice_8_9_9 = 0
Imposible_9_1_1: Choice_9_1_1 = 0
Imposible_9_1_2: Choice_9_1_2 = 0
Imposible_9_1_3: Choice_9_1_3 = 0
Imposible_9_1_4: Choice_9_1_4 = 0
Imposible_9_1_5: Choice_9_1_5 = 0
Imposible_9_1_6: Choice_9_1_6 = 0
Imposible_9_1_7: Choice_9_1_7 = 0
Imposible_9_1_8: Choice_9_1_8 = 0
Imposible_9_2_1: Choice_9_2_1 = 0
Imposible_9_2_2: Choice_9_2_2 = 0
Imposible_9_2_3: Choice_9_2_3 = 0
Imposible_9_2_4: Choice_9_2_4 = 0
Imposible_9_2_5: Choice_9_2_5 = 0
Imposible_9_2_7: Choice_9_2_7 = 0
Imposible_9_2_8: Choice_9_2_8 = 0
Imposible_9_2_9: Choice_9_2_9 = 0
Imposible_9_3_1: Choice_9_3_1 = 0
Imposible_9_3_3: Choice_9_3_3 = 0
Imposible_9_3_4: Choice_9_3_4 = 0
Imposible_9_3_5: Choice_9_3_5 = 0
Imposible_9_3_6: Choice_9_3_6 = 0
Imposible_9_3_7: Choice_9_3_7 = 0
Imposible_9_3_8: Choice_9_3_8 = 0
Imposible_9_3_9: Choice_9_3_9 = 0
Imposible_9_4_1: Choice_9_4_1 = 0
Imposible_9_4_2: Choice_9_4_2 = 0
Imposible_9_4_3: Choice_9_4_3 = 0
Imposible_9_4_4: Choice_9_4_4 = 0
Imposible_9_4_5: Choice_9_4_5 = 0
Imposible_9_4_6: Choice_9_4_6 = 0
Imposible_9_4_7: Choice_9_4_7 = 0
Imposible_9_4_9: Choice_9_4_9 = 0
Imposible_9_5_1: Choice_9_5_1 = 0
Imposible_9_5_2: Choice_9_5_2 = 0
Imposible_9_5_4: Choice_9_5_4 = 0
Imposible_9_5_5: Choice_9_5_5 = 0
Imposible_9_5_6: Choice_9_5_6 = 0
Imposible_9_5_7: Choice_9_5_7 = 0
Imposible_9_5_8: Choice_9_5_8 = 0
Imposible_9_5_9: Choice_9_5_9 = 0
Imposible_9_6_1: Choice_9_6_1 = 0
Imposible_9_6_2: Choice_9_6_2 = 0
Imposible_9_6_3: Choice_9_6_3 = 0
Imposible_9_6_5: Choice_9_6_5 = 0
Imposible_9_6_6: Choice_9_6_6 = 0
Imposible_9_6_7: Choice_9_6_7 = 0
Imposible_9_6_8: Choice_9_6_8 = 0
Imposible_9_6_9: Choice_9_6_9 = 0
Imposible_9_7_1: Choice_9_7_1 = 0
Imposible_9_7_2: Choice_9_7_2 = 0
Imposible_9_7_3: Choice_9_7_3 = 0
Imposible_9_7_4: Choice_9_7_4 = 0
Imposible_9_7_6: Choice_9_7_6 = 0
Imposible_9_7_7: Choice_9_7_7 = 0
Imposible_9_7_8: Choice_9_7_8 = 0
Imposible_9_7_9: Choice_9_7_9 = 0
Imposible_9_8_1: Choice_9_8_1 = 0
Imposible_9_8_2: Choice_9_8_2 = 0
Imposible_9_8_3: Choice_9_8_3 = 0
Imposible_9_8_4: Choice_9_8_4 = 0
Imposible_9_8_5: Choice_9_8_5 = 0
Imposible_9_8_6: Choice_9_8_6 = 0
Imposible_9_8_8: Choice_9_8_8 = 0
Imposible_9_8_9: Choice_9_8_9 = 0
Imposible_9_9_2: Choice_9_9_2 = 0
Imposible_9_9_3: Choice_9_9_3 = 0
Imposible_9_9_4: Choice_9_9_4 = 0
Imposible_9_9_5: Choice_9_9_5 = 0
Imposible_9_9_6: Choice_9_9_6 = 0
Imposible_9_9_7: Choice_9_9_7 = 0
Imposible_9_9_8: Choice_9_9_8 = 0
Imposible_9_9_9: Choice_9_9_9 = 0
Log10_1_5: - 0.301029995664 Choice_2_1_5 - 0.47712125472 Choice_3_1_5
 - 0.602059991328 Choice_4_1_5 - 0.698970004336 Choice_5_1_5
 - 0.778151250384 Choice_6_1_5 - 0.845098040014 Choice_7_1_5
 - 0.903089986992 Choice_8_1_5 - 0.954242509439 Choice_9_1_5 + Log10_1_5 = 0
Log10_1_6: - 0.301029995664 Choice_2_1_6 - 0.47712125472 Choice_3_1_6
 - 0.602059991328 Choice_4_1_6 - 0.698970004336 Choice_5_1_6
 - 0.778151250384 Choice_6_1_6 - 0.845098040014 Choice_7_1_6
 - 0.903089986992 Choice_8_1_6 - 0.954242509439 Choice_9_1_6 + Log10_1_6 = 0
Log10_2_5: - 0.301029995664 Choice_2_2_5 - 0.47712125472 Choice_3_2_5
 - 0.602059991328 Choice_4_2_5 - 0.698970004336 Choice_5_2_5
 - 0.778151250384 Choice_6_2_5 - 0.845098040014 Choice_7_2_5
 - 0.903089986992 Choice_8_2_5 - 0.954242509439 Choice_9_2_5 + Log10_2_5 = 0
Log10_2_6: - 0.301029995664 Choice_2_2_6 - 0.47712125472 Choice_3_2_6
 - 0.602059991328 Choice_4_2_6 - 0.698970004336 Choice_5_2_6
 - 0.778151250384 Choice_6_2_6 - 0.845098040014 Choice_7_2_6
 - 0.903089986992 Choice_8_2_6 - 0.954242509439 Choice_9_2_6 + Log10_2_6 = 0
Log10_6_2: - 0.301029995664 Choice_2_6_2 - 0.47712125472 Choice_3_6_2
 - 0.602059991328 Choice_4_6_2 - 0.698970004336 Choice_5_6_2
 - 0.778151250384 Choice_6_6_2 - 0.845098040014 Choice_7_6_2
 - 0.903089986992 Choice_8_6_2 - 0.954242509439 Choice_9_6_2 + Log10_6_2 = 0
Log10_6_3: - 0.301029995664 Choice_2_6_3 - 0.47712125472 Choice_3_6_3
 - 0.602059991328 Choice_4_6_3 - 0.698970004336 Choice_5_6_3
 - 0.778151250384 Choice_6_6_3 - 0.845098040014 Choice_7_6_3
 - 0.903089986992 Choice_8_6_3 - 0.954242509439 Choice_9_6_3 + Log10_6_3 = 0
Log10_7_2: - 0.301029995664 Choice_2_7_2 - 0.47712125472 Choice_3_7_2
 - 0.602059991328 Choice_4_7_2 - 0.698970004336 Choice_5_7_2
 - 0.778151250384 Choice_6_7_2 - 0.845098040014 Choice_7_7_2
 - 0.903089986992 Choice_8_7_2 - 0.954242509439 Choice_9_7_2 + Log10_7_2 = 0
Log10_7_3: - 0.301029995664 Choice_2_7_3 - 0.47712125472 Choice_3_7_3
 - 0.602059991328 Choice_4_7_3 - 0.698970004336 Choice_5_7_3
 - 0.778151250384 Choice_6_7_3 - 0.845098040014 Choice_7_7_3
 - 0.903089986992 Choice_8_7_3 - 0.954242509439 Choice_9_7_3 + Log10_7_3 = 0
Row_624_Unique_1: Choice_1_1_1 + Choice_1_1_2 + Choice_1_1_3 + Choice_1_1_4
 + Choice_1_1_5 + Choice_1_1_6 + Choice_1_1_7 + Choice_1_1_8 + Choice_1_1_9
 = 1
Row_624_Unique_2: Choice_2_1_1 + Choice_2_1_2 + Choice_2_1_3 + Choice_2_1_4
 + Choice_2_1_5 + Choice_2_1_6 + Choice_2_1_7 + Choice_2_1_8 + Choice_2_1_9
 = 1
Row_624_Unique_3: Choice_3_1_1 + Choice_3_1_2 + Choice_3_1_3 + Choice_3_1_4
 + Choice_3_1_5 + Choice_3_1_6 + Choice_3_1_7 + Choice_3_1_8 + Choice_3_1_9
 = 1
Row_624_Unique_4: Choice_4_1_1 + Choice_4_1_2 + Choice_4_1_3 + Choice_4_1_4
 + Choice_4_1_5 + Choice_4_1_6 + Choice_4_1_7 + Choice_4_1_8 + Choice_4_1_9
 = 1
Row_624_Unique_5: Choice_5_1_1 + Choice_5_1_2 + Choice_5_1_3 + Choice_5_1_4
 + Choice_5_1_5 + Choice_5_1_6 + Choice_5_1_7 + Choice_5_1_8 + Choice_5_1_9
 = 1
Row_624_Unique_6: Choice_6_1_1 + Choice_6_1_2 + Choice_6_1_3 + Choice_6_1_4
 + Choice_6_1_5 + Choice_6_1_6 + Choice_6_1_7 + Choice_6_1_8 + Choice_6_1_9
 = 1
Row_624_Unique_7: Choice_7_1_1 + Choice_7_1_2 + Choice_7_1_3 + Choice_7_1_4
 + Choice_7_1_5 + Choice_7_1_6 + Choice_7_1_7 + Choice_7_1_8 + Choice_7_1_9
 = 1
Row_624_Unique_8: Choice_8_1_1 + Choice_8_1_2 + Choice_8_1_3 + Choice_8_1_4
 + Choice_8_1_5 + Choice_8_1_6 + Choice_8_1_7 + Choice_8_1_8 + Choice_8_1_9
 = 1
Row_624_Unique_9: Choice_9_1_1 + Choice_9_1_2 + Choice_9_1_3 + Choice_9_1_4
 + Choice_9_1_5 + Choice_9_1_6 + Choice_9_1_7 + Choice_9_1_8 + Choice_9_1_9
 = 1
Row_625_Unique_1: Choice_1_2_1 + Choice_1_2_2 + Choice_1_2_3 + Choice_1_2_4
 + Choice_1_2_5 + Choice_1_2_6 + Choice_1_2_7 + Choice_1_2_8 + Choice_1_2_9
 = 1
Row_625_Unique_2: Choice_2_2_1 + Choice_2_2_2 + Choice_2_2_3 + Choice_2_2_4
 + Choice_2_2_5 + Choice_2_2_6 + Choice_2_2_7 + Choice_2_2_8 + Choice_2_2_9
 = 1
Row_625_Unique_3: Choice_3_2_1 + Choice_3_2_2 + Choice_3_2_3 + Choice_3_2_4
 + Choice_3_2_5 + Choice_3_2_6 + Choice_3_2_7 + Choice_3_2_8 + Choice_3_2_9
 = 1
Row_625_Unique_4: Choice_4_2_1 + Choice_4_2_2 + Choice_4_2_3 + Choice_4_2_4
 + Choice_4_2_5 + Choice_4_2_6 + Choice_4_2_7 + Choice_4_2_8 + Choice_4_2_9
 = 1
Row_625_Unique_5: Choice_5_2_1 + Choice_5_2_2 + Choice_5_2_3 + Choice_5_2_4
 + Choice_5_2_5 + Choice_5_2_6 + Choice_5_2_7 + Choice_5_2_8 + Choice_5_2_9
 = 1
Row_625_Unique_6: Choice_6_2_1 + Choice_6_2_2 + Choice_6_2_3 + Choice_6_2_4
 + Choice_6_2_5 + Choice_6_2_6 + Choice_6_2_7 + Choice_6_2_8 + Choice_6_2_9
 = 1
Row_625_Unique_7: Choice_7_2_1 + Choice_7_2_2 + Choice_7_2_3 + Choice_7_2_4
 + Choice_7_2_5 + Choice_7_2_6 + Choice_7_2_7 + Choice_7_2_8 + Choice_7_2_9
 = 1
Row_625_Unique_8: Choice_8_2_1 + Choice_8_2_2 + Choice_8_2_3 + Choice_8_2_4
 + Choice_8_2_5 + Choice_8_2_6 + Choice_8_2_7 + Choice_8_2_8 + Choice_8_2_9
 = 1
Row_625_Unique_9: Choice_9_2_1 + Choice_9_2_2 + Choice_9_2_3 + Choice_9_2_4
 + Choice_9_2_5 + Choice_9_2_6 + Choice_9_2_7 + Choice_9_2_8 + Choice_9_2_9
 = 1
Row_626_Unique_1: Choice_1_3_1 + Choice_1_3_2 + Choice_1_3_3 + Choice_1_3_4
 + Choice_1_3_5 + Choice_1_3_6 + Choice_1_3_7 + Choice_1_3_8 + Choice_1_3_9
 = 1
Row_626_Unique_2: Choice_2_3_1 + Choice_2_3_2 + Choice_2_3_3 + Choice_2_3_4
 + Choice_2_3_5 + Choice_2_3_6 + Choice_2_3_7 + Choice_2_3_8 + Choice_2_3_9
 = 1
Row_626_Unique_3: Choice_3_3_1 + Choice_3_3_2 + Choice_3_3_3 + Choice_3_3_4
 + Choice_3_3_5 + Choice_3_3_6 + Choice_3_3_7 + Choice_3_3_8 + Choice_3_3_9
 = 1
Row_626_Unique_4: Choice_4_3_1 + Choice_4_3_2 + Choice_4_3_3 + Choice_4_3_4
 + Choice_4_3_5 + Choice_4_3_6 + Choice_4_3_7 + Choice_4_3_8 + Choice_4_3_9
 = 1
Row_626_Unique_5: Choice_5_3_1 + Choice_5_3_2 + Choice_5_3_3 + Choice_5_3_4
 + Choice_5_3_5 + Choice_5_3_6 + Choice_5_3_7 + Choice_5_3_8 + Choice_5_3_9
 = 1
Row_626_Unique_6: Choice_6_3_1 + Choice_6_3_2 + Choice_6_3_3 + Choice_6_3_4
 + Choice_6_3_5 + Choice_6_3_6 + Choice_6_3_7 + Choice_6_3_8 + Choice_6_3_9
 = 1
Row_626_Unique_7: Choice_7_3_1 + Choice_7_3_2 + Choice_7_3_3 + Choice_7_3_4
 + Choice_7_3_5 + Choice_7_3_6 + Choice_7_3_7 + Choice_7_3_8 + Choice_7_3_9
 = 1
Row_626_Unique_8: Choice_8_3_1 + Choice_8_3_2 + Choice_8_3_3 + Choice_8_3_4
 + Choice_8_3_5 + Choice_8_3_6 + Choice_8_3_7 + Choice_8_3_8 + Choice_8_3_9
 = 1
Row_626_Unique_9: Choice_9_3_1 + Choice_9_3_2 + Choice_9_3_3 + Choice_9_3_4
 + Choice_9_3_5 + Choice_9_3_6 + Choice_9_3_7 + Choice_9_3_8 + Choice_9_3_9
 = 1
Row_627_Unique_1: Choice_1_4_1 + Choice_1_4_2 + Choice_1_4_3 + Choice_1_4_4
 + Choice_1_4_5 + Choice_1_4_6 + Choice_1_4_7 + Choice_1_4_8 + Choice_1_4_9
 = 1
Row_627_Unique_2: Choice_2_4_1 + Choice_2_4_2 + Choice_2_4_3 + Choice_2_4_4
 + Choice_2_4_5 + Choice_2_4_6 + Choice_2_4_7 + Choice_2_4_8 + Choice_2_4_9
 = 1
Row_627_Unique_3: Choice_3_4_1 + Choice_3_4_2 + Choice_3_4_3 + Choice_3_4_4
 + Choice_3_4_5 + Choice_3_4_6 + Choice_3_4_7 + Choice_3_4_8 + Choice_3_4_9
 = 1
Row_627_Unique_4: Choice_4_4_1 + Choice_4_4_2 + Choice_4_4_3 + Choice_4_4_4
 + Choice_4_4_5 + Choice_4_4_6 + Choice_4_4_7 + Choice_4_4_8 + Choice_4_4_9
 = 1
Row_627_Unique_5: Choice_5_4_1 + Choice_5_4_2 + Choice_5_4_3 + Choice_5_4_4
 + Choice_5_4_5 + Choice_5_4_6 + Choice_5_4_7 + Choice_5_4_8 + Choice_5_4_9
 = 1
Row_627_Unique_6: Choice_6_4_1 + Choice_6_4_2 + Choice_6_4_3 + Choice_6_4_4
 + Choice_6_4_5 + Choice_6_4_6 + Choice_6_4_7 + Choice_6_4_8 + Choice_6_4_9
 = 1
Row_627_Unique_7: Choice_7_4_1 + Choice_7_4_2 + Choice_7_4_3 + Choice_7_4_4
 + Choice_7_4_5 + Choice_7_4_6 + Choice_7_4_7 + Choice_7_4_8 + Choice_7_4_9
 = 1
Row_627_Unique_8: Choice_8_4_1 + Choice_8_4_2 + Choice_8_4_3 + Choice_8_4_4
 + Choice_8_4_5 + Choice_8_4_6 + Choice_8_4_7 + Choice_8_4_8 + Choice_8_4_9
 = 1
Row_627_Unique_9: Choice_9_4_1 + Choice_9_4_2 + Choice_9_4_3 + Choice_9_4_4
 + Choice_9_4_5 + Choice_9_4_6 + Choice_9_4_7 + Choice_9_4_8 + Choice_9_4_9
 = 1
Row_628_Unique_1: Choice_1_5_1 + Choice_1_5_2 + Choice_1_5_3 + Choice_1_5_4
 + Choice_1_5_5 + Choice_1_5_6 + Choice_1_5_7 + Choice_1_5_8 + Choice_1_5_9
 = 1
Row_628_Unique_2: Choice_2_5_1 + Choice_2_5_2 + Choice_2_5_3 + Choice_2_5_4
 + Choice_2_5_5 + Choice_2_5_6 + Choice_2_5_7 + Choice_2_5_8 + Choice_2_5_9
 = 1
Row_628_Unique_3: Choice_3_5_1 + Choice_3_5_2 + Choice_3_5_3 + Choice_3_5_4
 + Choice_3_5_5 + Choice_3_5_6 + Choice_3_5_7 + Choice_3_5_8 + Choice_3_5_9
 = 1
Row_628_Unique_4: Choice_4_5_1 + Choice_4_5_2 + Choice_4_5_3 + Choice_4_5_4
 + Choice_4_5_5 + Choice_4_5_6 + Choice_4_5_7 + Choice_4_5_8 + Choice_4_5_9
 = 1
Row_628_Unique_5: Choice_5_5_1 + Choice_5_5_2 + Choice_5_5_3 + Choice_5_5_4
 + Choice_5_5_5 + Choice_5_5_6 + Choice_5_5_7 + Choice_5_5_8 + Choice_5_5_9
 = 1
Row_628_Unique_6: Choice_6_5_1 + Choice_6_5_2 + Choice_6_5_3 + Choice_6_5_4
 + Choice_6_5_5 + Choice_6_5_6 + Choice_6_5_7 + Choice_6_5_8 + Choice_6_5_9
 = 1
Row_628_Unique_7: Choice_7_5_1 + Choice_7_5_2 + Choice_7_5_3 + Choice_7_5_4
 + Choice_7_5_5 + Choice_7_5_6 + Choice_7_5_7 + Choice_7_5_8 + Choice_7_5_9
 = 1
Row_628_Unique_8: Choice_8_5_1 + Choice_8_5_2 + Choice_8_5_3 + Choice_8_5_4
 + Choice_8_5_5 + Choice_8_5_6 + Choice_8_5_7 + Choice_8_5_8 + Choice_8_5_9
 = 1
Row_628_Unique_9: Choice_9_5_1 + Choice_9_5_2 + Choice_9_5_3 + Choice_9_5_4
 + Choice_9_5_5 + Choice_9_5_6 + Choice_9_5_7 + Choice_9_5_8 + Choice_9_5_9
 = 1
Row_629_Unique_1: Choice_1_6_1 + Choice_1_6_2 + Choice_1_6_3 + Choice_1_6_4
 + Choice_1_6_5 + Choice_1_6_6 + Choice_1_6_7 + Choice_1_6_8 + Choice_1_6_9
 = 1
Row_629_Unique_2: Choice_2_6_1 + Choice_2_6_2 + Choice_2_6_3 + Choice_2_6_4
 + Choice_2_6_5 + Choice_2_6_6 + Choice_2_6_7 + Choice_2_6_8 + Choice_2_6_9
 = 1
Row_629_Unique_3: Choice_3_6_1 + Choice_3_6_2 + Choice_3_6_3 + Choice_3_6_4
 + Choice_3_6_5 + Choice_3_6_6 + Choice_3_6_7 + Choice_3_6_8 + Choice_3_6_9
 = 1
Row_629_Unique_4: Choice_4_6_1 + Choice_4_6_2 + Choice_4_6_3 + Choice_4_6_4
 + Choice_4_6_5 + Choice_4_6_6 + Choice_4_6_7 + Choice_4_6_8 + Choice_4_6_9
 = 1
Row_629_Unique_5: Choice_5_6_1 + Choice_5_6_2 + Choice_5_6_3 + Choice_5_6_4
 + Choice_5_6_5 + Choice_5_6_6 + Choice_5_6_7 + Choice_5_6_8 + Choice_5_6_9
 = 1
Row_629_Unique_6: Choice_6_6_1 + Choice_6_6_2 + Choice_6_6_3 + Choice_6_6_4
 + Choice_6_6_5 + Choice_6_6_6 + Choice_6_6_7 + Choice_6_6_8 + Choice_6_6_9
 = 1
Row_629_Unique_7: Choice_7_6_1 + Choice_7_6_2 + Choice_7_6_3 + Choice_7_6_4
 + Choice_7_6_5 + Choice_7_6_6 + Choice_7_6_7 + Choice_7_6_8 + Choice_7_6_9
 = 1
Row_629_Unique_8: Choice_8_6_1 + Choice_8_6_2 + Choice_8_6_3 + Choice_8_6_4
 + Choice_8_6_5 + Choice_8_6_6 + Choice_8_6_7 + Choice_8_6_8 + Choice_8_6_9
 = 1
Row_629_Unique_9: Choice_9_6_1 + Choice_9_6_2 + Choice_9_6_3 + Choice_9_6_4
 + Choice_9_6_5 + Choice_9_6_6 + Choice_9_6_7 + Choice_9_6_8 + Choice_9_6_9
 = 1
Row_630_Unique_1: Choice_1_7_1 + Choice_1_7_2 + Choice_1_7_3 + Choice_1_7_4
 + Choice_1_7_5 + Choice_1_7_6 + Choice_1_7_7 + Choice_1_7_8 + Choice_1_7_9
 = 1
Row_630_Unique_2: Choice_2_7_1 + Choice_2_7_2 + Choice_2_7_3 + Choice_2_7_4
 + Choice_2_7_5 + Choice_2_7_6 + Choice_2_7_7 + Choice_2_7_8 + Choice_2_7_9
 = 1
Row_630_Unique_3: Choice_3_7_1 + Choice_3_7_2 + Choice_3_7_3 + Choice_3_7_4
 + Choice_3_7_5 + Choice_3_7_6 + Choice_3_7_7 + Choice_3_7_8 + Choice_3_7_9
 = 1
Row_630_Unique_4: Choice_4_7_1 + Choice_4_7_2 + Choice_4_7_3 + Choice_4_7_4
 + Choice_4_7_5 + Choice_4_7_6 + Choice_4_7_7 + Choice_4_7_8 + Choice_4_7_9
 = 1
Row_630_Unique_5: Choice_5_7_1 + Choice_5_7_2 + Choice_5_7_3 + Choice_5_7_4
 + Choice_5_7_5 + Choice_5_7_6 + Choice_5_7_7 + Choice_5_7_8 + Choice_5_7_9
 = 1
Row_630_Unique_6: Choice_6_7_1 + Choice_6_7_2 + Choice_6_7_3 + Choice_6_7_4
 + Choice_6_7_5 + Choice_6_7_6 + Choice_6_7_7 + Choice_6_7_8 + Choice_6_7_9
 = 1
Row_630_Unique_7: Choice_7_7_1 + Choice_7_7_2 + Choice_7_7_3 + Choice_7_7_4
 + Choice_7_7_5 + Choice_7_7_6 + Choice_7_7_7 + Choice_7_7_8 + Choice_7_7_9
 = 1
Row_630_Unique_8: Choice_8_7_1 + Choice_8_7_2 + Choice_8_7_3 + Choice_8_7_4
 + Choice_8_7_5 + Choice_8_7_6 + Choice_8_7_7 + Choice_8_7_8 + Choice_8_7_9
 = 1
Row_630_Unique_9: Choice_9_7_1 + Choice_9_7_2 + Choice_9_7_3 + Choice_9_7_4
 + Choice_9_7_5 + Choice_9_7_6 + Choice_9_7_7 + Choice_9_7_8 + Choice_9_7_9
 = 1
Row_631_Unique_1: Choice_1_8_1 + Choice_1_8_2 + Choice_1_8_3 + Choice_1_8_4
 + Choice_1_8_5 + Choice_1_8_6 + Choice_1_8_7 + Choice_1_8_8 + Choice_1_8_9
 = 1
Row_631_Unique_2: Choice_2_8_1 + Choice_2_8_2 + Choice_2_8_3 + Choice_2_8_4
 + Choice_2_8_5 + Choice_2_8_6 + Choice_2_8_7 + Choice_2_8_8 + Choice_2_8_9
 = 1
Row_631_Unique_3: Choice_3_8_1 + Choice_3_8_2 + Choice_3_8_3 + Choice_3_8_4
 + Choice_3_8_5 + Choice_3_8_6 + Choice_3_8_7 + Choice_3_8_8 + Choice_3_8_9
 = 1
Row_631_Unique_4: Choice_4_8_1 + Choice_4_8_2 + Choice_4_8_3 + Choice_4_8_4
 + Choice_4_8_5 + Choice_4_8_6 + Choice_4_8_7 + Choice_4_8_8 + Choice_4_8_9
 = 1
Row_631_Unique_5: Choice_5_8_1 + Choice_5_8_2 + Choice_5_8_3 + Choice_5_8_4
 + Choice_5_8_5 + Choice_5_8_6 + Choice_5_8_7 + Choice_5_8_8 + Choice_5_8_9
 = 1
Row_631_Unique_6: Choice_6_8_1 + Choice_6_8_2 + Choice_6_8_3 + Choice_6_8_4
 + Choice_6_8_5 + Choice_6_8_6 + Choice_6_8_7 + Choice_6_8_8 + Choice_6_8_9
 = 1
Row_631_Unique_7: Choice_7_8_1 + Choice_7_8_2 + Choice_7_8_3 + Choice_7_8_4
 + Choice_7_8_5 + Choice_7_8_6 + Choice_7_8_7 + Choice_7_8_8 + Choice_7_8_9
 = 1
Row_631_Unique_8: Choice_8_8_1 + Choice_8_8_2 + Choice_8_8_3 + Choice_8_8_4
 + Choice_8_8_5 + Choice_8_8_6 + Choice_8_8_7 + Choice_8_8_8 + Choice_8_8_9
 = 1
Row_631_Unique_9: Choice_9_8_1 + Choice_9_8_2 + Choice_9_8_3 + Choice_9_8_4
 + Choice_9_8_5 + Choice_9_8_6 + Choice_9_8_7 + Choice_9_8_8 + Choice_9_8_9
 = 1
Row_632_Unique_1: Choice_1_9_1 + Choice_1_9_2 + Choice_1_9_3 + Choice_1_9_4
 + Choice_1_9_5 + Choice_1_9_6 + Choice_1_9_7 + Choice_1_9_8 + Choice_1_9_9
 = 1
Row_632_Unique_2: Choice_2_9_1 + Choice_2_9_2 + Choice_2_9_3 + Choice_2_9_4
 + Choice_2_9_5 + Choice_2_9_6 + Choice_2_9_7 + Choice_2_9_8 + Choice_2_9_9
 = 1
Row_632_Unique_3: Choice_3_9_1 + Choice_3_9_2 + Choice_3_9_3 + Choice_3_9_4
 + Choice_3_9_5 + Choice_3_9_6 + Choice_3_9_7 + Choice_3_9_8 + Choice_3_9_9
 = 1
Row_632_Unique_4: Choice_4_9_1 + Choice_4_9_2 + Choice_4_9_3 + Choice_4_9_4
 + Choice_4_9_5 + Choice_4_9_6 + Choice_4_9_7 + Choice_4_9_8 + Choice_4_9_9
 = 1
Row_632_Unique_5: Choice_5_9_1 + Choice_5_9_2 + Choice_5_9_3 + Choice_5_9_4
 + Choice_5_9_5 + Choice_5_9_6 + Choice_5_9_7 + Choice_5_9_8 + Choice_5_9_9
 = 1
Row_632_Unique_6: Choice_6_9_1 + Choice_6_9_2 + Choice_6_9_3 + Choice_6_9_4
 + Choice_6_9_5 + Choice_6_9_6 + Choice_6_9_7 + Choice_6_9_8 + Choice_6_9_9
 = 1
Row_632_Unique_7: Choice_7_9_1 + Choice_7_9_2 + Choice_7_9_3 + Choice_7_9_4
 + Choice_7_9_5 + Choice_7_9_6 + Choice_7_9_7 + Choice_7_9_8 + Choice_7_9_9
 = 1
Row_632_Unique_8: Choice_8_9_1 + Choice_8_9_2 + Choice_8_9_3 + Choice_8_9_4
 + Choice_8_9_5 + Choice_8_9_6 + Choice_8_9_7 + Choice_8_9_8 + Choice_8_9_9
 = 1
Row_632_Unique_9: Choice_9_9_1 + Choice_9_9_2 + Choice_9_9_3 + Choice_9_9_4
 + Choice_9_9_5 + Choice_9_9_6 + Choice_9_9_7 + Choice_9_9_8 + Choice_9_9_9
 = 1
Total_Box_634: Values_1_1 + Values_1_2 + Values_1_3 + Values_2_1 + Values_2_2
 + Values_2_3 + Values_3_1 + Values_3_2 + Values_3_3 = 45
Total_Box_635: Values_4_1 + Values_4_2 + Values_4_3 + Values_5_1 + Values_5_2
 + Values_5_3 + Values_6_1 + Values_6_2 + Values_6_3 = 45
Total_Box_636: Values_7_1 + Values_7_2 + Values_7_3 + Values_8_1 + Values_8_2
 + Values_8_3 + Values_9_1 + Values_9_2 + Values_9_3 = 45
Total_Box_637: Values_1_4 + Values_1_5 + Values_1_6 + Values_2_4 + Values_2_5
 + Values_2_6 + Values_3_4 + Values_3_5 + Values_3_6 = 45
Total_Box_638: Values_4_4 + Values_4_5 + Values_4_6 + Values_5_4 + Values_5_5
 + Values_5_6 + Values_6_4 + Values_6_5 + Values_6_6 = 45
Total_Box_639: Values_7_4 + Values_7_5 + Values_7_6 + Values_8_4 + Values_8_5
 + Values_8_6 + Values_9_4 + Values_9_5 + Values_9_6 = 45
Total_Box_640: Values_1_7 + Values_1_8 + Values_1_9 + Values_2_7 + Values_2_8
 + Values_2_9 + Values_3_7 + Values_3_8 + Values_3_9 = 45
Total_Box_641: Values_4_7 + Values_4_8 + Values_4_9 + Values_5_7 + Values_5_8
 + Values_5_9 + Values_6_7 + Values_6_8 + Values_6_9 = 45
Total_Box_642: Values_7_7 + Values_7_8 + Values_7_9 + Values_8_7 + Values_8_8
 + Values_8_9 + Values_9_7 + Values_9_8 + Values_9_9 = 45
Total_Column_614: Values_1_1 + Values_2_1 + Values_3_1 + Values_4_1
 + Values_5_1 + Values_6_1 + Values_7_1 + Values_8_1 + Values_9_1 = 45
Total_Column_615: Values_1_2 + Values_2_2 + Values_3_2 + Values_4_2
 + Values_5_2 + Values_6_2 + Values_7_2 + Values_8_2 + Values_9_2 = 45
Total_Column_616: Values_1_3 + Values_2_3 + Values_3_3 + Values_4_3
 + Values_5_3 + Values_6_3 + Values_7_3 + Values_8_3 + Values_9_3 = 45
Total_Column_617: Values_1_4 + Values_2_4 + Values_3_4 + Values_4_4
 + Values_5_4 + Values_6_4 + Values_7_4 + Values_8_4 + Values_9_4 = 45
Total_Column_618: Values_1_5 + Values_2_5 + Values_3_5 + Values_4_5
 + Values_5_5 + Values_6_5 + Values_7_5 + Values_8_5 + Values_9_5 = 45
Total_Column_619: Values_1_6 + Values_2_6 + Values_3_6 + Values_4_6
 + Values_5_6 + Values_6_6 + Values_7_6 + Values_8_6 + Values_9_6 = 45
Total_Column_620: Values_1_7 + Values_2_7 + Values_3_7 + Values_4_7
 + Values_5_7 + Values_6_7 + Values_7_7 + Values_8_7 + Values_9_7 = 45
Total_Column_621: Values_1_8 + Values_2_8 + Values_3_8 + Values_4_8
 + Values_5_8 + Values_6_8 + Values_7_8 + Values_8_8 + Values_9_8 = 45
Total_Column_622: Values_1_9 + Values_2_9 + Values_3_9 + Values_4_9
 + Values_5_9 + Values_6_9 + Values_7_9 + Values_8_9 + Values_9_9 = 45
Total_Row_624: Values_1_1 + Values_1_2 + Values_1_3 + Values_1_4 + Values_1_5
 + Values_1_6 + Values_1_7 + Values_1_8 + Values_1_9 = 45
Total_Row_625: Values_2_1 + Values_2_2 + Values_2_3 + Values_2_4 + Values_2_5
 + Values_2_6 + Values_2_7 + Values_2_8 + Values_2_9 = 45
Total_Row_626: Values_3_1 + Values_3_2 + Values_3_3 + Values_3_4 + Values_3_5
 + Values_3_6 + Values_3_7 + Values_3_8 + Values_3_9 = 45
Total_Row_627: Values_4_1 + Values_4_2 + Values_4_3 + Values_4_4 + Values_4_5
 + Values_4_6 + Values_4_7 + Values_4_8 + Values_4_9 = 45
Total_Row_628: Values_5_1 + Values_5_2 + Values_5_3 + Values_5_4 + Values_5_5
 + Values_5_6 + Values_5_7 + Values_5_8 + Values_5_9 = 45
Total_Row_629: Values_6_1 + Values_6_2 + Values_6_3 + Values_6_4 + Values_6_5
 + Values_6_6 + Values_6_7 + Values_6_8 + Values_6_9 = 45
Total_Row_630: Values_7_1 + Values_7_2 + Values_7_3 + Values_7_4 + Values_7_5
 + Values_7_6 + Values_7_7 + Values_7_8 + Values_7_9 = 45
Total_Row_631: Values_8_1 + Values_8_2 + Values_8_3 + Values_8_4 + Values_8_5
 + Values_8_6 + Values_8_7 + Values_8_8 + Values_8_9 = 45
Total_Row_632: Values_9_1 + Values_9_2 + Values_9_3 + Values_9_4 + Values_9_5
 + Values_9_6 + Values_9_7 + Values_9_8 + Values_9_9 = 45
Unique_cell_1_1: Choice_1_1_1 + 2 Choice_2_1_1 + 3 Choice_3_1_1
 + 4 Choice_4_1_1 + 5 Choice_5_1_1 + 6 Choice_6_1_1 + 7 Choice_7_1_1
 + 8 Choice_8_1_1 + 9 Choice_9_1_1 - Values_1_1 = 0
Unique_cell_1_2: Choice_1_1_2 + 2 Choice_2_1_2 + 3 Choice_3_1_2
 + 4 Choice_4_1_2 + 5 Choice_5_1_2 + 6 Choice_6_1_2 + 7 Choice_7_1_2
 + 8 Choice_8_1_2 + 9 Choice_9_1_2 - Values_1_2 = 0
Unique_cell_1_3: Choice_1_1_3 + 2 Choice_2_1_3 + 3 Choice_3_1_3
 + 4 Choice_4_1_3 + 5 Choice_5_1_3 + 6 Choice_6_1_3 + 7 Choice_7_1_3
 + 8 Choice_8_1_3 + 9 Choice_9_1_3 - Values_1_3 = 0
Unique_cell_1_4: Choice_1_1_4 + 2 Choice_2_1_4 + 3 Choice_3_1_4
 + 4 Choice_4_1_4 + 5 Choice_5_1_4 + 6 Choice_6_1_4 + 7 Choice_7_1_4
 + 8 Choice_8_1_4 + 9 Choice_9_1_4 - Values_1_4 = 0
Unique_cell_1_5: Choice_1_1_5 + 2 Choice_2_1_5 + 3 Choice_3_1_5
 + 4 Choice_4_1_5 + 5 Choice_5_1_5 + 6 Choice_6_1_5 + 7 Choice_7_1_5
 + 8 Choice_8_1_5 + 9 Choice_9_1_5 - Values_1_5 = 0
Unique_cell_1_6: Choice_1_1_6 + 2 Choice_2_1_6 + 3 Choice_3_1_6
 + 4 Choice_4_1_6 + 5 Choice_5_1_6 + 6 Choice_6_1_6 + 7 Choice_7_1_6
 + 8 Choice_8_1_6 + 9 Choice_9_1_6 - Values_1_6 = 0
Unique_cell_1_7: Choice_1_1_7 + 2 Choice_2_1_7 + 3 Choice_3_1_7
 + 4 Choice_4_1_7 + 5 Choice_5_1_7 + 6 Choice_6_1_7 + 7 Choice_7_1_7
 + 8 Choice_8_1_7 + 9 Choice_9_1_7 - Values_1_7 = 0
Unique_cell_1_8: Choice_1_1_8 + 2 Choice_2_1_8 + 3 Choice_3_1_8
 + 4 Choice_4_1_8 + 5 Choice_5_1_8 + 6 Choice_6_1_8 + 7 Choice_7_1_8
 + 8 Choice_8_1_8 + 9 Choice_9_1_8 - Values_1_8 = 0
Unique_cell_1_9: Choice_1_1_9 + 2 Choice_2_1_9 + 3 Choice_3_1_9
 + 4 Choice_4_1_9 + 5 Choice_5_1_9 + 6 Choice_6_1_9 + 7 Choice_7_1_9
 + 8 Choice_8_1_9 + 9 Choice_9_1_9 - Values_1_9 = 0
Unique_cell_2_1: Choice_1_2_1 + 2 Choice_2_2_1 + 3 Choice_3_2_1
 + 4 Choice_4_2_1 + 5 Choice_5_2_1 + 6 Choice_6_2_1 + 7 Choice_7_2_1
 + 8 Choice_8_2_1 + 9 Choice_9_2_1 - Values_2_1 = 0
Unique_cell_2_2: Choice_1_2_2 + 2 Choice_2_2_2 + 3 Choice_3_2_2
 + 4 Choice_4_2_2 + 5 Choice_5_2_2 + 6 Choice_6_2_2 + 7 Choice_7_2_2
 + 8 Choice_8_2_2 + 9 Choice_9_2_2 - Values_2_2 = 0
Unique_cell_2_3: Choice_1_2_3 + 2 Choice_2_2_3 + 3 Choice_3_2_3
 + 4 Choice_4_2_3 + 5 Choice_5_2_3 + 6 Choice_6_2_3 + 7 Choice_7_2_3
 + 8 Choice_8_2_3 + 9 Choice_9_2_3 - Values_2_3 = 0
Unique_cell_2_4: Choice_1_2_4 + 2 Choice_2_2_4 + 3 Choice_3_2_4
 + 4 Choice_4_2_4 + 5 Choice_5_2_4 + 6 Choice_6_2_4 + 7 Choice_7_2_4
 + 8 Choice_8_2_4 + 9 Choice_9_2_4 - Values_2_4 = 0
Unique_cell_2_5: Choice_1_2_5 + 2 Choice_2_2_5 + 3 Choice_3_2_5
 + 4 Choice_4_2_5 + 5 Choice_5_2_5 + 6 Choice_6_2_5 + 7 Choice_7_2_5
 + 8 Choice_8_2_5 + 9 Choice_9_2_5 - Values_2_5 = 0
Unique_cell_2_6: Choice_1_2_6 + 2 Choice_2_2_6 + 3 Choice_3_2_6
 + 4 Choice_4_2_6 + 5 Choice_5_2_6 + 6 Choice_6_2_6 + 7 Choice_7_2_6
 + 8 Choice_8_2_6 + 9 Choice_9_2_6 - Values_2_6 = 0
Unique_cell_2_7: Choice_1_2_7 + 2 Choice_2_2_7 + 3 Choice_3_2_7
 + 4 Choice_4_2_7 + 5 Choice_5_2_7 + 6 Choice_6_2_7 + 7 Choice_7_2_7
 + 8 Choice_8_2_7 + 9 Choice_9_2_7 - Values_2_7 = 0
Unique_cell_2_8: Choice_1_2_8 + 2 Choice_2_2_8 + 3 Choice_3_2_8
 + 4 Choice_4_2_8 + 5 Choice_5_2_8 + 6 Choice_6_2_8 + 7 Choice_7_2_8
 + 8 Choice_8_2_8 + 9 Choice_9_2_8 - Values_2_8 = 0
Unique_cell_2_9: Choice_1_2_9 + 2 Choice_2_2_9 + 3 Choice_3_2_9
 + 4 Choice_4_2_9 + 5 Choice_5_2_9 + 6 Choice_6_2_9 + 7 Choice_7_2_9
 + 8 Choice_8_2_9 + 9 Choice_9_2_9 - Values_2_9 = 0
Unique_cell_3_1: Choice_1_3_1 + 2 Choice_2_3_1 + 3 Choice_3_3_1
 + 4 Choice_4_3_1 + 5 Choice_5_3_1 + 6 Choice_6_3_1 + 7 Choice_7_3_1
 + 8 Choice_8_3_1 + 9 Choice_9_3_1 - Values_3_1 = 0
Unique_cell_3_2: Choice_1_3_2 + 2 Choice_2_3_2 + 3 Choice_3_3_2
 + 4 Choice_4_3_2 + 5 Choice_5_3_2 + 6 Choice_6_3_2 + 7 Choice_7_3_2
 + 8 Choice_8_3_2 + 9 Choice_9_3_2 - Values_3_2 = 0
Unique_cell_3_3: Choice_1_3_3 + 2 Choice_2_3_3 + 3 Choice_3_3_3
 + 4 Choice_4_3_3 + 5 Choice_5_3_3 + 6 Choice_6_3_3 + 7 Choice_7_3_3
 + 8 Choice_8_3_3 + 9 Choice_9_3_3 - Values_3_3 = 0
Unique_cell_3_4: Choice_1_3_4 + 2 Choice_2_3_4 + 3 Choice_3_3_4
 + 4 Choice_4_3_4 + 5 Choice_5_3_4 + 6 Choice_6_3_4 + 7 Choice_7_3_4
 + 8 Choice_8_3_4 + 9 Choice_9_3_4 - Values_3_4 = 0
Unique_cell_3_5: Choice_1_3_5 + 2 Choice_2_3_5 + 3 Choice_3_3_5
 + 4 Choice_4_3_5 + 5 Choice_5_3_5 + 6 Choice_6_3_5 + 7 Choice_7_3_5
 + 8 Choice_8_3_5 + 9 Choice_9_3_5 - Values_3_5 = 0
Unique_cell_3_6: Choice_1_3_6 + 2 Choice_2_3_6 + 3 Choice_3_3_6
 + 4 Choice_4_3_6 + 5 Choice_5_3_6 + 6 Choice_6_3_6 + 7 Choice_7_3_6
 + 8 Choice_8_3_6 + 9 Choice_9_3_6 - Values_3_6 = 0
Unique_cell_3_7: Choice_1_3_7 + 2 Choice_2_3_7 + 3 Choice_3_3_7
 + 4 Choice_4_3_7 + 5 Choice_5_3_7 + 6 Choice_6_3_7 + 7 Choice_7_3_7
 + 8 Choice_8_3_7 + 9 Choice_9_3_7 - Values_3_7 = 0
Unique_cell_3_8: Choice_1_3_8 + 2 Choice_2_3_8 + 3 Choice_3_3_8
 + 4 Choice_4_3_8 + 5 Choice_5_3_8 + 6 Choice_6_3_8 + 7 Choice_7_3_8
 + 8 Choice_8_3_8 + 9 Choice_9_3_8 - Values_3_8 = 0
Unique_cell_3_9: Choice_1_3_9 + 2 Choice_2_3_9 + 3 Choice_3_3_9
 + 4 Choice_4_3_9 + 5 Choice_5_3_9 + 6 Choice_6_3_9 + 7 Choice_7_3_9
 + 8 Choice_8_3_9 + 9 Choice_9_3_9 - Values_3_9 = 0
Unique_cell_4_1: Choice_1_4_1 + 2 Choice_2_4_1 + 3 Choice_3_4_1
 + 4 Choice_4_4_1 + 5 Choice_5_4_1 + 6 Choice_6_4_1 + 7 Choice_7_4_1
 + 8 Choice_8_4_1 + 9 Choice_9_4_1 - Values_4_1 = 0
Unique_cell_4_2: Choice_1_4_2 + 2 Choice_2_4_2 + 3 Choice_3_4_2
 + 4 Choice_4_4_2 + 5 Choice_5_4_2 + 6 Choice_6_4_2 + 7 Choice_7_4_2
 + 8 Choice_8_4_2 + 9 Choice_9_4_2 - Values_4_2 = 0
Unique_cell_4_3: Choice_1_4_3 + 2 Choice_2_4_3 + 3 Choice_3_4_3
 + 4 Choice_4_4_3 + 5 Choice_5_4_3 + 6 Choice_6_4_3 + 7 Choice_7_4_3
 + 8 Choice_8_4_3 + 9 Choice_9_4_3 - Values_4_3 = 0
Unique_cell_4_4: Choice_1_4_4 + 2 Choice_2_4_4 + 3 Choice_3_4_4
 + 4 Choice_4_4_4 + 5 Choice_5_4_4 + 6 Choice_6_4_4 + 7 Choice_7_4_4
 + 8 Choice_8_4_4 + 9 Choice_9_4_4 - Values_4_4 = 0
Unique_cell_4_5: Choice_1_4_5 + 2 Choice_2_4_5 + 3 Choice_3_4_5
 + 4 Choice_4_4_5 + 5 Choice_5_4_5 + 6 Choice_6_4_5 + 7 Choice_7_4_5
 + 8 Choice_8_4_5 + 9 Choice_9_4_5 - Values_4_5 = 0
Unique_cell_4_6: Choice_1_4_6 + 2 Choice_2_4_6 + 3 Choice_3_4_6
 + 4 Choice_4_4_6 + 5 Choice_5_4_6 + 6 Choice_6_4_6 + 7 Choice_7_4_6
 + 8 Choice_8_4_6 + 9 Choice_9_4_6 - Values_4_6 = 0
Unique_cell_4_7: Choice_1_4_7 + 2 Choice_2_4_7 + 3 Choice_3_4_7
 + 4 Choice_4_4_7 + 5 Choice_5_4_7 + 6 Choice_6_4_7 + 7 Choice_7_4_7
 + 8 Choice_8_4_7 + 9 Choice_9_4_7 - Values_4_7 = 0
Unique_cell_4_8: Choice_1_4_8 + 2 Choice_2_4_8 + 3 Choice_3_4_8
 + 4 Choice_4_4_8 + 5 Choice_5_4_8 + 6 Choice_6_4_8 + 7 Choice_7_4_8
 + 8 Choice_8_4_8 + 9 Choice_9_4_8 - Values_4_8 = 0
Unique_cell_4_9: Choice_1_4_9 + 2 Choice_2_4_9 + 3 Choice_3_4_9
 + 4 Choice_4_4_9 + 5 Choice_5_4_9 + 6 Choice_6_4_9 + 7 Choice_7_4_9
 + 8 Choice_8_4_9 + 9 Choice_9_4_9 - Values_4_9 = 0
Unique_cell_5_1: Choice_1_5_1 + 2 Choice_2_5_1 + 3 Choice_3_5_1
 + 4 Choice_4_5_1 + 5 Choice_5_5_1 + 6 Choice_6_5_1 + 7 Choice_7_5_1
 + 8 Choice_8_5_1 + 9 Choice_9_5_1 - Values_5_1 = 0
Unique_cell_5_2: Choice_1_5_2 + 2 Choice_2_5_2 + 3 Choice_3_5_2
 + 4 Choice_4_5_2 + 5 Choice_5_5_2 + 6 Choice_6_5_2 + 7 Choice_7_5_2
 + 8 Choice_8_5_2 + 9 Choice_9_5_2 - Values_5_2 = 0
Unique_cell_5_3: Choice_1_5_3 + 2 Choice_2_5_3 + 3 Choice_3_5_3
 + 4 Choice_4_5_3 + 5 Choice_5_5_3 + 6 Choice_6_5_3 + 7 Choice_7_5_3
 + 8 Choice_8_5_3 + 9 Choice_9_5_3 - Values_5_3 = 0
Unique_cell_5_4: Choice_1_5_4 + 2 Choice_2_5_4 + 3 Choice_3_5_4
 + 4 Choice_4_5_4 + 5 Choice_5_5_4 + 6 Choice_6_5_4 + 7 Choice_7_5_4
 + 8 Choice_8_5_4 + 9 Choice_9_5_4 - Values_5_4 = 0
Unique_cell_5_5: Choice_1_5_5 + 2 Choice_2_5_5 + 3 Choice_3_5_5
 + 4 Choice_4_5_5 + 5 Choice_5_5_5 + 6 Choice_6_5_5 + 7 Choice_7_5_5
 + 8 Choice_8_5_5 + 9 Choice_9_5_5 - Values_5_5 = 0
Unique_cell_5_6: Choice_1_5_6 + 2 Choice_2_5_6 + 3 Choice_3_5_6
 + 4 Choice_4_5_6 + 5 Choice_5_5_6 + 6 Choice_6_5_6 + 7 Choice_7_5_6
 + 8 Choice_8_5_6 + 9 Choice_9_5_6 - Values_5_6 = 0
Unique_cell_5_7: Choice_1_5_7 + 2 Choice_2_5_7 + 3 Choice_3_5_7
 + 4 Choice_4_5_7 + 5 Choice_5_5_7 + 6 Choice_6_5_7 + 7 Choice_7_5_7
 + 8 Choice_8_5_7 + 9 Choice_9_5_7 - Values_5_7 = 0
Unique_cell_5_8: Choice_1_5_8 + 2 Choice_2_5_8 + 3 Choice_3_5_8
 + 4 Choice_4_5_8 + 5 Choice_5_5_8 + 6 Choice_6_5_8 + 7 Choice_7_5_8
 + 8 Choice_8_5_8 + 9 Choice_9_5_8 - Values_5_8 = 0
Unique_cell_5_9: Choice_1_5_9 + 2 Choice_2_5_9 + 3 Choice_3_5_9
 + 4 Choice_4_5_9 + 5 Choice_5_5_9 + 6 Choice_6_5_9 + 7 Choice_7_5_9
 + 8 Choice_8_5_9 + 9 Choice_9_5_9 - Values_5_9 = 0
Unique_cell_6_1: Choice_1_6_1 + 2 Choice_2_6_1 + 3 Choice_3_6_1
 + 4 Choice_4_6_1 + 5 Choice_5_6_1 + 6 Choice_6_6_1 + 7 Choice_7_6_1
 + 8 Choice_8_6_1 + 9 Choice_9_6_1 - Values_6_1 = 0
Unique_cell_6_2: Choice_1_6_2 + 2 Choice_2_6_2 + 3 Choice_3_6_2
 + 4 Choice_4_6_2 + 5 Choice_5_6_2 + 6 Choice_6_6_2 + 7 Choice_7_6_2
 + 8 Choice_8_6_2 + 9 Choice_9_6_2 - Values_6_2 = 0
Unique_cell_6_3: Choice_1_6_3 + 2 Choice_2_6_3 + 3 Choice_3_6_3
 + 4 Choice_4_6_3 + 5 Choice_5_6_3 + 6 Choice_6_6_3 + 7 Choice_7_6_3
 + 8 Choice_8_6_3 + 9 Choice_9_6_3 - Values_6_3 = 0
Unique_cell_6_4: Choice_1_6_4 + 2 Choice_2_6_4 + 3 Choice_3_6_4
 + 4 Choice_4_6_4 + 5 Choice_5_6_4 + 6 Choice_6_6_4 + 7 Choice_7_6_4
 + 8 Choice_8_6_4 + 9 Choice_9_6_4 - Values_6_4 = 0
Unique_cell_6_5: Choice_1_6_5 + 2 Choice_2_6_5 + 3 Choice_3_6_5
 + 4 Choice_4_6_5 + 5 Choice_5_6_5 + 6 Choice_6_6_5 + 7 Choice_7_6_5
 + 8 Choice_8_6_5 + 9 Choice_9_6_5 - Values_6_5 = 0
Unique_cell_6_6: Choice_1_6_6 + 2 Choice_2_6_6 + 3 Choice_3_6_6
 + 4 Choice_4_6_6 + 5 Choice_5_6_6 + 6 Choice_6_6_6 + 7 Choice_7_6_6
 + 8 Choice_8_6_6 + 9 Choice_9_6_6 - Values_6_6 = 0
Unique_cell_6_7: Choice_1_6_7 + 2 Choice_2_6_7 + 3 Choice_3_6_7
 + 4 Choice_4_6_7 + 5 Choice_5_6_7 + 6 Choice_6_6_7 + 7 Choice_7_6_7
 + 8 Choice_8_6_7 + 9 Choice_9_6_7 - Values_6_7 = 0
Unique_cell_6_8: Choice_1_6_8 + 2 Choice_2_6_8 + 3 Choice_3_6_8
 + 4 Choice_4_6_8 + 5 Choice_5_6_8 + 6 Choice_6_6_8 + 7 Choice_7_6_8
 + 8 Choice_8_6_8 + 9 Choice_9_6_8 - Values_6_8 = 0
Unique_cell_6_9: Choice_1_6_9 + 2 Choice_2_6_9 + 3 Choice_3_6_9
 + 4 Choice_4_6_9 + 5 Choice_5_6_9 + 6 Choice_6_6_9 + 7 Choice_7_6_9
 + 8 Choice_8_6_9 + 9 Choice_9_6_9 - Values_6_9 = 0
Unique_cell_7_1: Choice_1_7_1 + 2 Choice_2_7_1 + 3 Choice_3_7_1
 + 4 Choice_4_7_1 + 5 Choice_5_7_1 + 6 Choice_6_7_1 + 7 Choice_7_7_1
 + 8 Choice_8_7_1 + 9 Choice_9_7_1 - Values_7_1 = 0
Unique_cell_7_2: Choice_1_7_2 + 2 Choice_2_7_2 + 3 Choice_3_7_2
 + 4 Choice_4_7_2 + 5 Choice_5_7_2 + 6 Choice_6_7_2 + 7 Choice_7_7_2
 + 8 Choice_8_7_2 + 9 Choice_9_7_2 - Values_7_2 = 0
Unique_cell_7_3: Choice_1_7_3 + 2 Choice_2_7_3 + 3 Choice_3_7_3
 + 4 Choice_4_7_3 + 5 Choice_5_7_3 + 6 Choice_6_7_3 + 7 Choice_7_7_3
 + 8 Choice_8_7_3 + 9 Choice_9_7_3 - Values_7_3 = 0
Unique_cell_7_4: Choice_1_7_4 + 2 Choice_2_7_4 + 3 Choice_3_7_4
 + 4 Choice_4_7_4 + 5 Choice_5_7_4 + 6 Choice_6_7_4 + 7 Choice_7_7_4
 + 8 Choice_8_7_4 + 9 Choice_9_7_4 - Values_7_4 = 0
Unique_cell_7_5: Choice_1_7_5 + 2 Choice_2_7_5 + 3 Choice_3_7_5
 + 4 Choice_4_7_5 + 5 Choice_5_7_5 + 6 Choice_6_7_5 + 7 Choice_7_7_5
 + 8 Choice_8_7_5 + 9 Choice_9_7_5 - Values_7_5 = 0
Unique_cell_7_6: Choice_1_7_6 + 2 Choice_2_7_6 + 3 Choice_3_7_6
 + 4 Choice_4_7_6 + 5 Choice_5_7_6 + 6 Choice_6_7_6 + 7 Choice_7_7_6
 + 8 Choice_8_7_6 + 9 Choice_9_7_6 - Values_7_6 = 0
Unique_cell_7_7: Choice_1_7_7 + 2 Choice_2_7_7 + 3 Choice_3_7_7
 + 4 Choice_4_7_7 + 5 Choice_5_7_7 + 6 Choice_6_7_7 + 7 Choice_7_7_7
 + 8 Choice_8_7_7 + 9 Choice_9_7_7 - Values_7_7 = 0
Unique_cell_7_8: Choice_1_7_8 + 2 Choice_2_7_8 + 3 Choice_3_7_8
 + 4 Choice_4_7_8 + 5 Choice_5_7_8 + 6 Choice_6_7_8 + 7 Choice_7_7_8
 + 8 Choice_8_7_8 + 9 Choice_9_7_8 - Values_7_8 = 0
Unique_cell_7_9: Choice_1_7_9 + 2 Choice_2_7_9 + 3 Choice_3_7_9
 + 4 Choice_4_7_9 + 5 Choice_5_7_9 + 6 Choice_6_7_9 + 7 Choice_7_7_9
 + 8 Choice_8_7_9 + 9 Choice_9_7_9 - Values_7_9 = 0
Unique_cell_8_1: Choice_1_8_1 + 2 Choice_2_8_1 + 3 Choice_3_8_1
 + 4 Choice_4_8_1 + 5 Choice_5_8_1 + 6 Choice_6_8_1 + 7 Choice_7_8_1
 + 8 Choice_8_8_1 + 9 Choice_9_8_1 - Values_8_1 = 0
Unique_cell_8_2: Choice_1_8_2 + 2 Choice_2_8_2 + 3 Choice_3_8_2
 + 4 Choice_4_8_2 + 5 Choice_5_8_2 + 6 Choice_6_8_2 + 7 Choice_7_8_2
 + 8 Choice_8_8_2 + 9 Choice_9_8_2 - Values_8_2 = 0
Unique_cell_8_3: Choice_1_8_3 + 2 Choice_2_8_3 + 3 Choice_3_8_3
 + 4 Choice_4_8_3 + 5 Choice_5_8_3 + 6 Choice_6_8_3 + 7 Choice_7_8_3
 + 8 Choice_8_8_3 + 9 Choice_9_8_3 - Values_8_3 = 0
Unique_cell_8_4: Choice_1_8_4 + 2 Choice_2_8_4 + 3 Choice_3_8_4
 + 4 Choice_4_8_4 + 5 Choice_5_8_4 + 6 Choice_6_8_4 + 7 Choice_7_8_4
 + 8 Choice_8_8_4 + 9 Choice_9_8_4 - Values_8_4 = 0
Unique_cell_8_5: Choice_1_8_5 + 2 Choice_2_8_5 + 3 Choice_3_8_5
 + 4 Choice_4_8_5 + 5 Choice_5_8_5 + 6 Choice_6_8_5 + 7 Choice_7_8_5
 + 8 Choice_8_8_5 + 9 Choice_9_8_5 - Values_8_5 = 0
Unique_cell_8_6: Choice_1_8_6 + 2 Choice_2_8_6 + 3 Choice_3_8_6
 + 4 Choice_4_8_6 + 5 Choice_5_8_6 + 6 Choice_6_8_6 + 7 Choice_7_8_6
 + 8 Choice_8_8_6 + 9 Choice_9_8_6 - Values_8_6 = 0
Unique_cell_8_7: Choice_1_8_7 + 2 Choice_2_8_7 + 3 Choice_3_8_7
 + 4 Choice_4_8_7 + 5 Choice_5_8_7 + 6 Choice_6_8_7 + 7 Choice_7_8_7
 + 8 Choice_8_8_7 + 9 Choice_9_8_7 - Values_8_7 = 0
Unique_cell_8_8: Choice_1_8_8 + 2 Choice_2_8_8 + 3 Choice_3_8_8
 + 4 Choice_4_8_8 + 5 Choice_5_8_8 + 6 Choice_6_8_8 + 7 Choice_7_8_8
 + 8 Choice_8_8_8 + 9 Choice_9_8_8 - Values_8_8 = 0
Unique_cell_8_9: Choice_1_8_9 + 2 Choice_2_8_9 + 3 Choice_3_8_9
 + 4 Choice_4_8_9 + 5 Choice_5_8_9 + 6 Choice_6_8_9 + 7 Choice_7_8_9
 + 8 Choice_8_8_9 + 9 Choice_9_8_9 - Values_8_9 = 0
Unique_cell_9_1: Choice_1_9_1 + 2 Choice_2_9_1 + 3 Choice_3_9_1
 + 4 Choice_4_9_1 + 5 Choice_5_9_1 + 6 Choice_6_9_1 + 7 Choice_7_9_1
 + 8 Choice_8_9_1 + 9 Choice_9_9_1 - Values_9_1 = 0
Unique_cell_9_2: Choice_1_9_2 + 2 Choice_2_9_2 + 3 Choice_3_9_2
 + 4 Choice_4_9_2 + 5 Choice_5_9_2 + 6 Choice_6_9_2 + 7 Choice_7_9_2
 + 8 Choice_8_9_2 + 9 Choice_9_9_2 - Values_9_2 = 0
Unique_cell_9_3: Choice_1_9_3 + 2 Choice_2_9_3 + 3 Choice_3_9_3
 + 4 Choice_4_9_3 + 5 Choice_5_9_3 + 6 Choice_6_9_3 + 7 Choice_7_9_3
 + 8 Choice_8_9_3 + 9 Choice_9_9_3 - Values_9_3 = 0
Unique_cell_9_4: Choice_1_9_4 + 2 Choice_2_9_4 + 3 Choice_3_9_4
 + 4 Choice_4_9_4 + 5 Choice_5_9_4 + 6 Choice_6_9_4 + 7 Choice_7_9_4
 + 8 Choice_8_9_4 + 9 Choice_9_9_4 - Values_9_4 = 0
Unique_cell_9_5: Choice_1_9_5 + 2 Choice_2_9_5 + 3 Choice_3_9_5
 + 4 Choice_4_9_5 + 5 Choice_5_9_5 + 6 Choice_6_9_5 + 7 Choice_7_9_5
 + 8 Choice_8_9_5 + 9 Choice_9_9_5 - Values_9_5 = 0
Unique_cell_9_6: Choice_1_9_6 + 2 Choice_2_9_6 + 3 Choice_3_9_6
 + 4 Choice_4_9_6 + 5 Choice_5_9_6 + 6 Choice_6_9_6 + 7 Choice_7_9_6
 + 8 Choice_8_9_6 + 9 Choice_9_9_6 - Values_9_6 = 0
Unique_cell_9_7: Choice_1_9_7 + 2 Choice_2_9_7 + 3 Choice_3_9_7
 + 4 Choice_4_9_7 + 5 Choice_5_9_7 + 6 Choice_6_9_7 + 7 Choice_7_9_7
 + 8 Choice_8_9_7 + 9 Choice_9_9_7 - Values_9_7 = 0
Unique_cell_9_8: Choice_1_9_8 + 2 Choice_2_9_8 + 3 Choice_3_9_8
 + 4 Choice_4_9_8 + 5 Choice_5_9_8 + 6 Choice_6_9_8 + 7 Choice_7_9_8
 + 8 Choice_8_9_8 + 9 Choice_9_9_8 - Values_9_8 = 0
Unique_cell_9_9: Choice_1_9_9 + 2 Choice_2_9_9 + 3 Choice_3_9_9
 + 4 Choice_4_9_9 + 5 Choice_5_9_9 + 6 Choice_6_9_9 + 7 Choice_7_9_9
 + 8 Choice_8_9_9 + 9 Choice_9_9_9 - Values_9_9 = 0
Bounds
 Abs_Difference_0 <= 2
 Abs_Difference_1 <= 10
 Abs_Difference_2 <= 10
 Abs_Difference_3 <= 10
 Abs_Difference_4 <= 10
 Abs_Difference_5 <= 10
 Abs_Difference_6 <= 10
 Abs_Difference_7 <= 10
 Abs_Difference_8 <= 10
 Abs_Difference_9 <= 10
 FixedDifferencePair free
 FixedProductPair free
 FixedRatioPair free
 FixedSumPair free
 Log10_1_5 <= 2
 Log10_1_6 <= 2
 Log10_2_5 <= 2
 Log10_2_6 <= 2
 Log10_6_2 <= 2
 Log10_6_3 <= 2
 Log10_7_2 <= 2
 Log10_7_3 <= 2
 1 <= Values_1_1 <= 9
 1 <= Values_1_2 <= 9
 1 <= Values_1_3 <= 9
 1 <= Values_1_4 <= 9
 1 <= Values_1_5 <= 9
 1 <= Values_1_6 <= 9
 1 <= Values_1_7 <= 9
 1 <= Values_1_8 <= 9
 1 <= Values_1_9 <= 9
 1 <= Values_2_1 <= 9
 1 <= Values_2_2 <= 9
 1 <= Values_2_3 <= 9
 1 <= Values_2_4 <= 9
 1 <= Values_2_5 <= 9
 1 <= Values_2_6 <= 9
 1 <= Values_2_7 <= 9
 1 <= Values_2_8 <= 9
 1 <= Values_2_9 <= 9
 1 <= Values_3_1 <= 9
 1 <= Values_3_2 <= 9
 1 <= Values_3_3 <= 9
 1 <= Values_3_4 <= 9
 1 <= Values_3_5 <= 9
 1 <= Values_3_6 <= 9
 1 <= Values_3_7 <= 9
 1 <= Values_3_8 <= 9
 1 <= Values_3_9 <= 9
 1 <= Values_4_1 <= 9
 1 <= Values_4_2 <= 9
 1 <= Values_4_3 <= 9
 1 <= Values_4_4 <= 9
 1 <= Values_4_5 <= 9
 1 <= Values_4_6 <= 9
 1 <= Values_4_7 <= 9
 1 <= Values_4_8 <= 9
 1 <= Values_4_9 <= 9
 1 <= Values_5_1 <= 9
 1 <= Values_5_2 <= 9
 1 <= Values_5_3 <= 9
 1 <= Values_5_4 <= 9
 1 <= Values_5_5 <= 9
 1 <= Values_5_6 <= 9
 1 <= Values_5_7 <= 9
 1 <= Values_5_8 <= 9
 1 <= Values_5_9 <= 9
 1 <= Values_6_1 <= 9
 1 <= Values_6_2 <= 9
 1 <= Values_6_3 <= 9
 1 <= Values_6_4 <= 9
 1 <= Values_6_5 <= 9
 1 <= Values_6_6 <= 9
 1 <= Values_6_7 <= 9
 1 <= Values_6_8 <= 9
 1 <= Values_6_9 <= 9
 1 <= Values_7_1 <= 9
 1 <= Values_7_2 <= 9
 1 <= Values_7_3 <= 9
 1 <= Values_7_4 <= 9
 1 <= Values_7_5 <= 9
 1 <= Values_7_6 <= 9
 1 <= Values_7_7 <= 9
 1 <= Values_7_8 <= 9
 1 <= Values_7_9 <= 9
 1 <= Values_8_1 <= 9
 1 <= Values_8_2 <= 9
 1 <= Values_8_3 <= 9
 1 <= Values_8_4 <= 9
 1 <= Values_8_5 <= 9
 1 <= Values_8_6 <= 9
 1 <= Values_8_7 <= 9
 1 <= Values_8_8 <= 9
 1 <= Values_8_9 <= 9
 1 <= Values_9_1 <= 9
 1 <= Values_9_2 <= 9
 1 <= Values_9_3 <= 9
 1 <= Values_9_4 <= 9
 1 <= Values_9_5 <= 9
 1 <= Values_9_6 <= 9
 1 <= Values_9_7 <= 9
 1 <= Values_9_8 <= 9
 1 <= Values_9_9 <= 9
 __dummy = 0
Generals
Values_1_1
Values_1_2
Values_1_3
Values_1_4
Values_1_5
Values_1_6
Values_1_7
Values_1_8
Values_1_9
Values_2_1
Values_2_2
Values_2_3
Values_2_4
Values_2_5
Values_2_6
Values_2_7
Values_2_8
Values_2_9
Values_3_1
Values_3_2
Values_3_3
Values_3_4
Values_3_5
Values_3_6
Values_3_7
Values_3_8
Values_3_9
Values_4_1
Values_4_2
Values_4_3
Values_4_4
Values_4_5
Values_4_6
Values_4_7
Values_4_8
Values_4_9
Values_5_1
Values_5_2
Values_5_3
Values_5_4
Values_5_5
Values_5_6
Values_5_7
Values_5_8
Values_5_9
Values_6_1
Values_6_2
Values_6_3
Values_6_4
Values_6_5
Values_6_6
Values_6_7
Values_6_8
Values_6_9
Values_7_1
Values_7_2
Values_7_3
Values_7_4
Values_7_5
Values_7_6
Values_7_7
Values_7_8
Values_7_9
Values_8_1
Values_8_2
Values_8_3
Values_8_4
Values_8_5
Values_8_6
Values_8_7
Values_8_8
Values_8_9
Values_9_1
Values_9_2
Values_9_3
Values_9_4
Values_9_5
Values_9_6
Values_9_7
Values_9_8
Values_9_9
Binaries
Abs_Indicator_0
Abs_Indicator_1
Abs_Indicator_2
Abs_Indicator_3
Abs_Indicator_4
Abs_Indicator_5
Abs_Indicator_6
Abs_Indicator_7
Abs_Indicator_8
Abs_Indicator_9
Choice_1_1_1
Choice_1_1_2
Choice_1_1_3
Choice_1_1_4
Choice_1_1_5
Choice_1_1_6
Choice_1_1_7
Choice_1_1_8
Choice_1_1_9
Choice_1_2_1
Choice_1_2_2
Choice_1_2_3
Choice_1_2_4
Choice_1_2_5
Choice_1_2_6
Choice_1_2_7
Choice_1_2_8
Choice_1_2_9
Choice_1_3_1
Choice_1_3_2
Choice_1_3_3
Choice_1_3_4
Choice_1_3_5
Choice_1_3_6
Choice_1_3_7
Choice_1_3_8
Choice_1_3_9
Choice_1_4_1
Choice_1_4_2
Choice_1_4_3
Choice_1_4_4
Choice_1_4_5
Choice_1_4_6
Choice_1_4_7
Choice_1_4_8
Choice_1_4_9
Choice_1_5_1
Choice_1_5_2
Choice_1_5_3
Choice_1_5_4
Choice_1_5_5
Choice_1_5_6
Choice_1_5_7
Choice_1_5_8
Choice_1_5_9
Choice_1_6_1
Choice_1_6_2
Choice_1_6_3
Choice_1_6_4
Choice_1_6_5
Choice_1_6_6
Choice_1_6_7
Choice_1_6_8
Choice_1_6_9
Choice_1_7_1
Choice_1_7_2
Choice_1_7_3
Choice_1_7_4
Choice_1_7_5
Choice_1_7_6
Choice_1_7_7
Choice_1_7_8
Choice_1_7_9
Choice_1_8_1
Choice_1_8_2
Choice_1_8_3
Choice_1_8_4
Choice_1_8_5
Choice_1_8_6
Choice_1_8_7
Choice_1_8_8
Choice_1_8_9
Choice_1_9_1
Choice_1_9_2
Choice_1_9_3
Choice_1_9_4
Choice_1_9_5
Choice_1_9_6
Choice_1_9_7
Choice_1_9_8
Choice_1_9_9
Choice_2_1_1
Choice_2_1_2
Choice_2_1_3
Choice_2_1_4
Choice_2_1_5
Choice_2_1_6
Choice_2_1_7
Choice_2_1_8
Choice_2_1_9
Choice_2_2_1
Choice_2_2_2
Choice_2_2_3
Choice_2_2_4
Choice_2_2_5
Choice_2_2_6
Choice_2_2_7
Choice_2_2_8
Choice_2_2_9
Choice_2_3_1
Choice_2_3_2
Choice_2_3_3
Choice_2_3_4
Choice_2_3_5
Choice_2_3_6
Choice_2_3_7
Choice_2_3_8
Choice_2_3_9
Choice_2_4_1
Choice_2_4_2
Choice_2_4_3
Choice_2_4_4
Choice_2_4_5
Choice_2_4_6
Choice_2_4_7
Choice_2_4_8
Choice_2_4_9
Choice_2_5_1
Choice_2_5_2
Choice_2_5_3
Choice_2_5_4
Choice_2_5_5
Choice_2_5_6
Choice_2_5_7
Choice_2_5_8
Choice_2_5_9
Choice_2_6_1
Choice_2_6_2
Choice_2_6_3
Choice_2_6_4
Choice_2_6_5
Choice_2_6_6
Choice_2_6_7
Choice_2_6_8
Choice_2_6_9
Choice_2_7_1
Choice_2_7_2
Choice_2_7_3
Choice_2_7_4
Choice_2_7_5
Choice_2_7_6
Choice_2_7_7
Choice_2_7_8
Choice_2_7_9
Choice_2_8_1
Choice_2_8_2
Choice_2_8_3
Choice_2_8_4
Choice_2_8_5
Choice_2_8_6
Choice_2_8_7
Choice_2_8_8
Choice_2_8_9
Choice_2_9_1
Choice_2_9_2
Choice_2_9_3
Choice_2_9_4
Choice_2_9_5
Choice_2_9_6
Choice_2_9_7
Choice_2_9_8
Choice_2_9_9
Choice_3_1_1
Choice_3_1_2
Choice_3_1_3
Choice_3_1_4
Choice_3_1_5
Choice_3_1_6
Choice_3_1_7
Choice_3_1_8
Choice_3_1_9
Choice_3_2_1
Choice_3_2_2
Choice_3_2_3
Choice_3_2_4
Choice_3_2_5
Choice_3_2_6
Choice_3_2_7
Choice_3_2_8
Choice_3_2_9
Choice_3_3_1
Choice_3_3_2
Choice_3_3_3
Choice_3_3_4
Choice_3_3_5
Choice_3_3_6
Choice_3_3_7
Choice_3_3_8
Choice_3_3_9
Choice_3_4_1
Choice_3_4_2
Choice_3_4_3
Choice_3_4_4
Choice_3_4_5
Choice_3_4_6
Choice_3_4_7
Choice_3_4_8
Choice_3_4_9
Choice_3_5_1
Choice_3_5_2
Choice_3_5_3
Choice_3_5_4
Choice_3_5_5
Choice_3_5_6
Choice_3_5_7
Choice_3_5_8
Choice_3_5_9
Choice_3_6_1
Choice_3_6_2
Choice_3_6_3
Choice_3_6_4
Choice_3_6_5
Choice_3_6_6
Choice_3_6_7
Choice_3_6_8
Choice_3_6_9
Choice_3_7_1
Choice_3_7_2
Choice_3_7_3
Choice_3_7_4
Choice_3_7_5
Choice_3_7_6
Choice_3_7_7
Choice_3_7_8
Choice_3_7_9
Choice_3_8_1
Choice_3_8_2
Choice_3_8_3
Choice_3_8_4
Choice_3_8_5
Choice_3_8_6
Choice_3_8_7
Choice_3_8_8
Choice_3_8_9
Choice_3_9_1
Choice_3_9_2
Choice_3_9_3
Choice_3_9_4
Choice_3_9_5
Choice_3_9_6
Choice_3_9_7
Choice_3_9_8
Choice_3_9_9
Choice_4_1_1
Choice_4_1_2
Choice_4_1_3
Choice_4_1_4
Choice_4_1_5
Choice_4_1_6
Choice_4_1_7
Choice_4_1_8
Choice_4_1_9
Choice_4_2_1
Choice_4_2_2
Choice_4_2_3
Choice_4_2_4
Choice_4_2_5
Choice_4_2_6
Choice_4_2_7
Choice_4_2_8
Choice_4_2_9
Choice_4_3_1
Choice_4_3_2
Choice_4_3_3
Choice_4_3_4
Choice_4_3_5
Choice_4_3_6
Choice_4_3_7
Choice_4_3_8
Choice_4_3_9
Choice_4_4_1
Choice_4_4_2
Choice_4_4_3
Choice_4_4_4
Choice_4_4_5
Choice_4_4_6
Choice_4_4_7
Choice_4_4_8
Choice_4_4_9
Choice_4_5_1
Choice_4_5_2
Choice_4_5_3
Choice_4_5_4
Choice_4_5_5
Choice_4_5_6
Choice_4_5_7
Choice_4_5_8
Choice_4_5_9
Choice_4_6_1
Choice_4_6_2
Choice_4_6_3
Choice_4_6_4
Choice_4_6_5
Choice_4_6_6
Choice_4_6_7
Choice_4_6_8
Choice_4_6_9
Choice_4_7_1
Choice_4_7_2
Choice_4_7_3
Choice_4_7_4
Choice_4_7_5
Choice_4_7_6
Choice_4_7_7
Choice_4_7_8
Choice_4_7_9
Choice_4_8_1
Choice_4_8_2
Choice_4_8_3
Choice_4_8_4
Choice_4_8_5
Choice_4_8_6
Choice_4_8_7
Choice_4_8_8
Choice_4_8_9
Choice_4_9_1
Choice_4_9_2
Choice_4_9_3
Choice_4_9_4
Choice_4_9_5
Choice_4_9_6
Choice_4_9_7
Choice_4_9_8
Choice_4_9_9
Choice_5_1_1
Choice_5_1_2
Choice_5_1_3
Choice_5_1_4
Choice_5_1_5
Choice_5_1_6
Choice_5_1_7
Choice_5_1_8
Choice_5_1_9
Choice_5_2_1
Choice_5_2_2
Choice_5_2_3
Choice_5_2_4
Choice_5_2_5
Choice_5_2_6
Choice_5_2_7
Choice_5_2_8
Choice_5_2_9
Choice_5_3_1
Choice_5_3_2
Choice_5_3_3
Choice_5_3_4
Choice_5_3_5
Choice_5_3_6
Choice_5_3_7
Choice_5_3_8
Choice_5_3_9
Choice_5_4_1
Choice_5_4_2
Choice_5_4_3
Choice_5_4_4
Choice_5_4_5
Choice_5_4_6
Choice_5_4_7
Choice_5_4_8
Choice_5_4_9
Choice_5_5_1
Choice_5_5_2
Choice_5_5_3
Choice_5_5_4
Choice_5_5_5
Choice_5_5_6
Choice_5_5_7
Choice_5_5_8
Choice_5_5_9
Choice_5_6_1
Choice_5_6_2
Choice_5_6_3
Choice_5_6_4
Choice_5_6_5
Choice_5_6_6
Choice_5_6_7
Choice_5_6_8
Choice_5_6_9
Choice_5_7_1
Choice_5_7_2
Choice_5_7_3
Choice_5_7_4
Choice_5_7_5
Choice_5_7_6
Choice_5_7_7
Choice_5_7_8
Choice_5_7_9
Choice_5_8_1
Choice_5_8_2
Choice_5_8_3
Choice_5_8_4
Choice_5_8_5
Choice_5_8_6
Choice_5_8_7
Choice_5_8_8
Choice_5_8_9
Choice_5_9_1
Choice_5_9_2
Choice_5_9_3
Choice_5_9_4
Choice_5_9_5
Choice_5_9_6
Choice_5_9_7
Choice_5_9_8
Choice_5_9_9
Choice_6_1_1
Choice_6_1_2
Choice_6_1_3
Choice_6_1_4
Choice_6_1_5
Choice_6_1_6
Choice_6_1_7
Choice_6_1_8
Choice_6_1_9
Choice_6_2_1
Choice_6_2_2
Choice_6_2_3
Choice_6_2_4
Choice_6_2_5
Choice_6_2_6
Choice_6_2_7
Choice_6_2_8
Choice_6_2_9
Choice_6_3_1
Choice_6_3_2
Choice_6_3_3
Choice_6_3_4
Choice_6_3_5
Choice_6_3_6
Choice_6_3_7
Choice_6_3_8
Choice_6_3_9
Choice_6_4_1
Choice_6_4_2
Choice_6_4_3
Choice_6_4_4
Choice_6_4_5
Choice_6_4_6
Choice_6_4_7
Choice_6_4_8
Choice_6_4_9
Choice_6_5_1
Choice_6_5_2
Choice_6_5_3
Choice_6_5_4
Choice_6_5_5
Choice_6_5_6
Choice_6_5_7
Choice_6_5_8
Choice_6_5_9
Choice_6_6_1
Choice_6_6_2
Choice_6_6_3
Choice_6_6_4
Choice_6_6_5
Choice_6_6_6
Choice_6_6_7
Choice_6_6_8
Choice_6_6_9
Choice_6_7_1
Choice_6_7_2
Choice_6_7_3
Choice_6_7_4
Choice_6_7_5
Choice_6_7_6
Choice_6_7_7
Choice_6_7_8
Choice_6_7_9
Choice_6_8_1
Choice_6_8_2
Choice_6_8_3
Choice_6_8_4
Choice_6_8_5
Choice_6_8_6
Choice_6_8_7
Choice_6_8_8
Choice_6_8_9
Choice_6_9_1
Choice_6_9_2
Choice_6_9_3
Choice_6_9_4
Choice_6_9_5
Choice_6_9_6
Choice_6_9_7
Choice_6_9_8
Choice_6_9_9
Choice_7_1_1
Choice_7_1_2
Choice_7_1_3
Choice_7_1_4
Choice_7_1_5
Choice_7_1_6
Choice_7_1_7
Choice_7_1_8
Choice_7_1_9
Choice_7_2_1
Choice_7_2_2
Choice_7_2_3
Choice_7_2_4
Choice_7_2_5
Choice_7_2_6
Choice_7_2_7
Choice_7_2_8
Choice_7_2_9
Choice_7_3_1
Choice_7_3_2
Choice_7_3_3
Choice_7_3_4
Choice_7_3_5
Choice_7_3_6
Choice_7_3_7
Choice_7_3_8
Choice_7_3_9
Choice_7_4_1
Choice_7_4_2
Choice_7_4_3
Choice_7_4_4
Choice_7_4_5
Choice_7_4_6
Choice_7_4_7
Choice_7_4_8
Choice_7_4_9
Choice_7_5_1
Choice_7_5_2
Choice_7_5_3
Choice_7_5_4
Choice_7_5_5
Choice_7_5_6
Choice_7_5_7
Choice_7_5_8
Choice_7_5_9
Choice_7_6_1
Choice_7_6_2
Choice_7_6_3
Choice_7_6_4
Choice_7_6_5
Choice_7_6_6
Choice_7_6_7
Choice_7_6_8
Choice_7_6_9
Choice_7_7_1
Choice_7_7_2
Choice_7_7_3
Choice_7_7_4
Choice_7_7_5
Choice_7_7_6
Choice_7_7_7
Choice_7_7_8
Choice_7_7_9
Choice_7_8_1
Choice_7_8_2
Choice_7_8_3
Choice_7_8_4
Choice_7_8_5
Choice_7_8_6
Choice_7_8_7
Choice_7_8_8
Choice_7_8_9
Choice_7_9_1
Choice_7_9_2
Choice_7_9_3
Choice_7_9_4
Choice_7_9_5
Choice_7_9_6
Choice_7_9_7
Choice_7_9_8
Choice_7_9_9
Choice_8_1_1
Choice_8_1_2
Choice_8_1_3
Choice_8_1_4
Choice_8_1_5
Choice_8_1_6
Choice_8_1_7
Choice_8_1_8
Choice_8_1_9
Choice_8_2_1
Choice_8_2_2
Choice_8_2_3
Choice_8_2_4
Choice_8_2_5
Choice_8_2_6
Choice_8_2_7
Choice_8_2_8
Choice_8_2_9
Choice_8_3_1
Choice_8_3_2
Choice_8_3_3
Choice_8_3_4
Choice_8_3_5
Choice_8_3_6
Choice_8_3_7
Choice_8_3_8
Choice_8_3_9
Choice_8_4_1
Choice_8_4_2
Choice_8_4_3
Choice_8_4_4
Choice_8_4_5
Choice_8_4_6
Choice_8_4_7
Choice_8_4_8
Choice_8_4_9
Choice_8_5_1
Choice_8_5_2
Choice_8_5_3
Choice_8_5_4
Choice_8_5_5
Choice_8_5_6
Choice_8_5_7
Choice_8_5_8
Choice_8_5_9
Choice_8_6_1
Choice_8_6_2
Choice_8_6_3
Choice_8_6_4
Choice_8_6_5
Choice_8_6_6
Choice_8_6_7
Choice_8_6_8
Choice_8_6_9
Choice_8_7_1
Choice_8_7_2
Choice_8_7_3
Choice_8_7_4
Choice_8_7_5
Choice_8_7_6
Choice_8_7_7
Choice_8_7_8
Choice_8_7_9
Choice_8_8_1
Choice_8_8_2
Choice_8_8_3
Choice_8_8_4
Choice_8_8_5
Choice_8_8_6
Choice_8_8_7
Choice_8_8_8
Choice_8_8_9
Choice_8_9_1
Choice_8_9_2
Choice_8_9_3
Choice_8_9_4
Choice_8_9_5
Choice_8_9_6
Choice_8_9_7
Choice_8_9_8
Choice_8_9_9
Choice_9_1_1
Choice_9_1_2
Choice_9_1_3
Choice_9_1_4
Choice_9_1_5
Choice_9_1_6
Choice_9_1_7
Choice_9_1_8
Choice_9_1_9
Choice_9_2_1
Choice_9_2_2
Choice_9_2_3
Choice_9_2_4
Choice_9_2_5
Choice_9_2_6
Choice_9_2_7
Choice_9_2_8
Choice_9_2_9
Choice_9_3_1
Choice_9_3_2
Choice_9_3_3
Choice_9_3_4
Choice_9_3_5
Choice_9_3_6
Choice_9_3_7
Choice_9_3_8
Choice_9_3_9
Choice_9_4_1
Choice_9_4_2
Choice_9_4_3
Choice_9_4_4
Choice_9_4_5
Choice_9_4_6
Choice_9_4_7
Choice_9_4_8
Choice_9_4_9
Choice_9_5_1
Choice_9_5_2
Choice_9_5_3
Choice_9_5_4
Choice_9_5_5
Choice_9_5_6
Choice_9_5_7
Choice_9_5_8
Choice_9_5_9
Choice_9_6_1
Choice_9_6_2
Choice_9_6_3
Choice_9_6_4
Choice_9_6_5
Choice_9_6_6
Choice_9_6_7
Choice_9_6_8
Choice_9_6_9
Choice_9_7_1
Choice_9_7_2
Choice_9_7_3
Choice_9_7_4
Choice_9_7_5
Choice_9_7_6
Choice_9_7_7
Choice_9_7_8
Choice_9_7_9
Choice_9_8_1
Choice_9_8_2
Choice_9_8_3
Choice_9_8_4
Choice_9_8_5
Choice_9_8_6
Choice_9_8_7
Choice_9_8_8
Choice_9_8_9
Choice_9_9_1
Choice_9_9_2
Choice_9_9_3
Choice_9_9_4
Choice_9_9_5
Choice_9_9_6
Choice_9_9_7
Choice_9_9_8
Choice_9_9_9
End
