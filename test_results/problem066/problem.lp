\* Sudoku *\
Minimize
Objective: __dummy
Subject To
Arrow_131620: Values_1_2 + Values_2_3 - Values_2_5 + Values_3_4 = 0
Arrow_131620_1_7_tail: Choice_7_3_4 = 0
Arrow_131620_1_8_tail: Choice_8_3_4 = 0
Arrow_131620_1_9_tail: Choice_9_3_4 = 0
Arrow_131620_1_head: Choice_1_2_5 = 0
Arrow_131620_2_7_tail: Choice_7_2_3 = 0
Arrow_131620_2_8_tail: Choice_8_2_3 = 0
Arrow_131620_2_9_tail: Choice_9_2_3 = 0
Arrow_131620_2_head: Choice_2_2_5 = 0
Arrow_131620_3_7_tail: Choice_7_1_2 = 0
Arrow_131620_3_8_tail: Choice_8_1_2 = 0
Arrow_131620_3_9_tail: Choice_9_1_2 = 0
Arrow_131620_3_head: Choice_3_2_5 = 0
Arrow_131620_head: Values_2_5 >= 4
Arrow_131621: Values_4_3 + Values_5_3 + Values_6_2 + Values_7_2 - Values_8_2
 = 0
Arrow_131621_1_4_tail: Choice_4_7_2 = 0
Arrow_131621_1_5_tail: Choice_5_7_2 = 0
Arrow_131621_1_6_tail: Choice_6_7_2 = 0
Arrow_131621_1_7_tail: Choice_7_7_2 = 0
Arrow_131621_1_8_tail: Choice_8_7_2 = 0
Arrow_131621_1_9_tail: Choice_9_7_2 = 0
Arrow_131621_1_head: Choice_1_8_2 = 0
Arrow_131621_2_4_tail: Choice_4_6_2 = 0
Arrow_131621_2_5_tail: Choice_5_6_2 = 0
Arrow_131621_2_6_tail: Choice_6_6_2 = 0
Arrow_131621_2_7_tail: Choice_7_6_2 = 0
Arrow_131621_2_8_tail: Choice_8_6_2 = 0
Arrow_131621_2_9_tail: Choice_9_6_2 = 0
Arrow_131621_2_head: Choice_2_8_2 = 0
Arrow_131621_3_4_tail: Choice_4_5_3 = 0
Arrow_131621_3_5_tail: Choice_5_5_3 = 0
Arrow_131621_3_6_tail: Choice_6_5_3 = 0
Arrow_131621_3_7_tail: Choice_7_5_3 = 0
Arrow_131621_3_8_tail: Choice_8_5_3 = 0
Arrow_131621_3_9_tail: Choice_9_5_3 = 0
Arrow_131621_3_head: Choice_3_8_2 = 0
Arrow_131621_4_4_tail: Choice_4_4_3 = 0
Arrow_131621_4_5_tail: Choice_5_4_3 = 0
Arrow_131621_4_6_tail: Choice_6_4_3 = 0
Arrow_131621_4_7_tail: Choice_7_4_3 = 0
Arrow_131621_4_8_tail: Choice_8_4_3 = 0
Arrow_131621_4_9_tail: Choice_9_4_3 = 0
Arrow_131621_4_head: Choice_4_8_2 = 0
Arrow_131621_5_head: Choice_5_8_2 = 0
Arrow_131621_6_head: Choice_6_8_2 = 0
Arrow_131621_head: Values_8_2 >= 7
Arrow_131622: Values_5_5 + Values_6_4 + Values_7_4 - Values_8_5 = 0
Arrow_131622_1_7_tail: Choice_7_7_4 = 0
Arrow_131622_1_8_tail: Choice_8_7_4 = 0
Arrow_131622_1_9_tail: Choice_9_7_4 = 0
Arrow_131622_1_head: Choice_1_8_5 = 0
Arrow_131622_2_7_tail: Choice_7_6_4 = 0
Arrow_131622_2_8_tail: Choice_8_6_4 = 0
Arrow_131622_2_9_tail: Choice_9_6_4 = 0
Arrow_131622_2_head: Choice_2_8_5 = 0
Arrow_131622_3_7_tail: Choice_7_5_5 = 0
Arrow_131622_3_8_tail: Choice_8_5_5 = 0
Arrow_131622_3_9_tail: Choice_9_5_5 = 0
Arrow_131622_3_head: Choice_3_8_5 = 0
Arrow_131622_head: Values_8_5 >= 4
Arrow_131623: - Values_3_6 + Values_4_7 + Values_5_6 + Values_6_7 + Values_7_6
 = 0
Arrow_131623_1_6_tail: Choice_6_4_7 = 0
Arrow_131623_1_7_tail: Choice_7_4_7 = 0
Arrow_131623_1_8_tail: Choice_8_4_7 = 0
Arrow_131623_1_9_tail: Choice_9_4_7 = 0
Arrow_131623_1_head: Choice_1_3_6 = 0
Arrow_131623_2_6_tail: Choice_6_5_6 = 0
Arrow_131623_2_7_tail: Choice_7_5_6 = 0
Arrow_131623_2_8_tail: Choice_8_5_6 = 0
Arrow_131623_2_9_tail: Choice_9_5_6 = 0
Arrow_131623_2_head: Choice_2_3_6 = 0
Arrow_131623_3_6_tail: Choice_6_6_7 = 0
Arrow_131623_3_7_tail: Choice_7_6_7 = 0
Arrow_131623_3_8_tail: Choice_8_6_7 = 0
Arrow_131623_3_9_tail: Choice_9_6_7 = 0
Arrow_131623_3_head: Choice_3_3_6 = 0
Arrow_131623_4_6_tail: Choice_6_7_6 = 0
Arrow_131623_4_7_tail: Choice_7_7_6 = 0
Arrow_131623_4_8_tail: Choice_8_7_6 = 0
Arrow_131623_4_9_tail: Choice_9_7_6 = 0
Arrow_131623_4_head: Choice_4_3_6 = 0
Arrow_131623_head: Values_3_6 >= 5
Box_131610_Unique_1: Choice_1_1_1 + Choice_1_1_2 + Choice_1_1_3 + Choice_1_2_1
 + Choice_1_2_2 + Choice_1_2_3 + Choice_1_3_1 + Choice_1_3_2 + Choice_1_3_3
 = 1
Box_131610_Unique_2: Choice_2_1_1 + Choice_2_1_2 + Choice_2_1_3 + Choice_2_2_1
 + Choice_2_2_2 + Choice_2_2_3 + Choice_2_3_1 + Choice_2_3_2 + Choice_2_3_3
 = 1
Box_131610_Unique_3: Choice_3_1_1 + Choice_3_1_2 + Choice_3_1_3 + Choice_3_2_1
 + Choice_3_2_2 + Choice_3_2_3 + Choice_3_3_1 + Choice_3_3_2 + Choice_3_3_3
 = 1
Box_131610_Unique_4: Choice_4_1_1 + Choice_4_1_2 + Choice_4_1_3 + Choice_4_2_1
 + Choice_4_2_2 + Choice_4_2_3 + Choice_4_3_1 + Choice_4_3_2 + Choice_4_3_3
 = 1
Box_131610_Unique_5: Choice_5_1_1 + Choice_5_1_2 + Choice_5_1_3 + Choice_5_2_1
 + Choice_5_2_2 + Choice_5_2_3 + Choice_5_3_1 + Choice_5_3_2 + Choice_5_3_3
 = 1
Box_131610_Unique_6: Choice_6_1_1 + Choice_6_1_2 + Choice_6_1_3 + Choice_6_2_1
 + Choice_6_2_2 + Choice_6_2_3 + Choice_6_3_1 + Choice_6_3_2 + Choice_6_3_3
 = 1
Box_131610_Unique_7: Choice_7_1_1 + Choice_7_1_2 + Choice_7_1_3 + Choice_7_2_1
 + Choice_7_2_2 + Choice_7_2_3 + Choice_7_3_1 + Choice_7_3_2 + Choice_7_3_3
 = 1
Box_131610_Unique_8: Choice_8_1_1 + Choice_8_1_2 + Choice_8_1_3 + Choice_8_2_1
 + Choice_8_2_2 + Choice_8_2_3 + Choice_8_3_1 + Choice_8_3_2 + Choice_8_3_3
 = 1
Box_131610_Unique_9: Choice_9_1_1 + Choice_9_1_2 + Choice_9_1_3 + Choice_9_2_1
 + Choice_9_2_2 + Choice_9_2_3 + Choice_9_3_1 + Choice_9_3_2 + Choice_9_3_3
 = 1
Box_131611_Unique_1: Choice_1_4_1 + Choice_1_4_2 + Choice_1_4_3 + Choice_1_5_1
 + Choice_1_5_2 + Choice_1_5_3 + Choice_1_6_1 + Choice_1_6_2 + Choice_1_6_3
 = 1
Box_131611_Unique_2: Choice_2_4_1 + Choice_2_4_2 + Choice_2_4_3 + Choice_2_5_1
 + Choice_2_5_2 + Choice_2_5_3 + Choice_2_6_1 + Choice_2_6_2 + Choice_2_6_3
 = 1
Box_131611_Unique_3: Choice_3_4_1 + Choice_3_4_2 + Choice_3_4_3 + Choice_3_5_1
 + Choice_3_5_2 + Choice_3_5_3 + Choice_3_6_1 + Choice_3_6_2 + Choice_3_6_3
 = 1
Box_131611_Unique_4: Choice_4_4_1 + Choice_4_4_2 + Choice_4_4_3 + Choice_4_5_1
 + Choice_4_5_2 + Choice_4_5_3 + Choice_4_6_1 + Choice_4_6_2 + Choice_4_6_3
 = 1
Box_131611_Unique_5: Choice_5_4_1 + Choice_5_4_2 + Choice_5_4_3 + Choice_5_5_1
 + Choice_5_5_2 + Choice_5_5_3 + Choice_5_6_1 + Choice_5_6_2 + Choice_5_6_3
 = 1
Box_131611_Unique_6: Choice_6_4_1 + Choice_6_4_2 + Choice_6_4_3 + Choice_6_5_1
 + Choice_6_5_2 + Choice_6_5_3 + Choice_6_6_1 + Choice_6_6_2 + Choice_6_6_3
 = 1
Box_131611_Unique_7: Choice_7_4_1 + Choice_7_4_2 + Choice_7_4_3 + Choice_7_5_1
 + Choice_7_5_2 + Choice_7_5_3 + Choice_7_6_1 + Choice_7_6_2 + Choice_7_6_3
 = 1
Box_131611_Unique_8: Choice_8_4_1 + Choice_8_4_2 + Choice_8_4_3 + Choice_8_5_1
 + Choice_8_5_2 + Choice_8_5_3 + Choice_8_6_1 + Choice_8_6_2 + Choice_8_6_3
 = 1
Box_131611_Unique_9: Choice_9_4_1 + Choice_9_4_2 + Choice_9_4_3 + Choice_9_5_1
 + Choice_9_5_2 + Choice_9_5_3 + Choice_9_6_1 + Choice_9_6_2 + Choice_9_6_3
 = 1
Box_131612_Unique_1: Choice_1_7_1 + Choice_1_7_2 + Choice_1_7_3 + Choice_1_8_1
 + Choice_1_8_2 + Choice_1_8_3 + Choice_1_9_1 + Choice_1_9_2 + Choice_1_9_3
 = 1
Box_131612_Unique_2: Choice_2_7_1 + Choice_2_7_2 + Choice_2_7_3 + Choice_2_8_1
 + Choice_2_8_2 + Choice_2_8_3 + Choice_2_9_1 + Choice_2_9_2 + Choice_2_9_3
 = 1
Box_131612_Unique_3: Choice_3_7_1 + Choice_3_7_2 + Choice_3_7_3 + Choice_3_8_1
 + Choice_3_8_2 + Choice_3_8_3 + Choice_3_9_1 + Choice_3_9_2 + Choice_3_9_3
 = 1
Box_131612_Unique_4: Choice_4_7_1 + Choice_4_7_2 + Choice_4_7_3 + Choice_4_8_1
 + Choice_4_8_2 + Choice_4_8_3 + Choice_4_9_1 + Choice_4_9_2 + Choice_4_9_3
 = 1
Box_131612_Unique_5: Choice_5_7_1 + Choice_5_7_2 + Choice_5_7_3 + Choice_5_8_1
 + Choice_5_8_2 + Choice_5_8_3 + Choice_5_9_1 + Choice_5_9_2 + Choice_5_9_3
 = 1
Box_131612_Unique_6: Choice_6_7_1 + Choice_6_7_2 + Choice_6_7_3 + Choice_6_8_1
 + Choice_6_8_2 + Choice_6_8_3 + Choice_6_9_1 + Choice_6_9_2 + Choice_6_9_3
 = 1
Box_131612_Unique_7: Choice_7_7_1 + Choice_7_7_2 + Choice_7_7_3 + Choice_7_8_1
 + Choice_7_8_2 + Choice_7_8_3 + Choice_7_9_1 + Choice_7_9_2 + Choice_7_9_3
 = 1
Box_131612_Unique_8: Choice_8_7_1 + Choice_8_7_2 + Choice_8_7_3 + Choice_8_8_1
 + Choice_8_8_2 + Choice_8_8_3 + Choice_8_9_1 + Choice_8_9_2 + Choice_8_9_3
 = 1
Box_131612_Unique_9: Choice_9_7_1 + Choice_9_7_2 + Choice_9_7_3 + Choice_9_8_1
 + Choice_9_8_2 + Choice_9_8_3 + Choice_9_9_1 + Choice_9_9_2 + Choice_9_9_3
 = 1
Box_131613_Unique_1: Choice_1_1_4 + Choice_1_1_5 + Choice_1_1_6 + Choice_1_2_4
 + Choice_1_2_5 + Choice_1_2_6 + Choice_1_3_4 + Choice_1_3_5 + Choice_1_3_6
 = 1
Box_131613_Unique_2: Choice_2_1_4 + Choice_2_1_5 + Choice_2_1_6 + Choice_2_2_4
 + Choice_2_2_5 + Choice_2_2_6 + Choice_2_3_4 + Choice_2_3_5 + Choice_2_3_6
 = 1
Box_131613_Unique_3: Choice_3_1_4 + Choice_3_1_5 + Choice_3_1_6 + Choice_3_2_4
 + Choice_3_2_5 + Choice_3_2_6 + Choice_3_3_4 + Choice_3_3_5 + Choice_3_3_6
 = 1
Box_131613_Unique_4: Choice_4_1_4 + Choice_4_1_5 + Choice_4_1_6 + Choice_4_2_4
 + Choice_4_2_5 + Choice_4_2_6 + Choice_4_3_4 + Choice_4_3_5 + Choice_4_3_6
 = 1
Box_131613_Unique_5: Choice_5_1_4 + Choice_5_1_5 + Choice_5_1_6 + Choice_5_2_4
 + Choice_5_2_5 + Choice_5_2_6 + Choice_5_3_4 + Choice_5_3_5 + Choice_5_3_6
 = 1
Box_131613_Unique_6: Choice_6_1_4 + Choice_6_1_5 + Choice_6_1_6 + Choice_6_2_4
 + Choice_6_2_5 + Choice_6_2_6 + Choice_6_3_4 + Choice_6_3_5 + Choice_6_3_6
 = 1
Box_131613_Unique_7: Choice_7_1_4 + Choice_7_1_5 + Choice_7_1_6 + Choice_7_2_4
 + Choice_7_2_5 + Choice_7_2_6 + Choice_7_3_4 + Choice_7_3_5 + Choice_7_3_6
 = 1
Box_131613_Unique_8: Choice_8_1_4 + Choice_8_1_5 + Choice_8_1_6 + Choice_8_2_4
 + Choice_8_2_5 + Choice_8_2_6 + Choice_8_3_4 + Choice_8_3_5 + Choice_8_3_6
 = 1
Box_131613_Unique_9: Choice_9_1_4 + Choice_9_1_5 + Choice_9_1_6 + Choice_9_2_4
 + Choice_9_2_5 + Choice_9_2_6 + Choice_9_3_4 + Choice_9_3_5 + Choice_9_3_6
 = 1
Box_131614_Unique_1: Choice_1_4_4 + Choice_1_4_5 + Choice_1_4_6 + Choice_1_5_4
 + Choice_1_5_5 + Choice_1_5_6 + Choice_1_6_4 + Choice_1_6_5 + Choice_1_6_6
 = 1
Box_131614_Unique_2: Choice_2_4_4 + Choice_2_4_5 + Choice_2_4_6 + Choice_2_5_4
 + Choice_2_5_5 + Choice_2_5_6 + Choice_2_6_4 + Choice_2_6_5 + Choice_2_6_6
 = 1
Box_131614_Unique_3: Choice_3_4_4 + Choice_3_4_5 + Choice_3_4_6 + Choice_3_5_4
 + Choice_3_5_5 + Choice_3_5_6 + Choice_3_6_4 + Choice_3_6_5 + Choice_3_6_6
 = 1
Box_131614_Unique_4: Choice_4_4_4 + Choice_4_4_5 + Choice_4_4_6 + Choice_4_5_4
 + Choice_4_5_5 + Choice_4_5_6 + Choice_4_6_4 + Choice_4_6_5 + Choice_4_6_6
 = 1
Box_131614_Unique_5: Choice_5_4_4 + Choice_5_4_5 + Choice_5_4_6 + Choice_5_5_4
 + Choice_5_5_5 + Choice_5_5_6 + Choice_5_6_4 + Choice_5_6_5 + Choice_5_6_6
 = 1
Box_131614_Unique_6: Choice_6_4_4 + Choice_6_4_5 + Choice_6_4_6 + Choice_6_5_4
 + Choice_6_5_5 + Choice_6_5_6 + Choice_6_6_4 + Choice_6_6_5 + Choice_6_6_6
 = 1
Box_131614_Unique_7: Choice_7_4_4 + Choice_7_4_5 + Choice_7_4_6 + Choice_7_5_4
 + Choice_7_5_5 + Choice_7_5_6 + Choice_7_6_4 + Choice_7_6_5 + Choice_7_6_6
 = 1
Box_131614_Unique_8: Choice_8_4_4 + Choice_8_4_5 + Choice_8_4_6 + Choice_8_5_4
 + Choice_8_5_5 + Choice_8_5_6 + Choice_8_6_4 + Choice_8_6_5 + Choice_8_6_6
 = 1
Box_131614_Unique_9: Choice_9_4_4 + Choice_9_4_5 + Choice_9_4_6 + Choice_9_5_4
 + Choice_9_5_5 + Choice_9_5_6 + Choice_9_6_4 + Choice_9_6_5 + Choice_9_6_6
 = 1
Box_131615_Unique_1: Choice_1_7_4 + Choice_1_7_5 + Choice_1_7_6 + Choice_1_8_4
 + Choice_1_8_5 + Choice_1_8_6 + Choice_1_9_4 + Choice_1_9_5 + Choice_1_9_6
 = 1
Box_131615_Unique_2: Choice_2_7_4 + Choice_2_7_5 + Choice_2_7_6 + Choice_2_8_4
 + Choice_2_8_5 + Choice_2_8_6 + Choice_2_9_4 + Choice_2_9_5 + Choice_2_9_6
 = 1
Box_131615_Unique_3: Choice_3_7_4 + Choice_3_7_5 + Choice_3_7_6 + Choice_3_8_4
 + Choice_3_8_5 + Choice_3_8_6 + Choice_3_9_4 + Choice_3_9_5 + Choice_3_9_6
 = 1
Box_131615_Unique_4: Choice_4_7_4 + Choice_4_7_5 + Choice_4_7_6 + Choice_4_8_4
 + Choice_4_8_5 + Choice_4_8_6 + Choice_4_9_4 + Choice_4_9_5 + Choice_4_9_6
 = 1
Box_131615_Unique_5: Choice_5_7_4 + Choice_5_7_5 + Choice_5_7_6 + Choice_5_8_4
 + Choice_5_8_5 + Choice_5_8_6 + Choice_5_9_4 + Choice_5_9_5 + Choice_5_9_6
 = 1
Box_131615_Unique_6: Choice_6_7_4 + Choice_6_7_5 + Choice_6_7_6 + Choice_6_8_4
 + Choice_6_8_5 + Choice_6_8_6 + Choice_6_9_4 + Choice_6_9_5 + Choice_6_9_6
 = 1
Box_131615_Unique_7: Choice_7_7_4 + Choice_7_7_5 + Choice_7_7_6 + Choice_7_8_4
 + Choice_7_8_5 + Choice_7_8_6 + Choice_7_9_4 + Choice_7_9_5 + Choice_7_9_6
 = 1
Box_131615_Unique_8: Choice_8_7_4 + Choice_8_7_5 + Choice_8_7_6 + Choice_8_8_4
 + Choice_8_8_5 + Choice_8_8_6 + Choice_8_9_4 + Choice_8_9_5 + Choice_8_9_6
 = 1
Box_131615_Unique_9: Choice_9_7_4 + Choice_9_7_5 + Choice_9_7_6 + Choice_9_8_4
 + Choice_9_8_5 + Choice_9_8_6 + Choice_9_9_4 + Choice_9_9_5 + Choice_9_9_6
 = 1
Box_131616_Unique_1: Choice_1_1_7 + Choice_1_1_8 + Choice_1_1_9 + Choice_1_2_7
 + Choice_1_2_8 + Choice_1_2_9 + Choice_1_3_7 + Choice_1_3_8 + Choice_1_3_9
 = 1
Box_131616_Unique_2: Choice_2_1_7 + Choice_2_1_8 + Choice_2_1_9 + Choice_2_2_7
 + Choice_2_2_8 + Choice_2_2_9 + Choice_2_3_7 + Choice_2_3_8 + Choice_2_3_9
 = 1
Box_131616_Unique_3: Choice_3_1_7 + Choice_3_1_8 + Choice_3_1_9 + Choice_3_2_7
 + Choice_3_2_8 + Choice_3_2_9 + Choice_3_3_7 + Choice_3_3_8 + Choice_3_3_9
 = 1
Box_131616_Unique_4: Choice_4_1_7 + Choice_4_1_8 + Choice_4_1_9 + Choice_4_2_7
 + Choice_4_2_8 + Choice_4_2_9 + Choice_4_3_7 + Choice_4_3_8 + Choice_4_3_9
 = 1
Box_131616_Unique_5: Choice_5_1_7 + Choice_5_1_8 + Choice_5_1_9 + Choice_5_2_7
 + Choice_5_2_8 + Choice_5_2_9 + Choice_5_3_7 + Choice_5_3_8 + Choice_5_3_9
 = 1
Box_131616_Unique_6: Choice_6_1_7 + Choice_6_1_8 + Choice_6_1_9 + Choice_6_2_7
 + Choice_6_2_8 + Choice_6_2_9 + Choice_6_3_7 + Choice_6_3_8 + Choice_6_3_9
 = 1
Box_131616_Unique_7: Choice_7_1_7 + Choice_7_1_8 + Choice_7_1_9 + Choice_7_2_7
 + Choice_7_2_8 + Choice_7_2_9 + Choice_7_3_7 + Choice_7_3_8 + Choice_7_3_9
 = 1
Box_131616_Unique_8: Choice_8_1_7 + Choice_8_1_8 + Choice_8_1_9 + Choice_8_2_7
 + Choice_8_2_8 + Choice_8_2_9 + Choice_8_3_7 + Choice_8_3_8 + Choice_8_3_9
 = 1
Box_131616_Unique_9: Choice_9_1_7 + Choice_9_1_8 + Choice_9_1_9 + Choice_9_2_7
 + Choice_9_2_8 + Choice_9_2_9 + Choice_9_3_7 + Choice_9_3_8 + Choice_9_3_9
 = 1
Box_131617_Unique_1: Choice_1_4_7 + Choice_1_4_8 + Choice_1_4_9 + Choice_1_5_7
 + Choice_1_5_8 + Choice_1_5_9 + Choice_1_6_7 + Choice_1_6_8 + Choice_1_6_9
 = 1
Box_131617_Unique_2: Choice_2_4_7 + Choice_2_4_8 + Choice_2_4_9 + Choice_2_5_7
 + Choice_2_5_8 + Choice_2_5_9 + Choice_2_6_7 + Choice_2_6_8 + Choice_2_6_9
 = 1
Box_131617_Unique_3: Choice_3_4_7 + Choice_3_4_8 + Choice_3_4_9 + Choice_3_5_7
 + Choice_3_5_8 + Choice_3_5_9 + Choice_3_6_7 + Choice_3_6_8 + Choice_3_6_9
 = 1
Box_131617_Unique_4: Choice_4_4_7 + Choice_4_4_8 + Choice_4_4_9 + Choice_4_5_7
 + Choice_4_5_8 + Choice_4_5_9 + Choice_4_6_7 + Choice_4_6_8 + Choice_4_6_9
 = 1
Box_131617_Unique_5: Choice_5_4_7 + Choice_5_4_8 + Choice_5_4_9 + Choice_5_5_7
 + Choice_5_5_8 + Choice_5_5_9 + Choice_5_6_7 + Choice_5_6_8 + Choice_5_6_9
 = 1
Box_131617_Unique_6: Choice_6_4_7 + Choice_6_4_8 + Choice_6_4_9 + Choice_6_5_7
 + Choice_6_5_8 + Choice_6_5_9 + Choice_6_6_7 + Choice_6_6_8 + Choice_6_6_9
 = 1
Box_131617_Unique_7: Choice_7_4_7 + Choice_7_4_8 + Choice_7_4_9 + Choice_7_5_7
 + Choice_7_5_8 + Choice_7_5_9 + Choice_7_6_7 + Choice_7_6_8 + Choice_7_6_9
 = 1
Box_131617_Unique_8: Choice_8_4_7 + Choice_8_4_8 + Choice_8_4_9 + Choice_8_5_7
 + Choice_8_5_8 + Choice_8_5_9 + Choice_8_6_7 + Choice_8_6_8 + Choice_8_6_9
 = 1
Box_131617_Unique_9: Choice_9_4_7 + Choice_9_4_8 + Choice_9_4_9 + Choice_9_5_7
 + Choice_9_5_8 + Choice_9_5_9 + Choice_9_6_7 + Choice_9_6_8 + Choice_9_6_9
 = 1
Box_131618_Unique_1: Choice_1_7_7 + Choice_1_7_8 + Choice_1_7_9 + Choice_1_8_7
 + Choice_1_8_8 + Choice_1_8_9 + Choice_1_9_7 + Choice_1_9_8 + Choice_1_9_9
 = 1
Box_131618_Unique_2: Choice_2_7_7 + Choice_2_7_8 + Choice_2_7_9 + Choice_2_8_7
 + Choice_2_8_8 + Choice_2_8_9 + Choice_2_9_7 + Choice_2_9_8 + Choice_2_9_9
 = 1
Box_131618_Unique_3: Choice_3_7_7 + Choice_3_7_8 + Choice_3_7_9 + Choice_3_8_7
 + Choice_3_8_8 + Choice_3_8_9 + Choice_3_9_7 + Choice_3_9_8 + Choice_3_9_9
 = 1
Box_131618_Unique_4: Choice_4_7_7 + Choice_4_7_8 + Choice_4_7_9 + Choice_4_8_7
 + Choice_4_8_8 + Choice_4_8_9 + Choice_4_9_7 + Choice_4_9_8 + Choice_4_9_9
 = 1
Box_131618_Unique_5: Choice_5_7_7 + Choice_5_7_8 + Choice_5_7_9 + Choice_5_8_7
 + Choice_5_8_8 + Choice_5_8_9 + Choice_5_9_7 + Choice_5_9_8 + Choice_5_9_9
 = 1
Box_131618_Unique_6: Choice_6_7_7 + Choice_6_7_8 + Choice_6_7_9 + Choice_6_8_7
 + Choice_6_8_8 + Choice_6_8_9 + Choice_6_9_7 + Choice_6_9_8 + Choice_6_9_9
 = 1
Box_131618_Unique_7: Choice_7_7_7 + Choice_7_7_8 + Choice_7_7_9 + Choice_7_8_7
 + Choice_7_8_8 + Choice_7_8_9 + Choice_7_9_7 + Choice_7_9_8 + Choice_7_9_9
 = 1
Box_131618_Unique_8: Choice_8_7_7 + Choice_8_7_8 + Choice_8_7_9 + Choice_8_8_7
 + Choice_8_8_8 + Choice_8_8_9 + Choice_8_9_7 + Choice_8_9_8 + Choice_8_9_9
 = 1
Box_131618_Unique_9: Choice_9_7_7 + Choice_9_7_8 + Choice_9_7_9 + Choice_9_8_7
 + Choice_9_8_8 + Choice_9_8_9 + Choice_9_9_7 + Choice_9_9_8 + Choice_9_9_9
 = 1
Column_131590_Unique_1: Choice_1_1_1 + Choice_1_2_1 + Choice_1_3_1
 + Choice_1_4_1 + Choice_1_5_1 + Choice_1_6_1 + Choice_1_7_1 + Choice_1_8_1
 + Choice_1_9_1 = 1
Column_131590_Unique_2: Choice_2_1_1 + Choice_2_2_1 + Choice_2_3_1
 + Choice_2_4_1 + Choice_2_5_1 + Choice_2_6_1 + Choice_2_7_1 + Choice_2_8_1
 + Choice_2_9_1 = 1
Column_131590_Unique_3: Choice_3_1_1 + Choice_3_2_1 + Choice_3_3_1
 + Choice_3_4_1 + Choice_3_5_1 + Choice_3_6_1 + Choice_3_7_1 + Choice_3_8_1
 + Choice_3_9_1 = 1
Column_131590_Unique_4: Choice_4_1_1 + Choice_4_2_1 + Choice_4_3_1
 + Choice_4_4_1 + Choice_4_5_1 + Choice_4_6_1 + Choice_4_7_1 + Choice_4_8_1
 + Choice_4_9_1 = 1
Column_131590_Unique_5: Choice_5_1_1 + Choice_5_2_1 + Choice_5_3_1
 + Choice_5_4_1 + Choice_5_5_1 + Choice_5_6_1 + Choice_5_7_1 + Choice_5_8_1
 + Choice_5_9_1 = 1
Column_131590_Unique_6: Choice_6_1_1 + Choice_6_2_1 + Choice_6_3_1
 + Choice_6_4_1 + Choice_6_5_1 + Choice_6_6_1 + Choice_6_7_1 + Choice_6_8_1
 + Choice_6_9_1 = 1
Column_131590_Unique_7: Choice_7_1_1 + Choice_7_2_1 + Choice_7_3_1
 + Choice_7_4_1 + Choice_7_5_1 + Choice_7_6_1 + Choice_7_7_1 + Choice_7_8_1
 + Choice_7_9_1 = 1
Column_131590_Unique_8: Choice_8_1_1 + Choice_8_2_1 + Choice_8_3_1
 + Choice_8_4_1 + Choice_8_5_1 + Choice_8_6_1 + Choice_8_7_1 + Choice_8_8_1
 + Choice_8_9_1 = 1
Column_131590_Unique_9: Choice_9_1_1 + Choice_9_2_1 + Choice_9_3_1
 + Choice_9_4_1 + Choice_9_5_1 + Choice_9_6_1 + Choice_9_7_1 + Choice_9_8_1
 + Choice_9_9_1 = 1
Column_131591_Unique_1: Choice_1_1_2 + Choice_1_2_2 + Choice_1_3_2
 + Choice_1_4_2 + Choice_1_5_2 + Choice_1_6_2 + Choice_1_7_2 + Choice_1_8_2
 + Choice_1_9_2 = 1
Column_131591_Unique_2: Choice_2_1_2 + Choice_2_2_2 + Choice_2_3_2
 + Choice_2_4_2 + Choice_2_5_2 + Choice_2_6_2 + Choice_2_7_2 + Choice_2_8_2
 + Choice_2_9_2 = 1
Column_131591_Unique_3: Choice_3_1_2 + Choice_3_2_2 + Choice_3_3_2
 + Choice_3_4_2 + Choice_3_5_2 + Choice_3_6_2 + Choice_3_7_2 + Choice_3_8_2
 + Choice_3_9_2 = 1
Column_131591_Unique_4: Choice_4_1_2 + Choice_4_2_2 + Choice_4_3_2
 + Choice_4_4_2 + Choice_4_5_2 + Choice_4_6_2 + Choice_4_7_2 + Choice_4_8_2
 + Choice_4_9_2 = 1
Column_131591_Unique_5: Choice_5_1_2 + Choice_5_2_2 + Choice_5_3_2
 + Choice_5_4_2 + Choice_5_5_2 + Choice_5_6_2 + Choice_5_7_2 + Choice_5_8_2
 + Choice_5_9_2 = 1
Column_131591_Unique_6: Choice_6_1_2 + Choice_6_2_2 + Choice_6_3_2
 + Choice_6_4_2 + Choice_6_5_2 + Choice_6_6_2 + Choice_6_7_2 + Choice_6_8_2
 + Choice_6_9_2 = 1
Column_131591_Unique_7: Choice_7_1_2 + Choice_7_2_2 + Choice_7_3_2
 + Choice_7_4_2 + Choice_7_5_2 + Choice_7_6_2 + Choice_7_7_2 + Choice_7_8_2
 + Choice_7_9_2 = 1
Column_131591_Unique_8: Choice_8_1_2 + Choice_8_2_2 + Choice_8_3_2
 + Choice_8_4_2 + Choice_8_5_2 + Choice_8_6_2 + Choice_8_7_2 + Choice_8_8_2
 + Choice_8_9_2 = 1
Column_131591_Unique_9: Choice_9_1_2 + Choice_9_2_2 + Choice_9_3_2
 + Choice_9_4_2 + Choice_9_5_2 + Choice_9_6_2 + Choice_9_7_2 + Choice_9_8_2
 + Choice_9_9_2 = 1
Column_131592_Unique_1: Choice_1_1_3 + Choice_1_2_3 + Choice_1_3_3
 + Choice_1_4_3 + Choice_1_5_3 + Choice_1_6_3 + Choice_1_7_3 + Choice_1_8_3
 + Choice_1_9_3 = 1
Column_131592_Unique_2: Choice_2_1_3 + Choice_2_2_3 + Choice_2_3_3
 + Choice_2_4_3 + Choice_2_5_3 + Choice_2_6_3 + Choice_2_7_3 + Choice_2_8_3
 + Choice_2_9_3 = 1
Column_131592_Unique_3: Choice_3_1_3 + Choice_3_2_3 + Choice_3_3_3
 + Choice_3_4_3 + Choice_3_5_3 + Choice_3_6_3 + Choice_3_7_3 + Choice_3_8_3
 + Choice_3_9_3 = 1
Column_131592_Unique_4: Choice_4_1_3 + Choice_4_2_3 + Choice_4_3_3
 + Choice_4_4_3 + Choice_4_5_3 + Choice_4_6_3 + Choice_4_7_3 + Choice_4_8_3
 + Choice_4_9_3 = 1
Column_131592_Unique_5: Choice_5_1_3 + Choice_5_2_3 + Choice_5_3_3
 + Choice_5_4_3 + Choice_5_5_3 + Choice_5_6_3 + Choice_5_7_3 + Choice_5_8_3
 + Choice_5_9_3 = 1
Column_131592_Unique_6: Choice_6_1_3 + Choice_6_2_3 + Choice_6_3_3
 + Choice_6_4_3 + Choice_6_5_3 + Choice_6_6_3 + Choice_6_7_3 + Choice_6_8_3
 + Choice_6_9_3 = 1
Column_131592_Unique_7: Choice_7_1_3 + Choice_7_2_3 + Choice_7_3_3
 + Choice_7_4_3 + Choice_7_5_3 + Choice_7_6_3 + Choice_7_7_3 + Choice_7_8_3
 + Choice_7_9_3 = 1
Column_131592_Unique_8: Choice_8_1_3 + Choice_8_2_3 + Choice_8_3_3
 + Choice_8_4_3 + Choice_8_5_3 + Choice_8_6_3 + Choice_8_7_3 + Choice_8_8_3
 + Choice_8_9_3 = 1
Column_131592_Unique_9: Choice_9_1_3 + Choice_9_2_3 + Choice_9_3_3
 + Choice_9_4_3 + Choice_9_5_3 + Choice_9_6_3 + Choice_9_7_3 + Choice_9_8_3
 + Choice_9_9_3 = 1
Column_131593_Unique_1: Choice_1_1_4 + Choice_1_2_4 + Choice_1_3_4
 + Choice_1_4_4 + Choice_1_5_4 + Choice_1_6_4 + Choice_1_7_4 + Choice_1_8_4
 + Choice_1_9_4 = 1
Column_131593_Unique_2: Choice_2_1_4 + Choice_2_2_4 + Choice_2_3_4
 + Choice_2_4_4 + Choice_2_5_4 + Choice_2_6_4 + Choice_2_7_4 + Choice_2_8_4
 + Choice_2_9_4 = 1
Column_131593_Unique_3: Choice_3_1_4 + Choice_3_2_4 + Choice_3_3_4
 + Choice_3_4_4 + Choice_3_5_4 + Choice_3_6_4 + Choice_3_7_4 + Choice_3_8_4
 + Choice_3_9_4 = 1
Column_131593_Unique_4: Choice_4_1_4 + Choice_4_2_4 + Choice_4_3_4
 + Choice_4_4_4 + Choice_4_5_4 + Choice_4_6_4 + Choice_4_7_4 + Choice_4_8_4
 + Choice_4_9_4 = 1
Column_131593_Unique_5: Choice_5_1_4 + Choice_5_2_4 + Choice_5_3_4
 + Choice_5_4_4 + Choice_5_5_4 + Choice_5_6_4 + Choice_5_7_4 + Choice_5_8_4
 + Choice_5_9_4 = 1
Column_131593_Unique_6: Choice_6_1_4 + Choice_6_2_4 + Choice_6_3_4
 + Choice_6_4_4 + Choice_6_5_4 + Choice_6_6_4 + Choice_6_7_4 + Choice_6_8_4
 + Choice_6_9_4 = 1
Column_131593_Unique_7: Choice_7_1_4 + Choice_7_2_4 + Choice_7_3_4
 + Choice_7_4_4 + Choice_7_5_4 + Choice_7_6_4 + Choice_7_7_4 + Choice_7_8_4
 + Choice_7_9_4 = 1
Column_131593_Unique_8: Choice_8_1_4 + Choice_8_2_4 + Choice_8_3_4
 + Choice_8_4_4 + Choice_8_5_4 + Choice_8_6_4 + Choice_8_7_4 + Choice_8_8_4
 + Choice_8_9_4 = 1
Column_131593_Unique_9: Choice_9_1_4 + Choice_9_2_4 + Choice_9_3_4
 + Choice_9_4_4 + Choice_9_5_4 + Choice_9_6_4 + Choice_9_7_4 + Choice_9_8_4
 + Choice_9_9_4 = 1
Column_131594_Unique_1: Choice_1_1_5 + Choice_1_2_5 + Choice_1_3_5
 + Choice_1_4_5 + Choice_1_5_5 + Choice_1_6_5 + Choice_1_7_5 + Choice_1_8_5
 + Choice_1_9_5 = 1
Column_131594_Unique_2: Choice_2_1_5 + Choice_2_2_5 + Choice_2_3_5
 + Choice_2_4_5 + Choice_2_5_5 + Choice_2_6_5 + Choice_2_7_5 + Choice_2_8_5
 + Choice_2_9_5 = 1
Column_131594_Unique_3: Choice_3_1_5 + Choice_3_2_5 + Choice_3_3_5
 + Choice_3_4_5 + Choice_3_5_5 + Choice_3_6_5 + Choice_3_7_5 + Choice_3_8_5
 + Choice_3_9_5 = 1
Column_131594_Unique_4: Choice_4_1_5 + Choice_4_2_5 + Choice_4_3_5
 + Choice_4_4_5 + Choice_4_5_5 + Choice_4_6_5 + Choice_4_7_5 + Choice_4_8_5
 + Choice_4_9_5 = 1
Column_131594_Unique_5: Choice_5_1_5 + Choice_5_2_5 + Choice_5_3_5
 + Choice_5_4_5 + Choice_5_5_5 + Choice_5_6_5 + Choice_5_7_5 + Choice_5_8_5
 + Choice_5_9_5 = 1
Column_131594_Unique_6: Choice_6_1_5 + Choice_6_2_5 + Choice_6_3_5
 + Choice_6_4_5 + Choice_6_5_5 + Choice_6_6_5 + Choice_6_7_5 + Choice_6_8_5
 + Choice_6_9_5 = 1
Column_131594_Unique_7: Choice_7_1_5 + Choice_7_2_5 + Choice_7_3_5
 + Choice_7_4_5 + Choice_7_5_5 + Choice_7_6_5 + Choice_7_7_5 + Choice_7_8_5
 + Choice_7_9_5 = 1
Column_131594_Unique_8: Choice_8_1_5 + Choice_8_2_5 + Choice_8_3_5
 + Choice_8_4_5 + Choice_8_5_5 + Choice_8_6_5 + Choice_8_7_5 + Choice_8_8_5
 + Choice_8_9_5 = 1
Column_131594_Unique_9: Choice_9_1_5 + Choice_9_2_5 + Choice_9_3_5
 + Choice_9_4_5 + Choice_9_5_5 + Choice_9_6_5 + Choice_9_7_5 + Choice_9_8_5
 + Choice_9_9_5 = 1
Column_131595_Unique_1: Choice_1_1_6 + Choice_1_2_6 + Choice_1_3_6
 + Choice_1_4_6 + Choice_1_5_6 + Choice_1_6_6 + Choice_1_7_6 + Choice_1_8_6
 + Choice_1_9_6 = 1
Column_131595_Unique_2: Choice_2_1_6 + Choice_2_2_6 + Choice_2_3_6
 + Choice_2_4_6 + Choice_2_5_6 + Choice_2_6_6 + Choice_2_7_6 + Choice_2_8_6
 + Choice_2_9_6 = 1
Column_131595_Unique_3: Choice_3_1_6 + Choice_3_2_6 + Choice_3_3_6
 + Choice_3_4_6 + Choice_3_5_6 + Choice_3_6_6 + Choice_3_7_6 + Choice_3_8_6
 + Choice_3_9_6 = 1
Column_131595_Unique_4: Choice_4_1_6 + Choice_4_2_6 + Choice_4_3_6
 + Choice_4_4_6 + Choice_4_5_6 + Choice_4_6_6 + Choice_4_7_6 + Choice_4_8_6
 + Choice_4_9_6 = 1
Column_131595_Unique_5: Choice_5_1_6 + Choice_5_2_6 + Choice_5_3_6
 + Choice_5_4_6 + Choice_5_5_6 + Choice_5_6_6 + Choice_5_7_6 + Choice_5_8_6
 + Choice_5_9_6 = 1
Column_131595_Unique_6: Choice_6_1_6 + Choice_6_2_6 + Choice_6_3_6
 + Choice_6_4_6 + Choice_6_5_6 + Choice_6_6_6 + Choice_6_7_6 + Choice_6_8_6
 + Choice_6_9_6 = 1
Column_131595_Unique_7: Choice_7_1_6 + Choice_7_2_6 + Choice_7_3_6
 + Choice_7_4_6 + Choice_7_5_6 + Choice_7_6_6 + Choice_7_7_6 + Choice_7_8_6
 + Choice_7_9_6 = 1
Column_131595_Unique_8: Choice_8_1_6 + Choice_8_2_6 + Choice_8_3_6
 + Choice_8_4_6 + Choice_8_5_6 + Choice_8_6_6 + Choice_8_7_6 + Choice_8_8_6
 + Choice_8_9_6 = 1
Column_131595_Unique_9: Choice_9_1_6 + Choice_9_2_6 + Choice_9_3_6
 + Choice_9_4_6 + Choice_9_5_6 + Choice_9_6_6 + Choice_9_7_6 + Choice_9_8_6
 + Choice_9_9_6 = 1
Column_131596_Unique_1: Choice_1_1_7 + Choice_1_2_7 + Choice_1_3_7
 + Choice_1_4_7 + Choice_1_5_7 + Choice_1_6_7 + Choice_1_7_7 + Choice_1_8_7
 + Choice_1_9_7 = 1
Column_131596_Unique_2: Choice_2_1_7 + Choice_2_2_7 + Choice_2_3_7
 + Choice_2_4_7 + Choice_2_5_7 + Choice_2_6_7 + Choice_2_7_7 + Choice_2_8_7
 + Choice_2_9_7 = 1
Column_131596_Unique_3: Choice_3_1_7 + Choice_3_2_7 + Choice_3_3_7
 + Choice_3_4_7 + Choice_3_5_7 + Choice_3_6_7 + Choice_3_7_7 + Choice_3_8_7
 + Choice_3_9_7 = 1
Column_131596_Unique_4: Choice_4_1_7 + Choice_4_2_7 + Choice_4_3_7
 + Choice_4_4_7 + Choice_4_5_7 + Choice_4_6_7 + Choice_4_7_7 + Choice_4_8_7
 + Choice_4_9_7 = 1
Column_131596_Unique_5: Choice_5_1_7 + Choice_5_2_7 + Choice_5_3_7
 + Choice_5_4_7 + Choice_5_5_7 + Choice_5_6_7 + Choice_5_7_7 + Choice_5_8_7
 + Choice_5_9_7 = 1
Column_131596_Unique_6: Choice_6_1_7 + Choice_6_2_7 + Choice_6_3_7
 + Choice_6_4_7 + Choice_6_5_7 + Choice_6_6_7 + Choice_6_7_7 + Choice_6_8_7
 + Choice_6_9_7 = 1
Column_131596_Unique_7: Choice_7_1_7 + Choice_7_2_7 + Choice_7_3_7
 + Choice_7_4_7 + Choice_7_5_7 + Choice_7_6_7 + Choice_7_7_7 + Choice_7_8_7
 + Choice_7_9_7 = 1
Column_131596_Unique_8: Choice_8_1_7 + Choice_8_2_7 + Choice_8_3_7
 + Choice_8_4_7 + Choice_8_5_7 + Choice_8_6_7 + Choice_8_7_7 + Choice_8_8_7
 + Choice_8_9_7 = 1
Column_131596_Unique_9: Choice_9_1_7 + Choice_9_2_7 + Choice_9_3_7
 + Choice_9_4_7 + Choice_9_5_7 + Choice_9_6_7 + Choice_9_7_7 + Choice_9_8_7
 + Choice_9_9_7 = 1
Column_131597_Unique_1: Choice_1_1_8 + Choice_1_2_8 + Choice_1_3_8
 + Choice_1_4_8 + Choice_1_5_8 + Choice_1_6_8 + Choice_1_7_8 + Choice_1_8_8
 + Choice_1_9_8 = 1
Column_131597_Unique_2: Choice_2_1_8 + Choice_2_2_8 + Choice_2_3_8
 + Choice_2_4_8 + Choice_2_5_8 + Choice_2_6_8 + Choice_2_7_8 + Choice_2_8_8
 + Choice_2_9_8 = 1
Column_131597_Unique_3: Choice_3_1_8 + Choice_3_2_8 + Choice_3_3_8
 + Choice_3_4_8 + Choice_3_5_8 + Choice_3_6_8 + Choice_3_7_8 + Choice_3_8_8
 + Choice_3_9_8 = 1
Column_131597_Unique_4: Choice_4_1_8 + Choice_4_2_8 + Choice_4_3_8
 + Choice_4_4_8 + Choice_4_5_8 + Choice_4_6_8 + Choice_4_7_8 + Choice_4_8_8
 + Choice_4_9_8 = 1
Column_131597_Unique_5: Choice_5_1_8 + Choice_5_2_8 + Choice_5_3_8
 + Choice_5_4_8 + Choice_5_5_8 + Choice_5_6_8 + Choice_5_7_8 + Choice_5_8_8
 + Choice_5_9_8 = 1
Column_131597_Unique_6: Choice_6_1_8 + Choice_6_2_8 + Choice_6_3_8
 + Choice_6_4_8 + Choice_6_5_8 + Choice_6_6_8 + Choice_6_7_8 + Choice_6_8_8
 + Choice_6_9_8 = 1
Column_131597_Unique_7: Choice_7_1_8 + Choice_7_2_8 + Choice_7_3_8
 + Choice_7_4_8 + Choice_7_5_8 + Choice_7_6_8 + Choice_7_7_8 + Choice_7_8_8
 + Choice_7_9_8 = 1
Column_131597_Unique_8: Choice_8_1_8 + Choice_8_2_8 + Choice_8_3_8
 + Choice_8_4_8 + Choice_8_5_8 + Choice_8_6_8 + Choice_8_7_8 + Choice_8_8_8
 + Choice_8_9_8 = 1
Column_131597_Unique_9: Choice_9_1_8 + Choice_9_2_8 + Choice_9_3_8
 + Choice_9_4_8 + Choice_9_5_8 + Choice_9_6_8 + Choice_9_7_8 + Choice_9_8_8
 + Choice_9_9_8 = 1
Column_131598_Unique_1: Choice_1_1_9 + Choice_1_2_9 + Choice_1_3_9
 + Choice_1_4_9 + Choice_1_5_9 + Choice_1_6_9 + Choice_1_7_9 + Choice_1_8_9
 + Choice_1_9_9 = 1
Column_131598_Unique_2: Choice_2_1_9 + Choice_2_2_9 + Choice_2_3_9
 + Choice_2_4_9 + Choice_2_5_9 + Choice_2_6_9 + Choice_2_7_9 + Choice_2_8_9
 + Choice_2_9_9 = 1
Column_131598_Unique_3: Choice_3_1_9 + Choice_3_2_9 + Choice_3_3_9
 + Choice_3_4_9 + Choice_3_5_9 + Choice_3_6_9 + Choice_3_7_9 + Choice_3_8_9
 + Choice_3_9_9 = 1
Column_131598_Unique_4: Choice_4_1_9 + Choice_4_2_9 + Choice_4_3_9
 + Choice_4_4_9 + Choice_4_5_9 + Choice_4_6_9 + Choice_4_7_9 + Choice_4_8_9
 + Choice_4_9_9 = 1
Column_131598_Unique_5: Choice_5_1_9 + Choice_5_2_9 + Choice_5_3_9
 + Choice_5_4_9 + Choice_5_5_9 + Choice_5_6_9 + Choice_5_7_9 + Choice_5_8_9
 + Choice_5_9_9 = 1
Column_131598_Unique_6: Choice_6_1_9 + Choice_6_2_9 + Choice_6_3_9
 + Choice_6_4_9 + Choice_6_5_9 + Choice_6_6_9 + Choice_6_7_9 + Choice_6_8_9
 + Choice_6_9_9 = 1
Column_131598_Unique_7: Choice_7_1_9 + Choice_7_2_9 + Choice_7_3_9
 + Choice_7_4_9 + Choice_7_5_9 + Choice_7_6_9 + Choice_7_7_9 + Choice_7_8_9
 + Choice_7_9_9 = 1
Column_131598_Unique_8: Choice_8_1_9 + Choice_8_2_9 + Choice_8_3_9
 + Choice_8_4_9 + Choice_8_5_9 + Choice_8_6_9 + Choice_8_7_9 + Choice_8_8_9
 + Choice_8_9_9 = 1
Column_131598_Unique_9: Choice_9_1_9 + Choice_9_2_9 + Choice_9_3_9
 + Choice_9_4_9 + Choice_9_5_9 + Choice_9_6_9 + Choice_9_7_9 + Choice_9_8_9
 + Choice_9_9_9 = 1
DifferentPair_1_1_1_2_3: Choice_1_1_1 + Choice_1_2_3 <= 1
DifferentPair_1_1_1_3_2: Choice_1_1_1 + Choice_1_3_2 <= 1
DifferentPair_1_1_2_2_4: Choice_1_1_2 + Choice_1_2_4 <= 1
DifferentPair_1_1_2_3_1: Choice_1_1_2 + Choice_1_3_1 <= 1
DifferentPair_1_1_2_3_3: Choice_1_1_2 + Choice_1_3_3 <= 1
DifferentPair_1_1_3_2_1: Choice_1_1_3 + Choice_1_2_1 <= 1
DifferentPair_1_1_3_2_5: Choice_1_1_3 + Choice_1_2_5 <= 1
DifferentPair_1_1_3_3_2: Choice_1_1_3 + Choice_1_3_2 <= 1
DifferentPair_1_1_3_3_4: Choice_1_1_3 + Choice_1_3_4 <= 1
DifferentPair_1_1_4_2_2: Choice_1_1_4 + Choice_1_2_2 <= 1
DifferentPair_1_1_4_2_6: Choice_1_1_4 + Choice_1_2_6 <= 1
DifferentPair_1_1_4_3_3: Choice_1_1_4 + Choice_1_3_3 <= 1
DifferentPair_1_1_4_3_5: Choice_1_1_4 + Choice_1_3_5 <= 1
DifferentPair_1_1_5_2_3: Choice_1_1_5 + Choice_1_2_3 <= 1
DifferentPair_1_1_5_2_7: Choice_1_1_5 + Choice_1_2_7 <= 1
DifferentPair_1_1_5_3_4: Choice_1_1_5 + Choice_1_3_4 <= 1
DifferentPair_1_1_5_3_6: Choice_1_1_5 + Choice_1_3_6 <= 1
DifferentPair_1_1_6_2_4: Choice_1_1_6 + Choice_1_2_4 <= 1
DifferentPair_1_1_6_2_8: Choice_1_1_6 + Choice_1_2_8 <= 1
DifferentPair_1_1_6_3_5: Choice_1_1_6 + Choice_1_3_5 <= 1
DifferentPair_1_1_6_3_7: Choice_1_1_6 + Choice_1_3_7 <= 1
DifferentPair_1_1_7_2_5: Choice_1_1_7 + Choice_1_2_5 <= 1
DifferentPair_1_1_7_2_9: Choice_1_1_7 + Choice_1_2_9 <= 1
DifferentPair_1_1_7_3_6: Choice_1_1_7 + Choice_1_3_6 <= 1
DifferentPair_1_1_7_3_8: Choice_1_1_7 + Choice_1_3_8 <= 1
DifferentPair_1_1_8_2_6: Choice_1_1_8 + Choice_1_2_6 <= 1
DifferentPair_1_1_8_3_7: Choice_1_1_8 + Choice_1_3_7 <= 1
DifferentPair_1_1_8_3_9: Choice_1_1_8 + Choice_1_3_9 <= 1
DifferentPair_1_1_9_2_7: Choice_1_1_9 + Choice_1_2_7 <= 1
DifferentPair_1_1_9_3_8: Choice_1_1_9 + Choice_1_3_8 <= 1
DifferentPair_1_2_1_1_3: Choice_1_1_3 + Choice_1_2_1 <= 1
DifferentPair_1_2_1_3_3: Choice_1_2_1 + Choice_1_3_3 <= 1
DifferentPair_1_2_1_4_2: Choice_1_2_1 + Choice_1_4_2 <= 1
DifferentPair_1_2_2_1_4: Choice_1_1_4 + Choice_1_2_2 <= 1
DifferentPair_1_2_2_3_4: Choice_1_2_2 + Choice_1_3_4 <= 1
DifferentPair_1_2_2_4_1: Choice_1_2_2 + Choice_1_4_1 <= 1
DifferentPair_1_2_2_4_3: Choice_1_2_2 + Choice_1_4_3 <= 1
DifferentPair_1_2_3_1_1: Choice_1_1_1 + Choice_1_2_3 <= 1
DifferentPair_1_2_3_1_5: Choice_1_1_5 + Choice_1_2_3 <= 1
DifferentPair_1_2_3_3_1: Choice_1_2_3 + Choice_1_3_1 <= 1
DifferentPair_1_2_3_3_5: Choice_1_2_3 + Choice_1_3_5 <= 1
DifferentPair_1_2_3_4_2: Choice_1_2_3 + Choice_1_4_2 <= 1
DifferentPair_1_2_3_4_4: Choice_1_2_3 + Choice_1_4_4 <= 1
DifferentPair_1_2_4_1_2: Choice_1_1_2 + Choice_1_2_4 <= 1
DifferentPair_1_2_4_1_6: Choice_1_1_6 + Choice_1_2_4 <= 1
DifferentPair_1_2_4_3_2: Choice_1_2_4 + Choice_1_3_2 <= 1
DifferentPair_1_2_4_3_6: Choice_1_2_4 + Choice_1_3_6 <= 1
DifferentPair_1_2_4_4_3: Choice_1_2_4 + Choice_1_4_3 <= 1
DifferentPair_1_2_4_4_5: Choice_1_2_4 + Choice_1_4_5 <= 1
DifferentPair_1_2_5_1_3: Choice_1_1_3 + Choice_1_2_5 <= 1
DifferentPair_1_2_5_1_7: Choice_1_1_7 + Choice_1_2_5 <= 1
DifferentPair_1_2_5_3_3: Choice_1_2_5 + Choice_1_3_3 <= 1
DifferentPair_1_2_5_3_7: Choice_1_2_5 + Choice_1_3_7 <= 1
DifferentPair_1_2_5_4_4: Choice_1_2_5 + Choice_1_4_4 <= 1
DifferentPair_1_2_5_4_6: Choice_1_2_5 + Choice_1_4_6 <= 1
DifferentPair_1_2_6_1_4: Choice_1_1_4 + Choice_1_2_6 <= 1
DifferentPair_1_2_6_1_8: Choice_1_1_8 + Choice_1_2_6 <= 1
DifferentPair_1_2_6_3_4: Choice_1_2_6 + Choice_1_3_4 <= 1
DifferentPair_1_2_6_3_8: Choice_1_2_6 + Choice_1_3_8 <= 1
DifferentPair_1_2_6_4_5: Choice_1_2_6 + Choice_1_4_5 <= 1
DifferentPair_1_2_6_4_7: Choice_1_2_6 + Choice_1_4_7 <= 1
DifferentPair_1_2_7_1_5: Choice_1_1_5 + Choice_1_2_7 <= 1
DifferentPair_1_2_7_1_9: Choice_1_1_9 + Choice_1_2_7 <= 1
DifferentPair_1_2_7_3_5: Choice_1_2_7 + Choice_1_3_5 <= 1
DifferentPair_1_2_7_3_9: Choice_1_2_7 + Choice_1_3_9 <= 1
DifferentPair_1_2_7_4_6: Choice_1_2_7 + Choice_1_4_6 <= 1
DifferentPair_1_2_7_4_8: Choice_1_2_7 + Choice_1_4_8 <= 1
DifferentPair_1_2_8_1_6: Choice_1_1_6 + Choice_1_2_8 <= 1
DifferentPair_1_2_8_3_6: Choice_1_2_8 + Choice_1_3_6 <= 1
DifferentPair_1_2_8_4_7: Choice_1_2_8 + Choice_1_4_7 <= 1
DifferentPair_1_2_8_4_9: Choice_1_2_8 + Choice_1_4_9 <= 1
DifferentPair_1_2_9_1_7: Choice_1_1_7 + Choice_1_2_9 <= 1
DifferentPair_1_2_9_3_7: Choice_1_2_9 + Choice_1_3_7 <= 1
DifferentPair_1_2_9_4_8: Choice_1_2_9 + Choice_1_4_8 <= 1
DifferentPair_1_3_1_1_2: Choice_1_1_2 + Choice_1_3_1 <= 1
DifferentPair_1_3_1_2_3: Choice_1_2_3 + Choice_1_3_1 <= 1
DifferentPair_1_3_1_4_3: Choice_1_3_1 + Choice_1_4_3 <= 1
DifferentPair_1_3_1_5_2: Choice_1_3_1 + Choice_1_5_2 <= 1
DifferentPair_1_3_2_1_1: Choice_1_1_1 + Choice_1_3_2 <= 1
DifferentPair_1_3_2_1_3: Choice_1_1_3 + Choice_1_3_2 <= 1
DifferentPair_1_3_2_2_4: Choice_1_2_4 + Choice_1_3_2 <= 1
DifferentPair_1_3_2_4_4: Choice_1_3_2 + Choice_1_4_4 <= 1
DifferentPair_1_3_2_5_1: Choice_1_3_2 + Choice_1_5_1 <= 1
DifferentPair_1_3_2_5_3: Choice_1_3_2 + Choice_1_5_3 <= 1
DifferentPair_1_3_3_1_2: Choice_1_1_2 + Choice_1_3_3 <= 1
DifferentPair_1_3_3_1_4: Choice_1_1_4 + Choice_1_3_3 <= 1
DifferentPair_1_3_3_2_1: Choice_1_2_1 + Choice_1_3_3 <= 1
DifferentPair_1_3_3_2_5: Choice_1_2_5 + Choice_1_3_3 <= 1
DifferentPair_1_3_3_4_1: Choice_1_3_3 + Choice_1_4_1 <= 1
DifferentPair_1_3_3_4_5: Choice_1_3_3 + Choice_1_4_5 <= 1
DifferentPair_1_3_3_5_2: Choice_1_3_3 + Choice_1_5_2 <= 1
DifferentPair_1_3_3_5_4: Choice_1_3_3 + Choice_1_5_4 <= 1
DifferentPair_1_3_4_1_3: Choice_1_1_3 + Choice_1_3_4 <= 1
DifferentPair_1_3_4_1_5: Choice_1_1_5 + Choice_1_3_4 <= 1
DifferentPair_1_3_4_2_2: Choice_1_2_2 + Choice_1_3_4 <= 1
DifferentPair_1_3_4_2_6: Choice_1_2_6 + Choice_1_3_4 <= 1
DifferentPair_1_3_4_4_2: Choice_1_3_4 + Choice_1_4_2 <= 1
DifferentPair_1_3_4_4_6: Choice_1_3_4 + Choice_1_4_6 <= 1
DifferentPair_1_3_4_5_3: Choice_1_3_4 + Choice_1_5_3 <= 1
DifferentPair_1_3_4_5_5: Choice_1_3_4 + Choice_1_5_5 <= 1
DifferentPair_1_3_5_1_4: Choice_1_1_4 + Choice_1_3_5 <= 1
DifferentPair_1_3_5_1_6: Choice_1_1_6 + Choice_1_3_5 <= 1
DifferentPair_1_3_5_2_3: Choice_1_2_3 + Choice_1_3_5 <= 1
DifferentPair_1_3_5_2_7: Choice_1_2_7 + Choice_1_3_5 <= 1
DifferentPair_1_3_5_4_3: Choice_1_3_5 + Choice_1_4_3 <= 1
DifferentPair_1_3_5_4_7: Choice_1_3_5 + Choice_1_4_7 <= 1
DifferentPair_1_3_5_5_4: Choice_1_3_5 + Choice_1_5_4 <= 1
DifferentPair_1_3_5_5_6: Choice_1_3_5 + Choice_1_5_6 <= 1
DifferentPair_1_3_6_1_5: Choice_1_1_5 + Choice_1_3_6 <= 1
DifferentPair_1_3_6_1_7: Choice_1_1_7 + Choice_1_3_6 <= 1
DifferentPair_1_3_6_2_4: Choice_1_2_4 + Choice_1_3_6 <= 1
DifferentPair_1_3_6_2_8: Choice_1_2_8 + Choice_1_3_6 <= 1
DifferentPair_1_3_6_4_4: Choice_1_3_6 + Choice_1_4_4 <= 1
DifferentPair_1_3_6_4_8: Choice_1_3_6 + Choice_1_4_8 <= 1
DifferentPair_1_3_6_5_5: Choice_1_3_6 + Choice_1_5_5 <= 1
DifferentPair_1_3_6_5_7: Choice_1_3_6 + Choice_1_5_7 <= 1
DifferentPair_1_3_7_1_6: Choice_1_1_6 + Choice_1_3_7 <= 1
DifferentPair_1_3_7_1_8: Choice_1_1_8 + Choice_1_3_7 <= 1
DifferentPair_1_3_7_2_5: Choice_1_2_5 + Choice_1_3_7 <= 1
DifferentPair_1_3_7_2_9: Choice_1_2_9 + Choice_1_3_7 <= 1
DifferentPair_1_3_7_4_5: Choice_1_3_7 + Choice_1_4_5 <= 1
DifferentPair_1_3_7_4_9: Choice_1_3_7 + Choice_1_4_9 <= 1
DifferentPair_1_3_7_5_6: Choice_1_3_7 + Choice_1_5_6 <= 1
DifferentPair_1_3_7_5_8: Choice_1_3_7 + Choice_1_5_8 <= 1
DifferentPair_1_3_8_1_7: Choice_1_1_7 + Choice_1_3_8 <= 1
DifferentPair_1_3_8_1_9: Choice_1_1_9 + Choice_1_3_8 <= 1
DifferentPair_1_3_8_2_6: Choice_1_2_6 + Choice_1_3_8 <= 1
DifferentPair_1_3_8_4_6: Choice_1_3_8 + Choice_1_4_6 <= 1
DifferentPair_1_3_8_5_7: Choice_1_3_8 + Choice_1_5_7 <= 1
DifferentPair_1_3_8_5_9: Choice_1_3_8 + Choice_1_5_9 <= 1
DifferentPair_1_3_9_1_8: Choice_1_1_8 + Choice_1_3_9 <= 1
DifferentPair_1_3_9_2_7: Choice_1_2_7 + Choice_1_3_9 <= 1
DifferentPair_1_3_9_4_7: Choice_1_3_9 + Choice_1_4_7 <= 1
DifferentPair_1_3_9_5_8: Choice_1_3_9 + Choice_1_5_8 <= 1
DifferentPair_1_4_1_2_2: Choice_1_2_2 + Choice_1_4_1 <= 1
DifferentPair_1_4_1_3_3: Choice_1_3_3 + Choice_1_4_1 <= 1
DifferentPair_1_4_1_5_3: Choice_1_4_1 + Choice_1_5_3 <= 1
DifferentPair_1_4_1_6_2: Choice_1_4_1 + Choice_1_6_2 <= 1
DifferentPair_1_4_2_2_1: Choice_1_2_1 + Choice_1_4_2 <= 1
DifferentPair_1_4_2_2_3: Choice_1_2_3 + Choice_1_4_2 <= 1
DifferentPair_1_4_2_3_4: Choice_1_3_4 + Choice_1_4_2 <= 1
DifferentPair_1_4_2_5_4: Choice_1_4_2 + Choice_1_5_4 <= 1
DifferentPair_1_4_2_6_1: Choice_1_4_2 + Choice_1_6_1 <= 1
DifferentPair_1_4_2_6_3: Choice_1_4_2 + Choice_1_6_3 <= 1
DifferentPair_1_4_3_2_2: Choice_1_2_2 + Choice_1_4_3 <= 1
DifferentPair_1_4_3_2_4: Choice_1_2_4 + Choice_1_4_3 <= 1
DifferentPair_1_4_3_3_1: Choice_1_3_1 + Choice_1_4_3 <= 1
DifferentPair_1_4_3_3_5: Choice_1_3_5 + Choice_1_4_3 <= 1
DifferentPair_1_4_3_5_1: Choice_1_4_3 + Choice_1_5_1 <= 1
DifferentPair_1_4_3_5_5: Choice_1_4_3 + Choice_1_5_5 <= 1
DifferentPair_1_4_3_6_2: Choice_1_4_3 + Choice_1_6_2 <= 1
DifferentPair_1_4_3_6_4: Choice_1_4_3 + Choice_1_6_4 <= 1
DifferentPair_1_4_4_2_3: Choice_1_2_3 + Choice_1_4_4 <= 1
DifferentPair_1_4_4_2_5: Choice_1_2_5 + Choice_1_4_4 <= 1
DifferentPair_1_4_4_3_2: Choice_1_3_2 + Choice_1_4_4 <= 1
DifferentPair_1_4_4_3_6: Choice_1_3_6 + Choice_1_4_4 <= 1
DifferentPair_1_4_4_5_2: Choice_1_4_4 + Choice_1_5_2 <= 1
DifferentPair_1_4_4_5_6: Choice_1_4_4 + Choice_1_5_6 <= 1
DifferentPair_1_4_4_6_3: Choice_1_4_4 + Choice_1_6_3 <= 1
DifferentPair_1_4_4_6_5: Choice_1_4_4 + Choice_1_6_5 <= 1
DifferentPair_1_4_5_2_4: Choice_1_2_4 + Choice_1_4_5 <= 1
DifferentPair_1_4_5_2_6: Choice_1_2_6 + Choice_1_4_5 <= 1
DifferentPair_1_4_5_3_3: Choice_1_3_3 + Choice_1_4_5 <= 1
DifferentPair_1_4_5_3_7: Choice_1_3_7 + Choice_1_4_5 <= 1
DifferentPair_1_4_5_5_3: Choice_1_4_5 + Choice_1_5_3 <= 1
DifferentPair_1_4_5_5_7: Choice_1_4_5 + Choice_1_5_7 <= 1
DifferentPair_1_4_5_6_4: Choice_1_4_5 + Choice_1_6_4 <= 1
DifferentPair_1_4_5_6_6: Choice_1_4_5 + Choice_1_6_6 <= 1
DifferentPair_1_4_6_2_5: Choice_1_2_5 + Choice_1_4_6 <= 1
DifferentPair_1_4_6_2_7: Choice_1_2_7 + Choice_1_4_6 <= 1
DifferentPair_1_4_6_3_4: Choice_1_3_4 + Choice_1_4_6 <= 1
DifferentPair_1_4_6_3_8: Choice_1_3_8 + Choice_1_4_6 <= 1
DifferentPair_1_4_6_5_4: Choice_1_4_6 + Choice_1_5_4 <= 1
DifferentPair_1_4_6_5_8: Choice_1_4_6 + Choice_1_5_8 <= 1
DifferentPair_1_4_6_6_5: Choice_1_4_6 + Choice_1_6_5 <= 1
DifferentPair_1_4_6_6_7: Choice_1_4_6 + Choice_1_6_7 <= 1
DifferentPair_1_4_7_2_6: Choice_1_2_6 + Choice_1_4_7 <= 1
DifferentPair_1_4_7_2_8: Choice_1_2_8 + Choice_1_4_7 <= 1
DifferentPair_1_4_7_3_5: Choice_1_3_5 + Choice_1_4_7 <= 1
DifferentPair_1_4_7_3_9: Choice_1_3_9 + Choice_1_4_7 <= 1
DifferentPair_1_4_7_5_5: Choice_1_4_7 + Choice_1_5_5 <= 1
DifferentPair_1_4_7_5_9: Choice_1_4_7 + Choice_1_5_9 <= 1
DifferentPair_1_4_7_6_6: Choice_1_4_7 + Choice_1_6_6 <= 1
DifferentPair_1_4_7_6_8: Choice_1_4_7 + Choice_1_6_8 <= 1
DifferentPair_1_4_8_2_7: Choice_1_2_7 + Choice_1_4_8 <= 1
DifferentPair_1_4_8_2_9: Choice_1_2_9 + Choice_1_4_8 <= 1
DifferentPair_1_4_8_3_6: Choice_1_3_6 + Choice_1_4_8 <= 1
DifferentPair_1_4_8_5_6: Choice_1_4_8 + Choice_1_5_6 <= 1
DifferentPair_1_4_8_6_7: Choice_1_4_8 + Choice_1_6_7 <= 1
DifferentPair_1_4_8_6_9: Choice_1_4_8 + Choice_1_6_9 <= 1
DifferentPair_1_4_9_2_8: Choice_1_2_8 + Choice_1_4_9 <= 1
DifferentPair_1_4_9_3_7: Choice_1_3_7 + Choice_1_4_9 <= 1
DifferentPair_1_4_9_5_7: Choice_1_4_9 + Choice_1_5_7 <= 1
DifferentPair_1_4_9_6_8: Choice_1_4_9 + Choice_1_6_8 <= 1
DifferentPair_1_5_1_3_2: Choice_1_3_2 + Choice_1_5_1 <= 1
DifferentPair_1_5_1_4_3: Choice_1_4_3 + Choice_1_5_1 <= 1
DifferentPair_1_5_1_6_3: Choice_1_5_1 + Choice_1_6_3 <= 1
DifferentPair_1_5_1_7_2: Choice_1_5_1 + Choice_1_7_2 <= 1
DifferentPair_1_5_2_3_1: Choice_1_3_1 + Choice_1_5_2 <= 1
DifferentPair_1_5_2_3_3: Choice_1_3_3 + Choice_1_5_2 <= 1
DifferentPair_1_5_2_4_4: Choice_1_4_4 + Choice_1_5_2 <= 1
DifferentPair_1_5_2_6_4: Choice_1_5_2 + Choice_1_6_4 <= 1
DifferentPair_1_5_2_7_1: Choice_1_5_2 + Choice_1_7_1 <= 1
DifferentPair_1_5_2_7_3: Choice_1_5_2 + Choice_1_7_3 <= 1
DifferentPair_1_5_3_3_2: Choice_1_3_2 + Choice_1_5_3 <= 1
DifferentPair_1_5_3_3_4: Choice_1_3_4 + Choice_1_5_3 <= 1
DifferentPair_1_5_3_4_1: Choice_1_4_1 + Choice_1_5_3 <= 1
DifferentPair_1_5_3_4_5: Choice_1_4_5 + Choice_1_5_3 <= 1
DifferentPair_1_5_3_6_1: Choice_1_5_3 + Choice_1_6_1 <= 1
DifferentPair_1_5_3_6_5: Choice_1_5_3 + Choice_1_6_5 <= 1
DifferentPair_1_5_3_7_2: Choice_1_5_3 + Choice_1_7_2 <= 1
DifferentPair_1_5_3_7_4: Choice_1_5_3 + Choice_1_7_4 <= 1
DifferentPair_1_5_4_3_3: Choice_1_3_3 + Choice_1_5_4 <= 1
DifferentPair_1_5_4_3_5: Choice_1_3_5 + Choice_1_5_4 <= 1
DifferentPair_1_5_4_4_2: Choice_1_4_2 + Choice_1_5_4 <= 1
DifferentPair_1_5_4_4_6: Choice_1_4_6 + Choice_1_5_4 <= 1
DifferentPair_1_5_4_6_2: Choice_1_5_4 + Choice_1_6_2 <= 1
DifferentPair_1_5_4_6_6: Choice_1_5_4 + Choice_1_6_6 <= 1
DifferentPair_1_5_4_7_3: Choice_1_5_4 + Choice_1_7_3 <= 1
DifferentPair_1_5_4_7_5: Choice_1_5_4 + Choice_1_7_5 <= 1
DifferentPair_1_5_5_3_4: Choice_1_3_4 + Choice_1_5_5 <= 1
DifferentPair_1_5_5_3_6: Choice_1_3_6 + Choice_1_5_5 <= 1
DifferentPair_1_5_5_4_3: Choice_1_4_3 + Choice_1_5_5 <= 1
DifferentPair_1_5_5_4_7: Choice_1_4_7 + Choice_1_5_5 <= 1
DifferentPair_1_5_5_6_3: Choice_1_5_5 + Choice_1_6_3 <= 1
DifferentPair_1_5_5_6_7: Choice_1_5_5 + Choice_1_6_7 <= 1
DifferentPair_1_5_5_7_4: Choice_1_5_5 + Choice_1_7_4 <= 1
DifferentPair_1_5_5_7_6: Choice_1_5_5 + Choice_1_7_6 <= 1
DifferentPair_1_5_6_3_5: Choice_1_3_5 + Choice_1_5_6 <= 1
DifferentPair_1_5_6_3_7: Choice_1_3_7 + Choice_1_5_6 <= 1
DifferentPair_1_5_6_4_4: Choice_1_4_4 + Choice_1_5_6 <= 1
DifferentPair_1_5_6_4_8: Choice_1_4_8 + Choice_1_5_6 <= 1
DifferentPair_1_5_6_6_4: Choice_1_5_6 + Choice_1_6_4 <= 1
DifferentPair_1_5_6_6_8: Choice_1_5_6 + Choice_1_6_8 <= 1
DifferentPair_1_5_6_7_5: Choice_1_5_6 + Choice_1_7_5 <= 1
DifferentPair_1_5_6_7_7: Choice_1_5_6 + Choice_1_7_7 <= 1
DifferentPair_1_5_7_3_6: Choice_1_3_6 + Choice_1_5_7 <= 1
DifferentPair_1_5_7_3_8: Choice_1_3_8 + Choice_1_5_7 <= 1
DifferentPair_1_5_7_4_5: Choice_1_4_5 + Choice_1_5_7 <= 1
DifferentPair_1_5_7_4_9: Choice_1_4_9 + Choice_1_5_7 <= 1
DifferentPair_1_5_7_6_5: Choice_1_5_7 + Choice_1_6_5 <= 1
DifferentPair_1_5_7_6_9: Choice_1_5_7 + Choice_1_6_9 <= 1
DifferentPair_1_5_7_7_6: Choice_1_5_7 + Choice_1_7_6 <= 1
DifferentPair_1_5_7_7_8: Choice_1_5_7 + Choice_1_7_8 <= 1
DifferentPair_1_5_8_3_7: Choice_1_3_7 + Choice_1_5_8 <= 1
DifferentPair_1_5_8_3_9: Choice_1_3_9 + Choice_1_5_8 <= 1
DifferentPair_1_5_8_4_6: Choice_1_4_6 + Choice_1_5_8 <= 1
DifferentPair_1_5_8_6_6: Choice_1_5_8 + Choice_1_6_6 <= 1
DifferentPair_1_5_8_7_7: Choice_1_5_8 + Choice_1_7_7 <= 1
DifferentPair_1_5_8_7_9: Choice_1_5_8 + Choice_1_7_9 <= 1
DifferentPair_1_5_9_3_8: Choice_1_3_8 + Choice_1_5_9 <= 1
DifferentPair_1_5_9_4_7: Choice_1_4_7 + Choice_1_5_9 <= 1
DifferentPair_1_5_9_6_7: Choice_1_5_9 + Choice_1_6_7 <= 1
DifferentPair_1_5_9_7_8: Choice_1_5_9 + Choice_1_7_8 <= 1
DifferentPair_1_6_1_4_2: Choice_1_4_2 + Choice_1_6_1 <= 1
DifferentPair_1_6_1_5_3: Choice_1_5_3 + Choice_1_6_1 <= 1
DifferentPair_1_6_1_7_3: Choice_1_6_1 + Choice_1_7_3 <= 1
DifferentPair_1_6_1_8_2: Choice_1_6_1 + Choice_1_8_2 <= 1
DifferentPair_1_6_2_4_1: Choice_1_4_1 + Choice_1_6_2 <= 1
DifferentPair_1_6_2_4_3: Choice_1_4_3 + Choice_1_6_2 <= 1
DifferentPair_1_6_2_5_4: Choice_1_5_4 + Choice_1_6_2 <= 1
DifferentPair_1_6_2_7_4: Choice_1_6_2 + Choice_1_7_4 <= 1
DifferentPair_1_6_2_8_1: Choice_1_6_2 + Choice_1_8_1 <= 1
DifferentPair_1_6_2_8_3: Choice_1_6_2 + Choice_1_8_3 <= 1
DifferentPair_1_6_3_4_2: Choice_1_4_2 + Choice_1_6_3 <= 1
DifferentPair_1_6_3_4_4: Choice_1_4_4 + Choice_1_6_3 <= 1
DifferentPair_1_6_3_5_1: Choice_1_5_1 + Choice_1_6_3 <= 1
DifferentPair_1_6_3_5_5: Choice_1_5_5 + Choice_1_6_3 <= 1
DifferentPair_1_6_3_7_1: Choice_1_6_3 + Choice_1_7_1 <= 1
DifferentPair_1_6_3_7_5: Choice_1_6_3 + Choice_1_7_5 <= 1
DifferentPair_1_6_3_8_2: Choice_1_6_3 + Choice_1_8_2 <= 1
DifferentPair_1_6_3_8_4: Choice_1_6_3 + Choice_1_8_4 <= 1
DifferentPair_1_6_4_4_3: Choice_1_4_3 + Choice_1_6_4 <= 1
DifferentPair_1_6_4_4_5: Choice_1_4_5 + Choice_1_6_4 <= 1
DifferentPair_1_6_4_5_2: Choice_1_5_2 + Choice_1_6_4 <= 1
DifferentPair_1_6_4_5_6: Choice_1_5_6 + Choice_1_6_4 <= 1
DifferentPair_1_6_4_7_2: Choice_1_6_4 + Choice_1_7_2 <= 1
DifferentPair_1_6_4_7_6: Choice_1_6_4 + Choice_1_7_6 <= 1
DifferentPair_1_6_4_8_3: Choice_1_6_4 + Choice_1_8_3 <= 1
DifferentPair_1_6_4_8_5: Choice_1_6_4 + Choice_1_8_5 <= 1
DifferentPair_1_6_5_4_4: Choice_1_4_4 + Choice_1_6_5 <= 1
DifferentPair_1_6_5_4_6: Choice_1_4_6 + Choice_1_6_5 <= 1
DifferentPair_1_6_5_5_3: Choice_1_5_3 + Choice_1_6_5 <= 1
DifferentPair_1_6_5_5_7: Choice_1_5_7 + Choice_1_6_5 <= 1
DifferentPair_1_6_5_7_3: Choice_1_6_5 + Choice_1_7_3 <= 1
DifferentPair_1_6_5_7_7: Choice_1_6_5 + Choice_1_7_7 <= 1
DifferentPair_1_6_5_8_4: Choice_1_6_5 + Choice_1_8_4 <= 1
DifferentPair_1_6_5_8_6: Choice_1_6_5 + Choice_1_8_6 <= 1
DifferentPair_1_6_6_4_5: Choice_1_4_5 + Choice_1_6_6 <= 1
DifferentPair_1_6_6_4_7: Choice_1_4_7 + Choice_1_6_6 <= 1
DifferentPair_1_6_6_5_4: Choice_1_5_4 + Choice_1_6_6 <= 1
DifferentPair_1_6_6_5_8: Choice_1_5_8 + Choice_1_6_6 <= 1
DifferentPair_1_6_6_7_4: Choice_1_6_6 + Choice_1_7_4 <= 1
DifferentPair_1_6_6_7_8: Choice_1_6_6 + Choice_1_7_8 <= 1
DifferentPair_1_6_6_8_5: Choice_1_6_6 + Choice_1_8_5 <= 1
DifferentPair_1_6_6_8_7: Choice_1_6_6 + Choice_1_8_7 <= 1
DifferentPair_1_6_7_4_6: Choice_1_4_6 + Choice_1_6_7 <= 1
DifferentPair_1_6_7_4_8: Choice_1_4_8 + Choice_1_6_7 <= 1
DifferentPair_1_6_7_5_5: Choice_1_5_5 + Choice_1_6_7 <= 1
DifferentPair_1_6_7_5_9: Choice_1_5_9 + Choice_1_6_7 <= 1
DifferentPair_1_6_7_7_5: Choice_1_6_7 + Choice_1_7_5 <= 1
DifferentPair_1_6_7_7_9: Choice_1_6_7 + Choice_1_7_9 <= 1
DifferentPair_1_6_7_8_6: Choice_1_6_7 + Choice_1_8_6 <= 1
DifferentPair_1_6_7_8_8: Choice_1_6_7 + Choice_1_8_8 <= 1
DifferentPair_1_6_8_4_7: Choice_1_4_7 + Choice_1_6_8 <= 1
DifferentPair_1_6_8_4_9: Choice_1_4_9 + Choice_1_6_8 <= 1
DifferentPair_1_6_8_5_6: Choice_1_5_6 + Choice_1_6_8 <= 1
DifferentPair_1_6_8_7_6: Choice_1_6_8 + Choice_1_7_6 <= 1
DifferentPair_1_6_8_8_7: Choice_1_6_8 + Choice_1_8_7 <= 1
DifferentPair_1_6_8_8_9: Choice_1_6_8 + Choice_1_8_9 <= 1
DifferentPair_1_6_9_4_8: Choice_1_4_8 + Choice_1_6_9 <= 1
DifferentPair_1_6_9_5_7: Choice_1_5_7 + Choice_1_6_9 <= 1
DifferentPair_1_6_9_7_7: Choice_1_6_9 + Choice_1_7_7 <= 1
DifferentPair_1_6_9_8_8: Choice_1_6_9 + Choice_1_8_8 <= 1
DifferentPair_1_7_1_5_2: Choice_1_5_2 + Choice_1_7_1 <= 1
DifferentPair_1_7_1_6_3: Choice_1_6_3 + Choice_1_7_1 <= 1
DifferentPair_1_7_1_8_3: Choice_1_7_1 + Choice_1_8_3 <= 1
DifferentPair_1_7_1_9_2: Choice_1_7_1 + Choice_1_9_2 <= 1
DifferentPair_1_7_2_5_1: Choice_1_5_1 + Choice_1_7_2 <= 1
DifferentPair_1_7_2_5_3: Choice_1_5_3 + Choice_1_7_2 <= 1
DifferentPair_1_7_2_6_4: Choice_1_6_4 + Choice_1_7_2 <= 1
DifferentPair_1_7_2_8_4: Choice_1_7_2 + Choice_1_8_4 <= 1
DifferentPair_1_7_2_9_1: Choice_1_7_2 + Choice_1_9_1 <= 1
DifferentPair_1_7_2_9_3: Choice_1_7_2 + Choice_1_9_3 <= 1
DifferentPair_1_7_3_5_2: Choice_1_5_2 + Choice_1_7_3 <= 1
DifferentPair_1_7_3_5_4: Choice_1_5_4 + Choice_1_7_3 <= 1
DifferentPair_1_7_3_6_1: Choice_1_6_1 + Choice_1_7_3 <= 1
DifferentPair_1_7_3_6_5: Choice_1_6_5 + Choice_1_7_3 <= 1
DifferentPair_1_7_3_8_1: Choice_1_7_3 + Choice_1_8_1 <= 1
DifferentPair_1_7_3_8_5: Choice_1_7_3 + Choice_1_8_5 <= 1
DifferentPair_1_7_3_9_2: Choice_1_7_3 + Choice_1_9_2 <= 1
DifferentPair_1_7_3_9_4: Choice_1_7_3 + Choice_1_9_4 <= 1
DifferentPair_1_7_4_5_3: Choice_1_5_3 + Choice_1_7_4 <= 1
DifferentPair_1_7_4_5_5: Choice_1_5_5 + Choice_1_7_4 <= 1
DifferentPair_1_7_4_6_2: Choice_1_6_2 + Choice_1_7_4 <= 1
DifferentPair_1_7_4_6_6: Choice_1_6_6 + Choice_1_7_4 <= 1
DifferentPair_1_7_4_8_2: Choice_1_7_4 + Choice_1_8_2 <= 1
DifferentPair_1_7_4_8_6: Choice_1_7_4 + Choice_1_8_6 <= 1
DifferentPair_1_7_4_9_3: Choice_1_7_4 + Choice_1_9_3 <= 1
DifferentPair_1_7_4_9_5: Choice_1_7_4 + Choice_1_9_5 <= 1
DifferentPair_1_7_5_5_4: Choice_1_5_4 + Choice_1_7_5 <= 1
DifferentPair_1_7_5_5_6: Choice_1_5_6 + Choice_1_7_5 <= 1
DifferentPair_1_7_5_6_3: Choice_1_6_3 + Choice_1_7_5 <= 1
DifferentPair_1_7_5_6_7: Choice_1_6_7 + Choice_1_7_5 <= 1
DifferentPair_1_7_5_8_3: Choice_1_7_5 + Choice_1_8_3 <= 1
DifferentPair_1_7_5_8_7: Choice_1_7_5 + Choice_1_8_7 <= 1
DifferentPair_1_7_5_9_4: Choice_1_7_5 + Choice_1_9_4 <= 1
DifferentPair_1_7_5_9_6: Choice_1_7_5 + Choice_1_9_6 <= 1
DifferentPair_1_7_6_5_5: Choice_1_5_5 + Choice_1_7_6 <= 1
DifferentPair_1_7_6_5_7: Choice_1_5_7 + Choice_1_7_6 <= 1
DifferentPair_1_7_6_6_4: Choice_1_6_4 + Choice_1_7_6 <= 1
DifferentPair_1_7_6_6_8: Choice_1_6_8 + Choice_1_7_6 <= 1
DifferentPair_1_7_6_8_4: Choice_1_7_6 + Choice_1_8_4 <= 1
DifferentPair_1_7_6_8_8: Choice_1_7_6 + Choice_1_8_8 <= 1
DifferentPair_1_7_6_9_5: Choice_1_7_6 + Choice_1_9_5 <= 1
DifferentPair_1_7_6_9_7: Choice_1_7_6 + Choice_1_9_7 <= 1
DifferentPair_1_7_7_5_6: Choice_1_5_6 + Choice_1_7_7 <= 1
DifferentPair_1_7_7_5_8: Choice_1_5_8 + Choice_1_7_7 <= 1
DifferentPair_1_7_7_6_5: Choice_1_6_5 + Choice_1_7_7 <= 1
DifferentPair_1_7_7_6_9: Choice_1_6_9 + Choice_1_7_7 <= 1
DifferentPair_1_7_7_8_5: Choice_1_7_7 + Choice_1_8_5 <= 1
DifferentPair_1_7_7_8_9: Choice_1_7_7 + Choice_1_8_9 <= 1
DifferentPair_1_7_7_9_6: Choice_1_7_7 + Choice_1_9_6 <= 1
DifferentPair_1_7_7_9_8: Choice_1_7_7 + Choice_1_9_8 <= 1
DifferentPair_1_7_8_5_7: Choice_1_5_7 + Choice_1_7_8 <= 1
DifferentPair_1_7_8_5_9: Choice_1_5_9 + Choice_1_7_8 <= 1
DifferentPair_1_7_8_6_6: Choice_1_6_6 + Choice_1_7_8 <= 1
DifferentPair_1_7_8_8_6: Choice_1_7_8 + Choice_1_8_6 <= 1
DifferentPair_1_7_8_9_7: Choice_1_7_8 + Choice_1_9_7 <= 1
DifferentPair_1_7_8_9_9: Choice_1_7_8 + Choice_1_9_9 <= 1
DifferentPair_1_7_9_5_8: Choice_1_5_8 + Choice_1_7_9 <= 1
DifferentPair_1_7_9_6_7: Choice_1_6_7 + Choice_1_7_9 <= 1
DifferentPair_1_7_9_8_7: Choice_1_7_9 + Choice_1_8_7 <= 1
DifferentPair_1_7_9_9_8: Choice_1_7_9 + Choice_1_9_8 <= 1
DifferentPair_1_8_1_6_2: Choice_1_6_2 + Choice_1_8_1 <= 1
DifferentPair_1_8_1_7_3: Choice_1_7_3 + Choice_1_8_1 <= 1
DifferentPair_1_8_1_9_3: Choice_1_8_1 + Choice_1_9_3 <= 1
DifferentPair_1_8_2_6_1: Choice_1_6_1 + Choice_1_8_2 <= 1
DifferentPair_1_8_2_6_3: Choice_1_6_3 + Choice_1_8_2 <= 1
DifferentPair_1_8_2_7_4: Choice_1_7_4 + Choice_1_8_2 <= 1
DifferentPair_1_8_2_9_4: Choice_1_8_2 + Choice_1_9_4 <= 1
DifferentPair_1_8_3_6_2: Choice_1_6_2 + Choice_1_8_3 <= 1
DifferentPair_1_8_3_6_4: Choice_1_6_4 + Choice_1_8_3 <= 1
DifferentPair_1_8_3_7_1: Choice_1_7_1 + Choice_1_8_3 <= 1
DifferentPair_1_8_3_7_5: Choice_1_7_5 + Choice_1_8_3 <= 1
DifferentPair_1_8_3_9_1: Choice_1_8_3 + Choice_1_9_1 <= 1
DifferentPair_1_8_3_9_5: Choice_1_8_3 + Choice_1_9_5 <= 1
DifferentPair_1_8_4_6_3: Choice_1_6_3 + Choice_1_8_4 <= 1
DifferentPair_1_8_4_6_5: Choice_1_6_5 + Choice_1_8_4 <= 1
DifferentPair_1_8_4_7_2: Choice_1_7_2 + Choice_1_8_4 <= 1
DifferentPair_1_8_4_7_6: Choice_1_7_6 + Choice_1_8_4 <= 1
DifferentPair_1_8_4_9_2: Choice_1_8_4 + Choice_1_9_2 <= 1
DifferentPair_1_8_4_9_6: Choice_1_8_4 + Choice_1_9_6 <= 1
DifferentPair_1_8_5_6_4: Choice_1_6_4 + Choice_1_8_5 <= 1
DifferentPair_1_8_5_6_6: Choice_1_6_6 + Choice_1_8_5 <= 1
DifferentPair_1_8_5_7_3: Choice_1_7_3 + Choice_1_8_5 <= 1
DifferentPair_1_8_5_7_7: Choice_1_7_7 + Choice_1_8_5 <= 1
DifferentPair_1_8_5_9_3: Choice_1_8_5 + Choice_1_9_3 <= 1
DifferentPair_1_8_5_9_7: Choice_1_8_5 + Choice_1_9_7 <= 1
DifferentPair_1_8_6_6_5: Choice_1_6_5 + Choice_1_8_6 <= 1
DifferentPair_1_8_6_6_7: Choice_1_6_7 + Choice_1_8_6 <= 1
DifferentPair_1_8_6_7_4: Choice_1_7_4 + Choice_1_8_6 <= 1
DifferentPair_1_8_6_7_8: Choice_1_7_8 + Choice_1_8_6 <= 1
DifferentPair_1_8_6_9_4: Choice_1_8_6 + Choice_1_9_4 <= 1
DifferentPair_1_8_6_9_8: Choice_1_8_6 + Choice_1_9_8 <= 1
DifferentPair_1_8_7_6_6: Choice_1_6_6 + Choice_1_8_7 <= 1
DifferentPair_1_8_7_6_8: Choice_1_6_8 + Choice_1_8_7 <= 1
DifferentPair_1_8_7_7_5: Choice_1_7_5 + Choice_1_8_7 <= 1
DifferentPair_1_8_7_7_9: Choice_1_7_9 + Choice_1_8_7 <= 1
DifferentPair_1_8_7_9_5: Choice_1_8_7 + Choice_1_9_5 <= 1
DifferentPair_1_8_7_9_9: Choice_1_8_7 + Choice_1_9_9 <= 1
DifferentPair_1_8_8_6_7: Choice_1_6_7 + Choice_1_8_8 <= 1
DifferentPair_1_8_8_6_9: Choice_1_6_9 + Choice_1_8_8 <= 1
DifferentPair_1_8_8_7_6: Choice_1_7_6 + Choice_1_8_8 <= 1
DifferentPair_1_8_8_9_6: Choice_1_8_8 + Choice_1_9_6 <= 1
DifferentPair_1_8_9_6_8: Choice_1_6_8 + Choice_1_8_9 <= 1
DifferentPair_1_8_9_7_7: Choice_1_7_7 + Choice_1_8_9 <= 1
DifferentPair_1_8_9_9_7: Choice_1_8_9 + Choice_1_9_7 <= 1
DifferentPair_1_9_1_7_2: Choice_1_7_2 + Choice_1_9_1 <= 1
DifferentPair_1_9_1_8_3: Choice_1_8_3 + Choice_1_9_1 <= 1
DifferentPair_1_9_2_7_1: Choice_1_7_1 + Choice_1_9_2 <= 1
DifferentPair_1_9_2_7_3: Choice_1_7_3 + Choice_1_9_2 <= 1
DifferentPair_1_9_2_8_4: Choice_1_8_4 + Choice_1_9_2 <= 1
DifferentPair_1_9_3_7_2: Choice_1_7_2 + Choice_1_9_3 <= 1
DifferentPair_1_9_3_7_4: Choice_1_7_4 + Choice_1_9_3 <= 1
DifferentPair_1_9_3_8_1: Choice_1_8_1 + Choice_1_9_3 <= 1
DifferentPair_1_9_3_8_5: Choice_1_8_5 + Choice_1_9_3 <= 1
DifferentPair_1_9_4_7_3: Choice_1_7_3 + Choice_1_9_4 <= 1
DifferentPair_1_9_4_7_5: Choice_1_7_5 + Choice_1_9_4 <= 1
DifferentPair_1_9_4_8_2: Choice_1_8_2 + Choice_1_9_4 <= 1
DifferentPair_1_9_4_8_6: Choice_1_8_6 + Choice_1_9_4 <= 1
DifferentPair_1_9_5_7_4: Choice_1_7_4 + Choice_1_9_5 <= 1
DifferentPair_1_9_5_7_6: Choice_1_7_6 + Choice_1_9_5 <= 1
DifferentPair_1_9_5_8_3: Choice_1_8_3 + Choice_1_9_5 <= 1
DifferentPair_1_9_5_8_7: Choice_1_8_7 + Choice_1_9_5 <= 1
DifferentPair_1_9_6_7_5: Choice_1_7_5 + Choice_1_9_6 <= 1
DifferentPair_1_9_6_7_7: Choice_1_7_7 + Choice_1_9_6 <= 1
DifferentPair_1_9_6_8_4: Choice_1_8_4 + Choice_1_9_6 <= 1
DifferentPair_1_9_6_8_8: Choice_1_8_8 + Choice_1_9_6 <= 1
DifferentPair_1_9_7_7_6: Choice_1_7_6 + Choice_1_9_7 <= 1
DifferentPair_1_9_7_7_8: Choice_1_7_8 + Choice_1_9_7 <= 1
DifferentPair_1_9_7_8_5: Choice_1_8_5 + Choice_1_9_7 <= 1
DifferentPair_1_9_7_8_9: Choice_1_8_9 + Choice_1_9_7 <= 1
DifferentPair_1_9_8_7_7: Choice_1_7_7 + Choice_1_9_8 <= 1
DifferentPair_1_9_8_7_9: Choice_1_7_9 + Choice_1_9_8 <= 1
DifferentPair_1_9_8_8_6: Choice_1_8_6 + Choice_1_9_8 <= 1
DifferentPair_1_9_9_7_8: Choice_1_7_8 + Choice_1_9_9 <= 1
DifferentPair_1_9_9_8_7: Choice_1_8_7 + Choice_1_9_9 <= 1
DifferentPair_2_1_1_2_3: Choice_2_1_1 + Choice_2_2_3 <= 1
DifferentPair_2_1_1_3_2: Choice_2_1_1 + Choice_2_3_2 <= 1
DifferentPair_2_1_2_2_4: Choice_2_1_2 + Choice_2_2_4 <= 1
DifferentPair_2_1_2_3_1: Choice_2_1_2 + Choice_2_3_1 <= 1
DifferentPair_2_1_2_3_3: Choice_2_1_2 + Choice_2_3_3 <= 1
DifferentPair_2_1_3_2_1: Choice_2_1_3 + Choice_2_2_1 <= 1
DifferentPair_2_1_3_2_5: Choice_2_1_3 + Choice_2_2_5 <= 1
DifferentPair_2_1_3_3_2: Choice_2_1_3 + Choice_2_3_2 <= 1
DifferentPair_2_1_3_3_4: Choice_2_1_3 + Choice_2_3_4 <= 1
DifferentPair_2_1_4_2_2: Choice_2_1_4 + Choice_2_2_2 <= 1
DifferentPair_2_1_4_2_6: Choice_2_1_4 + Choice_2_2_6 <= 1
DifferentPair_2_1_4_3_3: Choice_2_1_4 + Choice_2_3_3 <= 1
DifferentPair_2_1_4_3_5: Choice_2_1_4 + Choice_2_3_5 <= 1
DifferentPair_2_1_5_2_3: Choice_2_1_5 + Choice_2_2_3 <= 1
DifferentPair_2_1_5_2_7: Choice_2_1_5 + Choice_2_2_7 <= 1
DifferentPair_2_1_5_3_4: Choice_2_1_5 + Choice_2_3_4 <= 1
DifferentPair_2_1_5_3_6: Choice_2_1_5 + Choice_2_3_6 <= 1
DifferentPair_2_1_6_2_4: Choice_2_1_6 + Choice_2_2_4 <= 1
DifferentPair_2_1_6_2_8: Choice_2_1_6 + Choice_2_2_8 <= 1
DifferentPair_2_1_6_3_5: Choice_2_1_6 + Choice_2_3_5 <= 1
DifferentPair_2_1_6_3_7: Choice_2_1_6 + Choice_2_3_7 <= 1
DifferentPair_2_1_7_2_5: Choice_2_1_7 + Choice_2_2_5 <= 1
DifferentPair_2_1_7_2_9: Choice_2_1_7 + Choice_2_2_9 <= 1
DifferentPair_2_1_7_3_6: Choice_2_1_7 + Choice_2_3_6 <= 1
DifferentPair_2_1_7_3_8: Choice_2_1_7 + Choice_2_3_8 <= 1
DifferentPair_2_1_8_2_6: Choice_2_1_8 + Choice_2_2_6 <= 1
DifferentPair_2_1_8_3_7: Choice_2_1_8 + Choice_2_3_7 <= 1
DifferentPair_2_1_8_3_9: Choice_2_1_8 + Choice_2_3_9 <= 1
DifferentPair_2_1_9_2_7: Choice_2_1_9 + Choice_2_2_7 <= 1
DifferentPair_2_1_9_3_8: Choice_2_1_9 + Choice_2_3_8 <= 1
DifferentPair_2_2_1_1_3: Choice_2_1_3 + Choice_2_2_1 <= 1
DifferentPair_2_2_1_3_3: Choice_2_2_1 + Choice_2_3_3 <= 1
DifferentPair_2_2_1_4_2: Choice_2_2_1 + Choice_2_4_2 <= 1
DifferentPair_2_2_2_1_4: Choice_2_1_4 + Choice_2_2_2 <= 1
DifferentPair_2_2_2_3_4: Choice_2_2_2 + Choice_2_3_4 <= 1
DifferentPair_2_2_2_4_1: Choice_2_2_2 + Choice_2_4_1 <= 1
DifferentPair_2_2_2_4_3: Choice_2_2_2 + Choice_2_4_3 <= 1
DifferentPair_2_2_3_1_1: Choice_2_1_1 + Choice_2_2_3 <= 1
DifferentPair_2_2_3_1_5: Choice_2_1_5 + Choice_2_2_3 <= 1
DifferentPair_2_2_3_3_1: Choice_2_2_3 + Choice_2_3_1 <= 1
DifferentPair_2_2_3_3_5: Choice_2_2_3 + Choice_2_3_5 <= 1
DifferentPair_2_2_3_4_2: Choice_2_2_3 + Choice_2_4_2 <= 1
DifferentPair_2_2_3_4_4: Choice_2_2_3 + Choice_2_4_4 <= 1
DifferentPair_2_2_4_1_2: Choice_2_1_2 + Choice_2_2_4 <= 1
DifferentPair_2_2_4_1_6: Choice_2_1_6 + Choice_2_2_4 <= 1
DifferentPair_2_2_4_3_2: Choice_2_2_4 + Choice_2_3_2 <= 1
DifferentPair_2_2_4_3_6: Choice_2_2_4 + Choice_2_3_6 <= 1
DifferentPair_2_2_4_4_3: Choice_2_2_4 + Choice_2_4_3 <= 1
DifferentPair_2_2_4_4_5: Choice_2_2_4 + Choice_2_4_5 <= 1
DifferentPair_2_2_5_1_3: Choice_2_1_3 + Choice_2_2_5 <= 1
DifferentPair_2_2_5_1_7: Choice_2_1_7 + Choice_2_2_5 <= 1
DifferentPair_2_2_5_3_3: Choice_2_2_5 + Choice_2_3_3 <= 1
DifferentPair_2_2_5_3_7: Choice_2_2_5 + Choice_2_3_7 <= 1
DifferentPair_2_2_5_4_4: Choice_2_2_5 + Choice_2_4_4 <= 1
DifferentPair_2_2_5_4_6: Choice_2_2_5 + Choice_2_4_6 <= 1
DifferentPair_2_2_6_1_4: Choice_2_1_4 + Choice_2_2_6 <= 1
DifferentPair_2_2_6_1_8: Choice_2_1_8 + Choice_2_2_6 <= 1
DifferentPair_2_2_6_3_4: Choice_2_2_6 + Choice_2_3_4 <= 1
DifferentPair_2_2_6_3_8: Choice_2_2_6 + Choice_2_3_8 <= 1
DifferentPair_2_2_6_4_5: Choice_2_2_6 + Choice_2_4_5 <= 1
DifferentPair_2_2_6_4_7: Choice_2_2_6 + Choice_2_4_7 <= 1
DifferentPair_2_2_7_1_5: Choice_2_1_5 + Choice_2_2_7 <= 1
DifferentPair_2_2_7_1_9: Choice_2_1_9 + Choice_2_2_7 <= 1
DifferentPair_2_2_7_3_5: Choice_2_2_7 + Choice_2_3_5 <= 1
DifferentPair_2_2_7_3_9: Choice_2_2_7 + Choice_2_3_9 <= 1
DifferentPair_2_2_7_4_6: Choice_2_2_7 + Choice_2_4_6 <= 1
DifferentPair_2_2_7_4_8: Choice_2_2_7 + Choice_2_4_8 <= 1
DifferentPair_2_2_8_1_6: Choice_2_1_6 + Choice_2_2_8 <= 1
DifferentPair_2_2_8_3_6: Choice_2_2_8 + Choice_2_3_6 <= 1
DifferentPair_2_2_8_4_7: Choice_2_2_8 + Choice_2_4_7 <= 1
DifferentPair_2_2_8_4_9: Choice_2_2_8 + Choice_2_4_9 <= 1
DifferentPair_2_2_9_1_7: Choice_2_1_7 + Choice_2_2_9 <= 1
DifferentPair_2_2_9_3_7: Choice_2_2_9 + Choice_2_3_7 <= 1
DifferentPair_2_2_9_4_8: Choice_2_2_9 + Choice_2_4_8 <= 1
DifferentPair_2_3_1_1_2: Choice_2_1_2 + Choice_2_3_1 <= 1
DifferentPair_2_3_1_2_3: Choice_2_2_3 + Choice_2_3_1 <= 1
DifferentPair_2_3_1_4_3: Choice_2_3_1 + Choice_2_4_3 <= 1
DifferentPair_2_3_1_5_2: Choice_2_3_1 + Choice_2_5_2 <= 1
DifferentPair_2_3_2_1_1: Choice_2_1_1 + Choice_2_3_2 <= 1
DifferentPair_2_3_2_1_3: Choice_2_1_3 + Choice_2_3_2 <= 1
DifferentPair_2_3_2_2_4: Choice_2_2_4 + Choice_2_3_2 <= 1
DifferentPair_2_3_2_4_4: Choice_2_3_2 + Choice_2_4_4 <= 1
DifferentPair_2_3_2_5_1: Choice_2_3_2 + Choice_2_5_1 <= 1
DifferentPair_2_3_2_5_3: Choice_2_3_2 + Choice_2_5_3 <= 1
DifferentPair_2_3_3_1_2: Choice_2_1_2 + Choice_2_3_3 <= 1
DifferentPair_2_3_3_1_4: Choice_2_1_4 + Choice_2_3_3 <= 1
DifferentPair_2_3_3_2_1: Choice_2_2_1 + Choice_2_3_3 <= 1
DifferentPair_2_3_3_2_5: Choice_2_2_5 + Choice_2_3_3 <= 1
DifferentPair_2_3_3_4_1: Choice_2_3_3 + Choice_2_4_1 <= 1
DifferentPair_2_3_3_4_5: Choice_2_3_3 + Choice_2_4_5 <= 1
DifferentPair_2_3_3_5_2: Choice_2_3_3 + Choice_2_5_2 <= 1
DifferentPair_2_3_3_5_4: Choice_2_3_3 + Choice_2_5_4 <= 1
DifferentPair_2_3_4_1_3: Choice_2_1_3 + Choice_2_3_4 <= 1
DifferentPair_2_3_4_1_5: Choice_2_1_5 + Choice_2_3_4 <= 1
DifferentPair_2_3_4_2_2: Choice_2_2_2 + Choice_2_3_4 <= 1
DifferentPair_2_3_4_2_6: Choice_2_2_6 + Choice_2_3_4 <= 1
DifferentPair_2_3_4_4_2: Choice_2_3_4 + Choice_2_4_2 <= 1
DifferentPair_2_3_4_4_6: Choice_2_3_4 + Choice_2_4_6 <= 1
DifferentPair_2_3_4_5_3: Choice_2_3_4 + Choice_2_5_3 <= 1
DifferentPair_2_3_4_5_5: Choice_2_3_4 + Choice_2_5_5 <= 1
DifferentPair_2_3_5_1_4: Choice_2_1_4 + Choice_2_3_5 <= 1
DifferentPair_2_3_5_1_6: Choice_2_1_6 + Choice_2_3_5 <= 1
DifferentPair_2_3_5_2_3: Choice_2_2_3 + Choice_2_3_5 <= 1
DifferentPair_2_3_5_2_7: Choice_2_2_7 + Choice_2_3_5 <= 1
DifferentPair_2_3_5_4_3: Choice_2_3_5 + Choice_2_4_3 <= 1
DifferentPair_2_3_5_4_7: Choice_2_3_5 + Choice_2_4_7 <= 1
DifferentPair_2_3_5_5_4: Choice_2_3_5 + Choice_2_5_4 <= 1
DifferentPair_2_3_5_5_6: Choice_2_3_5 + Choice_2_5_6 <= 1
DifferentPair_2_3_6_1_5: Choice_2_1_5 + Choice_2_3_6 <= 1
DifferentPair_2_3_6_1_7: Choice_2_1_7 + Choice_2_3_6 <= 1
DifferentPair_2_3_6_2_4: Choice_2_2_4 + Choice_2_3_6 <= 1
DifferentPair_2_3_6_2_8: Choice_2_2_8 + Choice_2_3_6 <= 1
DifferentPair_2_3_6_4_4: Choice_2_3_6 + Choice_2_4_4 <= 1
DifferentPair_2_3_6_4_8: Choice_2_3_6 + Choice_2_4_8 <= 1
DifferentPair_2_3_6_5_5: Choice_2_3_6 + Choice_2_5_5 <= 1
DifferentPair_2_3_6_5_7: Choice_2_3_6 + Choice_2_5_7 <= 1
DifferentPair_2_3_7_1_6: Choice_2_1_6 + Choice_2_3_7 <= 1
DifferentPair_2_3_7_1_8: Choice_2_1_8 + Choice_2_3_7 <= 1
DifferentPair_2_3_7_2_5: Choice_2_2_5 + Choice_2_3_7 <= 1
DifferentPair_2_3_7_2_9: Choice_2_2_9 + Choice_2_3_7 <= 1
DifferentPair_2_3_7_4_5: Choice_2_3_7 + Choice_2_4_5 <= 1
DifferentPair_2_3_7_4_9: Choice_2_3_7 + Choice_2_4_9 <= 1
DifferentPair_2_3_7_5_6: Choice_2_3_7 + Choice_2_5_6 <= 1
DifferentPair_2_3_7_5_8: Choice_2_3_7 + Choice_2_5_8 <= 1
DifferentPair_2_3_8_1_7: Choice_2_1_7 + Choice_2_3_8 <= 1
DifferentPair_2_3_8_1_9: Choice_2_1_9 + Choice_2_3_8 <= 1
DifferentPair_2_3_8_2_6: Choice_2_2_6 + Choice_2_3_8 <= 1
DifferentPair_2_3_8_4_6: Choice_2_3_8 + Choice_2_4_6 <= 1
DifferentPair_2_3_8_5_7: Choice_2_3_8 + Choice_2_5_7 <= 1
DifferentPair_2_3_8_5_9: Choice_2_3_8 + Choice_2_5_9 <= 1
DifferentPair_2_3_9_1_8: Choice_2_1_8 + Choice_2_3_9 <= 1
DifferentPair_2_3_9_2_7: Choice_2_2_7 + Choice_2_3_9 <= 1
DifferentPair_2_3_9_4_7: Choice_2_3_9 + Choice_2_4_7 <= 1
DifferentPair_2_3_9_5_8: Choice_2_3_9 + Choice_2_5_8 <= 1
DifferentPair_2_4_1_2_2: Choice_2_2_2 + Choice_2_4_1 <= 1
DifferentPair_2_4_1_3_3: Choice_2_3_3 + Choice_2_4_1 <= 1
DifferentPair_2_4_1_5_3: Choice_2_4_1 + Choice_2_5_3 <= 1
DifferentPair_2_4_1_6_2: Choice_2_4_1 + Choice_2_6_2 <= 1
DifferentPair_2_4_2_2_1: Choice_2_2_1 + Choice_2_4_2 <= 1
DifferentPair_2_4_2_2_3: Choice_2_2_3 + Choice_2_4_2 <= 1
DifferentPair_2_4_2_3_4: Choice_2_3_4 + Choice_2_4_2 <= 1
DifferentPair_2_4_2_5_4: Choice_2_4_2 + Choice_2_5_4 <= 1
DifferentPair_2_4_2_6_1: Choice_2_4_2 + Choice_2_6_1 <= 1
DifferentPair_2_4_2_6_3: Choice_2_4_2 + Choice_2_6_3 <= 1
DifferentPair_2_4_3_2_2: Choice_2_2_2 + Choice_2_4_3 <= 1
DifferentPair_2_4_3_2_4: Choice_2_2_4 + Choice_2_4_3 <= 1
DifferentPair_2_4_3_3_1: Choice_2_3_1 + Choice_2_4_3 <= 1
DifferentPair_2_4_3_3_5: Choice_2_3_5 + Choice_2_4_3 <= 1
DifferentPair_2_4_3_5_1: Choice_2_4_3 + Choice_2_5_1 <= 1
DifferentPair_2_4_3_5_5: Choice_2_4_3 + Choice_2_5_5 <= 1
DifferentPair_2_4_3_6_2: Choice_2_4_3 + Choice_2_6_2 <= 1
DifferentPair_2_4_3_6_4: Choice_2_4_3 + Choice_2_6_4 <= 1
DifferentPair_2_4_4_2_3: Choice_2_2_3 + Choice_2_4_4 <= 1
DifferentPair_2_4_4_2_5: Choice_2_2_5 + Choice_2_4_4 <= 1
DifferentPair_2_4_4_3_2: Choice_2_3_2 + Choice_2_4_4 <= 1
DifferentPair_2_4_4_3_6: Choice_2_3_6 + Choice_2_4_4 <= 1
DifferentPair_2_4_4_5_2: Choice_2_4_4 + Choice_2_5_2 <= 1
DifferentPair_2_4_4_5_6: Choice_2_4_4 + Choice_2_5_6 <= 1
DifferentPair_2_4_4_6_3: Choice_2_4_4 + Choice_2_6_3 <= 1
DifferentPair_2_4_4_6_5: Choice_2_4_4 + Choice_2_6_5 <= 1
DifferentPair_2_4_5_2_4: Choice_2_2_4 + Choice_2_4_5 <= 1
DifferentPair_2_4_5_2_6: Choice_2_2_6 + Choice_2_4_5 <= 1
DifferentPair_2_4_5_3_3: Choice_2_3_3 + Choice_2_4_5 <= 1
DifferentPair_2_4_5_3_7: Choice_2_3_7 + Choice_2_4_5 <= 1
DifferentPair_2_4_5_5_3: Choice_2_4_5 + Choice_2_5_3 <= 1
DifferentPair_2_4_5_5_7: Choice_2_4_5 + Choice_2_5_7 <= 1
DifferentPair_2_4_5_6_4: Choice_2_4_5 + Choice_2_6_4 <= 1
DifferentPair_2_4_5_6_6: Choice_2_4_5 + Choice_2_6_6 <= 1
DifferentPair_2_4_6_2_5: Choice_2_2_5 + Choice_2_4_6 <= 1
DifferentPair_2_4_6_2_7: Choice_2_2_7 + Choice_2_4_6 <= 1
DifferentPair_2_4_6_3_4: Choice_2_3_4 + Choice_2_4_6 <= 1
DifferentPair_2_4_6_3_8: Choice_2_3_8 + Choice_2_4_6 <= 1
DifferentPair_2_4_6_5_4: Choice_2_4_6 + Choice_2_5_4 <= 1
DifferentPair_2_4_6_5_8: Choice_2_4_6 + Choice_2_5_8 <= 1
DifferentPair_2_4_6_6_5: Choice_2_4_6 + Choice_2_6_5 <= 1
DifferentPair_2_4_6_6_7: Choice_2_4_6 + Choice_2_6_7 <= 1
DifferentPair_2_4_7_2_6: Choice_2_2_6 + Choice_2_4_7 <= 1
DifferentPair_2_4_7_2_8: Choice_2_2_8 + Choice_2_4_7 <= 1
DifferentPair_2_4_7_3_5: Choice_2_3_5 + Choice_2_4_7 <= 1
DifferentPair_2_4_7_3_9: Choice_2_3_9 + Choice_2_4_7 <= 1
DifferentPair_2_4_7_5_5: Choice_2_4_7 + Choice_2_5_5 <= 1
DifferentPair_2_4_7_5_9: Choice_2_4_7 + Choice_2_5_9 <= 1
DifferentPair_2_4_7_6_6: Choice_2_4_7 + Choice_2_6_6 <= 1
DifferentPair_2_4_7_6_8: Choice_2_4_7 + Choice_2_6_8 <= 1
DifferentPair_2_4_8_2_7: Choice_2_2_7 + Choice_2_4_8 <= 1
DifferentPair_2_4_8_2_9: Choice_2_2_9 + Choice_2_4_8 <= 1
DifferentPair_2_4_8_3_6: Choice_2_3_6 + Choice_2_4_8 <= 1
DifferentPair_2_4_8_5_6: Choice_2_4_8 + Choice_2_5_6 <= 1
DifferentPair_2_4_8_6_7: Choice_2_4_8 + Choice_2_6_7 <= 1
DifferentPair_2_4_8_6_9: Choice_2_4_8 + Choice_2_6_9 <= 1
DifferentPair_2_4_9_2_8: Choice_2_2_8 + Choice_2_4_9 <= 1
DifferentPair_2_4_9_3_7: Choice_2_3_7 + Choice_2_4_9 <= 1
DifferentPair_2_4_9_5_7: Choice_2_4_9 + Choice_2_5_7 <= 1
DifferentPair_2_4_9_6_8: Choice_2_4_9 + Choice_2_6_8 <= 1
DifferentPair_2_5_1_3_2: Choice_2_3_2 + Choice_2_5_1 <= 1
DifferentPair_2_5_1_4_3: Choice_2_4_3 + Choice_2_5_1 <= 1
DifferentPair_2_5_1_6_3: Choice_2_5_1 + Choice_2_6_3 <= 1
DifferentPair_2_5_1_7_2: Choice_2_5_1 + Choice_2_7_2 <= 1
DifferentPair_2_5_2_3_1: Choice_2_3_1 + Choice_2_5_2 <= 1
DifferentPair_2_5_2_3_3: Choice_2_3_3 + Choice_2_5_2 <= 1
DifferentPair_2_5_2_4_4: Choice_2_4_4 + Choice_2_5_2 <= 1
DifferentPair_2_5_2_6_4: Choice_2_5_2 + Choice_2_6_4 <= 1
DifferentPair_2_5_2_7_1: Choice_2_5_2 + Choice_2_7_1 <= 1
DifferentPair_2_5_2_7_3: Choice_2_5_2 + Choice_2_7_3 <= 1
DifferentPair_2_5_3_3_2: Choice_2_3_2 + Choice_2_5_3 <= 1
DifferentPair_2_5_3_3_4: Choice_2_3_4 + Choice_2_5_3 <= 1
DifferentPair_2_5_3_4_1: Choice_2_4_1 + Choice_2_5_3 <= 1
DifferentPair_2_5_3_4_5: Choice_2_4_5 + Choice_2_5_3 <= 1
DifferentPair_2_5_3_6_1: Choice_2_5_3 + Choice_2_6_1 <= 1
DifferentPair_2_5_3_6_5: Choice_2_5_3 + Choice_2_6_5 <= 1
DifferentPair_2_5_3_7_2: Choice_2_5_3 + Choice_2_7_2 <= 1
DifferentPair_2_5_3_7_4: Choice_2_5_3 + Choice_2_7_4 <= 1
DifferentPair_2_5_4_3_3: Choice_2_3_3 + Choice_2_5_4 <= 1
DifferentPair_2_5_4_3_5: Choice_2_3_5 + Choice_2_5_4 <= 1
DifferentPair_2_5_4_4_2: Choice_2_4_2 + Choice_2_5_4 <= 1
DifferentPair_2_5_4_4_6: Choice_2_4_6 + Choice_2_5_4 <= 1
DifferentPair_2_5_4_6_2: Choice_2_5_4 + Choice_2_6_2 <= 1
DifferentPair_2_5_4_6_6: Choice_2_5_4 + Choice_2_6_6 <= 1
DifferentPair_2_5_4_7_3: Choice_2_5_4 + Choice_2_7_3 <= 1
DifferentPair_2_5_4_7_5: Choice_2_5_4 + Choice_2_7_5 <= 1
DifferentPair_2_5_5_3_4: Choice_2_3_4 + Choice_2_5_5 <= 1
DifferentPair_2_5_5_3_6: Choice_2_3_6 + Choice_2_5_5 <= 1
DifferentPair_2_5_5_4_3: Choice_2_4_3 + Choice_2_5_5 <= 1
DifferentPair_2_5_5_4_7: Choice_2_4_7 + Choice_2_5_5 <= 1
DifferentPair_2_5_5_6_3: Choice_2_5_5 + Choice_2_6_3 <= 1
DifferentPair_2_5_5_6_7: Choice_2_5_5 + Choice_2_6_7 <= 1
DifferentPair_2_5_5_7_4: Choice_2_5_5 + Choice_2_7_4 <= 1
DifferentPair_2_5_5_7_6: Choice_2_5_5 + Choice_2_7_6 <= 1
DifferentPair_2_5_6_3_5: Choice_2_3_5 + Choice_2_5_6 <= 1
DifferentPair_2_5_6_3_7: Choice_2_3_7 + Choice_2_5_6 <= 1
DifferentPair_2_5_6_4_4: Choice_2_4_4 + Choice_2_5_6 <= 1
DifferentPair_2_5_6_4_8: Choice_2_4_8 + Choice_2_5_6 <= 1
DifferentPair_2_5_6_6_4: Choice_2_5_6 + Choice_2_6_4 <= 1
DifferentPair_2_5_6_6_8: Choice_2_5_6 + Choice_2_6_8 <= 1
DifferentPair_2_5_6_7_5: Choice_2_5_6 + Choice_2_7_5 <= 1
DifferentPair_2_5_6_7_7: Choice_2_5_6 + Choice_2_7_7 <= 1
DifferentPair_2_5_7_3_6: Choice_2_3_6 + Choice_2_5_7 <= 1
DifferentPair_2_5_7_3_8: Choice_2_3_8 + Choice_2_5_7 <= 1
DifferentPair_2_5_7_4_5: Choice_2_4_5 + Choice_2_5_7 <= 1
DifferentPair_2_5_7_4_9: Choice_2_4_9 + Choice_2_5_7 <= 1
DifferentPair_2_5_7_6_5: Choice_2_5_7 + Choice_2_6_5 <= 1
DifferentPair_2_5_7_6_9: Choice_2_5_7 + Choice_2_6_9 <= 1
DifferentPair_2_5_7_7_6: Choice_2_5_7 + Choice_2_7_6 <= 1
DifferentPair_2_5_7_7_8: Choice_2_5_7 + Choice_2_7_8 <= 1
DifferentPair_2_5_8_3_7: Choice_2_3_7 + Choice_2_5_8 <= 1
DifferentPair_2_5_8_3_9: Choice_2_3_9 + Choice_2_5_8 <= 1
DifferentPair_2_5_8_4_6: Choice_2_4_6 + Choice_2_5_8 <= 1
DifferentPair_2_5_8_6_6: Choice_2_5_8 + Choice_2_6_6 <= 1
DifferentPair_2_5_8_7_7: Choice_2_5_8 + Choice_2_7_7 <= 1
DifferentPair_2_5_8_7_9: Choice_2_5_8 + Choice_2_7_9 <= 1
DifferentPair_2_5_9_3_8: Choice_2_3_8 + Choice_2_5_9 <= 1
DifferentPair_2_5_9_4_7: Choice_2_4_7 + Choice_2_5_9 <= 1
DifferentPair_2_5_9_6_7: Choice_2_5_9 + Choice_2_6_7 <= 1
DifferentPair_2_5_9_7_8: Choice_2_5_9 + Choice_2_7_8 <= 1
DifferentPair_2_6_1_4_2: Choice_2_4_2 + Choice_2_6_1 <= 1
DifferentPair_2_6_1_5_3: Choice_2_5_3 + Choice_2_6_1 <= 1
DifferentPair_2_6_1_7_3: Choice_2_6_1 + Choice_2_7_3 <= 1
DifferentPair_2_6_1_8_2: Choice_2_6_1 + Choice_2_8_2 <= 1
DifferentPair_2_6_2_4_1: Choice_2_4_1 + Choice_2_6_2 <= 1
DifferentPair_2_6_2_4_3: Choice_2_4_3 + Choice_2_6_2 <= 1
DifferentPair_2_6_2_5_4: Choice_2_5_4 + Choice_2_6_2 <= 1
DifferentPair_2_6_2_7_4: Choice_2_6_2 + Choice_2_7_4 <= 1
DifferentPair_2_6_2_8_1: Choice_2_6_2 + Choice_2_8_1 <= 1
DifferentPair_2_6_2_8_3: Choice_2_6_2 + Choice_2_8_3 <= 1
DifferentPair_2_6_3_4_2: Choice_2_4_2 + Choice_2_6_3 <= 1
DifferentPair_2_6_3_4_4: Choice_2_4_4 + Choice_2_6_3 <= 1
DifferentPair_2_6_3_5_1: Choice_2_5_1 + Choice_2_6_3 <= 1
DifferentPair_2_6_3_5_5: Choice_2_5_5 + Choice_2_6_3 <= 1
DifferentPair_2_6_3_7_1: Choice_2_6_3 + Choice_2_7_1 <= 1
DifferentPair_2_6_3_7_5: Choice_2_6_3 + Choice_2_7_5 <= 1
DifferentPair_2_6_3_8_2: Choice_2_6_3 + Choice_2_8_2 <= 1
DifferentPair_2_6_3_8_4: Choice_2_6_3 + Choice_2_8_4 <= 1
DifferentPair_2_6_4_4_3: Choice_2_4_3 + Choice_2_6_4 <= 1
DifferentPair_2_6_4_4_5: Choice_2_4_5 + Choice_2_6_4 <= 1
DifferentPair_2_6_4_5_2: Choice_2_5_2 + Choice_2_6_4 <= 1
DifferentPair_2_6_4_5_6: Choice_2_5_6 + Choice_2_6_4 <= 1
DifferentPair_2_6_4_7_2: Choice_2_6_4 + Choice_2_7_2 <= 1
DifferentPair_2_6_4_7_6: Choice_2_6_4 + Choice_2_7_6 <= 1
DifferentPair_2_6_4_8_3: Choice_2_6_4 + Choice_2_8_3 <= 1
DifferentPair_2_6_4_8_5: Choice_2_6_4 + Choice_2_8_5 <= 1
DifferentPair_2_6_5_4_4: Choice_2_4_4 + Choice_2_6_5 <= 1
DifferentPair_2_6_5_4_6: Choice_2_4_6 + Choice_2_6_5 <= 1
DifferentPair_2_6_5_5_3: Choice_2_5_3 + Choice_2_6_5 <= 1
DifferentPair_2_6_5_5_7: Choice_2_5_7 + Choice_2_6_5 <= 1
DifferentPair_2_6_5_7_3: Choice_2_6_5 + Choice_2_7_3 <= 1
DifferentPair_2_6_5_7_7: Choice_2_6_5 + Choice_2_7_7 <= 1
DifferentPair_2_6_5_8_4: Choice_2_6_5 + Choice_2_8_4 <= 1
DifferentPair_2_6_5_8_6: Choice_2_6_5 + Choice_2_8_6 <= 1
DifferentPair_2_6_6_4_5: Choice_2_4_5 + Choice_2_6_6 <= 1
DifferentPair_2_6_6_4_7: Choice_2_4_7 + Choice_2_6_6 <= 1
DifferentPair_2_6_6_5_4: Choice_2_5_4 + Choice_2_6_6 <= 1
DifferentPair_2_6_6_5_8: Choice_2_5_8 + Choice_2_6_6 <= 1
DifferentPair_2_6_6_7_4: Choice_2_6_6 + Choice_2_7_4 <= 1
DifferentPair_2_6_6_7_8: Choice_2_6_6 + Choice_2_7_8 <= 1
DifferentPair_2_6_6_8_5: Choice_2_6_6 + Choice_2_8_5 <= 1
DifferentPair_2_6_6_8_7: Choice_2_6_6 + Choice_2_8_7 <= 1
DifferentPair_2_6_7_4_6: Choice_2_4_6 + Choice_2_6_7 <= 1
DifferentPair_2_6_7_4_8: Choice_2_4_8 + Choice_2_6_7 <= 1
DifferentPair_2_6_7_5_5: Choice_2_5_5 + Choice_2_6_7 <= 1
DifferentPair_2_6_7_5_9: Choice_2_5_9 + Choice_2_6_7 <= 1
DifferentPair_2_6_7_7_5: Choice_2_6_7 + Choice_2_7_5 <= 1
DifferentPair_2_6_7_7_9: Choice_2_6_7 + Choice_2_7_9 <= 1
DifferentPair_2_6_7_8_6: Choice_2_6_7 + Choice_2_8_6 <= 1
DifferentPair_2_6_7_8_8: Choice_2_6_7 + Choice_2_8_8 <= 1
DifferentPair_2_6_8_4_7: Choice_2_4_7 + Choice_2_6_8 <= 1
DifferentPair_2_6_8_4_9: Choice_2_4_9 + Choice_2_6_8 <= 1
DifferentPair_2_6_8_5_6: Choice_2_5_6 + Choice_2_6_8 <= 1
DifferentPair_2_6_8_7_6: Choice_2_6_8 + Choice_2_7_6 <= 1
DifferentPair_2_6_8_8_7: Choice_2_6_8 + Choice_2_8_7 <= 1
DifferentPair_2_6_8_8_9: Choice_2_6_8 + Choice_2_8_9 <= 1
DifferentPair_2_6_9_4_8: Choice_2_4_8 + Choice_2_6_9 <= 1
DifferentPair_2_6_9_5_7: Choice_2_5_7 + Choice_2_6_9 <= 1
DifferentPair_2_6_9_7_7: Choice_2_6_9 + Choice_2_7_7 <= 1
DifferentPair_2_6_9_8_8: Choice_2_6_9 + Choice_2_8_8 <= 1
DifferentPair_2_7_1_5_2: Choice_2_5_2 + Choice_2_7_1 <= 1
DifferentPair_2_7_1_6_3: Choice_2_6_3 + Choice_2_7_1 <= 1
DifferentPair_2_7_1_8_3: Choice_2_7_1 + Choice_2_8_3 <= 1
DifferentPair_2_7_1_9_2: Choice_2_7_1 + Choice_2_9_2 <= 1
DifferentPair_2_7_2_5_1: Choice_2_5_1 + Choice_2_7_2 <= 1
DifferentPair_2_7_2_5_3: Choice_2_5_3 + Choice_2_7_2 <= 1
DifferentPair_2_7_2_6_4: Choice_2_6_4 + Choice_2_7_2 <= 1
DifferentPair_2_7_2_8_4: Choice_2_7_2 + Choice_2_8_4 <= 1
DifferentPair_2_7_2_9_1: Choice_2_7_2 + Choice_2_9_1 <= 1
DifferentPair_2_7_2_9_3: Choice_2_7_2 + Choice_2_9_3 <= 1
DifferentPair_2_7_3_5_2: Choice_2_5_2 + Choice_2_7_3 <= 1
DifferentPair_2_7_3_5_4: Choice_2_5_4 + Choice_2_7_3 <= 1
DifferentPair_2_7_3_6_1: Choice_2_6_1 + Choice_2_7_3 <= 1
DifferentPair_2_7_3_6_5: Choice_2_6_5 + Choice_2_7_3 <= 1
DifferentPair_2_7_3_8_1: Choice_2_7_3 + Choice_2_8_1 <= 1
DifferentPair_2_7_3_8_5: Choice_2_7_3 + Choice_2_8_5 <= 1
DifferentPair_2_7_3_9_2: Choice_2_7_3 + Choice_2_9_2 <= 1
DifferentPair_2_7_3_9_4: Choice_2_7_3 + Choice_2_9_4 <= 1
DifferentPair_2_7_4_5_3: Choice_2_5_3 + Choice_2_7_4 <= 1
DifferentPair_2_7_4_5_5: Choice_2_5_5 + Choice_2_7_4 <= 1
DifferentPair_2_7_4_6_2: Choice_2_6_2 + Choice_2_7_4 <= 1
DifferentPair_2_7_4_6_6: Choice_2_6_6 + Choice_2_7_4 <= 1
DifferentPair_2_7_4_8_2: Choice_2_7_4 + Choice_2_8_2 <= 1
DifferentPair_2_7_4_8_6: Choice_2_7_4 + Choice_2_8_6 <= 1
DifferentPair_2_7_4_9_3: Choice_2_7_4 + Choice_2_9_3 <= 1
DifferentPair_2_7_4_9_5: Choice_2_7_4 + Choice_2_9_5 <= 1
DifferentPair_2_7_5_5_4: Choice_2_5_4 + Choice_2_7_5 <= 1
DifferentPair_2_7_5_5_6: Choice_2_5_6 + Choice_2_7_5 <= 1
DifferentPair_2_7_5_6_3: Choice_2_6_3 + Choice_2_7_5 <= 1
DifferentPair_2_7_5_6_7: Choice_2_6_7 + Choice_2_7_5 <= 1
DifferentPair_2_7_5_8_3: Choice_2_7_5 + Choice_2_8_3 <= 1
DifferentPair_2_7_5_8_7: Choice_2_7_5 + Choice_2_8_7 <= 1
DifferentPair_2_7_5_9_4: Choice_2_7_5 + Choice_2_9_4 <= 1
DifferentPair_2_7_5_9_6: Choice_2_7_5 + Choice_2_9_6 <= 1
DifferentPair_2_7_6_5_5: Choice_2_5_5 + Choice_2_7_6 <= 1
DifferentPair_2_7_6_5_7: Choice_2_5_7 + Choice_2_7_6 <= 1
DifferentPair_2_7_6_6_4: Choice_2_6_4 + Choice_2_7_6 <= 1
DifferentPair_2_7_6_6_8: Choice_2_6_8 + Choice_2_7_6 <= 1
DifferentPair_2_7_6_8_4: Choice_2_7_6 + Choice_2_8_4 <= 1
DifferentPair_2_7_6_8_8: Choice_2_7_6 + Choice_2_8_8 <= 1
DifferentPair_2_7_6_9_5: Choice_2_7_6 + Choice_2_9_5 <= 1
DifferentPair_2_7_6_9_7: Choice_2_7_6 + Choice_2_9_7 <= 1
DifferentPair_2_7_7_5_6: Choice_2_5_6 + Choice_2_7_7 <= 1
DifferentPair_2_7_7_5_8: Choice_2_5_8 + Choice_2_7_7 <= 1
DifferentPair_2_7_7_6_5: Choice_2_6_5 + Choice_2_7_7 <= 1
DifferentPair_2_7_7_6_9: Choice_2_6_9 + Choice_2_7_7 <= 1
DifferentPair_2_7_7_8_5: Choice_2_7_7 + Choice_2_8_5 <= 1
DifferentPair_2_7_7_8_9: Choice_2_7_7 + Choice_2_8_9 <= 1
DifferentPair_2_7_7_9_6: Choice_2_7_7 + Choice_2_9_6 <= 1
DifferentPair_2_7_7_9_8: Choice_2_7_7 + Choice_2_9_8 <= 1
DifferentPair_2_7_8_5_7: Choice_2_5_7 + Choice_2_7_8 <= 1
DifferentPair_2_7_8_5_9: Choice_2_5_9 + Choice_2_7_8 <= 1
DifferentPair_2_7_8_6_6: Choice_2_6_6 + Choice_2_7_8 <= 1
DifferentPair_2_7_8_8_6: Choice_2_7_8 + Choice_2_8_6 <= 1
DifferentPair_2_7_8_9_7: Choice_2_7_8 + Choice_2_9_7 <= 1
DifferentPair_2_7_8_9_9: Choice_2_7_8 + Choice_2_9_9 <= 1
DifferentPair_2_7_9_5_8: Choice_2_5_8 + Choice_2_7_9 <= 1
DifferentPair_2_7_9_6_7: Choice_2_6_7 + Choice_2_7_9 <= 1
DifferentPair_2_7_9_8_7: Choice_2_7_9 + Choice_2_8_7 <= 1
DifferentPair_2_7_9_9_8: Choice_2_7_9 + Choice_2_9_8 <= 1
DifferentPair_2_8_1_6_2: Choice_2_6_2 + Choice_2_8_1 <= 1
DifferentPair_2_8_1_7_3: Choice_2_7_3 + Choice_2_8_1 <= 1
DifferentPair_2_8_1_9_3: Choice_2_8_1 + Choice_2_9_3 <= 1
DifferentPair_2_8_2_6_1: Choice_2_6_1 + Choice_2_8_2 <= 1
DifferentPair_2_8_2_6_3: Choice_2_6_3 + Choice_2_8_2 <= 1
DifferentPair_2_8_2_7_4: Choice_2_7_4 + Choice_2_8_2 <= 1
DifferentPair_2_8_2_9_4: Choice_2_8_2 + Choice_2_9_4 <= 1
DifferentPair_2_8_3_6_2: Choice_2_6_2 + Choice_2_8_3 <= 1
DifferentPair_2_8_3_6_4: Choice_2_6_4 + Choice_2_8_3 <= 1
DifferentPair_2_8_3_7_1: Choice_2_7_1 + Choice_2_8_3 <= 1
DifferentPair_2_8_3_7_5: Choice_2_7_5 + Choice_2_8_3 <= 1
DifferentPair_2_8_3_9_1: Choice_2_8_3 + Choice_2_9_1 <= 1
DifferentPair_2_8_3_9_5: Choice_2_8_3 + Choice_2_9_5 <= 1
DifferentPair_2_8_4_6_3: Choice_2_6_3 + Choice_2_8_4 <= 1
DifferentPair_2_8_4_6_5: Choice_2_6_5 + Choice_2_8_4 <= 1
DifferentPair_2_8_4_7_2: Choice_2_7_2 + Choice_2_8_4 <= 1
DifferentPair_2_8_4_7_6: Choice_2_7_6 + Choice_2_8_4 <= 1
DifferentPair_2_8_4_9_2: Choice_2_8_4 + Choice_2_9_2 <= 1
DifferentPair_2_8_4_9_6: Choice_2_8_4 + Choice_2_9_6 <= 1
DifferentPair_2_8_5_6_4: Choice_2_6_4 + Choice_2_8_5 <= 1
DifferentPair_2_8_5_6_6: Choice_2_6_6 + Choice_2_8_5 <= 1
DifferentPair_2_8_5_7_3: Choice_2_7_3 + Choice_2_8_5 <= 1
DifferentPair_2_8_5_7_7: Choice_2_7_7 + Choice_2_8_5 <= 1
DifferentPair_2_8_5_9_3: Choice_2_8_5 + Choice_2_9_3 <= 1
DifferentPair_2_8_5_9_7: Choice_2_8_5 + Choice_2_9_7 <= 1
DifferentPair_2_8_6_6_5: Choice_2_6_5 + Choice_2_8_6 <= 1
DifferentPair_2_8_6_6_7: Choice_2_6_7 + Choice_2_8_6 <= 1
DifferentPair_2_8_6_7_4: Choice_2_7_4 + Choice_2_8_6 <= 1
DifferentPair_2_8_6_7_8: Choice_2_7_8 + Choice_2_8_6 <= 1
DifferentPair_2_8_6_9_4: Choice_2_8_6 + Choice_2_9_4 <= 1
DifferentPair_2_8_6_9_8: Choice_2_8_6 + Choice_2_9_8 <= 1
DifferentPair_2_8_7_6_6: Choice_2_6_6 + Choice_2_8_7 <= 1
DifferentPair_2_8_7_6_8: Choice_2_6_8 + Choice_2_8_7 <= 1
DifferentPair_2_8_7_7_5: Choice_2_7_5 + Choice_2_8_7 <= 1
DifferentPair_2_8_7_7_9: Choice_2_7_9 + Choice_2_8_7 <= 1
DifferentPair_2_8_7_9_5: Choice_2_8_7 + Choice_2_9_5 <= 1
DifferentPair_2_8_7_9_9: Choice_2_8_7 + Choice_2_9_9 <= 1
DifferentPair_2_8_8_6_7: Choice_2_6_7 + Choice_2_8_8 <= 1
DifferentPair_2_8_8_6_9: Choice_2_6_9 + Choice_2_8_8 <= 1
DifferentPair_2_8_8_7_6: Choice_2_7_6 + Choice_2_8_8 <= 1
DifferentPair_2_8_8_9_6: Choice_2_8_8 + Choice_2_9_6 <= 1
DifferentPair_2_8_9_6_8: Choice_2_6_8 + Choice_2_8_9 <= 1
DifferentPair_2_8_9_7_7: Choice_2_7_7 + Choice_2_8_9 <= 1
DifferentPair_2_8_9_9_7: Choice_2_8_9 + Choice_2_9_7 <= 1
DifferentPair_2_9_1_7_2: Choice_2_7_2 + Choice_2_9_1 <= 1
DifferentPair_2_9_1_8_3: Choice_2_8_3 + Choice_2_9_1 <= 1
DifferentPair_2_9_2_7_1: Choice_2_7_1 + Choice_2_9_2 <= 1
DifferentPair_2_9_2_7_3: Choice_2_7_3 + Choice_2_9_2 <= 1
DifferentPair_2_9_2_8_4: Choice_2_8_4 + Choice_2_9_2 <= 1
DifferentPair_2_9_3_7_2: Choice_2_7_2 + Choice_2_9_3 <= 1
DifferentPair_2_9_3_7_4: Choice_2_7_4 + Choice_2_9_3 <= 1
DifferentPair_2_9_3_8_1: Choice_2_8_1 + Choice_2_9_3 <= 1
DifferentPair_2_9_3_8_5: Choice_2_8_5 + Choice_2_9_3 <= 1
DifferentPair_2_9_4_7_3: Choice_2_7_3 + Choice_2_9_4 <= 1
DifferentPair_2_9_4_7_5: Choice_2_7_5 + Choice_2_9_4 <= 1
DifferentPair_2_9_4_8_2: Choice_2_8_2 + Choice_2_9_4 <= 1
DifferentPair_2_9_4_8_6: Choice_2_8_6 + Choice_2_9_4 <= 1
DifferentPair_2_9_5_7_4: Choice_2_7_4 + Choice_2_9_5 <= 1
DifferentPair_2_9_5_7_6: Choice_2_7_6 + Choice_2_9_5 <= 1
DifferentPair_2_9_5_8_3: Choice_2_8_3 + Choice_2_9_5 <= 1
DifferentPair_2_9_5_8_7: Choice_2_8_7 + Choice_2_9_5 <= 1
DifferentPair_2_9_6_7_5: Choice_2_7_5 + Choice_2_9_6 <= 1
DifferentPair_2_9_6_7_7: Choice_2_7_7 + Choice_2_9_6 <= 1
DifferentPair_2_9_6_8_4: Choice_2_8_4 + Choice_2_9_6 <= 1
DifferentPair_2_9_6_8_8: Choice_2_8_8 + Choice_2_9_6 <= 1
DifferentPair_2_9_7_7_6: Choice_2_7_6 + Choice_2_9_7 <= 1
DifferentPair_2_9_7_7_8: Choice_2_7_8 + Choice_2_9_7 <= 1
DifferentPair_2_9_7_8_5: Choice_2_8_5 + Choice_2_9_7 <= 1
DifferentPair_2_9_7_8_9: Choice_2_8_9 + Choice_2_9_7 <= 1
DifferentPair_2_9_8_7_7: Choice_2_7_7 + Choice_2_9_8 <= 1
DifferentPair_2_9_8_7_9: Choice_2_7_9 + Choice_2_9_8 <= 1
DifferentPair_2_9_8_8_6: Choice_2_8_6 + Choice_2_9_8 <= 1
DifferentPair_2_9_9_7_8: Choice_2_7_8 + Choice_2_9_9 <= 1
DifferentPair_2_9_9_8_7: Choice_2_8_7 + Choice_2_9_9 <= 1
DifferentPair_3_1_1_2_3: Choice_3_1_1 + Choice_3_2_3 <= 1
DifferentPair_3_1_1_3_2: Choice_3_1_1 + Choice_3_3_2 <= 1
DifferentPair_3_1_2_2_4: Choice_3_1_2 + Choice_3_2_4 <= 1
DifferentPair_3_1_2_3_1: Choice_3_1_2 + Choice_3_3_1 <= 1
DifferentPair_3_1_2_3_3: Choice_3_1_2 + Choice_3_3_3 <= 1
DifferentPair_3_1_3_2_1: Choice_3_1_3 + Choice_3_2_1 <= 1
DifferentPair_3_1_3_2_5: Choice_3_1_3 + Choice_3_2_5 <= 1
DifferentPair_3_1_3_3_2: Choice_3_1_3 + Choice_3_3_2 <= 1
DifferentPair_3_1_3_3_4: Choice_3_1_3 + Choice_3_3_4 <= 1
DifferentPair_3_1_4_2_2: Choice_3_1_4 + Choice_3_2_2 <= 1
DifferentPair_3_1_4_2_6: Choice_3_1_4 + Choice_3_2_6 <= 1
DifferentPair_3_1_4_3_3: Choice_3_1_4 + Choice_3_3_3 <= 1
DifferentPair_3_1_4_3_5: Choice_3_1_4 + Choice_3_3_5 <= 1
DifferentPair_3_1_5_2_3: Choice_3_1_5 + Choice_3_2_3 <= 1
DifferentPair_3_1_5_2_7: Choice_3_1_5 + Choice_3_2_7 <= 1
DifferentPair_3_1_5_3_4: Choice_3_1_5 + Choice_3_3_4 <= 1
DifferentPair_3_1_5_3_6: Choice_3_1_5 + Choice_3_3_6 <= 1
DifferentPair_3_1_6_2_4: Choice_3_1_6 + Choice_3_2_4 <= 1
DifferentPair_3_1_6_2_8: Choice_3_1_6 + Choice_3_2_8 <= 1
DifferentPair_3_1_6_3_5: Choice_3_1_6 + Choice_3_3_5 <= 1
DifferentPair_3_1_6_3_7: Choice_3_1_6 + Choice_3_3_7 <= 1
DifferentPair_3_1_7_2_5: Choice_3_1_7 + Choice_3_2_5 <= 1
DifferentPair_3_1_7_2_9: Choice_3_1_7 + Choice_3_2_9 <= 1
DifferentPair_3_1_7_3_6: Choice_3_1_7 + Choice_3_3_6 <= 1
DifferentPair_3_1_7_3_8: Choice_3_1_7 + Choice_3_3_8 <= 1
DifferentPair_3_1_8_2_6: Choice_3_1_8 + Choice_3_2_6 <= 1
DifferentPair_3_1_8_3_7: Choice_3_1_8 + Choice_3_3_7 <= 1
DifferentPair_3_1_8_3_9: Choice_3_1_8 + Choice_3_3_9 <= 1
DifferentPair_3_1_9_2_7: Choice_3_1_9 + Choice_3_2_7 <= 1
DifferentPair_3_1_9_3_8: Choice_3_1_9 + Choice_3_3_8 <= 1
DifferentPair_3_2_1_1_3: Choice_3_1_3 + Choice_3_2_1 <= 1
DifferentPair_3_2_1_3_3: Choice_3_2_1 + Choice_3_3_3 <= 1
DifferentPair_3_2_1_4_2: Choice_3_2_1 + Choice_3_4_2 <= 1
DifferentPair_3_2_2_1_4: Choice_3_1_4 + Choice_3_2_2 <= 1
DifferentPair_3_2_2_3_4: Choice_3_2_2 + Choice_3_3_4 <= 1
DifferentPair_3_2_2_4_1: Choice_3_2_2 + Choice_3_4_1 <= 1
DifferentPair_3_2_2_4_3: Choice_3_2_2 + Choice_3_4_3 <= 1
DifferentPair_3_2_3_1_1: Choice_3_1_1 + Choice_3_2_3 <= 1
DifferentPair_3_2_3_1_5: Choice_3_1_5 + Choice_3_2_3 <= 1
DifferentPair_3_2_3_3_1: Choice_3_2_3 + Choice_3_3_1 <= 1
DifferentPair_3_2_3_3_5: Choice_3_2_3 + Choice_3_3_5 <= 1
DifferentPair_3_2_3_4_2: Choice_3_2_3 + Choice_3_4_2 <= 1
DifferentPair_3_2_3_4_4: Choice_3_2_3 + Choice_3_4_4 <= 1
DifferentPair_3_2_4_1_2: Choice_3_1_2 + Choice_3_2_4 <= 1
DifferentPair_3_2_4_1_6: Choice_3_1_6 + Choice_3_2_4 <= 1
DifferentPair_3_2_4_3_2: Choice_3_2_4 + Choice_3_3_2 <= 1
DifferentPair_3_2_4_3_6: Choice_3_2_4 + Choice_3_3_6 <= 1
DifferentPair_3_2_4_4_3: Choice_3_2_4 + Choice_3_4_3 <= 1
DifferentPair_3_2_4_4_5: Choice_3_2_4 + Choice_3_4_5 <= 1
DifferentPair_3_2_5_1_3: Choice_3_1_3 + Choice_3_2_5 <= 1
DifferentPair_3_2_5_1_7: Choice_3_1_7 + Choice_3_2_5 <= 1
DifferentPair_3_2_5_3_3: Choice_3_2_5 + Choice_3_3_3 <= 1
DifferentPair_3_2_5_3_7: Choice_3_2_5 + Choice_3_3_7 <= 1
DifferentPair_3_2_5_4_4: Choice_3_2_5 + Choice_3_4_4 <= 1
DifferentPair_3_2_5_4_6: Choice_3_2_5 + Choice_3_4_6 <= 1
DifferentPair_3_2_6_1_4: Choice_3_1_4 + Choice_3_2_6 <= 1
DifferentPair_3_2_6_1_8: Choice_3_1_8 + Choice_3_2_6 <= 1
DifferentPair_3_2_6_3_4: Choice_3_2_6 + Choice_3_3_4 <= 1
DifferentPair_3_2_6_3_8: Choice_3_2_6 + Choice_3_3_8 <= 1
DifferentPair_3_2_6_4_5: Choice_3_2_6 + Choice_3_4_5 <= 1
DifferentPair_3_2_6_4_7: Choice_3_2_6 + Choice_3_4_7 <= 1
DifferentPair_3_2_7_1_5: Choice_3_1_5 + Choice_3_2_7 <= 1
DifferentPair_3_2_7_1_9: Choice_3_1_9 + Choice_3_2_7 <= 1
DifferentPair_3_2_7_3_5: Choice_3_2_7 + Choice_3_3_5 <= 1
DifferentPair_3_2_7_3_9: Choice_3_2_7 + Choice_3_3_9 <= 1
DifferentPair_3_2_7_4_6: Choice_3_2_7 + Choice_3_4_6 <= 1
DifferentPair_3_2_7_4_8: Choice_3_2_7 + Choice_3_4_8 <= 1
DifferentPair_3_2_8_1_6: Choice_3_1_6 + Choice_3_2_8 <= 1
DifferentPair_3_2_8_3_6: Choice_3_2_8 + Choice_3_3_6 <= 1
DifferentPair_3_2_8_4_7: Choice_3_2_8 + Choice_3_4_7 <= 1
DifferentPair_3_2_8_4_9: Choice_3_2_8 + Choice_3_4_9 <= 1
DifferentPair_3_2_9_1_7: Choice_3_1_7 + Choice_3_2_9 <= 1
DifferentPair_3_2_9_3_7: Choice_3_2_9 + Choice_3_3_7 <= 1
DifferentPair_3_2_9_4_8: Choice_3_2_9 + Choice_3_4_8 <= 1
DifferentPair_3_3_1_1_2: Choice_3_1_2 + Choice_3_3_1 <= 1
DifferentPair_3_3_1_2_3: Choice_3_2_3 + Choice_3_3_1 <= 1
DifferentPair_3_3_1_4_3: Choice_3_3_1 + Choice_3_4_3 <= 1
DifferentPair_3_3_1_5_2: Choice_3_3_1 + Choice_3_5_2 <= 1
DifferentPair_3_3_2_1_1: Choice_3_1_1 + Choice_3_3_2 <= 1
DifferentPair_3_3_2_1_3: Choice_3_1_3 + Choice_3_3_2 <= 1
DifferentPair_3_3_2_2_4: Choice_3_2_4 + Choice_3_3_2 <= 1
DifferentPair_3_3_2_4_4: Choice_3_3_2 + Choice_3_4_4 <= 1
DifferentPair_3_3_2_5_1: Choice_3_3_2 + Choice_3_5_1 <= 1
DifferentPair_3_3_2_5_3: Choice_3_3_2 + Choice_3_5_3 <= 1
DifferentPair_3_3_3_1_2: Choice_3_1_2 + Choice_3_3_3 <= 1
DifferentPair_3_3_3_1_4: Choice_3_1_4 + Choice_3_3_3 <= 1
DifferentPair_3_3_3_2_1: Choice_3_2_1 + Choice_3_3_3 <= 1
DifferentPair_3_3_3_2_5: Choice_3_2_5 + Choice_3_3_3 <= 1
DifferentPair_3_3_3_4_1: Choice_3_3_3 + Choice_3_4_1 <= 1
DifferentPair_3_3_3_4_5: Choice_3_3_3 + Choice_3_4_5 <= 1
DifferentPair_3_3_3_5_2: Choice_3_3_3 + Choice_3_5_2 <= 1
DifferentPair_3_3_3_5_4: Choice_3_3_3 + Choice_3_5_4 <= 1
DifferentPair_3_3_4_1_3: Choice_3_1_3 + Choice_3_3_4 <= 1
DifferentPair_3_3_4_1_5: Choice_3_1_5 + Choice_3_3_4 <= 1
DifferentPair_3_3_4_2_2: Choice_3_2_2 + Choice_3_3_4 <= 1
DifferentPair_3_3_4_2_6: Choice_3_2_6 + Choice_3_3_4 <= 1
DifferentPair_3_3_4_4_2: Choice_3_3_4 + Choice_3_4_2 <= 1
DifferentPair_3_3_4_4_6: Choice_3_3_4 + Choice_3_4_6 <= 1
DifferentPair_3_3_4_5_3: Choice_3_3_4 + Choice_3_5_3 <= 1
DifferentPair_3_3_4_5_5: Choice_3_3_4 + Choice_3_5_5 <= 1
DifferentPair_3_3_5_1_4: Choice_3_1_4 + Choice_3_3_5 <= 1
DifferentPair_3_3_5_1_6: Choice_3_1_6 + Choice_3_3_5 <= 1
DifferentPair_3_3_5_2_3: Choice_3_2_3 + Choice_3_3_5 <= 1
DifferentPair_3_3_5_2_7: Choice_3_2_7 + Choice_3_3_5 <= 1
DifferentPair_3_3_5_4_3: Choice_3_3_5 + Choice_3_4_3 <= 1
DifferentPair_3_3_5_4_7: Choice_3_3_5 + Choice_3_4_7 <= 1
DifferentPair_3_3_5_5_4: Choice_3_3_5 + Choice_3_5_4 <= 1
DifferentPair_3_3_5_5_6: Choice_3_3_5 + Choice_3_5_6 <= 1
DifferentPair_3_3_6_1_5: Choice_3_1_5 + Choice_3_3_6 <= 1
DifferentPair_3_3_6_1_7: Choice_3_1_7 + Choice_3_3_6 <= 1
DifferentPair_3_3_6_2_4: Choice_3_2_4 + Choice_3_3_6 <= 1
DifferentPair_3_3_6_2_8: Choice_3_2_8 + Choice_3_3_6 <= 1
DifferentPair_3_3_6_4_4: Choice_3_3_6 + Choice_3_4_4 <= 1
DifferentPair_3_3_6_4_8: Choice_3_3_6 + Choice_3_4_8 <= 1
DifferentPair_3_3_6_5_5: Choice_3_3_6 + Choice_3_5_5 <= 1
DifferentPair_3_3_6_5_7: Choice_3_3_6 + Choice_3_5_7 <= 1
DifferentPair_3_3_7_1_6: Choice_3_1_6 + Choice_3_3_7 <= 1
DifferentPair_3_3_7_1_8: Choice_3_1_8 + Choice_3_3_7 <= 1
DifferentPair_3_3_7_2_5: Choice_3_2_5 + Choice_3_3_7 <= 1
DifferentPair_3_3_7_2_9: Choice_3_2_9 + Choice_3_3_7 <= 1
DifferentPair_3_3_7_4_5: Choice_3_3_7 + Choice_3_4_5 <= 1
DifferentPair_3_3_7_4_9: Choice_3_3_7 + Choice_3_4_9 <= 1
DifferentPair_3_3_7_5_6: Choice_3_3_7 + Choice_3_5_6 <= 1
DifferentPair_3_3_7_5_8: Choice_3_3_7 + Choice_3_5_8 <= 1
DifferentPair_3_3_8_1_7: Choice_3_1_7 + Choice_3_3_8 <= 1
DifferentPair_3_3_8_1_9: Choice_3_1_9 + Choice_3_3_8 <= 1
DifferentPair_3_3_8_2_6: Choice_3_2_6 + Choice_3_3_8 <= 1
DifferentPair_3_3_8_4_6: Choice_3_3_8 + Choice_3_4_6 <= 1
DifferentPair_3_3_8_5_7: Choice_3_3_8 + Choice_3_5_7 <= 1
DifferentPair_3_3_8_5_9: Choice_3_3_8 + Choice_3_5_9 <= 1
DifferentPair_3_3_9_1_8: Choice_3_1_8 + Choice_3_3_9 <= 1
DifferentPair_3_3_9_2_7: Choice_3_2_7 + Choice_3_3_9 <= 1
DifferentPair_3_3_9_4_7: Choice_3_3_9 + Choice_3_4_7 <= 1
DifferentPair_3_3_9_5_8: Choice_3_3_9 + Choice_3_5_8 <= 1
DifferentPair_3_4_1_2_2: Choice_3_2_2 + Choice_3_4_1 <= 1
DifferentPair_3_4_1_3_3: Choice_3_3_3 + Choice_3_4_1 <= 1
DifferentPair_3_4_1_5_3: Choice_3_4_1 + Choice_3_5_3 <= 1
DifferentPair_3_4_1_6_2: Choice_3_4_1 + Choice_3_6_2 <= 1
DifferentPair_3_4_2_2_1: Choice_3_2_1 + Choice_3_4_2 <= 1
DifferentPair_3_4_2_2_3: Choice_3_2_3 + Choice_3_4_2 <= 1
DifferentPair_3_4_2_3_4: Choice_3_3_4 + Choice_3_4_2 <= 1
DifferentPair_3_4_2_5_4: Choice_3_4_2 + Choice_3_5_4 <= 1
DifferentPair_3_4_2_6_1: Choice_3_4_2 + Choice_3_6_1 <= 1
DifferentPair_3_4_2_6_3: Choice_3_4_2 + Choice_3_6_3 <= 1
DifferentPair_3_4_3_2_2: Choice_3_2_2 + Choice_3_4_3 <= 1
DifferentPair_3_4_3_2_4: Choice_3_2_4 + Choice_3_4_3 <= 1
DifferentPair_3_4_3_3_1: Choice_3_3_1 + Choice_3_4_3 <= 1
DifferentPair_3_4_3_3_5: Choice_3_3_5 + Choice_3_4_3 <= 1
DifferentPair_3_4_3_5_1: Choice_3_4_3 + Choice_3_5_1 <= 1
DifferentPair_3_4_3_5_5: Choice_3_4_3 + Choice_3_5_5 <= 1
DifferentPair_3_4_3_6_2: Choice_3_4_3 + Choice_3_6_2 <= 1
DifferentPair_3_4_3_6_4: Choice_3_4_3 + Choice_3_6_4 <= 1
DifferentPair_3_4_4_2_3: Choice_3_2_3 + Choice_3_4_4 <= 1
DifferentPair_3_4_4_2_5: Choice_3_2_5 + Choice_3_4_4 <= 1
DifferentPair_3_4_4_3_2: Choice_3_3_2 + Choice_3_4_4 <= 1
DifferentPair_3_4_4_3_6: Choice_3_3_6 + Choice_3_4_4 <= 1
DifferentPair_3_4_4_5_2: Choice_3_4_4 + Choice_3_5_2 <= 1
DifferentPair_3_4_4_5_6: Choice_3_4_4 + Choice_3_5_6 <= 1
DifferentPair_3_4_4_6_3: Choice_3_4_4 + Choice_3_6_3 <= 1
DifferentPair_3_4_4_6_5: Choice_3_4_4 + Choice_3_6_5 <= 1
DifferentPair_3_4_5_2_4: Choice_3_2_4 + Choice_3_4_5 <= 1
DifferentPair_3_4_5_2_6: Choice_3_2_6 + Choice_3_4_5 <= 1
DifferentPair_3_4_5_3_3: Choice_3_3_3 + Choice_3_4_5 <= 1
DifferentPair_3_4_5_3_7: Choice_3_3_7 + Choice_3_4_5 <= 1
DifferentPair_3_4_5_5_3: Choice_3_4_5 + Choice_3_5_3 <= 1
DifferentPair_3_4_5_5_7: Choice_3_4_5 + Choice_3_5_7 <= 1
DifferentPair_3_4_5_6_4: Choice_3_4_5 + Choice_3_6_4 <= 1
DifferentPair_3_4_5_6_6: Choice_3_4_5 + Choice_3_6_6 <= 1
DifferentPair_3_4_6_2_5: Choice_3_2_5 + Choice_3_4_6 <= 1
DifferentPair_3_4_6_2_7: Choice_3_2_7 + Choice_3_4_6 <= 1
DifferentPair_3_4_6_3_4: Choice_3_3_4 + Choice_3_4_6 <= 1
DifferentPair_3_4_6_3_8: Choice_3_3_8 + Choice_3_4_6 <= 1
DifferentPair_3_4_6_5_4: Choice_3_4_6 + Choice_3_5_4 <= 1
DifferentPair_3_4_6_5_8: Choice_3_4_6 + Choice_3_5_8 <= 1
DifferentPair_3_4_6_6_5: Choice_3_4_6 + Choice_3_6_5 <= 1
DifferentPair_3_4_6_6_7: Choice_3_4_6 + Choice_3_6_7 <= 1
DifferentPair_3_4_7_2_6: Choice_3_2_6 + Choice_3_4_7 <= 1
DifferentPair_3_4_7_2_8: Choice_3_2_8 + Choice_3_4_7 <= 1
DifferentPair_3_4_7_3_5: Choice_3_3_5 + Choice_3_4_7 <= 1
DifferentPair_3_4_7_3_9: Choice_3_3_9 + Choice_3_4_7 <= 1
DifferentPair_3_4_7_5_5: Choice_3_4_7 + Choice_3_5_5 <= 1
DifferentPair_3_4_7_5_9: Choice_3_4_7 + Choice_3_5_9 <= 1
DifferentPair_3_4_7_6_6: Choice_3_4_7 + Choice_3_6_6 <= 1
DifferentPair_3_4_7_6_8: Choice_3_4_7 + Choice_3_6_8 <= 1
DifferentPair_3_4_8_2_7: Choice_3_2_7 + Choice_3_4_8 <= 1
DifferentPair_3_4_8_2_9: Choice_3_2_9 + Choice_3_4_8 <= 1
DifferentPair_3_4_8_3_6: Choice_3_3_6 + Choice_3_4_8 <= 1
DifferentPair_3_4_8_5_6: Choice_3_4_8 + Choice_3_5_6 <= 1
DifferentPair_3_4_8_6_7: Choice_3_4_8 + Choice_3_6_7 <= 1
DifferentPair_3_4_8_6_9: Choice_3_4_8 + Choice_3_6_9 <= 1
DifferentPair_3_4_9_2_8: Choice_3_2_8 + Choice_3_4_9 <= 1
DifferentPair_3_4_9_3_7: Choice_3_3_7 + Choice_3_4_9 <= 1
DifferentPair_3_4_9_5_7: Choice_3_4_9 + Choice_3_5_7 <= 1
DifferentPair_3_4_9_6_8: Choice_3_4_9 + Choice_3_6_8 <= 1
DifferentPair_3_5_1_3_2: Choice_3_3_2 + Choice_3_5_1 <= 1
DifferentPair_3_5_1_4_3: Choice_3_4_3 + Choice_3_5_1 <= 1
DifferentPair_3_5_1_6_3: Choice_3_5_1 + Choice_3_6_3 <= 1
DifferentPair_3_5_1_7_2: Choice_3_5_1 + Choice_3_7_2 <= 1
DifferentPair_3_5_2_3_1: Choice_3_3_1 + Choice_3_5_2 <= 1
DifferentPair_3_5_2_3_3: Choice_3_3_3 + Choice_3_5_2 <= 1
DifferentPair_3_5_2_4_4: Choice_3_4_4 + Choice_3_5_2 <= 1
DifferentPair_3_5_2_6_4: Choice_3_5_2 + Choice_3_6_4 <= 1
DifferentPair_3_5_2_7_1: Choice_3_5_2 + Choice_3_7_1 <= 1
DifferentPair_3_5_2_7_3: Choice_3_5_2 + Choice_3_7_3 <= 1
DifferentPair_3_5_3_3_2: Choice_3_3_2 + Choice_3_5_3 <= 1
DifferentPair_3_5_3_3_4: Choice_3_3_4 + Choice_3_5_3 <= 1
DifferentPair_3_5_3_4_1: Choice_3_4_1 + Choice_3_5_3 <= 1
DifferentPair_3_5_3_4_5: Choice_3_4_5 + Choice_3_5_3 <= 1
DifferentPair_3_5_3_6_1: Choice_3_5_3 + Choice_3_6_1 <= 1
DifferentPair_3_5_3_6_5: Choice_3_5_3 + Choice_3_6_5 <= 1
DifferentPair_3_5_3_7_2: Choice_3_5_3 + Choice_3_7_2 <= 1
DifferentPair_3_5_3_7_4: Choice_3_5_3 + Choice_3_7_4 <= 1
DifferentPair_3_5_4_3_3: Choice_3_3_3 + Choice_3_5_4 <= 1
DifferentPair_3_5_4_3_5: Choice_3_3_5 + Choice_3_5_4 <= 1
DifferentPair_3_5_4_4_2: Choice_3_4_2 + Choice_3_5_4 <= 1
DifferentPair_3_5_4_4_6: Choice_3_4_6 + Choice_3_5_4 <= 1
DifferentPair_3_5_4_6_2: Choice_3_5_4 + Choice_3_6_2 <= 1
DifferentPair_3_5_4_6_6: Choice_3_5_4 + Choice_3_6_6 <= 1
DifferentPair_3_5_4_7_3: Choice_3_5_4 + Choice_3_7_3 <= 1
DifferentPair_3_5_4_7_5: Choice_3_5_4 + Choice_3_7_5 <= 1
DifferentPair_3_5_5_3_4: Choice_3_3_4 + Choice_3_5_5 <= 1
DifferentPair_3_5_5_3_6: Choice_3_3_6 + Choice_3_5_5 <= 1
DifferentPair_3_5_5_4_3: Choice_3_4_3 + Choice_3_5_5 <= 1
DifferentPair_3_5_5_4_7: Choice_3_4_7 + Choice_3_5_5 <= 1
DifferentPair_3_5_5_6_3: Choice_3_5_5 + Choice_3_6_3 <= 1
DifferentPair_3_5_5_6_7: Choice_3_5_5 + Choice_3_6_7 <= 1
DifferentPair_3_5_5_7_4: Choice_3_5_5 + Choice_3_7_4 <= 1
DifferentPair_3_5_5_7_6: Choice_3_5_5 + Choice_3_7_6 <= 1
DifferentPair_3_5_6_3_5: Choice_3_3_5 + Choice_3_5_6 <= 1
DifferentPair_3_5_6_3_7: Choice_3_3_7 + Choice_3_5_6 <= 1
DifferentPair_3_5_6_4_4: Choice_3_4_4 + Choice_3_5_6 <= 1
DifferentPair_3_5_6_4_8: Choice_3_4_8 + Choice_3_5_6 <= 1
DifferentPair_3_5_6_6_4: Choice_3_5_6 + Choice_3_6_4 <= 1
DifferentPair_3_5_6_6_8: Choice_3_5_6 + Choice_3_6_8 <= 1
DifferentPair_3_5_6_7_5: Choice_3_5_6 + Choice_3_7_5 <= 1
DifferentPair_3_5_6_7_7: Choice_3_5_6 + Choice_3_7_7 <= 1
DifferentPair_3_5_7_3_6: Choice_3_3_6 + Choice_3_5_7 <= 1
DifferentPair_3_5_7_3_8: Choice_3_3_8 + Choice_3_5_7 <= 1
DifferentPair_3_5_7_4_5: Choice_3_4_5 + Choice_3_5_7 <= 1
DifferentPair_3_5_7_4_9: Choice_3_4_9 + Choice_3_5_7 <= 1
DifferentPair_3_5_7_6_5: Choice_3_5_7 + Choice_3_6_5 <= 1
DifferentPair_3_5_7_6_9: Choice_3_5_7 + Choice_3_6_9 <= 1
DifferentPair_3_5_7_7_6: Choice_3_5_7 + Choice_3_7_6 <= 1
DifferentPair_3_5_7_7_8: Choice_3_5_7 + Choice_3_7_8 <= 1
DifferentPair_3_5_8_3_7: Choice_3_3_7 + Choice_3_5_8 <= 1
DifferentPair_3_5_8_3_9: Choice_3_3_9 + Choice_3_5_8 <= 1
DifferentPair_3_5_8_4_6: Choice_3_4_6 + Choice_3_5_8 <= 1
DifferentPair_3_5_8_6_6: Choice_3_5_8 + Choice_3_6_6 <= 1
DifferentPair_3_5_8_7_7: Choice_3_5_8 + Choice_3_7_7 <= 1
DifferentPair_3_5_8_7_9: Choice_3_5_8 + Choice_3_7_9 <= 1
DifferentPair_3_5_9_3_8: Choice_3_3_8 + Choice_3_5_9 <= 1
DifferentPair_3_5_9_4_7: Choice_3_4_7 + Choice_3_5_9 <= 1
DifferentPair_3_5_9_6_7: Choice_3_5_9 + Choice_3_6_7 <= 1
DifferentPair_3_5_9_7_8: Choice_3_5_9 + Choice_3_7_8 <= 1
DifferentPair_3_6_1_4_2: Choice_3_4_2 + Choice_3_6_1 <= 1
DifferentPair_3_6_1_5_3: Choice_3_5_3 + Choice_3_6_1 <= 1
DifferentPair_3_6_1_7_3: Choice_3_6_1 + Choice_3_7_3 <= 1
DifferentPair_3_6_1_8_2: Choice_3_6_1 + Choice_3_8_2 <= 1
DifferentPair_3_6_2_4_1: Choice_3_4_1 + Choice_3_6_2 <= 1
DifferentPair_3_6_2_4_3: Choice_3_4_3 + Choice_3_6_2 <= 1
DifferentPair_3_6_2_5_4: Choice_3_5_4 + Choice_3_6_2 <= 1
DifferentPair_3_6_2_7_4: Choice_3_6_2 + Choice_3_7_4 <= 1
DifferentPair_3_6_2_8_1: Choice_3_6_2 + Choice_3_8_1 <= 1
DifferentPair_3_6_2_8_3: Choice_3_6_2 + Choice_3_8_3 <= 1
DifferentPair_3_6_3_4_2: Choice_3_4_2 + Choice_3_6_3 <= 1
DifferentPair_3_6_3_4_4: Choice_3_4_4 + Choice_3_6_3 <= 1
DifferentPair_3_6_3_5_1: Choice_3_5_1 + Choice_3_6_3 <= 1
DifferentPair_3_6_3_5_5: Choice_3_5_5 + Choice_3_6_3 <= 1
DifferentPair_3_6_3_7_1: Choice_3_6_3 + Choice_3_7_1 <= 1
DifferentPair_3_6_3_7_5: Choice_3_6_3 + Choice_3_7_5 <= 1
DifferentPair_3_6_3_8_2: Choice_3_6_3 + Choice_3_8_2 <= 1
DifferentPair_3_6_3_8_4: Choice_3_6_3 + Choice_3_8_4 <= 1
DifferentPair_3_6_4_4_3: Choice_3_4_3 + Choice_3_6_4 <= 1
DifferentPair_3_6_4_4_5: Choice_3_4_5 + Choice_3_6_4 <= 1
DifferentPair_3_6_4_5_2: Choice_3_5_2 + Choice_3_6_4 <= 1
DifferentPair_3_6_4_5_6: Choice_3_5_6 + Choice_3_6_4 <= 1
DifferentPair_3_6_4_7_2: Choice_3_6_4 + Choice_3_7_2 <= 1
DifferentPair_3_6_4_7_6: Choice_3_6_4 + Choice_3_7_6 <= 1
DifferentPair_3_6_4_8_3: Choice_3_6_4 + Choice_3_8_3 <= 1
DifferentPair_3_6_4_8_5: Choice_3_6_4 + Choice_3_8_5 <= 1
DifferentPair_3_6_5_4_4: Choice_3_4_4 + Choice_3_6_5 <= 1
DifferentPair_3_6_5_4_6: Choice_3_4_6 + Choice_3_6_5 <= 1
DifferentPair_3_6_5_5_3: Choice_3_5_3 + Choice_3_6_5 <= 1
DifferentPair_3_6_5_5_7: Choice_3_5_7 + Choice_3_6_5 <= 1
DifferentPair_3_6_5_7_3: Choice_3_6_5 + Choice_3_7_3 <= 1
DifferentPair_3_6_5_7_7: Choice_3_6_5 + Choice_3_7_7 <= 1
DifferentPair_3_6_5_8_4: Choice_3_6_5 + Choice_3_8_4 <= 1
DifferentPair_3_6_5_8_6: Choice_3_6_5 + Choice_3_8_6 <= 1
DifferentPair_3_6_6_4_5: Choice_3_4_5 + Choice_3_6_6 <= 1
DifferentPair_3_6_6_4_7: Choice_3_4_7 + Choice_3_6_6 <= 1
DifferentPair_3_6_6_5_4: Choice_3_5_4 + Choice_3_6_6 <= 1
DifferentPair_3_6_6_5_8: Choice_3_5_8 + Choice_3_6_6 <= 1
DifferentPair_3_6_6_7_4: Choice_3_6_6 + Choice_3_7_4 <= 1
DifferentPair_3_6_6_7_8: Choice_3_6_6 + Choice_3_7_8 <= 1
DifferentPair_3_6_6_8_5: Choice_3_6_6 + Choice_3_8_5 <= 1
DifferentPair_3_6_6_8_7: Choice_3_6_6 + Choice_3_8_7 <= 1
DifferentPair_3_6_7_4_6: Choice_3_4_6 + Choice_3_6_7 <= 1
DifferentPair_3_6_7_4_8: Choice_3_4_8 + Choice_3_6_7 <= 1
DifferentPair_3_6_7_5_5: Choice_3_5_5 + Choice_3_6_7 <= 1
DifferentPair_3_6_7_5_9: Choice_3_5_9 + Choice_3_6_7 <= 1
DifferentPair_3_6_7_7_5: Choice_3_6_7 + Choice_3_7_5 <= 1
DifferentPair_3_6_7_7_9: Choice_3_6_7 + Choice_3_7_9 <= 1
DifferentPair_3_6_7_8_6: Choice_3_6_7 + Choice_3_8_6 <= 1
DifferentPair_3_6_7_8_8: Choice_3_6_7 + Choice_3_8_8 <= 1
DifferentPair_3_6_8_4_7: Choice_3_4_7 + Choice_3_6_8 <= 1
DifferentPair_3_6_8_4_9: Choice_3_4_9 + Choice_3_6_8 <= 1
DifferentPair_3_6_8_5_6: Choice_3_5_6 + Choice_3_6_8 <= 1
DifferentPair_3_6_8_7_6: Choice_3_6_8 + Choice_3_7_6 <= 1
DifferentPair_3_6_8_8_7: Choice_3_6_8 + Choice_3_8_7 <= 1
DifferentPair_3_6_8_8_9: Choice_3_6_8 + Choice_3_8_9 <= 1
DifferentPair_3_6_9_4_8: Choice_3_4_8 + Choice_3_6_9 <= 1
DifferentPair_3_6_9_5_7: Choice_3_5_7 + Choice_3_6_9 <= 1
DifferentPair_3_6_9_7_7: Choice_3_6_9 + Choice_3_7_7 <= 1
DifferentPair_3_6_9_8_8: Choice_3_6_9 + Choice_3_8_8 <= 1
DifferentPair_3_7_1_5_2: Choice_3_5_2 + Choice_3_7_1 <= 1
DifferentPair_3_7_1_6_3: Choice_3_6_3 + Choice_3_7_1 <= 1
DifferentPair_3_7_1_8_3: Choice_3_7_1 + Choice_3_8_3 <= 1
DifferentPair_3_7_1_9_2: Choice_3_7_1 + Choice_3_9_2 <= 1
DifferentPair_3_7_2_5_1: Choice_3_5_1 + Choice_3_7_2 <= 1
DifferentPair_3_7_2_5_3: Choice_3_5_3 + Choice_3_7_2 <= 1
DifferentPair_3_7_2_6_4: Choice_3_6_4 + Choice_3_7_2 <= 1
DifferentPair_3_7_2_8_4: Choice_3_7_2 + Choice_3_8_4 <= 1
DifferentPair_3_7_2_9_1: Choice_3_7_2 + Choice_3_9_1 <= 1
DifferentPair_3_7_2_9_3: Choice_3_7_2 + Choice_3_9_3 <= 1
DifferentPair_3_7_3_5_2: Choice_3_5_2 + Choice_3_7_3 <= 1
DifferentPair_3_7_3_5_4: Choice_3_5_4 + Choice_3_7_3 <= 1
DifferentPair_3_7_3_6_1: Choice_3_6_1 + Choice_3_7_3 <= 1
DifferentPair_3_7_3_6_5: Choice_3_6_5 + Choice_3_7_3 <= 1
DifferentPair_3_7_3_8_1: Choice_3_7_3 + Choice_3_8_1 <= 1
DifferentPair_3_7_3_8_5: Choice_3_7_3 + Choice_3_8_5 <= 1
DifferentPair_3_7_3_9_2: Choice_3_7_3 + Choice_3_9_2 <= 1
DifferentPair_3_7_3_9_4: Choice_3_7_3 + Choice_3_9_4 <= 1
DifferentPair_3_7_4_5_3: Choice_3_5_3 + Choice_3_7_4 <= 1
DifferentPair_3_7_4_5_5: Choice_3_5_5 + Choice_3_7_4 <= 1
DifferentPair_3_7_4_6_2: Choice_3_6_2 + Choice_3_7_4 <= 1
DifferentPair_3_7_4_6_6: Choice_3_6_6 + Choice_3_7_4 <= 1
DifferentPair_3_7_4_8_2: Choice_3_7_4 + Choice_3_8_2 <= 1
DifferentPair_3_7_4_8_6: Choice_3_7_4 + Choice_3_8_6 <= 1
DifferentPair_3_7_4_9_3: Choice_3_7_4 + Choice_3_9_3 <= 1
DifferentPair_3_7_4_9_5: Choice_3_7_4 + Choice_3_9_5 <= 1
DifferentPair_3_7_5_5_4: Choice_3_5_4 + Choice_3_7_5 <= 1
DifferentPair_3_7_5_5_6: Choice_3_5_6 + Choice_3_7_5 <= 1
DifferentPair_3_7_5_6_3: Choice_3_6_3 + Choice_3_7_5 <= 1
DifferentPair_3_7_5_6_7: Choice_3_6_7 + Choice_3_7_5 <= 1
DifferentPair_3_7_5_8_3: Choice_3_7_5 + Choice_3_8_3 <= 1
DifferentPair_3_7_5_8_7: Choice_3_7_5 + Choice_3_8_7 <= 1
DifferentPair_3_7_5_9_4: Choice_3_7_5 + Choice_3_9_4 <= 1
DifferentPair_3_7_5_9_6: Choice_3_7_5 + Choice_3_9_6 <= 1
DifferentPair_3_7_6_5_5: Choice_3_5_5 + Choice_3_7_6 <= 1
DifferentPair_3_7_6_5_7: Choice_3_5_7 + Choice_3_7_6 <= 1
DifferentPair_3_7_6_6_4: Choice_3_6_4 + Choice_3_7_6 <= 1
DifferentPair_3_7_6_6_8: Choice_3_6_8 + Choice_3_7_6 <= 1
DifferentPair_3_7_6_8_4: Choice_3_7_6 + Choice_3_8_4 <= 1
DifferentPair_3_7_6_8_8: Choice_3_7_6 + Choice_3_8_8 <= 1
DifferentPair_3_7_6_9_5: Choice_3_7_6 + Choice_3_9_5 <= 1
DifferentPair_3_7_6_9_7: Choice_3_7_6 + Choice_3_9_7 <= 1
DifferentPair_3_7_7_5_6: Choice_3_5_6 + Choice_3_7_7 <= 1
DifferentPair_3_7_7_5_8: Choice_3_5_8 + Choice_3_7_7 <= 1
DifferentPair_3_7_7_6_5: Choice_3_6_5 + Choice_3_7_7 <= 1
DifferentPair_3_7_7_6_9: Choice_3_6_9 + Choice_3_7_7 <= 1
DifferentPair_3_7_7_8_5: Choice_3_7_7 + Choice_3_8_5 <= 1
DifferentPair_3_7_7_8_9: Choice_3_7_7 + Choice_3_8_9 <= 1
DifferentPair_3_7_7_9_6: Choice_3_7_7 + Choice_3_9_6 <= 1
DifferentPair_3_7_7_9_8: Choice_3_7_7 + Choice_3_9_8 <= 1
DifferentPair_3_7_8_5_7: Choice_3_5_7 + Choice_3_7_8 <= 1
DifferentPair_3_7_8_5_9: Choice_3_5_9 + Choice_3_7_8 <= 1
DifferentPair_3_7_8_6_6: Choice_3_6_6 + Choice_3_7_8 <= 1
DifferentPair_3_7_8_8_6: Choice_3_7_8 + Choice_3_8_6 <= 1
DifferentPair_3_7_8_9_7: Choice_3_7_8 + Choice_3_9_7 <= 1
DifferentPair_3_7_8_9_9: Choice_3_7_8 + Choice_3_9_9 <= 1
DifferentPair_3_7_9_5_8: Choice_3_5_8 + Choice_3_7_9 <= 1
DifferentPair_3_7_9_6_7: Choice_3_6_7 + Choice_3_7_9 <= 1
DifferentPair_3_7_9_8_7: Choice_3_7_9 + Choice_3_8_7 <= 1
DifferentPair_3_7_9_9_8: Choice_3_7_9 + Choice_3_9_8 <= 1
DifferentPair_3_8_1_6_2: Choice_3_6_2 + Choice_3_8_1 <= 1
DifferentPair_3_8_1_7_3: Choice_3_7_3 + Choice_3_8_1 <= 1
DifferentPair_3_8_1_9_3: Choice_3_8_1 + Choice_3_9_3 <= 1
DifferentPair_3_8_2_6_1: Choice_3_6_1 + Choice_3_8_2 <= 1
DifferentPair_3_8_2_6_3: Choice_3_6_3 + Choice_3_8_2 <= 1
DifferentPair_3_8_2_7_4: Choice_3_7_4 + Choice_3_8_2 <= 1
DifferentPair_3_8_2_9_4: Choice_3_8_2 + Choice_3_9_4 <= 1
DifferentPair_3_8_3_6_2: Choice_3_6_2 + Choice_3_8_3 <= 1
DifferentPair_3_8_3_6_4: Choice_3_6_4 + Choice_3_8_3 <= 1
DifferentPair_3_8_3_7_1: Choice_3_7_1 + Choice_3_8_3 <= 1
DifferentPair_3_8_3_7_5: Choice_3_7_5 + Choice_3_8_3 <= 1
DifferentPair_3_8_3_9_1: Choice_3_8_3 + Choice_3_9_1 <= 1
DifferentPair_3_8_3_9_5: Choice_3_8_3 + Choice_3_9_5 <= 1
DifferentPair_3_8_4_6_3: Choice_3_6_3 + Choice_3_8_4 <= 1
DifferentPair_3_8_4_6_5: Choice_3_6_5 + Choice_3_8_4 <= 1
DifferentPair_3_8_4_7_2: Choice_3_7_2 + Choice_3_8_4 <= 1
DifferentPair_3_8_4_7_6: Choice_3_7_6 + Choice_3_8_4 <= 1
DifferentPair_3_8_4_9_2: Choice_3_8_4 + Choice_3_9_2 <= 1
DifferentPair_3_8_4_9_6: Choice_3_8_4 + Choice_3_9_6 <= 1
DifferentPair_3_8_5_6_4: Choice_3_6_4 + Choice_3_8_5 <= 1
DifferentPair_3_8_5_6_6: Choice_3_6_6 + Choice_3_8_5 <= 1
DifferentPair_3_8_5_7_3: Choice_3_7_3 + Choice_3_8_5 <= 1
DifferentPair_3_8_5_7_7: Choice_3_7_7 + Choice_3_8_5 <= 1
DifferentPair_3_8_5_9_3: Choice_3_8_5 + Choice_3_9_3 <= 1
DifferentPair_3_8_5_9_7: Choice_3_8_5 + Choice_3_9_7 <= 1
DifferentPair_3_8_6_6_5: Choice_3_6_5 + Choice_3_8_6 <= 1
DifferentPair_3_8_6_6_7: Choice_3_6_7 + Choice_3_8_6 <= 1
DifferentPair_3_8_6_7_4: Choice_3_7_4 + Choice_3_8_6 <= 1
DifferentPair_3_8_6_7_8: Choice_3_7_8 + Choice_3_8_6 <= 1
DifferentPair_3_8_6_9_4: Choice_3_8_6 + Choice_3_9_4 <= 1
DifferentPair_3_8_6_9_8: Choice_3_8_6 + Choice_3_9_8 <= 1
DifferentPair_3_8_7_6_6: Choice_3_6_6 + Choice_3_8_7 <= 1
DifferentPair_3_8_7_6_8: Choice_3_6_8 + Choice_3_8_7 <= 1
DifferentPair_3_8_7_7_5: Choice_3_7_5 + Choice_3_8_7 <= 1
DifferentPair_3_8_7_7_9: Choice_3_7_9 + Choice_3_8_7 <= 1
DifferentPair_3_8_7_9_5: Choice_3_8_7 + Choice_3_9_5 <= 1
DifferentPair_3_8_7_9_9: Choice_3_8_7 + Choice_3_9_9 <= 1
DifferentPair_3_8_8_6_7: Choice_3_6_7 + Choice_3_8_8 <= 1
DifferentPair_3_8_8_6_9: Choice_3_6_9 + Choice_3_8_8 <= 1
DifferentPair_3_8_8_7_6: Choice_3_7_6 + Choice_3_8_8 <= 1
DifferentPair_3_8_8_9_6: Choice_3_8_8 + Choice_3_9_6 <= 1
DifferentPair_3_8_9_6_8: Choice_3_6_8 + Choice_3_8_9 <= 1
DifferentPair_3_8_9_7_7: Choice_3_7_7 + Choice_3_8_9 <= 1
DifferentPair_3_8_9_9_7: Choice_3_8_9 + Choice_3_9_7 <= 1
DifferentPair_3_9_1_7_2: Choice_3_7_2 + Choice_3_9_1 <= 1
DifferentPair_3_9_1_8_3: Choice_3_8_3 + Choice_3_9_1 <= 1
DifferentPair_3_9_2_7_1: Choice_3_7_1 + Choice_3_9_2 <= 1
DifferentPair_3_9_2_7_3: Choice_3_7_3 + Choice_3_9_2 <= 1
DifferentPair_3_9_2_8_4: Choice_3_8_4 + Choice_3_9_2 <= 1
DifferentPair_3_9_3_7_2: Choice_3_7_2 + Choice_3_9_3 <= 1
DifferentPair_3_9_3_7_4: Choice_3_7_4 + Choice_3_9_3 <= 1
DifferentPair_3_9_3_8_1: Choice_3_8_1 + Choice_3_9_3 <= 1
DifferentPair_3_9_3_8_5: Choice_3_8_5 + Choice_3_9_3 <= 1
DifferentPair_3_9_4_7_3: Choice_3_7_3 + Choice_3_9_4 <= 1
DifferentPair_3_9_4_7_5: Choice_3_7_5 + Choice_3_9_4 <= 1
DifferentPair_3_9_4_8_2: Choice_3_8_2 + Choice_3_9_4 <= 1
DifferentPair_3_9_4_8_6: Choice_3_8_6 + Choice_3_9_4 <= 1
DifferentPair_3_9_5_7_4: Choice_3_7_4 + Choice_3_9_5 <= 1
DifferentPair_3_9_5_7_6: Choice_3_7_6 + Choice_3_9_5 <= 1
DifferentPair_3_9_5_8_3: Choice_3_8_3 + Choice_3_9_5 <= 1
DifferentPair_3_9_5_8_7: Choice_3_8_7 + Choice_3_9_5 <= 1
DifferentPair_3_9_6_7_5: Choice_3_7_5 + Choice_3_9_6 <= 1
DifferentPair_3_9_6_7_7: Choice_3_7_7 + Choice_3_9_6 <= 1
DifferentPair_3_9_6_8_4: Choice_3_8_4 + Choice_3_9_6 <= 1
DifferentPair_3_9_6_8_8: Choice_3_8_8 + Choice_3_9_6 <= 1
DifferentPair_3_9_7_7_6: Choice_3_7_6 + Choice_3_9_7 <= 1
DifferentPair_3_9_7_7_8: Choice_3_7_8 + Choice_3_9_7 <= 1
DifferentPair_3_9_7_8_5: Choice_3_8_5 + Choice_3_9_7 <= 1
DifferentPair_3_9_7_8_9: Choice_3_8_9 + Choice_3_9_7 <= 1
DifferentPair_3_9_8_7_7: Choice_3_7_7 + Choice_3_9_8 <= 1
DifferentPair_3_9_8_7_9: Choice_3_7_9 + Choice_3_9_8 <= 1
DifferentPair_3_9_8_8_6: Choice_3_8_6 + Choice_3_9_8 <= 1
DifferentPair_3_9_9_7_8: Choice_3_7_8 + Choice_3_9_9 <= 1
DifferentPair_3_9_9_8_7: Choice_3_8_7 + Choice_3_9_9 <= 1
DifferentPair_4_1_1_2_3: Choice_4_1_1 + Choice_4_2_3 <= 1
DifferentPair_4_1_1_3_2: Choice_4_1_1 + Choice_4_3_2 <= 1
DifferentPair_4_1_2_2_4: Choice_4_1_2 + Choice_4_2_4 <= 1
DifferentPair_4_1_2_3_1: Choice_4_1_2 + Choice_4_3_1 <= 1
DifferentPair_4_1_2_3_3: Choice_4_1_2 + Choice_4_3_3 <= 1
DifferentPair_4_1_3_2_1: Choice_4_1_3 + Choice_4_2_1 <= 1
DifferentPair_4_1_3_2_5: Choice_4_1_3 + Choice_4_2_5 <= 1
DifferentPair_4_1_3_3_2: Choice_4_1_3 + Choice_4_3_2 <= 1
DifferentPair_4_1_3_3_4: Choice_4_1_3 + Choice_4_3_4 <= 1
DifferentPair_4_1_4_2_2: Choice_4_1_4 + Choice_4_2_2 <= 1
DifferentPair_4_1_4_2_6: Choice_4_1_4 + Choice_4_2_6 <= 1
DifferentPair_4_1_4_3_3: Choice_4_1_4 + Choice_4_3_3 <= 1
DifferentPair_4_1_4_3_5: Choice_4_1_4 + Choice_4_3_5 <= 1
DifferentPair_4_1_5_2_3: Choice_4_1_5 + Choice_4_2_3 <= 1
DifferentPair_4_1_5_2_7: Choice_4_1_5 + Choice_4_2_7 <= 1
DifferentPair_4_1_5_3_4: Choice_4_1_5 + Choice_4_3_4 <= 1
DifferentPair_4_1_5_3_6: Choice_4_1_5 + Choice_4_3_6 <= 1
DifferentPair_4_1_6_2_4: Choice_4_1_6 + Choice_4_2_4 <= 1
DifferentPair_4_1_6_2_8: Choice_4_1_6 + Choice_4_2_8 <= 1
DifferentPair_4_1_6_3_5: Choice_4_1_6 + Choice_4_3_5 <= 1
DifferentPair_4_1_6_3_7: Choice_4_1_6 + Choice_4_3_7 <= 1
DifferentPair_4_1_7_2_5: Choice_4_1_7 + Choice_4_2_5 <= 1
DifferentPair_4_1_7_2_9: Choice_4_1_7 + Choice_4_2_9 <= 1
DifferentPair_4_1_7_3_6: Choice_4_1_7 + Choice_4_3_6 <= 1
DifferentPair_4_1_7_3_8: Choice_4_1_7 + Choice_4_3_8 <= 1
DifferentPair_4_1_8_2_6: Choice_4_1_8 + Choice_4_2_6 <= 1
DifferentPair_4_1_8_3_7: Choice_4_1_8 + Choice_4_3_7 <= 1
DifferentPair_4_1_8_3_9: Choice_4_1_8 + Choice_4_3_9 <= 1
DifferentPair_4_1_9_2_7: Choice_4_1_9 + Choice_4_2_7 <= 1
DifferentPair_4_1_9_3_8: Choice_4_1_9 + Choice_4_3_8 <= 1
DifferentPair_4_2_1_1_3: Choice_4_1_3 + Choice_4_2_1 <= 1
DifferentPair_4_2_1_3_3: Choice_4_2_1 + Choice_4_3_3 <= 1
DifferentPair_4_2_1_4_2: Choice_4_2_1 + Choice_4_4_2 <= 1
DifferentPair_4_2_2_1_4: Choice_4_1_4 + Choice_4_2_2 <= 1
DifferentPair_4_2_2_3_4: Choice_4_2_2 + Choice_4_3_4 <= 1
DifferentPair_4_2_2_4_1: Choice_4_2_2 + Choice_4_4_1 <= 1
DifferentPair_4_2_2_4_3: Choice_4_2_2 + Choice_4_4_3 <= 1
DifferentPair_4_2_3_1_1: Choice_4_1_1 + Choice_4_2_3 <= 1
DifferentPair_4_2_3_1_5: Choice_4_1_5 + Choice_4_2_3 <= 1
DifferentPair_4_2_3_3_1: Choice_4_2_3 + Choice_4_3_1 <= 1
DifferentPair_4_2_3_3_5: Choice_4_2_3 + Choice_4_3_5 <= 1
DifferentPair_4_2_3_4_2: Choice_4_2_3 + Choice_4_4_2 <= 1
DifferentPair_4_2_3_4_4: Choice_4_2_3 + Choice_4_4_4 <= 1
DifferentPair_4_2_4_1_2: Choice_4_1_2 + Choice_4_2_4 <= 1
DifferentPair_4_2_4_1_6: Choice_4_1_6 + Choice_4_2_4 <= 1
DifferentPair_4_2_4_3_2: Choice_4_2_4 + Choice_4_3_2 <= 1
DifferentPair_4_2_4_3_6: Choice_4_2_4 + Choice_4_3_6 <= 1
DifferentPair_4_2_4_4_3: Choice_4_2_4 + Choice_4_4_3 <= 1
DifferentPair_4_2_4_4_5: Choice_4_2_4 + Choice_4_4_5 <= 1
DifferentPair_4_2_5_1_3: Choice_4_1_3 + Choice_4_2_5 <= 1
DifferentPair_4_2_5_1_7: Choice_4_1_7 + Choice_4_2_5 <= 1
DifferentPair_4_2_5_3_3: Choice_4_2_5 + Choice_4_3_3 <= 1
DifferentPair_4_2_5_3_7: Choice_4_2_5 + Choice_4_3_7 <= 1
DifferentPair_4_2_5_4_4: Choice_4_2_5 + Choice_4_4_4 <= 1
DifferentPair_4_2_5_4_6: Choice_4_2_5 + Choice_4_4_6 <= 1
DifferentPair_4_2_6_1_4: Choice_4_1_4 + Choice_4_2_6 <= 1
DifferentPair_4_2_6_1_8: Choice_4_1_8 + Choice_4_2_6 <= 1
DifferentPair_4_2_6_3_4: Choice_4_2_6 + Choice_4_3_4 <= 1
DifferentPair_4_2_6_3_8: Choice_4_2_6 + Choice_4_3_8 <= 1
DifferentPair_4_2_6_4_5: Choice_4_2_6 + Choice_4_4_5 <= 1
DifferentPair_4_2_6_4_7: Choice_4_2_6 + Choice_4_4_7 <= 1
DifferentPair_4_2_7_1_5: Choice_4_1_5 + Choice_4_2_7 <= 1
DifferentPair_4_2_7_1_9: Choice_4_1_9 + Choice_4_2_7 <= 1
DifferentPair_4_2_7_3_5: Choice_4_2_7 + Choice_4_3_5 <= 1
DifferentPair_4_2_7_3_9: Choice_4_2_7 + Choice_4_3_9 <= 1
DifferentPair_4_2_7_4_6: Choice_4_2_7 + Choice_4_4_6 <= 1
DifferentPair_4_2_7_4_8: Choice_4_2_7 + Choice_4_4_8 <= 1
DifferentPair_4_2_8_1_6: Choice_4_1_6 + Choice_4_2_8 <= 1
DifferentPair_4_2_8_3_6: Choice_4_2_8 + Choice_4_3_6 <= 1
DifferentPair_4_2_8_4_7: Choice_4_2_8 + Choice_4_4_7 <= 1
DifferentPair_4_2_8_4_9: Choice_4_2_8 + Choice_4_4_9 <= 1
DifferentPair_4_2_9_1_7: Choice_4_1_7 + Choice_4_2_9 <= 1
DifferentPair_4_2_9_3_7: Choice_4_2_9 + Choice_4_3_7 <= 1
DifferentPair_4_2_9_4_8: Choice_4_2_9 + Choice_4_4_8 <= 1
DifferentPair_4_3_1_1_2: Choice_4_1_2 + Choice_4_3_1 <= 1
DifferentPair_4_3_1_2_3: Choice_4_2_3 + Choice_4_3_1 <= 1
DifferentPair_4_3_1_4_3: Choice_4_3_1 + Choice_4_4_3 <= 1
DifferentPair_4_3_1_5_2: Choice_4_3_1 + Choice_4_5_2 <= 1
DifferentPair_4_3_2_1_1: Choice_4_1_1 + Choice_4_3_2 <= 1
DifferentPair_4_3_2_1_3: Choice_4_1_3 + Choice_4_3_2 <= 1
DifferentPair_4_3_2_2_4: Choice_4_2_4 + Choice_4_3_2 <= 1
DifferentPair_4_3_2_4_4: Choice_4_3_2 + Choice_4_4_4 <= 1
DifferentPair_4_3_2_5_1: Choice_4_3_2 + Choice_4_5_1 <= 1
DifferentPair_4_3_2_5_3: Choice_4_3_2 + Choice_4_5_3 <= 1
DifferentPair_4_3_3_1_2: Choice_4_1_2 + Choice_4_3_3 <= 1
DifferentPair_4_3_3_1_4: Choice_4_1_4 + Choice_4_3_3 <= 1
DifferentPair_4_3_3_2_1: Choice_4_2_1 + Choice_4_3_3 <= 1
DifferentPair_4_3_3_2_5: Choice_4_2_5 + Choice_4_3_3 <= 1
DifferentPair_4_3_3_4_1: Choice_4_3_3 + Choice_4_4_1 <= 1
DifferentPair_4_3_3_4_5: Choice_4_3_3 + Choice_4_4_5 <= 1
DifferentPair_4_3_3_5_2: Choice_4_3_3 + Choice_4_5_2 <= 1
DifferentPair_4_3_3_5_4: Choice_4_3_3 + Choice_4_5_4 <= 1
DifferentPair_4_3_4_1_3: Choice_4_1_3 + Choice_4_3_4 <= 1
DifferentPair_4_3_4_1_5: Choice_4_1_5 + Choice_4_3_4 <= 1
DifferentPair_4_3_4_2_2: Choice_4_2_2 + Choice_4_3_4 <= 1
DifferentPair_4_3_4_2_6: Choice_4_2_6 + Choice_4_3_4 <= 1
DifferentPair_4_3_4_4_2: Choice_4_3_4 + Choice_4_4_2 <= 1
DifferentPair_4_3_4_4_6: Choice_4_3_4 + Choice_4_4_6 <= 1
DifferentPair_4_3_4_5_3: Choice_4_3_4 + Choice_4_5_3 <= 1
DifferentPair_4_3_4_5_5: Choice_4_3_4 + Choice_4_5_5 <= 1
DifferentPair_4_3_5_1_4: Choice_4_1_4 + Choice_4_3_5 <= 1
DifferentPair_4_3_5_1_6: Choice_4_1_6 + Choice_4_3_5 <= 1
DifferentPair_4_3_5_2_3: Choice_4_2_3 + Choice_4_3_5 <= 1
DifferentPair_4_3_5_2_7: Choice_4_2_7 + Choice_4_3_5 <= 1
DifferentPair_4_3_5_4_3: Choice_4_3_5 + Choice_4_4_3 <= 1
DifferentPair_4_3_5_4_7: Choice_4_3_5 + Choice_4_4_7 <= 1
DifferentPair_4_3_5_5_4: Choice_4_3_5 + Choice_4_5_4 <= 1
DifferentPair_4_3_5_5_6: Choice_4_3_5 + Choice_4_5_6 <= 1
DifferentPair_4_3_6_1_5: Choice_4_1_5 + Choice_4_3_6 <= 1
DifferentPair_4_3_6_1_7: Choice_4_1_7 + Choice_4_3_6 <= 1
DifferentPair_4_3_6_2_4: Choice_4_2_4 + Choice_4_3_6 <= 1
DifferentPair_4_3_6_2_8: Choice_4_2_8 + Choice_4_3_6 <= 1
DifferentPair_4_3_6_4_4: Choice_4_3_6 + Choice_4_4_4 <= 1
DifferentPair_4_3_6_4_8: Choice_4_3_6 + Choice_4_4_8 <= 1
DifferentPair_4_3_6_5_5: Choice_4_3_6 + Choice_4_5_5 <= 1
DifferentPair_4_3_6_5_7: Choice_4_3_6 + Choice_4_5_7 <= 1
DifferentPair_4_3_7_1_6: Choice_4_1_6 + Choice_4_3_7 <= 1
DifferentPair_4_3_7_1_8: Choice_4_1_8 + Choice_4_3_7 <= 1
DifferentPair_4_3_7_2_5: Choice_4_2_5 + Choice_4_3_7 <= 1
DifferentPair_4_3_7_2_9: Choice_4_2_9 + Choice_4_3_7 <= 1
DifferentPair_4_3_7_4_5: Choice_4_3_7 + Choice_4_4_5 <= 1
DifferentPair_4_3_7_4_9: Choice_4_3_7 + Choice_4_4_9 <= 1
DifferentPair_4_3_7_5_6: Choice_4_3_7 + Choice_4_5_6 <= 1
DifferentPair_4_3_7_5_8: Choice_4_3_7 + Choice_4_5_8 <= 1
DifferentPair_4_3_8_1_7: Choice_4_1_7 + Choice_4_3_8 <= 1
DifferentPair_4_3_8_1_9: Choice_4_1_9 + Choice_4_3_8 <= 1
DifferentPair_4_3_8_2_6: Choice_4_2_6 + Choice_4_3_8 <= 1
DifferentPair_4_3_8_4_6: Choice_4_3_8 + Choice_4_4_6 <= 1
DifferentPair_4_3_8_5_7: Choice_4_3_8 + Choice_4_5_7 <= 1
DifferentPair_4_3_8_5_9: Choice_4_3_8 + Choice_4_5_9 <= 1
DifferentPair_4_3_9_1_8: Choice_4_1_8 + Choice_4_3_9 <= 1
DifferentPair_4_3_9_2_7: Choice_4_2_7 + Choice_4_3_9 <= 1
DifferentPair_4_3_9_4_7: Choice_4_3_9 + Choice_4_4_7 <= 1
DifferentPair_4_3_9_5_8: Choice_4_3_9 + Choice_4_5_8 <= 1
DifferentPair_4_4_1_2_2: Choice_4_2_2 + Choice_4_4_1 <= 1
DifferentPair_4_4_1_3_3: Choice_4_3_3 + Choice_4_4_1 <= 1
DifferentPair_4_4_1_5_3: Choice_4_4_1 + Choice_4_5_3 <= 1
DifferentPair_4_4_1_6_2: Choice_4_4_1 + Choice_4_6_2 <= 1
DifferentPair_4_4_2_2_1: Choice_4_2_1 + Choice_4_4_2 <= 1
DifferentPair_4_4_2_2_3: Choice_4_2_3 + Choice_4_4_2 <= 1
DifferentPair_4_4_2_3_4: Choice_4_3_4 + Choice_4_4_2 <= 1
DifferentPair_4_4_2_5_4: Choice_4_4_2 + Choice_4_5_4 <= 1
DifferentPair_4_4_2_6_1: Choice_4_4_2 + Choice_4_6_1 <= 1
DifferentPair_4_4_2_6_3: Choice_4_4_2 + Choice_4_6_3 <= 1
DifferentPair_4_4_3_2_2: Choice_4_2_2 + Choice_4_4_3 <= 1
DifferentPair_4_4_3_2_4: Choice_4_2_4 + Choice_4_4_3 <= 1
DifferentPair_4_4_3_3_1: Choice_4_3_1 + Choice_4_4_3 <= 1
DifferentPair_4_4_3_3_5: Choice_4_3_5 + Choice_4_4_3 <= 1
DifferentPair_4_4_3_5_1: Choice_4_4_3 + Choice_4_5_1 <= 1
DifferentPair_4_4_3_5_5: Choice_4_4_3 + Choice_4_5_5 <= 1
DifferentPair_4_4_3_6_2: Choice_4_4_3 + Choice_4_6_2 <= 1
DifferentPair_4_4_3_6_4: Choice_4_4_3 + Choice_4_6_4 <= 1
DifferentPair_4_4_4_2_3: Choice_4_2_3 + Choice_4_4_4 <= 1
DifferentPair_4_4_4_2_5: Choice_4_2_5 + Choice_4_4_4 <= 1
DifferentPair_4_4_4_3_2: Choice_4_3_2 + Choice_4_4_4 <= 1
DifferentPair_4_4_4_3_6: Choice_4_3_6 + Choice_4_4_4 <= 1
DifferentPair_4_4_4_5_2: Choice_4_4_4 + Choice_4_5_2 <= 1
DifferentPair_4_4_4_5_6: Choice_4_4_4 + Choice_4_5_6 <= 1
DifferentPair_4_4_4_6_3: Choice_4_4_4 + Choice_4_6_3 <= 1
DifferentPair_4_4_4_6_5: Choice_4_4_4 + Choice_4_6_5 <= 1
DifferentPair_4_4_5_2_4: Choice_4_2_4 + Choice_4_4_5 <= 1
DifferentPair_4_4_5_2_6: Choice_4_2_6 + Choice_4_4_5 <= 1
DifferentPair_4_4_5_3_3: Choice_4_3_3 + Choice_4_4_5 <= 1
DifferentPair_4_4_5_3_7: Choice_4_3_7 + Choice_4_4_5 <= 1
DifferentPair_4_4_5_5_3: Choice_4_4_5 + Choice_4_5_3 <= 1
DifferentPair_4_4_5_5_7: Choice_4_4_5 + Choice_4_5_7 <= 1
DifferentPair_4_4_5_6_4: Choice_4_4_5 + Choice_4_6_4 <= 1
DifferentPair_4_4_5_6_6: Choice_4_4_5 + Choice_4_6_6 <= 1
DifferentPair_4_4_6_2_5: Choice_4_2_5 + Choice_4_4_6 <= 1
DifferentPair_4_4_6_2_7: Choice_4_2_7 + Choice_4_4_6 <= 1
DifferentPair_4_4_6_3_4: Choice_4_3_4 + Choice_4_4_6 <= 1
DifferentPair_4_4_6_3_8: Choice_4_3_8 + Choice_4_4_6 <= 1
DifferentPair_4_4_6_5_4: Choice_4_4_6 + Choice_4_5_4 <= 1
DifferentPair_4_4_6_5_8: Choice_4_4_6 + Choice_4_5_8 <= 1
DifferentPair_4_4_6_6_5: Choice_4_4_6 + Choice_4_6_5 <= 1
DifferentPair_4_4_6_6_7: Choice_4_4_6 + Choice_4_6_7 <= 1
DifferentPair_4_4_7_2_6: Choice_4_2_6 + Choice_4_4_7 <= 1
DifferentPair_4_4_7_2_8: Choice_4_2_8 + Choice_4_4_7 <= 1
DifferentPair_4_4_7_3_5: Choice_4_3_5 + Choice_4_4_7 <= 1
DifferentPair_4_4_7_3_9: Choice_4_3_9 + Choice_4_4_7 <= 1
DifferentPair_4_4_7_5_5: Choice_4_4_7 + Choice_4_5_5 <= 1
DifferentPair_4_4_7_5_9: Choice_4_4_7 + Choice_4_5_9 <= 1
DifferentPair_4_4_7_6_6: Choice_4_4_7 + Choice_4_6_6 <= 1
DifferentPair_4_4_7_6_8: Choice_4_4_7 + Choice_4_6_8 <= 1
DifferentPair_4_4_8_2_7: Choice_4_2_7 + Choice_4_4_8 <= 1
DifferentPair_4_4_8_2_9: Choice_4_2_9 + Choice_4_4_8 <= 1
DifferentPair_4_4_8_3_6: Choice_4_3_6 + Choice_4_4_8 <= 1
DifferentPair_4_4_8_5_6: Choice_4_4_8 + Choice_4_5_6 <= 1
DifferentPair_4_4_8_6_7: Choice_4_4_8 + Choice_4_6_7 <= 1
DifferentPair_4_4_8_6_9: Choice_4_4_8 + Choice_4_6_9 <= 1
DifferentPair_4_4_9_2_8: Choice_4_2_8 + Choice_4_4_9 <= 1
DifferentPair_4_4_9_3_7: Choice_4_3_7 + Choice_4_4_9 <= 1
DifferentPair_4_4_9_5_7: Choice_4_4_9 + Choice_4_5_7 <= 1
DifferentPair_4_4_9_6_8: Choice_4_4_9 + Choice_4_6_8 <= 1
DifferentPair_4_5_1_3_2: Choice_4_3_2 + Choice_4_5_1 <= 1
DifferentPair_4_5_1_4_3: Choice_4_4_3 + Choice_4_5_1 <= 1
DifferentPair_4_5_1_6_3: Choice_4_5_1 + Choice_4_6_3 <= 1
DifferentPair_4_5_1_7_2: Choice_4_5_1 + Choice_4_7_2 <= 1
DifferentPair_4_5_2_3_1: Choice_4_3_1 + Choice_4_5_2 <= 1
DifferentPair_4_5_2_3_3: Choice_4_3_3 + Choice_4_5_2 <= 1
DifferentPair_4_5_2_4_4: Choice_4_4_4 + Choice_4_5_2 <= 1
DifferentPair_4_5_2_6_4: Choice_4_5_2 + Choice_4_6_4 <= 1
DifferentPair_4_5_2_7_1: Choice_4_5_2 + Choice_4_7_1 <= 1
DifferentPair_4_5_2_7_3: Choice_4_5_2 + Choice_4_7_3 <= 1
DifferentPair_4_5_3_3_2: Choice_4_3_2 + Choice_4_5_3 <= 1
DifferentPair_4_5_3_3_4: Choice_4_3_4 + Choice_4_5_3 <= 1
DifferentPair_4_5_3_4_1: Choice_4_4_1 + Choice_4_5_3 <= 1
DifferentPair_4_5_3_4_5: Choice_4_4_5 + Choice_4_5_3 <= 1
DifferentPair_4_5_3_6_1: Choice_4_5_3 + Choice_4_6_1 <= 1
DifferentPair_4_5_3_6_5: Choice_4_5_3 + Choice_4_6_5 <= 1
DifferentPair_4_5_3_7_2: Choice_4_5_3 + Choice_4_7_2 <= 1
DifferentPair_4_5_3_7_4: Choice_4_5_3 + Choice_4_7_4 <= 1
DifferentPair_4_5_4_3_3: Choice_4_3_3 + Choice_4_5_4 <= 1
DifferentPair_4_5_4_3_5: Choice_4_3_5 + Choice_4_5_4 <= 1
DifferentPair_4_5_4_4_2: Choice_4_4_2 + Choice_4_5_4 <= 1
DifferentPair_4_5_4_4_6: Choice_4_4_6 + Choice_4_5_4 <= 1
DifferentPair_4_5_4_6_2: Choice_4_5_4 + Choice_4_6_2 <= 1
DifferentPair_4_5_4_6_6: Choice_4_5_4 + Choice_4_6_6 <= 1
DifferentPair_4_5_4_7_3: Choice_4_5_4 + Choice_4_7_3 <= 1
DifferentPair_4_5_4_7_5: Choice_4_5_4 + Choice_4_7_5 <= 1
DifferentPair_4_5_5_3_4: Choice_4_3_4 + Choice_4_5_5 <= 1
DifferentPair_4_5_5_3_6: Choice_4_3_6 + Choice_4_5_5 <= 1
DifferentPair_4_5_5_4_3: Choice_4_4_3 + Choice_4_5_5 <= 1
DifferentPair_4_5_5_4_7: Choice_4_4_7 + Choice_4_5_5 <= 1
DifferentPair_4_5_5_6_3: Choice_4_5_5 + Choice_4_6_3 <= 1
DifferentPair_4_5_5_6_7: Choice_4_5_5 + Choice_4_6_7 <= 1
DifferentPair_4_5_5_7_4: Choice_4_5_5 + Choice_4_7_4 <= 1
DifferentPair_4_5_5_7_6: Choice_4_5_5 + Choice_4_7_6 <= 1
DifferentPair_4_5_6_3_5: Choice_4_3_5 + Choice_4_5_6 <= 1
DifferentPair_4_5_6_3_7: Choice_4_3_7 + Choice_4_5_6 <= 1
DifferentPair_4_5_6_4_4: Choice_4_4_4 + Choice_4_5_6 <= 1
DifferentPair_4_5_6_4_8: Choice_4_4_8 + Choice_4_5_6 <= 1
DifferentPair_4_5_6_6_4: Choice_4_5_6 + Choice_4_6_4 <= 1
DifferentPair_4_5_6_6_8: Choice_4_5_6 + Choice_4_6_8 <= 1
DifferentPair_4_5_6_7_5: Choice_4_5_6 + Choice_4_7_5 <= 1
DifferentPair_4_5_6_7_7: Choice_4_5_6 + Choice_4_7_7 <= 1
DifferentPair_4_5_7_3_6: Choice_4_3_6 + Choice_4_5_7 <= 1
DifferentPair_4_5_7_3_8: Choice_4_3_8 + Choice_4_5_7 <= 1
DifferentPair_4_5_7_4_5: Choice_4_4_5 + Choice_4_5_7 <= 1
DifferentPair_4_5_7_4_9: Choice_4_4_9 + Choice_4_5_7 <= 1
DifferentPair_4_5_7_6_5: Choice_4_5_7 + Choice_4_6_5 <= 1
DifferentPair_4_5_7_6_9: Choice_4_5_7 + Choice_4_6_9 <= 1
DifferentPair_4_5_7_7_6: Choice_4_5_7 + Choice_4_7_6 <= 1
DifferentPair_4_5_7_7_8: Choice_4_5_7 + Choice_4_7_8 <= 1
DifferentPair_4_5_8_3_7: Choice_4_3_7 + Choice_4_5_8 <= 1
DifferentPair_4_5_8_3_9: Choice_4_3_9 + Choice_4_5_8 <= 1
DifferentPair_4_5_8_4_6: Choice_4_4_6 + Choice_4_5_8 <= 1
DifferentPair_4_5_8_6_6: Choice_4_5_8 + Choice_4_6_6 <= 1
DifferentPair_4_5_8_7_7: Choice_4_5_8 + Choice_4_7_7 <= 1
DifferentPair_4_5_8_7_9: Choice_4_5_8 + Choice_4_7_9 <= 1
DifferentPair_4_5_9_3_8: Choice_4_3_8 + Choice_4_5_9 <= 1
DifferentPair_4_5_9_4_7: Choice_4_4_7 + Choice_4_5_9 <= 1
DifferentPair_4_5_9_6_7: Choice_4_5_9 + Choice_4_6_7 <= 1
DifferentPair_4_5_9_7_8: Choice_4_5_9 + Choice_4_7_8 <= 1
DifferentPair_4_6_1_4_2: Choice_4_4_2 + Choice_4_6_1 <= 1
DifferentPair_4_6_1_5_3: Choice_4_5_3 + Choice_4_6_1 <= 1
DifferentPair_4_6_1_7_3: Choice_4_6_1 + Choice_4_7_3 <= 1
DifferentPair_4_6_1_8_2: Choice_4_6_1 + Choice_4_8_2 <= 1
DifferentPair_4_6_2_4_1: Choice_4_4_1 + Choice_4_6_2 <= 1
DifferentPair_4_6_2_4_3: Choice_4_4_3 + Choice_4_6_2 <= 1
DifferentPair_4_6_2_5_4: Choice_4_5_4 + Choice_4_6_2 <= 1
DifferentPair_4_6_2_7_4: Choice_4_6_2 + Choice_4_7_4 <= 1
DifferentPair_4_6_2_8_1: Choice_4_6_2 + Choice_4_8_1 <= 1
DifferentPair_4_6_2_8_3: Choice_4_6_2 + Choice_4_8_3 <= 1
DifferentPair_4_6_3_4_2: Choice_4_4_2 + Choice_4_6_3 <= 1
DifferentPair_4_6_3_4_4: Choice_4_4_4 + Choice_4_6_3 <= 1
DifferentPair_4_6_3_5_1: Choice_4_5_1 + Choice_4_6_3 <= 1
DifferentPair_4_6_3_5_5: Choice_4_5_5 + Choice_4_6_3 <= 1
DifferentPair_4_6_3_7_1: Choice_4_6_3 + Choice_4_7_1 <= 1
DifferentPair_4_6_3_7_5: Choice_4_6_3 + Choice_4_7_5 <= 1
DifferentPair_4_6_3_8_2: Choice_4_6_3 + Choice_4_8_2 <= 1
DifferentPair_4_6_3_8_4: Choice_4_6_3 + Choice_4_8_4 <= 1
DifferentPair_4_6_4_4_3: Choice_4_4_3 + Choice_4_6_4 <= 1
DifferentPair_4_6_4_4_5: Choice_4_4_5 + Choice_4_6_4 <= 1
DifferentPair_4_6_4_5_2: Choice_4_5_2 + Choice_4_6_4 <= 1
DifferentPair_4_6_4_5_6: Choice_4_5_6 + Choice_4_6_4 <= 1
DifferentPair_4_6_4_7_2: Choice_4_6_4 + Choice_4_7_2 <= 1
DifferentPair_4_6_4_7_6: Choice_4_6_4 + Choice_4_7_6 <= 1
DifferentPair_4_6_4_8_3: Choice_4_6_4 + Choice_4_8_3 <= 1
DifferentPair_4_6_4_8_5: Choice_4_6_4 + Choice_4_8_5 <= 1
DifferentPair_4_6_5_4_4: Choice_4_4_4 + Choice_4_6_5 <= 1
DifferentPair_4_6_5_4_6: Choice_4_4_6 + Choice_4_6_5 <= 1
DifferentPair_4_6_5_5_3: Choice_4_5_3 + Choice_4_6_5 <= 1
DifferentPair_4_6_5_5_7: Choice_4_5_7 + Choice_4_6_5 <= 1
DifferentPair_4_6_5_7_3: Choice_4_6_5 + Choice_4_7_3 <= 1
DifferentPair_4_6_5_7_7: Choice_4_6_5 + Choice_4_7_7 <= 1
DifferentPair_4_6_5_8_4: Choice_4_6_5 + Choice_4_8_4 <= 1
DifferentPair_4_6_5_8_6: Choice_4_6_5 + Choice_4_8_6 <= 1
DifferentPair_4_6_6_4_5: Choice_4_4_5 + Choice_4_6_6 <= 1
DifferentPair_4_6_6_4_7: Choice_4_4_7 + Choice_4_6_6 <= 1
DifferentPair_4_6_6_5_4: Choice_4_5_4 + Choice_4_6_6 <= 1
DifferentPair_4_6_6_5_8: Choice_4_5_8 + Choice_4_6_6 <= 1
DifferentPair_4_6_6_7_4: Choice_4_6_6 + Choice_4_7_4 <= 1
DifferentPair_4_6_6_7_8: Choice_4_6_6 + Choice_4_7_8 <= 1
DifferentPair_4_6_6_8_5: Choice_4_6_6 + Choice_4_8_5 <= 1
DifferentPair_4_6_6_8_7: Choice_4_6_6 + Choice_4_8_7 <= 1
DifferentPair_4_6_7_4_6: Choice_4_4_6 + Choice_4_6_7 <= 1
DifferentPair_4_6_7_4_8: Choice_4_4_8 + Choice_4_6_7 <= 1
DifferentPair_4_6_7_5_5: Choice_4_5_5 + Choice_4_6_7 <= 1
DifferentPair_4_6_7_5_9: Choice_4_5_9 + Choice_4_6_7 <= 1
DifferentPair_4_6_7_7_5: Choice_4_6_7 + Choice_4_7_5 <= 1
DifferentPair_4_6_7_7_9: Choice_4_6_7 + Choice_4_7_9 <= 1
DifferentPair_4_6_7_8_6: Choice_4_6_7 + Choice_4_8_6 <= 1
DifferentPair_4_6_7_8_8: Choice_4_6_7 + Choice_4_8_8 <= 1
DifferentPair_4_6_8_4_7: Choice_4_4_7 + Choice_4_6_8 <= 1
DifferentPair_4_6_8_4_9: Choice_4_4_9 + Choice_4_6_8 <= 1
DifferentPair_4_6_8_5_6: Choice_4_5_6 + Choice_4_6_8 <= 1
DifferentPair_4_6_8_7_6: Choice_4_6_8 + Choice_4_7_6 <= 1
DifferentPair_4_6_8_8_7: Choice_4_6_8 + Choice_4_8_7 <= 1
DifferentPair_4_6_8_8_9: Choice_4_6_8 + Choice_4_8_9 <= 1
DifferentPair_4_6_9_4_8: Choice_4_4_8 + Choice_4_6_9 <= 1
DifferentPair_4_6_9_5_7: Choice_4_5_7 + Choice_4_6_9 <= 1
DifferentPair_4_6_9_7_7: Choice_4_6_9 + Choice_4_7_7 <= 1
DifferentPair_4_6_9_8_8: Choice_4_6_9 + Choice_4_8_8 <= 1
DifferentPair_4_7_1_5_2: Choice_4_5_2 + Choice_4_7_1 <= 1
DifferentPair_4_7_1_6_3: Choice_4_6_3 + Choice_4_7_1 <= 1
DifferentPair_4_7_1_8_3: Choice_4_7_1 + Choice_4_8_3 <= 1
DifferentPair_4_7_1_9_2: Choice_4_7_1 + Choice_4_9_2 <= 1
DifferentPair_4_7_2_5_1: Choice_4_5_1 + Choice_4_7_2 <= 1
DifferentPair_4_7_2_5_3: Choice_4_5_3 + Choice_4_7_2 <= 1
DifferentPair_4_7_2_6_4: Choice_4_6_4 + Choice_4_7_2 <= 1
DifferentPair_4_7_2_8_4: Choice_4_7_2 + Choice_4_8_4 <= 1
DifferentPair_4_7_2_9_1: Choice_4_7_2 + Choice_4_9_1 <= 1
DifferentPair_4_7_2_9_3: Choice_4_7_2 + Choice_4_9_3 <= 1
DifferentPair_4_7_3_5_2: Choice_4_5_2 + Choice_4_7_3 <= 1
DifferentPair_4_7_3_5_4: Choice_4_5_4 + Choice_4_7_3 <= 1
DifferentPair_4_7_3_6_1: Choice_4_6_1 + Choice_4_7_3 <= 1
DifferentPair_4_7_3_6_5: Choice_4_6_5 + Choice_4_7_3 <= 1
DifferentPair_4_7_3_8_1: Choice_4_7_3 + Choice_4_8_1 <= 1
DifferentPair_4_7_3_8_5: Choice_4_7_3 + Choice_4_8_5 <= 1
DifferentPair_4_7_3_9_2: Choice_4_7_3 + Choice_4_9_2 <= 1
DifferentPair_4_7_3_9_4: Choice_4_7_3 + Choice_4_9_4 <= 1
DifferentPair_4_7_4_5_3: Choice_4_5_3 + Choice_4_7_4 <= 1
DifferentPair_4_7_4_5_5: Choice_4_5_5 + Choice_4_7_4 <= 1
DifferentPair_4_7_4_6_2: Choice_4_6_2 + Choice_4_7_4 <= 1
DifferentPair_4_7_4_6_6: Choice_4_6_6 + Choice_4_7_4 <= 1
DifferentPair_4_7_4_8_2: Choice_4_7_4 + Choice_4_8_2 <= 1
DifferentPair_4_7_4_8_6: Choice_4_7_4 + Choice_4_8_6 <= 1
DifferentPair_4_7_4_9_3: Choice_4_7_4 + Choice_4_9_3 <= 1
DifferentPair_4_7_4_9_5: Choice_4_7_4 + Choice_4_9_5 <= 1
DifferentPair_4_7_5_5_4: Choice_4_5_4 + Choice_4_7_5 <= 1
DifferentPair_4_7_5_5_6: Choice_4_5_6 + Choice_4_7_5 <= 1
DifferentPair_4_7_5_6_3: Choice_4_6_3 + Choice_4_7_5 <= 1
DifferentPair_4_7_5_6_7: Choice_4_6_7 + Choice_4_7_5 <= 1
DifferentPair_4_7_5_8_3: Choice_4_7_5 + Choice_4_8_3 <= 1
DifferentPair_4_7_5_8_7: Choice_4_7_5 + Choice_4_8_7 <= 1
DifferentPair_4_7_5_9_4: Choice_4_7_5 + Choice_4_9_4 <= 1
DifferentPair_4_7_5_9_6: Choice_4_7_5 + Choice_4_9_6 <= 1
DifferentPair_4_7_6_5_5: Choice_4_5_5 + Choice_4_7_6 <= 1
DifferentPair_4_7_6_5_7: Choice_4_5_7 + Choice_4_7_6 <= 1
DifferentPair_4_7_6_6_4: Choice_4_6_4 + Choice_4_7_6 <= 1
DifferentPair_4_7_6_6_8: Choice_4_6_8 + Choice_4_7_6 <= 1
DifferentPair_4_7_6_8_4: Choice_4_7_6 + Choice_4_8_4 <= 1
DifferentPair_4_7_6_8_8: Choice_4_7_6 + Choice_4_8_8 <= 1
DifferentPair_4_7_6_9_5: Choice_4_7_6 + Choice_4_9_5 <= 1
DifferentPair_4_7_6_9_7: Choice_4_7_6 + Choice_4_9_7 <= 1
DifferentPair_4_7_7_5_6: Choice_4_5_6 + Choice_4_7_7 <= 1
DifferentPair_4_7_7_5_8: Choice_4_5_8 + Choice_4_7_7 <= 1
DifferentPair_4_7_7_6_5: Choice_4_6_5 + Choice_4_7_7 <= 1
DifferentPair_4_7_7_6_9: Choice_4_6_9 + Choice_4_7_7 <= 1
DifferentPair_4_7_7_8_5: Choice_4_7_7 + Choice_4_8_5 <= 1
DifferentPair_4_7_7_8_9: Choice_4_7_7 + Choice_4_8_9 <= 1
DifferentPair_4_7_7_9_6: Choice_4_7_7 + Choice_4_9_6 <= 1
DifferentPair_4_7_7_9_8: Choice_4_7_7 + Choice_4_9_8 <= 1
DifferentPair_4_7_8_5_7: Choice_4_5_7 + Choice_4_7_8 <= 1
DifferentPair_4_7_8_5_9: Choice_4_5_9 + Choice_4_7_8 <= 1
DifferentPair_4_7_8_6_6: Choice_4_6_6 + Choice_4_7_8 <= 1
DifferentPair_4_7_8_8_6: Choice_4_7_8 + Choice_4_8_6 <= 1
DifferentPair_4_7_8_9_7: Choice_4_7_8 + Choice_4_9_7 <= 1
DifferentPair_4_7_8_9_9: Choice_4_7_8 + Choice_4_9_9 <= 1
DifferentPair_4_7_9_5_8: Choice_4_5_8 + Choice_4_7_9 <= 1
DifferentPair_4_7_9_6_7: Choice_4_6_7 + Choice_4_7_9 <= 1
DifferentPair_4_7_9_8_7: Choice_4_7_9 + Choice_4_8_7 <= 1
DifferentPair_4_7_9_9_8: Choice_4_7_9 + Choice_4_9_8 <= 1
DifferentPair_4_8_1_6_2: Choice_4_6_2 + Choice_4_8_1 <= 1
DifferentPair_4_8_1_7_3: Choice_4_7_3 + Choice_4_8_1 <= 1
DifferentPair_4_8_1_9_3: Choice_4_8_1 + Choice_4_9_3 <= 1
DifferentPair_4_8_2_6_1: Choice_4_6_1 + Choice_4_8_2 <= 1
DifferentPair_4_8_2_6_3: Choice_4_6_3 + Choice_4_8_2 <= 1
DifferentPair_4_8_2_7_4: Choice_4_7_4 + Choice_4_8_2 <= 1
DifferentPair_4_8_2_9_4: Choice_4_8_2 + Choice_4_9_4 <= 1
DifferentPair_4_8_3_6_2: Choice_4_6_2 + Choice_4_8_3 <= 1
DifferentPair_4_8_3_6_4: Choice_4_6_4 + Choice_4_8_3 <= 1
DifferentPair_4_8_3_7_1: Choice_4_7_1 + Choice_4_8_3 <= 1
DifferentPair_4_8_3_7_5: Choice_4_7_5 + Choice_4_8_3 <= 1
DifferentPair_4_8_3_9_1: Choice_4_8_3 + Choice_4_9_1 <= 1
DifferentPair_4_8_3_9_5: Choice_4_8_3 + Choice_4_9_5 <= 1
DifferentPair_4_8_4_6_3: Choice_4_6_3 + Choice_4_8_4 <= 1
DifferentPair_4_8_4_6_5: Choice_4_6_5 + Choice_4_8_4 <= 1
DifferentPair_4_8_4_7_2: Choice_4_7_2 + Choice_4_8_4 <= 1
DifferentPair_4_8_4_7_6: Choice_4_7_6 + Choice_4_8_4 <= 1
DifferentPair_4_8_4_9_2: Choice_4_8_4 + Choice_4_9_2 <= 1
DifferentPair_4_8_4_9_6: Choice_4_8_4 + Choice_4_9_6 <= 1
DifferentPair_4_8_5_6_4: Choice_4_6_4 + Choice_4_8_5 <= 1
DifferentPair_4_8_5_6_6: Choice_4_6_6 + Choice_4_8_5 <= 1
DifferentPair_4_8_5_7_3: Choice_4_7_3 + Choice_4_8_5 <= 1
DifferentPair_4_8_5_7_7: Choice_4_7_7 + Choice_4_8_5 <= 1
DifferentPair_4_8_5_9_3: Choice_4_8_5 + Choice_4_9_3 <= 1
DifferentPair_4_8_5_9_7: Choice_4_8_5 + Choice_4_9_7 <= 1
DifferentPair_4_8_6_6_5: Choice_4_6_5 + Choice_4_8_6 <= 1
DifferentPair_4_8_6_6_7: Choice_4_6_7 + Choice_4_8_6 <= 1
DifferentPair_4_8_6_7_4: Choice_4_7_4 + Choice_4_8_6 <= 1
DifferentPair_4_8_6_7_8: Choice_4_7_8 + Choice_4_8_6 <= 1
DifferentPair_4_8_6_9_4: Choice_4_8_6 + Choice_4_9_4 <= 1
DifferentPair_4_8_6_9_8: Choice_4_8_6 + Choice_4_9_8 <= 1
DifferentPair_4_8_7_6_6: Choice_4_6_6 + Choice_4_8_7 <= 1
DifferentPair_4_8_7_6_8: Choice_4_6_8 + Choice_4_8_7 <= 1
DifferentPair_4_8_7_7_5: Choice_4_7_5 + Choice_4_8_7 <= 1
DifferentPair_4_8_7_7_9: Choice_4_7_9 + Choice_4_8_7 <= 1
DifferentPair_4_8_7_9_5: Choice_4_8_7 + Choice_4_9_5 <= 1
DifferentPair_4_8_7_9_9: Choice_4_8_7 + Choice_4_9_9 <= 1
DifferentPair_4_8_8_6_7: Choice_4_6_7 + Choice_4_8_8 <= 1
DifferentPair_4_8_8_6_9: Choice_4_6_9 + Choice_4_8_8 <= 1
DifferentPair_4_8_8_7_6: Choice_4_7_6 + Choice_4_8_8 <= 1
DifferentPair_4_8_8_9_6: Choice_4_8_8 + Choice_4_9_6 <= 1
DifferentPair_4_8_9_6_8: Choice_4_6_8 + Choice_4_8_9 <= 1
DifferentPair_4_8_9_7_7: Choice_4_7_7 + Choice_4_8_9 <= 1
DifferentPair_4_8_9_9_7: Choice_4_8_9 + Choice_4_9_7 <= 1
DifferentPair_4_9_1_7_2: Choice_4_7_2 + Choice_4_9_1 <= 1
DifferentPair_4_9_1_8_3: Choice_4_8_3 + Choice_4_9_1 <= 1
DifferentPair_4_9_2_7_1: Choice_4_7_1 + Choice_4_9_2 <= 1
DifferentPair_4_9_2_7_3: Choice_4_7_3 + Choice_4_9_2 <= 1
DifferentPair_4_9_2_8_4: Choice_4_8_4 + Choice_4_9_2 <= 1
DifferentPair_4_9_3_7_2: Choice_4_7_2 + Choice_4_9_3 <= 1
DifferentPair_4_9_3_7_4: Choice_4_7_4 + Choice_4_9_3 <= 1
DifferentPair_4_9_3_8_1: Choice_4_8_1 + Choice_4_9_3 <= 1
DifferentPair_4_9_3_8_5: Choice_4_8_5 + Choice_4_9_3 <= 1
DifferentPair_4_9_4_7_3: Choice_4_7_3 + Choice_4_9_4 <= 1
DifferentPair_4_9_4_7_5: Choice_4_7_5 + Choice_4_9_4 <= 1
DifferentPair_4_9_4_8_2: Choice_4_8_2 + Choice_4_9_4 <= 1
DifferentPair_4_9_4_8_6: Choice_4_8_6 + Choice_4_9_4 <= 1
DifferentPair_4_9_5_7_4: Choice_4_7_4 + Choice_4_9_5 <= 1
DifferentPair_4_9_5_7_6: Choice_4_7_6 + Choice_4_9_5 <= 1
DifferentPair_4_9_5_8_3: Choice_4_8_3 + Choice_4_9_5 <= 1
DifferentPair_4_9_5_8_7: Choice_4_8_7 + Choice_4_9_5 <= 1
DifferentPair_4_9_6_7_5: Choice_4_7_5 + Choice_4_9_6 <= 1
DifferentPair_4_9_6_7_7: Choice_4_7_7 + Choice_4_9_6 <= 1
DifferentPair_4_9_6_8_4: Choice_4_8_4 + Choice_4_9_6 <= 1
DifferentPair_4_9_6_8_8: Choice_4_8_8 + Choice_4_9_6 <= 1
DifferentPair_4_9_7_7_6: Choice_4_7_6 + Choice_4_9_7 <= 1
DifferentPair_4_9_7_7_8: Choice_4_7_8 + Choice_4_9_7 <= 1
DifferentPair_4_9_7_8_5: Choice_4_8_5 + Choice_4_9_7 <= 1
DifferentPair_4_9_7_8_9: Choice_4_8_9 + Choice_4_9_7 <= 1
DifferentPair_4_9_8_7_7: Choice_4_7_7 + Choice_4_9_8 <= 1
DifferentPair_4_9_8_7_9: Choice_4_7_9 + Choice_4_9_8 <= 1
DifferentPair_4_9_8_8_6: Choice_4_8_6 + Choice_4_9_8 <= 1
DifferentPair_4_9_9_7_8: Choice_4_7_8 + Choice_4_9_9 <= 1
DifferentPair_4_9_9_8_7: Choice_4_8_7 + Choice_4_9_9 <= 1
DifferentPair_5_1_1_2_3: Choice_5_1_1 + Choice_5_2_3 <= 1
DifferentPair_5_1_1_3_2: Choice_5_1_1 + Choice_5_3_2 <= 1
DifferentPair_5_1_2_2_4: Choice_5_1_2 + Choice_5_2_4 <= 1
DifferentPair_5_1_2_3_1: Choice_5_1_2 + Choice_5_3_1 <= 1
DifferentPair_5_1_2_3_3: Choice_5_1_2 + Choice_5_3_3 <= 1
DifferentPair_5_1_3_2_1: Choice_5_1_3 + Choice_5_2_1 <= 1
DifferentPair_5_1_3_2_5: Choice_5_1_3 + Choice_5_2_5 <= 1
DifferentPair_5_1_3_3_2: Choice_5_1_3 + Choice_5_3_2 <= 1
DifferentPair_5_1_3_3_4: Choice_5_1_3 + Choice_5_3_4 <= 1
DifferentPair_5_1_4_2_2: Choice_5_1_4 + Choice_5_2_2 <= 1
DifferentPair_5_1_4_2_6: Choice_5_1_4 + Choice_5_2_6 <= 1
DifferentPair_5_1_4_3_3: Choice_5_1_4 + Choice_5_3_3 <= 1
DifferentPair_5_1_4_3_5: Choice_5_1_4 + Choice_5_3_5 <= 1
DifferentPair_5_1_5_2_3: Choice_5_1_5 + Choice_5_2_3 <= 1
DifferentPair_5_1_5_2_7: Choice_5_1_5 + Choice_5_2_7 <= 1
DifferentPair_5_1_5_3_4: Choice_5_1_5 + Choice_5_3_4 <= 1
DifferentPair_5_1_5_3_6: Choice_5_1_5 + Choice_5_3_6 <= 1
DifferentPair_5_1_6_2_4: Choice_5_1_6 + Choice_5_2_4 <= 1
DifferentPair_5_1_6_2_8: Choice_5_1_6 + Choice_5_2_8 <= 1
DifferentPair_5_1_6_3_5: Choice_5_1_6 + Choice_5_3_5 <= 1
DifferentPair_5_1_6_3_7: Choice_5_1_6 + Choice_5_3_7 <= 1
DifferentPair_5_1_7_2_5: Choice_5_1_7 + Choice_5_2_5 <= 1
DifferentPair_5_1_7_2_9: Choice_5_1_7 + Choice_5_2_9 <= 1
DifferentPair_5_1_7_3_6: Choice_5_1_7 + Choice_5_3_6 <= 1
DifferentPair_5_1_7_3_8: Choice_5_1_7 + Choice_5_3_8 <= 1
DifferentPair_5_1_8_2_6: Choice_5_1_8 + Choice_5_2_6 <= 1
DifferentPair_5_1_8_3_7: Choice_5_1_8 + Choice_5_3_7 <= 1
DifferentPair_5_1_8_3_9: Choice_5_1_8 + Choice_5_3_9 <= 1
DifferentPair_5_1_9_2_7: Choice_5_1_9 + Choice_5_2_7 <= 1
DifferentPair_5_1_9_3_8: Choice_5_1_9 + Choice_5_3_8 <= 1
DifferentPair_5_2_1_1_3: Choice_5_1_3 + Choice_5_2_1 <= 1
DifferentPair_5_2_1_3_3: Choice_5_2_1 + Choice_5_3_3 <= 1
DifferentPair_5_2_1_4_2: Choice_5_2_1 + Choice_5_4_2 <= 1
DifferentPair_5_2_2_1_4: Choice_5_1_4 + Choice_5_2_2 <= 1
DifferentPair_5_2_2_3_4: Choice_5_2_2 + Choice_5_3_4 <= 1
DifferentPair_5_2_2_4_1: Choice_5_2_2 + Choice_5_4_1 <= 1
DifferentPair_5_2_2_4_3: Choice_5_2_2 + Choice_5_4_3 <= 1
DifferentPair_5_2_3_1_1: Choice_5_1_1 + Choice_5_2_3 <= 1
DifferentPair_5_2_3_1_5: Choice_5_1_5 + Choice_5_2_3 <= 1
DifferentPair_5_2_3_3_1: Choice_5_2_3 + Choice_5_3_1 <= 1
DifferentPair_5_2_3_3_5: Choice_5_2_3 + Choice_5_3_5 <= 1
DifferentPair_5_2_3_4_2: Choice_5_2_3 + Choice_5_4_2 <= 1
DifferentPair_5_2_3_4_4: Choice_5_2_3 + Choice_5_4_4 <= 1
DifferentPair_5_2_4_1_2: Choice_5_1_2 + Choice_5_2_4 <= 1
DifferentPair_5_2_4_1_6: Choice_5_1_6 + Choice_5_2_4 <= 1
DifferentPair_5_2_4_3_2: Choice_5_2_4 + Choice_5_3_2 <= 1
DifferentPair_5_2_4_3_6: Choice_5_2_4 + Choice_5_3_6 <= 1
DifferentPair_5_2_4_4_3: Choice_5_2_4 + Choice_5_4_3 <= 1
DifferentPair_5_2_4_4_5: Choice_5_2_4 + Choice_5_4_5 <= 1
DifferentPair_5_2_5_1_3: Choice_5_1_3 + Choice_5_2_5 <= 1
DifferentPair_5_2_5_1_7: Choice_5_1_7 + Choice_5_2_5 <= 1
DifferentPair_5_2_5_3_3: Choice_5_2_5 + Choice_5_3_3 <= 1
DifferentPair_5_2_5_3_7: Choice_5_2_5 + Choice_5_3_7 <= 1
DifferentPair_5_2_5_4_4: Choice_5_2_5 + Choice_5_4_4 <= 1
DifferentPair_5_2_5_4_6: Choice_5_2_5 + Choice_5_4_6 <= 1
DifferentPair_5_2_6_1_4: Choice_5_1_4 + Choice_5_2_6 <= 1
DifferentPair_5_2_6_1_8: Choice_5_1_8 + Choice_5_2_6 <= 1
DifferentPair_5_2_6_3_4: Choice_5_2_6 + Choice_5_3_4 <= 1
DifferentPair_5_2_6_3_8: Choice_5_2_6 + Choice_5_3_8 <= 1
DifferentPair_5_2_6_4_5: Choice_5_2_6 + Choice_5_4_5 <= 1
DifferentPair_5_2_6_4_7: Choice_5_2_6 + Choice_5_4_7 <= 1
DifferentPair_5_2_7_1_5: Choice_5_1_5 + Choice_5_2_7 <= 1
DifferentPair_5_2_7_1_9: Choice_5_1_9 + Choice_5_2_7 <= 1
DifferentPair_5_2_7_3_5: Choice_5_2_7 + Choice_5_3_5 <= 1
DifferentPair_5_2_7_3_9: Choice_5_2_7 + Choice_5_3_9 <= 1
DifferentPair_5_2_7_4_6: Choice_5_2_7 + Choice_5_4_6 <= 1
DifferentPair_5_2_7_4_8: Choice_5_2_7 + Choice_5_4_8 <= 1
DifferentPair_5_2_8_1_6: Choice_5_1_6 + Choice_5_2_8 <= 1
DifferentPair_5_2_8_3_6: Choice_5_2_8 + Choice_5_3_6 <= 1
DifferentPair_5_2_8_4_7: Choice_5_2_8 + Choice_5_4_7 <= 1
DifferentPair_5_2_8_4_9: Choice_5_2_8 + Choice_5_4_9 <= 1
DifferentPair_5_2_9_1_7: Choice_5_1_7 + Choice_5_2_9 <= 1
DifferentPair_5_2_9_3_7: Choice_5_2_9 + Choice_5_3_7 <= 1
DifferentPair_5_2_9_4_8: Choice_5_2_9 + Choice_5_4_8 <= 1
DifferentPair_5_3_1_1_2: Choice_5_1_2 + Choice_5_3_1 <= 1
DifferentPair_5_3_1_2_3: Choice_5_2_3 + Choice_5_3_1 <= 1
DifferentPair_5_3_1_4_3: Choice_5_3_1 + Choice_5_4_3 <= 1
DifferentPair_5_3_1_5_2: Choice_5_3_1 + Choice_5_5_2 <= 1
DifferentPair_5_3_2_1_1: Choice_5_1_1 + Choice_5_3_2 <= 1
DifferentPair_5_3_2_1_3: Choice_5_1_3 + Choice_5_3_2 <= 1
DifferentPair_5_3_2_2_4: Choice_5_2_4 + Choice_5_3_2 <= 1
DifferentPair_5_3_2_4_4: Choice_5_3_2 + Choice_5_4_4 <= 1
DifferentPair_5_3_2_5_1: Choice_5_3_2 + Choice_5_5_1 <= 1
DifferentPair_5_3_2_5_3: Choice_5_3_2 + Choice_5_5_3 <= 1
DifferentPair_5_3_3_1_2: Choice_5_1_2 + Choice_5_3_3 <= 1
DifferentPair_5_3_3_1_4: Choice_5_1_4 + Choice_5_3_3 <= 1
DifferentPair_5_3_3_2_1: Choice_5_2_1 + Choice_5_3_3 <= 1
DifferentPair_5_3_3_2_5: Choice_5_2_5 + Choice_5_3_3 <= 1
DifferentPair_5_3_3_4_1: Choice_5_3_3 + Choice_5_4_1 <= 1
DifferentPair_5_3_3_4_5: Choice_5_3_3 + Choice_5_4_5 <= 1
DifferentPair_5_3_3_5_2: Choice_5_3_3 + Choice_5_5_2 <= 1
DifferentPair_5_3_3_5_4: Choice_5_3_3 + Choice_5_5_4 <= 1
DifferentPair_5_3_4_1_3: Choice_5_1_3 + Choice_5_3_4 <= 1
DifferentPair_5_3_4_1_5: Choice_5_1_5 + Choice_5_3_4 <= 1
DifferentPair_5_3_4_2_2: Choice_5_2_2 + Choice_5_3_4 <= 1
DifferentPair_5_3_4_2_6: Choice_5_2_6 + Choice_5_3_4 <= 1
DifferentPair_5_3_4_4_2: Choice_5_3_4 + Choice_5_4_2 <= 1
DifferentPair_5_3_4_4_6: Choice_5_3_4 + Choice_5_4_6 <= 1
DifferentPair_5_3_4_5_3: Choice_5_3_4 + Choice_5_5_3 <= 1
DifferentPair_5_3_4_5_5: Choice_5_3_4 + Choice_5_5_5 <= 1
DifferentPair_5_3_5_1_4: Choice_5_1_4 + Choice_5_3_5 <= 1
DifferentPair_5_3_5_1_6: Choice_5_1_6 + Choice_5_3_5 <= 1
DifferentPair_5_3_5_2_3: Choice_5_2_3 + Choice_5_3_5 <= 1
DifferentPair_5_3_5_2_7: Choice_5_2_7 + Choice_5_3_5 <= 1
DifferentPair_5_3_5_4_3: Choice_5_3_5 + Choice_5_4_3 <= 1
DifferentPair_5_3_5_4_7: Choice_5_3_5 + Choice_5_4_7 <= 1
DifferentPair_5_3_5_5_4: Choice_5_3_5 + Choice_5_5_4 <= 1
DifferentPair_5_3_5_5_6: Choice_5_3_5 + Choice_5_5_6 <= 1
DifferentPair_5_3_6_1_5: Choice_5_1_5 + Choice_5_3_6 <= 1
DifferentPair_5_3_6_1_7: Choice_5_1_7 + Choice_5_3_6 <= 1
DifferentPair_5_3_6_2_4: Choice_5_2_4 + Choice_5_3_6 <= 1
DifferentPair_5_3_6_2_8: Choice_5_2_8 + Choice_5_3_6 <= 1
DifferentPair_5_3_6_4_4: Choice_5_3_6 + Choice_5_4_4 <= 1
DifferentPair_5_3_6_4_8: Choice_5_3_6 + Choice_5_4_8 <= 1
DifferentPair_5_3_6_5_5: Choice_5_3_6 + Choice_5_5_5 <= 1
DifferentPair_5_3_6_5_7: Choice_5_3_6 + Choice_5_5_7 <= 1
DifferentPair_5_3_7_1_6: Choice_5_1_6 + Choice_5_3_7 <= 1
DifferentPair_5_3_7_1_8: Choice_5_1_8 + Choice_5_3_7 <= 1
DifferentPair_5_3_7_2_5: Choice_5_2_5 + Choice_5_3_7 <= 1
DifferentPair_5_3_7_2_9: Choice_5_2_9 + Choice_5_3_7 <= 1
DifferentPair_5_3_7_4_5: Choice_5_3_7 + Choice_5_4_5 <= 1
DifferentPair_5_3_7_4_9: Choice_5_3_7 + Choice_5_4_9 <= 1
DifferentPair_5_3_7_5_6: Choice_5_3_7 + Choice_5_5_6 <= 1
DifferentPair_5_3_7_5_8: Choice_5_3_7 + Choice_5_5_8 <= 1
DifferentPair_5_3_8_1_7: Choice_5_1_7 + Choice_5_3_8 <= 1
DifferentPair_5_3_8_1_9: Choice_5_1_9 + Choice_5_3_8 <= 1
DifferentPair_5_3_8_2_6: Choice_5_2_6 + Choice_5_3_8 <= 1
DifferentPair_5_3_8_4_6: Choice_5_3_8 + Choice_5_4_6 <= 1
DifferentPair_5_3_8_5_7: Choice_5_3_8 + Choice_5_5_7 <= 1
DifferentPair_5_3_8_5_9: Choice_5_3_8 + Choice_5_5_9 <= 1
DifferentPair_5_3_9_1_8: Choice_5_1_8 + Choice_5_3_9 <= 1
DifferentPair_5_3_9_2_7: Choice_5_2_7 + Choice_5_3_9 <= 1
DifferentPair_5_3_9_4_7: Choice_5_3_9 + Choice_5_4_7 <= 1
DifferentPair_5_3_9_5_8: Choice_5_3_9 + Choice_5_5_8 <= 1
DifferentPair_5_4_1_2_2: Choice_5_2_2 + Choice_5_4_1 <= 1
DifferentPair_5_4_1_3_3: Choice_5_3_3 + Choice_5_4_1 <= 1
DifferentPair_5_4_1_5_3: Choice_5_4_1 + Choice_5_5_3 <= 1
DifferentPair_5_4_1_6_2: Choice_5_4_1 + Choice_5_6_2 <= 1
DifferentPair_5_4_2_2_1: Choice_5_2_1 + Choice_5_4_2 <= 1
DifferentPair_5_4_2_2_3: Choice_5_2_3 + Choice_5_4_2 <= 1
DifferentPair_5_4_2_3_4: Choice_5_3_4 + Choice_5_4_2 <= 1
DifferentPair_5_4_2_5_4: Choice_5_4_2 + Choice_5_5_4 <= 1
DifferentPair_5_4_2_6_1: Choice_5_4_2 + Choice_5_6_1 <= 1
DifferentPair_5_4_2_6_3: Choice_5_4_2 + Choice_5_6_3 <= 1
DifferentPair_5_4_3_2_2: Choice_5_2_2 + Choice_5_4_3 <= 1
DifferentPair_5_4_3_2_4: Choice_5_2_4 + Choice_5_4_3 <= 1
DifferentPair_5_4_3_3_1: Choice_5_3_1 + Choice_5_4_3 <= 1
DifferentPair_5_4_3_3_5: Choice_5_3_5 + Choice_5_4_3 <= 1
DifferentPair_5_4_3_5_1: Choice_5_4_3 + Choice_5_5_1 <= 1
DifferentPair_5_4_3_5_5: Choice_5_4_3 + Choice_5_5_5 <= 1
DifferentPair_5_4_3_6_2: Choice_5_4_3 + Choice_5_6_2 <= 1
DifferentPair_5_4_3_6_4: Choice_5_4_3 + Choice_5_6_4 <= 1
DifferentPair_5_4_4_2_3: Choice_5_2_3 + Choice_5_4_4 <= 1
DifferentPair_5_4_4_2_5: Choice_5_2_5 + Choice_5_4_4 <= 1
DifferentPair_5_4_4_3_2: Choice_5_3_2 + Choice_5_4_4 <= 1
DifferentPair_5_4_4_3_6: Choice_5_3_6 + Choice_5_4_4 <= 1
DifferentPair_5_4_4_5_2: Choice_5_4_4 + Choice_5_5_2 <= 1
DifferentPair_5_4_4_5_6: Choice_5_4_4 + Choice_5_5_6 <= 1
DifferentPair_5_4_4_6_3: Choice_5_4_4 + Choice_5_6_3 <= 1
DifferentPair_5_4_4_6_5: Choice_5_4_4 + Choice_5_6_5 <= 1
DifferentPair_5_4_5_2_4: Choice_5_2_4 + Choice_5_4_5 <= 1
DifferentPair_5_4_5_2_6: Choice_5_2_6 + Choice_5_4_5 <= 1
DifferentPair_5_4_5_3_3: Choice_5_3_3 + Choice_5_4_5 <= 1
DifferentPair_5_4_5_3_7: Choice_5_3_7 + Choice_5_4_5 <= 1
DifferentPair_5_4_5_5_3: Choice_5_4_5 + Choice_5_5_3 <= 1
DifferentPair_5_4_5_5_7: Choice_5_4_5 + Choice_5_5_7 <= 1
DifferentPair_5_4_5_6_4: Choice_5_4_5 + Choice_5_6_4 <= 1
DifferentPair_5_4_5_6_6: Choice_5_4_5 + Choice_5_6_6 <= 1
DifferentPair_5_4_6_2_5: Choice_5_2_5 + Choice_5_4_6 <= 1
DifferentPair_5_4_6_2_7: Choice_5_2_7 + Choice_5_4_6 <= 1
DifferentPair_5_4_6_3_4: Choice_5_3_4 + Choice_5_4_6 <= 1
DifferentPair_5_4_6_3_8: Choice_5_3_8 + Choice_5_4_6 <= 1
DifferentPair_5_4_6_5_4: Choice_5_4_6 + Choice_5_5_4 <= 1
DifferentPair_5_4_6_5_8: Choice_5_4_6 + Choice_5_5_8 <= 1
DifferentPair_5_4_6_6_5: Choice_5_4_6 + Choice_5_6_5 <= 1
DifferentPair_5_4_6_6_7: Choice_5_4_6 + Choice_5_6_7 <= 1
DifferentPair_5_4_7_2_6: Choice_5_2_6 + Choice_5_4_7 <= 1
DifferentPair_5_4_7_2_8: Choice_5_2_8 + Choice_5_4_7 <= 1
DifferentPair_5_4_7_3_5: Choice_5_3_5 + Choice_5_4_7 <= 1
DifferentPair_5_4_7_3_9: Choice_5_3_9 + Choice_5_4_7 <= 1
DifferentPair_5_4_7_5_5: Choice_5_4_7 + Choice_5_5_5 <= 1
DifferentPair_5_4_7_5_9: Choice_5_4_7 + Choice_5_5_9 <= 1
DifferentPair_5_4_7_6_6: Choice_5_4_7 + Choice_5_6_6 <= 1
DifferentPair_5_4_7_6_8: Choice_5_4_7 + Choice_5_6_8 <= 1
DifferentPair_5_4_8_2_7: Choice_5_2_7 + Choice_5_4_8 <= 1
DifferentPair_5_4_8_2_9: Choice_5_2_9 + Choice_5_4_8 <= 1
DifferentPair_5_4_8_3_6: Choice_5_3_6 + Choice_5_4_8 <= 1
DifferentPair_5_4_8_5_6: Choice_5_4_8 + Choice_5_5_6 <= 1
DifferentPair_5_4_8_6_7: Choice_5_4_8 + Choice_5_6_7 <= 1
DifferentPair_5_4_8_6_9: Choice_5_4_8 + Choice_5_6_9 <= 1
DifferentPair_5_4_9_2_8: Choice_5_2_8 + Choice_5_4_9 <= 1
DifferentPair_5_4_9_3_7: Choice_5_3_7 + Choice_5_4_9 <= 1
DifferentPair_5_4_9_5_7: Choice_5_4_9 + Choice_5_5_7 <= 1
DifferentPair_5_4_9_6_8: Choice_5_4_9 + Choice_5_6_8 <= 1
DifferentPair_5_5_1_3_2: Choice_5_3_2 + Choice_5_5_1 <= 1
DifferentPair_5_5_1_4_3: Choice_5_4_3 + Choice_5_5_1 <= 1
DifferentPair_5_5_1_6_3: Choice_5_5_1 + Choice_5_6_3 <= 1
DifferentPair_5_5_1_7_2: Choice_5_5_1 + Choice_5_7_2 <= 1
DifferentPair_5_5_2_3_1: Choice_5_3_1 + Choice_5_5_2 <= 1
DifferentPair_5_5_2_3_3: Choice_5_3_3 + Choice_5_5_2 <= 1
DifferentPair_5_5_2_4_4: Choice_5_4_4 + Choice_5_5_2 <= 1
DifferentPair_5_5_2_6_4: Choice_5_5_2 + Choice_5_6_4 <= 1
DifferentPair_5_5_2_7_1: Choice_5_5_2 + Choice_5_7_1 <= 1
DifferentPair_5_5_2_7_3: Choice_5_5_2 + Choice_5_7_3 <= 1
DifferentPair_5_5_3_3_2: Choice_5_3_2 + Choice_5_5_3 <= 1
DifferentPair_5_5_3_3_4: Choice_5_3_4 + Choice_5_5_3 <= 1
DifferentPair_5_5_3_4_1: Choice_5_4_1 + Choice_5_5_3 <= 1
DifferentPair_5_5_3_4_5: Choice_5_4_5 + Choice_5_5_3 <= 1
DifferentPair_5_5_3_6_1: Choice_5_5_3 + Choice_5_6_1 <= 1
DifferentPair_5_5_3_6_5: Choice_5_5_3 + Choice_5_6_5 <= 1
DifferentPair_5_5_3_7_2: Choice_5_5_3 + Choice_5_7_2 <= 1
DifferentPair_5_5_3_7_4: Choice_5_5_3 + Choice_5_7_4 <= 1
DifferentPair_5_5_4_3_3: Choice_5_3_3 + Choice_5_5_4 <= 1
DifferentPair_5_5_4_3_5: Choice_5_3_5 + Choice_5_5_4 <= 1
DifferentPair_5_5_4_4_2: Choice_5_4_2 + Choice_5_5_4 <= 1
DifferentPair_5_5_4_4_6: Choice_5_4_6 + Choice_5_5_4 <= 1
DifferentPair_5_5_4_6_2: Choice_5_5_4 + Choice_5_6_2 <= 1
DifferentPair_5_5_4_6_6: Choice_5_5_4 + Choice_5_6_6 <= 1
DifferentPair_5_5_4_7_3: Choice_5_5_4 + Choice_5_7_3 <= 1
DifferentPair_5_5_4_7_5: Choice_5_5_4 + Choice_5_7_5 <= 1
DifferentPair_5_5_5_3_4: Choice_5_3_4 + Choice_5_5_5 <= 1
DifferentPair_5_5_5_3_6: Choice_5_3_6 + Choice_5_5_5 <= 1
DifferentPair_5_5_5_4_3: Choice_5_4_3 + Choice_5_5_5 <= 1
DifferentPair_5_5_5_4_7: Choice_5_4_7 + Choice_5_5_5 <= 1
DifferentPair_5_5_5_6_3: Choice_5_5_5 + Choice_5_6_3 <= 1
DifferentPair_5_5_5_6_7: Choice_5_5_5 + Choice_5_6_7 <= 1
DifferentPair_5_5_5_7_4: Choice_5_5_5 + Choice_5_7_4 <= 1
DifferentPair_5_5_5_7_6: Choice_5_5_5 + Choice_5_7_6 <= 1
DifferentPair_5_5_6_3_5: Choice_5_3_5 + Choice_5_5_6 <= 1
DifferentPair_5_5_6_3_7: Choice_5_3_7 + Choice_5_5_6 <= 1
DifferentPair_5_5_6_4_4: Choice_5_4_4 + Choice_5_5_6 <= 1
DifferentPair_5_5_6_4_8: Choice_5_4_8 + Choice_5_5_6 <= 1
DifferentPair_5_5_6_6_4: Choice_5_5_6 + Choice_5_6_4 <= 1
DifferentPair_5_5_6_6_8: Choice_5_5_6 + Choice_5_6_8 <= 1
DifferentPair_5_5_6_7_5: Choice_5_5_6 + Choice_5_7_5 <= 1
DifferentPair_5_5_6_7_7: Choice_5_5_6 + Choice_5_7_7 <= 1
DifferentPair_5_5_7_3_6: Choice_5_3_6 + Choice_5_5_7 <= 1
DifferentPair_5_5_7_3_8: Choice_5_3_8 + Choice_5_5_7 <= 1
DifferentPair_5_5_7_4_5: Choice_5_4_5 + Choice_5_5_7 <= 1
DifferentPair_5_5_7_4_9: Choice_5_4_9 + Choice_5_5_7 <= 1
DifferentPair_5_5_7_6_5: Choice_5_5_7 + Choice_5_6_5 <= 1
DifferentPair_5_5_7_6_9: Choice_5_5_7 + Choice_5_6_9 <= 1
DifferentPair_5_5_7_7_6: Choice_5_5_7 + Choice_5_7_6 <= 1
DifferentPair_5_5_7_7_8: Choice_5_5_7 + Choice_5_7_8 <= 1
DifferentPair_5_5_8_3_7: Choice_5_3_7 + Choice_5_5_8 <= 1
DifferentPair_5_5_8_3_9: Choice_5_3_9 + Choice_5_5_8 <= 1
DifferentPair_5_5_8_4_6: Choice_5_4_6 + Choice_5_5_8 <= 1
DifferentPair_5_5_8_6_6: Choice_5_5_8 + Choice_5_6_6 <= 1
DifferentPair_5_5_8_7_7: Choice_5_5_8 + Choice_5_7_7 <= 1
DifferentPair_5_5_8_7_9: Choice_5_5_8 + Choice_5_7_9 <= 1
DifferentPair_5_5_9_3_8: Choice_5_3_8 + Choice_5_5_9 <= 1
DifferentPair_5_5_9_4_7: Choice_5_4_7 + Choice_5_5_9 <= 1
DifferentPair_5_5_9_6_7: Choice_5_5_9 + Choice_5_6_7 <= 1
DifferentPair_5_5_9_7_8: Choice_5_5_9 + Choice_5_7_8 <= 1
DifferentPair_5_6_1_4_2: Choice_5_4_2 + Choice_5_6_1 <= 1
DifferentPair_5_6_1_5_3: Choice_5_5_3 + Choice_5_6_1 <= 1
DifferentPair_5_6_1_7_3: Choice_5_6_1 + Choice_5_7_3 <= 1
DifferentPair_5_6_1_8_2: Choice_5_6_1 + Choice_5_8_2 <= 1
DifferentPair_5_6_2_4_1: Choice_5_4_1 + Choice_5_6_2 <= 1
DifferentPair_5_6_2_4_3: Choice_5_4_3 + Choice_5_6_2 <= 1
DifferentPair_5_6_2_5_4: Choice_5_5_4 + Choice_5_6_2 <= 1
DifferentPair_5_6_2_7_4: Choice_5_6_2 + Choice_5_7_4 <= 1
DifferentPair_5_6_2_8_1: Choice_5_6_2 + Choice_5_8_1 <= 1
DifferentPair_5_6_2_8_3: Choice_5_6_2 + Choice_5_8_3 <= 1
DifferentPair_5_6_3_4_2: Choice_5_4_2 + Choice_5_6_3 <= 1
DifferentPair_5_6_3_4_4: Choice_5_4_4 + Choice_5_6_3 <= 1
DifferentPair_5_6_3_5_1: Choice_5_5_1 + Choice_5_6_3 <= 1
DifferentPair_5_6_3_5_5: Choice_5_5_5 + Choice_5_6_3 <= 1
DifferentPair_5_6_3_7_1: Choice_5_6_3 + Choice_5_7_1 <= 1
DifferentPair_5_6_3_7_5: Choice_5_6_3 + Choice_5_7_5 <= 1
DifferentPair_5_6_3_8_2: Choice_5_6_3 + Choice_5_8_2 <= 1
DifferentPair_5_6_3_8_4: Choice_5_6_3 + Choice_5_8_4 <= 1
DifferentPair_5_6_4_4_3: Choice_5_4_3 + Choice_5_6_4 <= 1
DifferentPair_5_6_4_4_5: Choice_5_4_5 + Choice_5_6_4 <= 1
DifferentPair_5_6_4_5_2: Choice_5_5_2 + Choice_5_6_4 <= 1
DifferentPair_5_6_4_5_6: Choice_5_5_6 + Choice_5_6_4 <= 1
DifferentPair_5_6_4_7_2: Choice_5_6_4 + Choice_5_7_2 <= 1
DifferentPair_5_6_4_7_6: Choice_5_6_4 + Choice_5_7_6 <= 1
DifferentPair_5_6_4_8_3: Choice_5_6_4 + Choice_5_8_3 <= 1
DifferentPair_5_6_4_8_5: Choice_5_6_4 + Choice_5_8_5 <= 1
DifferentPair_5_6_5_4_4: Choice_5_4_4 + Choice_5_6_5 <= 1
DifferentPair_5_6_5_4_6: Choice_5_4_6 + Choice_5_6_5 <= 1
DifferentPair_5_6_5_5_3: Choice_5_5_3 + Choice_5_6_5 <= 1
DifferentPair_5_6_5_5_7: Choice_5_5_7 + Choice_5_6_5 <= 1
DifferentPair_5_6_5_7_3: Choice_5_6_5 + Choice_5_7_3 <= 1
DifferentPair_5_6_5_7_7: Choice_5_6_5 + Choice_5_7_7 <= 1
DifferentPair_5_6_5_8_4: Choice_5_6_5 + Choice_5_8_4 <= 1
DifferentPair_5_6_5_8_6: Choice_5_6_5 + Choice_5_8_6 <= 1
DifferentPair_5_6_6_4_5: Choice_5_4_5 + Choice_5_6_6 <= 1
DifferentPair_5_6_6_4_7: Choice_5_4_7 + Choice_5_6_6 <= 1
DifferentPair_5_6_6_5_4: Choice_5_5_4 + Choice_5_6_6 <= 1
DifferentPair_5_6_6_5_8: Choice_5_5_8 + Choice_5_6_6 <= 1
DifferentPair_5_6_6_7_4: Choice_5_6_6 + Choice_5_7_4 <= 1
DifferentPair_5_6_6_7_8: Choice_5_6_6 + Choice_5_7_8 <= 1
DifferentPair_5_6_6_8_5: Choice_5_6_6 + Choice_5_8_5 <= 1
DifferentPair_5_6_6_8_7: Choice_5_6_6 + Choice_5_8_7 <= 1
DifferentPair_5_6_7_4_6: Choice_5_4_6 + Choice_5_6_7 <= 1
DifferentPair_5_6_7_4_8: Choice_5_4_8 + Choice_5_6_7 <= 1
DifferentPair_5_6_7_5_5: Choice_5_5_5 + Choice_5_6_7 <= 1
DifferentPair_5_6_7_5_9: Choice_5_5_9 + Choice_5_6_7 <= 1
DifferentPair_5_6_7_7_5: Choice_5_6_7 + Choice_5_7_5 <= 1
DifferentPair_5_6_7_7_9: Choice_5_6_7 + Choice_5_7_9 <= 1
DifferentPair_5_6_7_8_6: Choice_5_6_7 + Choice_5_8_6 <= 1
DifferentPair_5_6_7_8_8: Choice_5_6_7 + Choice_5_8_8 <= 1
DifferentPair_5_6_8_4_7: Choice_5_4_7 + Choice_5_6_8 <= 1
DifferentPair_5_6_8_4_9: Choice_5_4_9 + Choice_5_6_8 <= 1
DifferentPair_5_6_8_5_6: Choice_5_5_6 + Choice_5_6_8 <= 1
DifferentPair_5_6_8_7_6: Choice_5_6_8 + Choice_5_7_6 <= 1
DifferentPair_5_6_8_8_7: Choice_5_6_8 + Choice_5_8_7 <= 1
DifferentPair_5_6_8_8_9: Choice_5_6_8 + Choice_5_8_9 <= 1
DifferentPair_5_6_9_4_8: Choice_5_4_8 + Choice_5_6_9 <= 1
DifferentPair_5_6_9_5_7: Choice_5_5_7 + Choice_5_6_9 <= 1
DifferentPair_5_6_9_7_7: Choice_5_6_9 + Choice_5_7_7 <= 1
DifferentPair_5_6_9_8_8: Choice_5_6_9 + Choice_5_8_8 <= 1
DifferentPair_5_7_1_5_2: Choice_5_5_2 + Choice_5_7_1 <= 1
DifferentPair_5_7_1_6_3: Choice_5_6_3 + Choice_5_7_1 <= 1
DifferentPair_5_7_1_8_3: Choice_5_7_1 + Choice_5_8_3 <= 1
DifferentPair_5_7_1_9_2: Choice_5_7_1 + Choice_5_9_2 <= 1
DifferentPair_5_7_2_5_1: Choice_5_5_1 + Choice_5_7_2 <= 1
DifferentPair_5_7_2_5_3: Choice_5_5_3 + Choice_5_7_2 <= 1
DifferentPair_5_7_2_6_4: Choice_5_6_4 + Choice_5_7_2 <= 1
DifferentPair_5_7_2_8_4: Choice_5_7_2 + Choice_5_8_4 <= 1
DifferentPair_5_7_2_9_1: Choice_5_7_2 + Choice_5_9_1 <= 1
DifferentPair_5_7_2_9_3: Choice_5_7_2 + Choice_5_9_3 <= 1
DifferentPair_5_7_3_5_2: Choice_5_5_2 + Choice_5_7_3 <= 1
DifferentPair_5_7_3_5_4: Choice_5_5_4 + Choice_5_7_3 <= 1
DifferentPair_5_7_3_6_1: Choice_5_6_1 + Choice_5_7_3 <= 1
DifferentPair_5_7_3_6_5: Choice_5_6_5 + Choice_5_7_3 <= 1
DifferentPair_5_7_3_8_1: Choice_5_7_3 + Choice_5_8_1 <= 1
DifferentPair_5_7_3_8_5: Choice_5_7_3 + Choice_5_8_5 <= 1
DifferentPair_5_7_3_9_2: Choice_5_7_3 + Choice_5_9_2 <= 1
DifferentPair_5_7_3_9_4: Choice_5_7_3 + Choice_5_9_4 <= 1
DifferentPair_5_7_4_5_3: Choice_5_5_3 + Choice_5_7_4 <= 1
DifferentPair_5_7_4_5_5: Choice_5_5_5 + Choice_5_7_4 <= 1
DifferentPair_5_7_4_6_2: Choice_5_6_2 + Choice_5_7_4 <= 1
DifferentPair_5_7_4_6_6: Choice_5_6_6 + Choice_5_7_4 <= 1
DifferentPair_5_7_4_8_2: Choice_5_7_4 + Choice_5_8_2 <= 1
DifferentPair_5_7_4_8_6: Choice_5_7_4 + Choice_5_8_6 <= 1
DifferentPair_5_7_4_9_3: Choice_5_7_4 + Choice_5_9_3 <= 1
DifferentPair_5_7_4_9_5: Choice_5_7_4 + Choice_5_9_5 <= 1
DifferentPair_5_7_5_5_4: Choice_5_5_4 + Choice_5_7_5 <= 1
DifferentPair_5_7_5_5_6: Choice_5_5_6 + Choice_5_7_5 <= 1
DifferentPair_5_7_5_6_3: Choice_5_6_3 + Choice_5_7_5 <= 1
DifferentPair_5_7_5_6_7: Choice_5_6_7 + Choice_5_7_5 <= 1
DifferentPair_5_7_5_8_3: Choice_5_7_5 + Choice_5_8_3 <= 1
DifferentPair_5_7_5_8_7: Choice_5_7_5 + Choice_5_8_7 <= 1
DifferentPair_5_7_5_9_4: Choice_5_7_5 + Choice_5_9_4 <= 1
DifferentPair_5_7_5_9_6: Choice_5_7_5 + Choice_5_9_6 <= 1
DifferentPair_5_7_6_5_5: Choice_5_5_5 + Choice_5_7_6 <= 1
DifferentPair_5_7_6_5_7: Choice_5_5_7 + Choice_5_7_6 <= 1
DifferentPair_5_7_6_6_4: Choice_5_6_4 + Choice_5_7_6 <= 1
DifferentPair_5_7_6_6_8: Choice_5_6_8 + Choice_5_7_6 <= 1
DifferentPair_5_7_6_8_4: Choice_5_7_6 + Choice_5_8_4 <= 1
DifferentPair_5_7_6_8_8: Choice_5_7_6 + Choice_5_8_8 <= 1
DifferentPair_5_7_6_9_5: Choice_5_7_6 + Choice_5_9_5 <= 1
DifferentPair_5_7_6_9_7: Choice_5_7_6 + Choice_5_9_7 <= 1
DifferentPair_5_7_7_5_6: Choice_5_5_6 + Choice_5_7_7 <= 1
DifferentPair_5_7_7_5_8: Choice_5_5_8 + Choice_5_7_7 <= 1
DifferentPair_5_7_7_6_5: Choice_5_6_5 + Choice_5_7_7 <= 1
DifferentPair_5_7_7_6_9: Choice_5_6_9 + Choice_5_7_7 <= 1
DifferentPair_5_7_7_8_5: Choice_5_7_7 + Choice_5_8_5 <= 1
DifferentPair_5_7_7_8_9: Choice_5_7_7 + Choice_5_8_9 <= 1
DifferentPair_5_7_7_9_6: Choice_5_7_7 + Choice_5_9_6 <= 1
DifferentPair_5_7_7_9_8: Choice_5_7_7 + Choice_5_9_8 <= 1
DifferentPair_5_7_8_5_7: Choice_5_5_7 + Choice_5_7_8 <= 1
DifferentPair_5_7_8_5_9: Choice_5_5_9 + Choice_5_7_8 <= 1
DifferentPair_5_7_8_6_6: Choice_5_6_6 + Choice_5_7_8 <= 1
DifferentPair_5_7_8_8_6: Choice_5_7_8 + Choice_5_8_6 <= 1
DifferentPair_5_7_8_9_7: Choice_5_7_8 + Choice_5_9_7 <= 1
DifferentPair_5_7_8_9_9: Choice_5_7_8 + Choice_5_9_9 <= 1
DifferentPair_5_7_9_5_8: Choice_5_5_8 + Choice_5_7_9 <= 1
DifferentPair_5_7_9_6_7: Choice_5_6_7 + Choice_5_7_9 <= 1
DifferentPair_5_7_9_8_7: Choice_5_7_9 + Choice_5_8_7 <= 1
DifferentPair_5_7_9_9_8: Choice_5_7_9 + Choice_5_9_8 <= 1
DifferentPair_5_8_1_6_2: Choice_5_6_2 + Choice_5_8_1 <= 1
DifferentPair_5_8_1_7_3: Choice_5_7_3 + Choice_5_8_1 <= 1
DifferentPair_5_8_1_9_3: Choice_5_8_1 + Choice_5_9_3 <= 1
DifferentPair_5_8_2_6_1: Choice_5_6_1 + Choice_5_8_2 <= 1
DifferentPair_5_8_2_6_3: Choice_5_6_3 + Choice_5_8_2 <= 1
DifferentPair_5_8_2_7_4: Choice_5_7_4 + Choice_5_8_2 <= 1
DifferentPair_5_8_2_9_4: Choice_5_8_2 + Choice_5_9_4 <= 1
DifferentPair_5_8_3_6_2: Choice_5_6_2 + Choice_5_8_3 <= 1
DifferentPair_5_8_3_6_4: Choice_5_6_4 + Choice_5_8_3 <= 1
DifferentPair_5_8_3_7_1: Choice_5_7_1 + Choice_5_8_3 <= 1
DifferentPair_5_8_3_7_5: Choice_5_7_5 + Choice_5_8_3 <= 1
DifferentPair_5_8_3_9_1: Choice_5_8_3 + Choice_5_9_1 <= 1
DifferentPair_5_8_3_9_5: Choice_5_8_3 + Choice_5_9_5 <= 1
DifferentPair_5_8_4_6_3: Choice_5_6_3 + Choice_5_8_4 <= 1
DifferentPair_5_8_4_6_5: Choice_5_6_5 + Choice_5_8_4 <= 1
DifferentPair_5_8_4_7_2: Choice_5_7_2 + Choice_5_8_4 <= 1
DifferentPair_5_8_4_7_6: Choice_5_7_6 + Choice_5_8_4 <= 1
DifferentPair_5_8_4_9_2: Choice_5_8_4 + Choice_5_9_2 <= 1
DifferentPair_5_8_4_9_6: Choice_5_8_4 + Choice_5_9_6 <= 1
DifferentPair_5_8_5_6_4: Choice_5_6_4 + Choice_5_8_5 <= 1
DifferentPair_5_8_5_6_6: Choice_5_6_6 + Choice_5_8_5 <= 1
DifferentPair_5_8_5_7_3: Choice_5_7_3 + Choice_5_8_5 <= 1
DifferentPair_5_8_5_7_7: Choice_5_7_7 + Choice_5_8_5 <= 1
DifferentPair_5_8_5_9_3: Choice_5_8_5 + Choice_5_9_3 <= 1
DifferentPair_5_8_5_9_7: Choice_5_8_5 + Choice_5_9_7 <= 1
DifferentPair_5_8_6_6_5: Choice_5_6_5 + Choice_5_8_6 <= 1
DifferentPair_5_8_6_6_7: Choice_5_6_7 + Choice_5_8_6 <= 1
DifferentPair_5_8_6_7_4: Choice_5_7_4 + Choice_5_8_6 <= 1
DifferentPair_5_8_6_7_8: Choice_5_7_8 + Choice_5_8_6 <= 1
DifferentPair_5_8_6_9_4: Choice_5_8_6 + Choice_5_9_4 <= 1
DifferentPair_5_8_6_9_8: Choice_5_8_6 + Choice_5_9_8 <= 1
DifferentPair_5_8_7_6_6: Choice_5_6_6 + Choice_5_8_7 <= 1
DifferentPair_5_8_7_6_8: Choice_5_6_8 + Choice_5_8_7 <= 1
DifferentPair_5_8_7_7_5: Choice_5_7_5 + Choice_5_8_7 <= 1
DifferentPair_5_8_7_7_9: Choice_5_7_9 + Choice_5_8_7 <= 1
DifferentPair_5_8_7_9_5: Choice_5_8_7 + Choice_5_9_5 <= 1
DifferentPair_5_8_7_9_9: Choice_5_8_7 + Choice_5_9_9 <= 1
DifferentPair_5_8_8_6_7: Choice_5_6_7 + Choice_5_8_8 <= 1
DifferentPair_5_8_8_6_9: Choice_5_6_9 + Choice_5_8_8 <= 1
DifferentPair_5_8_8_7_6: Choice_5_7_6 + Choice_5_8_8 <= 1
DifferentPair_5_8_8_9_6: Choice_5_8_8 + Choice_5_9_6 <= 1
DifferentPair_5_8_9_6_8: Choice_5_6_8 + Choice_5_8_9 <= 1
DifferentPair_5_8_9_7_7: Choice_5_7_7 + Choice_5_8_9 <= 1
DifferentPair_5_8_9_9_7: Choice_5_8_9 + Choice_5_9_7 <= 1
DifferentPair_5_9_1_7_2: Choice_5_7_2 + Choice_5_9_1 <= 1
DifferentPair_5_9_1_8_3: Choice_5_8_3 + Choice_5_9_1 <= 1
DifferentPair_5_9_2_7_1: Choice_5_7_1 + Choice_5_9_2 <= 1
DifferentPair_5_9_2_7_3: Choice_5_7_3 + Choice_5_9_2 <= 1
DifferentPair_5_9_2_8_4: Choice_5_8_4 + Choice_5_9_2 <= 1
DifferentPair_5_9_3_7_2: Choice_5_7_2 + Choice_5_9_3 <= 1
DifferentPair_5_9_3_7_4: Choice_5_7_4 + Choice_5_9_3 <= 1
DifferentPair_5_9_3_8_1: Choice_5_8_1 + Choice_5_9_3 <= 1
DifferentPair_5_9_3_8_5: Choice_5_8_5 + Choice_5_9_3 <= 1
DifferentPair_5_9_4_7_3: Choice_5_7_3 + Choice_5_9_4 <= 1
DifferentPair_5_9_4_7_5: Choice_5_7_5 + Choice_5_9_4 <= 1
DifferentPair_5_9_4_8_2: Choice_5_8_2 + Choice_5_9_4 <= 1
DifferentPair_5_9_4_8_6: Choice_5_8_6 + Choice_5_9_4 <= 1
DifferentPair_5_9_5_7_4: Choice_5_7_4 + Choice_5_9_5 <= 1
DifferentPair_5_9_5_7_6: Choice_5_7_6 + Choice_5_9_5 <= 1
DifferentPair_5_9_5_8_3: Choice_5_8_3 + Choice_5_9_5 <= 1
DifferentPair_5_9_5_8_7: Choice_5_8_7 + Choice_5_9_5 <= 1
DifferentPair_5_9_6_7_5: Choice_5_7_5 + Choice_5_9_6 <= 1
DifferentPair_5_9_6_7_7: Choice_5_7_7 + Choice_5_9_6 <= 1
DifferentPair_5_9_6_8_4: Choice_5_8_4 + Choice_5_9_6 <= 1
DifferentPair_5_9_6_8_8: Choice_5_8_8 + Choice_5_9_6 <= 1
DifferentPair_5_9_7_7_6: Choice_5_7_6 + Choice_5_9_7 <= 1
DifferentPair_5_9_7_7_8: Choice_5_7_8 + Choice_5_9_7 <= 1
DifferentPair_5_9_7_8_5: Choice_5_8_5 + Choice_5_9_7 <= 1
DifferentPair_5_9_7_8_9: Choice_5_8_9 + Choice_5_9_7 <= 1
DifferentPair_5_9_8_7_7: Choice_5_7_7 + Choice_5_9_8 <= 1
DifferentPair_5_9_8_7_9: Choice_5_7_9 + Choice_5_9_8 <= 1
DifferentPair_5_9_8_8_6: Choice_5_8_6 + Choice_5_9_8 <= 1
DifferentPair_5_9_9_7_8: Choice_5_7_8 + Choice_5_9_9 <= 1
DifferentPair_5_9_9_8_7: Choice_5_8_7 + Choice_5_9_9 <= 1
DifferentPair_6_1_1_2_3: Choice_6_1_1 + Choice_6_2_3 <= 1
DifferentPair_6_1_1_3_2: Choice_6_1_1 + Choice_6_3_2 <= 1
DifferentPair_6_1_2_2_4: Choice_6_1_2 + Choice_6_2_4 <= 1
DifferentPair_6_1_2_3_1: Choice_6_1_2 + Choice_6_3_1 <= 1
DifferentPair_6_1_2_3_3: Choice_6_1_2 + Choice_6_3_3 <= 1
DifferentPair_6_1_3_2_1: Choice_6_1_3 + Choice_6_2_1 <= 1
DifferentPair_6_1_3_2_5: Choice_6_1_3 + Choice_6_2_5 <= 1
DifferentPair_6_1_3_3_2: Choice_6_1_3 + Choice_6_3_2 <= 1
DifferentPair_6_1_3_3_4: Choice_6_1_3 + Choice_6_3_4 <= 1
DifferentPair_6_1_4_2_2: Choice_6_1_4 + Choice_6_2_2 <= 1
DifferentPair_6_1_4_2_6: Choice_6_1_4 + Choice_6_2_6 <= 1
DifferentPair_6_1_4_3_3: Choice_6_1_4 + Choice_6_3_3 <= 1
DifferentPair_6_1_4_3_5: Choice_6_1_4 + Choice_6_3_5 <= 1
DifferentPair_6_1_5_2_3: Choice_6_1_5 + Choice_6_2_3 <= 1
DifferentPair_6_1_5_2_7: Choice_6_1_5 + Choice_6_2_7 <= 1
DifferentPair_6_1_5_3_4: Choice_6_1_5 + Choice_6_3_4 <= 1
DifferentPair_6_1_5_3_6: Choice_6_1_5 + Choice_6_3_6 <= 1
DifferentPair_6_1_6_2_4: Choice_6_1_6 + Choice_6_2_4 <= 1
DifferentPair_6_1_6_2_8: Choice_6_1_6 + Choice_6_2_8 <= 1
DifferentPair_6_1_6_3_5: Choice_6_1_6 + Choice_6_3_5 <= 1
DifferentPair_6_1_6_3_7: Choice_6_1_6 + Choice_6_3_7 <= 1
DifferentPair_6_1_7_2_5: Choice_6_1_7 + Choice_6_2_5 <= 1
DifferentPair_6_1_7_2_9: Choice_6_1_7 + Choice_6_2_9 <= 1
DifferentPair_6_1_7_3_6: Choice_6_1_7 + Choice_6_3_6 <= 1
DifferentPair_6_1_7_3_8: Choice_6_1_7 + Choice_6_3_8 <= 1
DifferentPair_6_1_8_2_6: Choice_6_1_8 + Choice_6_2_6 <= 1
DifferentPair_6_1_8_3_7: Choice_6_1_8 + Choice_6_3_7 <= 1
DifferentPair_6_1_8_3_9: Choice_6_1_8 + Choice_6_3_9 <= 1
DifferentPair_6_1_9_2_7: Choice_6_1_9 + Choice_6_2_7 <= 1
DifferentPair_6_1_9_3_8: Choice_6_1_9 + Choice_6_3_8 <= 1
DifferentPair_6_2_1_1_3: Choice_6_1_3 + Choice_6_2_1 <= 1
DifferentPair_6_2_1_3_3: Choice_6_2_1 + Choice_6_3_3 <= 1
DifferentPair_6_2_1_4_2: Choice_6_2_1 + Choice_6_4_2 <= 1
DifferentPair_6_2_2_1_4: Choice_6_1_4 + Choice_6_2_2 <= 1
DifferentPair_6_2_2_3_4: Choice_6_2_2 + Choice_6_3_4 <= 1
DifferentPair_6_2_2_4_1: Choice_6_2_2 + Choice_6_4_1 <= 1
DifferentPair_6_2_2_4_3: Choice_6_2_2 + Choice_6_4_3 <= 1
DifferentPair_6_2_3_1_1: Choice_6_1_1 + Choice_6_2_3 <= 1
DifferentPair_6_2_3_1_5: Choice_6_1_5 + Choice_6_2_3 <= 1
DifferentPair_6_2_3_3_1: Choice_6_2_3 + Choice_6_3_1 <= 1
DifferentPair_6_2_3_3_5: Choice_6_2_3 + Choice_6_3_5 <= 1
DifferentPair_6_2_3_4_2: Choice_6_2_3 + Choice_6_4_2 <= 1
DifferentPair_6_2_3_4_4: Choice_6_2_3 + Choice_6_4_4 <= 1
DifferentPair_6_2_4_1_2: Choice_6_1_2 + Choice_6_2_4 <= 1
DifferentPair_6_2_4_1_6: Choice_6_1_6 + Choice_6_2_4 <= 1
DifferentPair_6_2_4_3_2: Choice_6_2_4 + Choice_6_3_2 <= 1
DifferentPair_6_2_4_3_6: Choice_6_2_4 + Choice_6_3_6 <= 1
DifferentPair_6_2_4_4_3: Choice_6_2_4 + Choice_6_4_3 <= 1
DifferentPair_6_2_4_4_5: Choice_6_2_4 + Choice_6_4_5 <= 1
DifferentPair_6_2_5_1_3: Choice_6_1_3 + Choice_6_2_5 <= 1
DifferentPair_6_2_5_1_7: Choice_6_1_7 + Choice_6_2_5 <= 1
DifferentPair_6_2_5_3_3: Choice_6_2_5 + Choice_6_3_3 <= 1
DifferentPair_6_2_5_3_7: Choice_6_2_5 + Choice_6_3_7 <= 1
DifferentPair_6_2_5_4_4: Choice_6_2_5 + Choice_6_4_4 <= 1
DifferentPair_6_2_5_4_6: Choice_6_2_5 + Choice_6_4_6 <= 1
DifferentPair_6_2_6_1_4: Choice_6_1_4 + Choice_6_2_6 <= 1
DifferentPair_6_2_6_1_8: Choice_6_1_8 + Choice_6_2_6 <= 1
DifferentPair_6_2_6_3_4: Choice_6_2_6 + Choice_6_3_4 <= 1
DifferentPair_6_2_6_3_8: Choice_6_2_6 + Choice_6_3_8 <= 1
DifferentPair_6_2_6_4_5: Choice_6_2_6 + Choice_6_4_5 <= 1
DifferentPair_6_2_6_4_7: Choice_6_2_6 + Choice_6_4_7 <= 1
DifferentPair_6_2_7_1_5: Choice_6_1_5 + Choice_6_2_7 <= 1
DifferentPair_6_2_7_1_9: Choice_6_1_9 + Choice_6_2_7 <= 1
DifferentPair_6_2_7_3_5: Choice_6_2_7 + Choice_6_3_5 <= 1
DifferentPair_6_2_7_3_9: Choice_6_2_7 + Choice_6_3_9 <= 1
DifferentPair_6_2_7_4_6: Choice_6_2_7 + Choice_6_4_6 <= 1
DifferentPair_6_2_7_4_8: Choice_6_2_7 + Choice_6_4_8 <= 1
DifferentPair_6_2_8_1_6: Choice_6_1_6 + Choice_6_2_8 <= 1
DifferentPair_6_2_8_3_6: Choice_6_2_8 + Choice_6_3_6 <= 1
DifferentPair_6_2_8_4_7: Choice_6_2_8 + Choice_6_4_7 <= 1
DifferentPair_6_2_8_4_9: Choice_6_2_8 + Choice_6_4_9 <= 1
DifferentPair_6_2_9_1_7: Choice_6_1_7 + Choice_6_2_9 <= 1
DifferentPair_6_2_9_3_7: Choice_6_2_9 + Choice_6_3_7 <= 1
DifferentPair_6_2_9_4_8: Choice_6_2_9 + Choice_6_4_8 <= 1
DifferentPair_6_3_1_1_2: Choice_6_1_2 + Choice_6_3_1 <= 1
DifferentPair_6_3_1_2_3: Choice_6_2_3 + Choice_6_3_1 <= 1
DifferentPair_6_3_1_4_3: Choice_6_3_1 + Choice_6_4_3 <= 1
DifferentPair_6_3_1_5_2: Choice_6_3_1 + Choice_6_5_2 <= 1
DifferentPair_6_3_2_1_1: Choice_6_1_1 + Choice_6_3_2 <= 1
DifferentPair_6_3_2_1_3: Choice_6_1_3 + Choice_6_3_2 <= 1
DifferentPair_6_3_2_2_4: Choice_6_2_4 + Choice_6_3_2 <= 1
DifferentPair_6_3_2_4_4: Choice_6_3_2 + Choice_6_4_4 <= 1
DifferentPair_6_3_2_5_1: Choice_6_3_2 + Choice_6_5_1 <= 1
DifferentPair_6_3_2_5_3: Choice_6_3_2 + Choice_6_5_3 <= 1
DifferentPair_6_3_3_1_2: Choice_6_1_2 + Choice_6_3_3 <= 1
DifferentPair_6_3_3_1_4: Choice_6_1_4 + Choice_6_3_3 <= 1
DifferentPair_6_3_3_2_1: Choice_6_2_1 + Choice_6_3_3 <= 1
DifferentPair_6_3_3_2_5: Choice_6_2_5 + Choice_6_3_3 <= 1
DifferentPair_6_3_3_4_1: Choice_6_3_3 + Choice_6_4_1 <= 1
DifferentPair_6_3_3_4_5: Choice_6_3_3 + Choice_6_4_5 <= 1
DifferentPair_6_3_3_5_2: Choice_6_3_3 + Choice_6_5_2 <= 1
DifferentPair_6_3_3_5_4: Choice_6_3_3 + Choice_6_5_4 <= 1
DifferentPair_6_3_4_1_3: Choice_6_1_3 + Choice_6_3_4 <= 1
DifferentPair_6_3_4_1_5: Choice_6_1_5 + Choice_6_3_4 <= 1
DifferentPair_6_3_4_2_2: Choice_6_2_2 + Choice_6_3_4 <= 1
DifferentPair_6_3_4_2_6: Choice_6_2_6 + Choice_6_3_4 <= 1
DifferentPair_6_3_4_4_2: Choice_6_3_4 + Choice_6_4_2 <= 1
DifferentPair_6_3_4_4_6: Choice_6_3_4 + Choice_6_4_6 <= 1
DifferentPair_6_3_4_5_3: Choice_6_3_4 + Choice_6_5_3 <= 1
DifferentPair_6_3_4_5_5: Choice_6_3_4 + Choice_6_5_5 <= 1
DifferentPair_6_3_5_1_4: Choice_6_1_4 + Choice_6_3_5 <= 1
DifferentPair_6_3_5_1_6: Choice_6_1_6 + Choice_6_3_5 <= 1
DifferentPair_6_3_5_2_3: Choice_6_2_3 + Choice_6_3_5 <= 1
DifferentPair_6_3_5_2_7: Choice_6_2_7 + Choice_6_3_5 <= 1
DifferentPair_6_3_5_4_3: Choice_6_3_5 + Choice_6_4_3 <= 1
DifferentPair_6_3_5_4_7: Choice_6_3_5 + Choice_6_4_7 <= 1
DifferentPair_6_3_5_5_4: Choice_6_3_5 + Choice_6_5_4 <= 1
DifferentPair_6_3_5_5_6: Choice_6_3_5 + Choice_6_5_6 <= 1
DifferentPair_6_3_6_1_5: Choice_6_1_5 + Choice_6_3_6 <= 1
DifferentPair_6_3_6_1_7: Choice_6_1_7 + Choice_6_3_6 <= 1
DifferentPair_6_3_6_2_4: Choice_6_2_4 + Choice_6_3_6 <= 1
DifferentPair_6_3_6_2_8: Choice_6_2_8 + Choice_6_3_6 <= 1
DifferentPair_6_3_6_4_4: Choice_6_3_6 + Choice_6_4_4 <= 1
DifferentPair_6_3_6_4_8: Choice_6_3_6 + Choice_6_4_8 <= 1
DifferentPair_6_3_6_5_5: Choice_6_3_6 + Choice_6_5_5 <= 1
DifferentPair_6_3_6_5_7: Choice_6_3_6 + Choice_6_5_7 <= 1
DifferentPair_6_3_7_1_6: Choice_6_1_6 + Choice_6_3_7 <= 1
DifferentPair_6_3_7_1_8: Choice_6_1_8 + Choice_6_3_7 <= 1
DifferentPair_6_3_7_2_5: Choice_6_2_5 + Choice_6_3_7 <= 1
DifferentPair_6_3_7_2_9: Choice_6_2_9 + Choice_6_3_7 <= 1
DifferentPair_6_3_7_4_5: Choice_6_3_7 + Choice_6_4_5 <= 1
DifferentPair_6_3_7_4_9: Choice_6_3_7 + Choice_6_4_9 <= 1
DifferentPair_6_3_7_5_6: Choice_6_3_7 + Choice_6_5_6 <= 1
DifferentPair_6_3_7_5_8: Choice_6_3_7 + Choice_6_5_8 <= 1
DifferentPair_6_3_8_1_7: Choice_6_1_7 + Choice_6_3_8 <= 1
DifferentPair_6_3_8_1_9: Choice_6_1_9 + Choice_6_3_8 <= 1
DifferentPair_6_3_8_2_6: Choice_6_2_6 + Choice_6_3_8 <= 1
DifferentPair_6_3_8_4_6: Choice_6_3_8 + Choice_6_4_6 <= 1
DifferentPair_6_3_8_5_7: Choice_6_3_8 + Choice_6_5_7 <= 1
DifferentPair_6_3_8_5_9: Choice_6_3_8 + Choice_6_5_9 <= 1
DifferentPair_6_3_9_1_8: Choice_6_1_8 + Choice_6_3_9 <= 1
DifferentPair_6_3_9_2_7: Choice_6_2_7 + Choice_6_3_9 <= 1
DifferentPair_6_3_9_4_7: Choice_6_3_9 + Choice_6_4_7 <= 1
DifferentPair_6_3_9_5_8: Choice_6_3_9 + Choice_6_5_8 <= 1
DifferentPair_6_4_1_2_2: Choice_6_2_2 + Choice_6_4_1 <= 1
DifferentPair_6_4_1_3_3: Choice_6_3_3 + Choice_6_4_1 <= 1
DifferentPair_6_4_1_5_3: Choice_6_4_1 + Choice_6_5_3 <= 1
DifferentPair_6_4_1_6_2: Choice_6_4_1 + Choice_6_6_2 <= 1
DifferentPair_6_4_2_2_1: Choice_6_2_1 + Choice_6_4_2 <= 1
DifferentPair_6_4_2_2_3: Choice_6_2_3 + Choice_6_4_2 <= 1
DifferentPair_6_4_2_3_4: Choice_6_3_4 + Choice_6_4_2 <= 1
DifferentPair_6_4_2_5_4: Choice_6_4_2 + Choice_6_5_4 <= 1
DifferentPair_6_4_2_6_1: Choice_6_4_2 + Choice_6_6_1 <= 1
DifferentPair_6_4_2_6_3: Choice_6_4_2 + Choice_6_6_3 <= 1
DifferentPair_6_4_3_2_2: Choice_6_2_2 + Choice_6_4_3 <= 1
DifferentPair_6_4_3_2_4: Choice_6_2_4 + Choice_6_4_3 <= 1
DifferentPair_6_4_3_3_1: Choice_6_3_1 + Choice_6_4_3 <= 1
DifferentPair_6_4_3_3_5: Choice_6_3_5 + Choice_6_4_3 <= 1
DifferentPair_6_4_3_5_1: Choice_6_4_3 + Choice_6_5_1 <= 1
DifferentPair_6_4_3_5_5: Choice_6_4_3 + Choice_6_5_5 <= 1
DifferentPair_6_4_3_6_2: Choice_6_4_3 + Choice_6_6_2 <= 1
DifferentPair_6_4_3_6_4: Choice_6_4_3 + Choice_6_6_4 <= 1
DifferentPair_6_4_4_2_3: Choice_6_2_3 + Choice_6_4_4 <= 1
DifferentPair_6_4_4_2_5: Choice_6_2_5 + Choice_6_4_4 <= 1
DifferentPair_6_4_4_3_2: Choice_6_3_2 + Choice_6_4_4 <= 1
DifferentPair_6_4_4_3_6: Choice_6_3_6 + Choice_6_4_4 <= 1
DifferentPair_6_4_4_5_2: Choice_6_4_4 + Choice_6_5_2 <= 1
DifferentPair_6_4_4_5_6: Choice_6_4_4 + Choice_6_5_6 <= 1
DifferentPair_6_4_4_6_3: Choice_6_4_4 + Choice_6_6_3 <= 1
DifferentPair_6_4_4_6_5: Choice_6_4_4 + Choice_6_6_5 <= 1
DifferentPair_6_4_5_2_4: Choice_6_2_4 + Choice_6_4_5 <= 1
DifferentPair_6_4_5_2_6: Choice_6_2_6 + Choice_6_4_5 <= 1
DifferentPair_6_4_5_3_3: Choice_6_3_3 + Choice_6_4_5 <= 1
DifferentPair_6_4_5_3_7: Choice_6_3_7 + Choice_6_4_5 <= 1
DifferentPair_6_4_5_5_3: Choice_6_4_5 + Choice_6_5_3 <= 1
DifferentPair_6_4_5_5_7: Choice_6_4_5 + Choice_6_5_7 <= 1
DifferentPair_6_4_5_6_4: Choice_6_4_5 + Choice_6_6_4 <= 1
DifferentPair_6_4_5_6_6: Choice_6_4_5 + Choice_6_6_6 <= 1
DifferentPair_6_4_6_2_5: Choice_6_2_5 + Choice_6_4_6 <= 1
DifferentPair_6_4_6_2_7: Choice_6_2_7 + Choice_6_4_6 <= 1
DifferentPair_6_4_6_3_4: Choice_6_3_4 + Choice_6_4_6 <= 1
DifferentPair_6_4_6_3_8: Choice_6_3_8 + Choice_6_4_6 <= 1
DifferentPair_6_4_6_5_4: Choice_6_4_6 + Choice_6_5_4 <= 1
DifferentPair_6_4_6_5_8: Choice_6_4_6 + Choice_6_5_8 <= 1
DifferentPair_6_4_6_6_5: Choice_6_4_6 + Choice_6_6_5 <= 1
DifferentPair_6_4_6_6_7: Choice_6_4_6 + Choice_6_6_7 <= 1
DifferentPair_6_4_7_2_6: Choice_6_2_6 + Choice_6_4_7 <= 1
DifferentPair_6_4_7_2_8: Choice_6_2_8 + Choice_6_4_7 <= 1
DifferentPair_6_4_7_3_5: Choice_6_3_5 + Choice_6_4_7 <= 1
DifferentPair_6_4_7_3_9: Choice_6_3_9 + Choice_6_4_7 <= 1
DifferentPair_6_4_7_5_5: Choice_6_4_7 + Choice_6_5_5 <= 1
DifferentPair_6_4_7_5_9: Choice_6_4_7 + Choice_6_5_9 <= 1
DifferentPair_6_4_7_6_6: Choice_6_4_7 + Choice_6_6_6 <= 1
DifferentPair_6_4_7_6_8: Choice_6_4_7 + Choice_6_6_8 <= 1
DifferentPair_6_4_8_2_7: Choice_6_2_7 + Choice_6_4_8 <= 1
DifferentPair_6_4_8_2_9: Choice_6_2_9 + Choice_6_4_8 <= 1
DifferentPair_6_4_8_3_6: Choice_6_3_6 + Choice_6_4_8 <= 1
DifferentPair_6_4_8_5_6: Choice_6_4_8 + Choice_6_5_6 <= 1
DifferentPair_6_4_8_6_7: Choice_6_4_8 + Choice_6_6_7 <= 1
DifferentPair_6_4_8_6_9: Choice_6_4_8 + Choice_6_6_9 <= 1
DifferentPair_6_4_9_2_8: Choice_6_2_8 + Choice_6_4_9 <= 1
DifferentPair_6_4_9_3_7: Choice_6_3_7 + Choice_6_4_9 <= 1
DifferentPair_6_4_9_5_7: Choice_6_4_9 + Choice_6_5_7 <= 1
DifferentPair_6_4_9_6_8: Choice_6_4_9 + Choice_6_6_8 <= 1
DifferentPair_6_5_1_3_2: Choice_6_3_2 + Choice_6_5_1 <= 1
DifferentPair_6_5_1_4_3: Choice_6_4_3 + Choice_6_5_1 <= 1
DifferentPair_6_5_1_6_3: Choice_6_5_1 + Choice_6_6_3 <= 1
DifferentPair_6_5_1_7_2: Choice_6_5_1 + Choice_6_7_2 <= 1
DifferentPair_6_5_2_3_1: Choice_6_3_1 + Choice_6_5_2 <= 1
DifferentPair_6_5_2_3_3: Choice_6_3_3 + Choice_6_5_2 <= 1
DifferentPair_6_5_2_4_4: Choice_6_4_4 + Choice_6_5_2 <= 1
DifferentPair_6_5_2_6_4: Choice_6_5_2 + Choice_6_6_4 <= 1
DifferentPair_6_5_2_7_1: Choice_6_5_2 + Choice_6_7_1 <= 1
DifferentPair_6_5_2_7_3: Choice_6_5_2 + Choice_6_7_3 <= 1
DifferentPair_6_5_3_3_2: Choice_6_3_2 + Choice_6_5_3 <= 1
DifferentPair_6_5_3_3_4: Choice_6_3_4 + Choice_6_5_3 <= 1
DifferentPair_6_5_3_4_1: Choice_6_4_1 + Choice_6_5_3 <= 1
DifferentPair_6_5_3_4_5: Choice_6_4_5 + Choice_6_5_3 <= 1
DifferentPair_6_5_3_6_1: Choice_6_5_3 + Choice_6_6_1 <= 1
DifferentPair_6_5_3_6_5: Choice_6_5_3 + Choice_6_6_5 <= 1
DifferentPair_6_5_3_7_2: Choice_6_5_3 + Choice_6_7_2 <= 1
DifferentPair_6_5_3_7_4: Choice_6_5_3 + Choice_6_7_4 <= 1
DifferentPair_6_5_4_3_3: Choice_6_3_3 + Choice_6_5_4 <= 1
DifferentPair_6_5_4_3_5: Choice_6_3_5 + Choice_6_5_4 <= 1
DifferentPair_6_5_4_4_2: Choice_6_4_2 + Choice_6_5_4 <= 1
DifferentPair_6_5_4_4_6: Choice_6_4_6 + Choice_6_5_4 <= 1
DifferentPair_6_5_4_6_2: Choice_6_5_4 + Choice_6_6_2 <= 1
DifferentPair_6_5_4_6_6: Choice_6_5_4 + Choice_6_6_6 <= 1
DifferentPair_6_5_4_7_3: Choice_6_5_4 + Choice_6_7_3 <= 1
DifferentPair_6_5_4_7_5: Choice_6_5_4 + Choice_6_7_5 <= 1
DifferentPair_6_5_5_3_4: Choice_6_3_4 + Choice_6_5_5 <= 1
DifferentPair_6_5_5_3_6: Choice_6_3_6 + Choice_6_5_5 <= 1
DifferentPair_6_5_5_4_3: Choice_6_4_3 + Choice_6_5_5 <= 1
DifferentPair_6_5_5_4_7: Choice_6_4_7 + Choice_6_5_5 <= 1
DifferentPair_6_5_5_6_3: Choice_6_5_5 + Choice_6_6_3 <= 1
DifferentPair_6_5_5_6_7: Choice_6_5_5 + Choice_6_6_7 <= 1
DifferentPair_6_5_5_7_4: Choice_6_5_5 + Choice_6_7_4 <= 1
DifferentPair_6_5_5_7_6: Choice_6_5_5 + Choice_6_7_6 <= 1
DifferentPair_6_5_6_3_5: Choice_6_3_5 + Choice_6_5_6 <= 1
DifferentPair_6_5_6_3_7: Choice_6_3_7 + Choice_6_5_6 <= 1
DifferentPair_6_5_6_4_4: Choice_6_4_4 + Choice_6_5_6 <= 1
DifferentPair_6_5_6_4_8: Choice_6_4_8 + Choice_6_5_6 <= 1
DifferentPair_6_5_6_6_4: Choice_6_5_6 + Choice_6_6_4 <= 1
DifferentPair_6_5_6_6_8: Choice_6_5_6 + Choice_6_6_8 <= 1
DifferentPair_6_5_6_7_5: Choice_6_5_6 + Choice_6_7_5 <= 1
DifferentPair_6_5_6_7_7: Choice_6_5_6 + Choice_6_7_7 <= 1
DifferentPair_6_5_7_3_6: Choice_6_3_6 + Choice_6_5_7 <= 1
DifferentPair_6_5_7_3_8: Choice_6_3_8 + Choice_6_5_7 <= 1
DifferentPair_6_5_7_4_5: Choice_6_4_5 + Choice_6_5_7 <= 1
DifferentPair_6_5_7_4_9: Choice_6_4_9 + Choice_6_5_7 <= 1
DifferentPair_6_5_7_6_5: Choice_6_5_7 + Choice_6_6_5 <= 1
DifferentPair_6_5_7_6_9: Choice_6_5_7 + Choice_6_6_9 <= 1
DifferentPair_6_5_7_7_6: Choice_6_5_7 + Choice_6_7_6 <= 1
DifferentPair_6_5_7_7_8: Choice_6_5_7 + Choice_6_7_8 <= 1
DifferentPair_6_5_8_3_7: Choice_6_3_7 + Choice_6_5_8 <= 1
DifferentPair_6_5_8_3_9: Choice_6_3_9 + Choice_6_5_8 <= 1
DifferentPair_6_5_8_4_6: Choice_6_4_6 + Choice_6_5_8 <= 1
DifferentPair_6_5_8_6_6: Choice_6_5_8 + Choice_6_6_6 <= 1
DifferentPair_6_5_8_7_7: Choice_6_5_8 + Choice_6_7_7 <= 1
DifferentPair_6_5_8_7_9: Choice_6_5_8 + Choice_6_7_9 <= 1
DifferentPair_6_5_9_3_8: Choice_6_3_8 + Choice_6_5_9 <= 1
DifferentPair_6_5_9_4_7: Choice_6_4_7 + Choice_6_5_9 <= 1
DifferentPair_6_5_9_6_7: Choice_6_5_9 + Choice_6_6_7 <= 1
DifferentPair_6_5_9_7_8: Choice_6_5_9 + Choice_6_7_8 <= 1
DifferentPair_6_6_1_4_2: Choice_6_4_2 + Choice_6_6_1 <= 1
DifferentPair_6_6_1_5_3: Choice_6_5_3 + Choice_6_6_1 <= 1
DifferentPair_6_6_1_7_3: Choice_6_6_1 + Choice_6_7_3 <= 1
DifferentPair_6_6_1_8_2: Choice_6_6_1 + Choice_6_8_2 <= 1
DifferentPair_6_6_2_4_1: Choice_6_4_1 + Choice_6_6_2 <= 1
DifferentPair_6_6_2_4_3: Choice_6_4_3 + Choice_6_6_2 <= 1
DifferentPair_6_6_2_5_4: Choice_6_5_4 + Choice_6_6_2 <= 1
DifferentPair_6_6_2_7_4: Choice_6_6_2 + Choice_6_7_4 <= 1
DifferentPair_6_6_2_8_1: Choice_6_6_2 + Choice_6_8_1 <= 1
DifferentPair_6_6_2_8_3: Choice_6_6_2 + Choice_6_8_3 <= 1
DifferentPair_6_6_3_4_2: Choice_6_4_2 + Choice_6_6_3 <= 1
DifferentPair_6_6_3_4_4: Choice_6_4_4 + Choice_6_6_3 <= 1
DifferentPair_6_6_3_5_1: Choice_6_5_1 + Choice_6_6_3 <= 1
DifferentPair_6_6_3_5_5: Choice_6_5_5 + Choice_6_6_3 <= 1
DifferentPair_6_6_3_7_1: Choice_6_6_3 + Choice_6_7_1 <= 1
DifferentPair_6_6_3_7_5: Choice_6_6_3 + Choice_6_7_5 <= 1
DifferentPair_6_6_3_8_2: Choice_6_6_3 + Choice_6_8_2 <= 1
DifferentPair_6_6_3_8_4: Choice_6_6_3 + Choice_6_8_4 <= 1
DifferentPair_6_6_4_4_3: Choice_6_4_3 + Choice_6_6_4 <= 1
DifferentPair_6_6_4_4_5: Choice_6_4_5 + Choice_6_6_4 <= 1
DifferentPair_6_6_4_5_2: Choice_6_5_2 + Choice_6_6_4 <= 1
DifferentPair_6_6_4_5_6: Choice_6_5_6 + Choice_6_6_4 <= 1
DifferentPair_6_6_4_7_2: Choice_6_6_4 + Choice_6_7_2 <= 1
DifferentPair_6_6_4_7_6: Choice_6_6_4 + Choice_6_7_6 <= 1
DifferentPair_6_6_4_8_3: Choice_6_6_4 + Choice_6_8_3 <= 1
DifferentPair_6_6_4_8_5: Choice_6_6_4 + Choice_6_8_5 <= 1
DifferentPair_6_6_5_4_4: Choice_6_4_4 + Choice_6_6_5 <= 1
DifferentPair_6_6_5_4_6: Choice_6_4_6 + Choice_6_6_5 <= 1
DifferentPair_6_6_5_5_3: Choice_6_5_3 + Choice_6_6_5 <= 1
DifferentPair_6_6_5_5_7: Choice_6_5_7 + Choice_6_6_5 <= 1
DifferentPair_6_6_5_7_3: Choice_6_6_5 + Choice_6_7_3 <= 1
DifferentPair_6_6_5_7_7: Choice_6_6_5 + Choice_6_7_7 <= 1
DifferentPair_6_6_5_8_4: Choice_6_6_5 + Choice_6_8_4 <= 1
DifferentPair_6_6_5_8_6: Choice_6_6_5 + Choice_6_8_6 <= 1
DifferentPair_6_6_6_4_5: Choice_6_4_5 + Choice_6_6_6 <= 1
DifferentPair_6_6_6_4_7: Choice_6_4_7 + Choice_6_6_6 <= 1
DifferentPair_6_6_6_5_4: Choice_6_5_4 + Choice_6_6_6 <= 1
DifferentPair_6_6_6_5_8: Choice_6_5_8 + Choice_6_6_6 <= 1
DifferentPair_6_6_6_7_4: Choice_6_6_6 + Choice_6_7_4 <= 1
DifferentPair_6_6_6_7_8: Choice_6_6_6 + Choice_6_7_8 <= 1
DifferentPair_6_6_6_8_5: Choice_6_6_6 + Choice_6_8_5 <= 1
DifferentPair_6_6_6_8_7: Choice_6_6_6 + Choice_6_8_7 <= 1
DifferentPair_6_6_7_4_6: Choice_6_4_6 + Choice_6_6_7 <= 1
DifferentPair_6_6_7_4_8: Choice_6_4_8 + Choice_6_6_7 <= 1
DifferentPair_6_6_7_5_5: Choice_6_5_5 + Choice_6_6_7 <= 1
DifferentPair_6_6_7_5_9: Choice_6_5_9 + Choice_6_6_7 <= 1
DifferentPair_6_6_7_7_5: Choice_6_6_7 + Choice_6_7_5 <= 1
DifferentPair_6_6_7_7_9: Choice_6_6_7 + Choice_6_7_9 <= 1
DifferentPair_6_6_7_8_6: Choice_6_6_7 + Choice_6_8_6 <= 1
DifferentPair_6_6_7_8_8: Choice_6_6_7 + Choice_6_8_8 <= 1
DifferentPair_6_6_8_4_7: Choice_6_4_7 + Choice_6_6_8 <= 1
DifferentPair_6_6_8_4_9: Choice_6_4_9 + Choice_6_6_8 <= 1
DifferentPair_6_6_8_5_6: Choice_6_5_6 + Choice_6_6_8 <= 1
DifferentPair_6_6_8_7_6: Choice_6_6_8 + Choice_6_7_6 <= 1
DifferentPair_6_6_8_8_7: Choice_6_6_8 + Choice_6_8_7 <= 1
DifferentPair_6_6_8_8_9: Choice_6_6_8 + Choice_6_8_9 <= 1
DifferentPair_6_6_9_4_8: Choice_6_4_8 + Choice_6_6_9 <= 1
DifferentPair_6_6_9_5_7: Choice_6_5_7 + Choice_6_6_9 <= 1
DifferentPair_6_6_9_7_7: Choice_6_6_9 + Choice_6_7_7 <= 1
DifferentPair_6_6_9_8_8: Choice_6_6_9 + Choice_6_8_8 <= 1
DifferentPair_6_7_1_5_2: Choice_6_5_2 + Choice_6_7_1 <= 1
DifferentPair_6_7_1_6_3: Choice_6_6_3 + Choice_6_7_1 <= 1
DifferentPair_6_7_1_8_3: Choice_6_7_1 + Choice_6_8_3 <= 1
DifferentPair_6_7_1_9_2: Choice_6_7_1 + Choice_6_9_2 <= 1
DifferentPair_6_7_2_5_1: Choice_6_5_1 + Choice_6_7_2 <= 1
DifferentPair_6_7_2_5_3: Choice_6_5_3 + Choice_6_7_2 <= 1
DifferentPair_6_7_2_6_4: Choice_6_6_4 + Choice_6_7_2 <= 1
DifferentPair_6_7_2_8_4: Choice_6_7_2 + Choice_6_8_4 <= 1
DifferentPair_6_7_2_9_1: Choice_6_7_2 + Choice_6_9_1 <= 1
DifferentPair_6_7_2_9_3: Choice_6_7_2 + Choice_6_9_3 <= 1
DifferentPair_6_7_3_5_2: Choice_6_5_2 + Choice_6_7_3 <= 1
DifferentPair_6_7_3_5_4: Choice_6_5_4 + Choice_6_7_3 <= 1
DifferentPair_6_7_3_6_1: Choice_6_6_1 + Choice_6_7_3 <= 1
DifferentPair_6_7_3_6_5: Choice_6_6_5 + Choice_6_7_3 <= 1
DifferentPair_6_7_3_8_1: Choice_6_7_3 + Choice_6_8_1 <= 1
DifferentPair_6_7_3_8_5: Choice_6_7_3 + Choice_6_8_5 <= 1
DifferentPair_6_7_3_9_2: Choice_6_7_3 + Choice_6_9_2 <= 1
DifferentPair_6_7_3_9_4: Choice_6_7_3 + Choice_6_9_4 <= 1
DifferentPair_6_7_4_5_3: Choice_6_5_3 + Choice_6_7_4 <= 1
DifferentPair_6_7_4_5_5: Choice_6_5_5 + Choice_6_7_4 <= 1
DifferentPair_6_7_4_6_2: Choice_6_6_2 + Choice_6_7_4 <= 1
DifferentPair_6_7_4_6_6: Choice_6_6_6 + Choice_6_7_4 <= 1
DifferentPair_6_7_4_8_2: Choice_6_7_4 + Choice_6_8_2 <= 1
DifferentPair_6_7_4_8_6: Choice_6_7_4 + Choice_6_8_6 <= 1
DifferentPair_6_7_4_9_3: Choice_6_7_4 + Choice_6_9_3 <= 1
DifferentPair_6_7_4_9_5: Choice_6_7_4 + Choice_6_9_5 <= 1
DifferentPair_6_7_5_5_4: Choice_6_5_4 + Choice_6_7_5 <= 1
DifferentPair_6_7_5_5_6: Choice_6_5_6 + Choice_6_7_5 <= 1
DifferentPair_6_7_5_6_3: Choice_6_6_3 + Choice_6_7_5 <= 1
DifferentPair_6_7_5_6_7: Choice_6_6_7 + Choice_6_7_5 <= 1
DifferentPair_6_7_5_8_3: Choice_6_7_5 + Choice_6_8_3 <= 1
DifferentPair_6_7_5_8_7: Choice_6_7_5 + Choice_6_8_7 <= 1
DifferentPair_6_7_5_9_4: Choice_6_7_5 + Choice_6_9_4 <= 1
DifferentPair_6_7_5_9_6: Choice_6_7_5 + Choice_6_9_6 <= 1
DifferentPair_6_7_6_5_5: Choice_6_5_5 + Choice_6_7_6 <= 1
DifferentPair_6_7_6_5_7: Choice_6_5_7 + Choice_6_7_6 <= 1
DifferentPair_6_7_6_6_4: Choice_6_6_4 + Choice_6_7_6 <= 1
DifferentPair_6_7_6_6_8: Choice_6_6_8 + Choice_6_7_6 <= 1
DifferentPair_6_7_6_8_4: Choice_6_7_6 + Choice_6_8_4 <= 1
DifferentPair_6_7_6_8_8: Choice_6_7_6 + Choice_6_8_8 <= 1
DifferentPair_6_7_6_9_5: Choice_6_7_6 + Choice_6_9_5 <= 1
DifferentPair_6_7_6_9_7: Choice_6_7_6 + Choice_6_9_7 <= 1
DifferentPair_6_7_7_5_6: Choice_6_5_6 + Choice_6_7_7 <= 1
DifferentPair_6_7_7_5_8: Choice_6_5_8 + Choice_6_7_7 <= 1
DifferentPair_6_7_7_6_5: Choice_6_6_5 + Choice_6_7_7 <= 1
DifferentPair_6_7_7_6_9: Choice_6_6_9 + Choice_6_7_7 <= 1
DifferentPair_6_7_7_8_5: Choice_6_7_7 + Choice_6_8_5 <= 1
DifferentPair_6_7_7_8_9: Choice_6_7_7 + Choice_6_8_9 <= 1
DifferentPair_6_7_7_9_6: Choice_6_7_7 + Choice_6_9_6 <= 1
DifferentPair_6_7_7_9_8: Choice_6_7_7 + Choice_6_9_8 <= 1
DifferentPair_6_7_8_5_7: Choice_6_5_7 + Choice_6_7_8 <= 1
DifferentPair_6_7_8_5_9: Choice_6_5_9 + Choice_6_7_8 <= 1
DifferentPair_6_7_8_6_6: Choice_6_6_6 + Choice_6_7_8 <= 1
DifferentPair_6_7_8_8_6: Choice_6_7_8 + Choice_6_8_6 <= 1
DifferentPair_6_7_8_9_7: Choice_6_7_8 + Choice_6_9_7 <= 1
DifferentPair_6_7_8_9_9: Choice_6_7_8 + Choice_6_9_9 <= 1
DifferentPair_6_7_9_5_8: Choice_6_5_8 + Choice_6_7_9 <= 1
DifferentPair_6_7_9_6_7: Choice_6_6_7 + Choice_6_7_9 <= 1
DifferentPair_6_7_9_8_7: Choice_6_7_9 + Choice_6_8_7 <= 1
DifferentPair_6_7_9_9_8: Choice_6_7_9 + Choice_6_9_8 <= 1
DifferentPair_6_8_1_6_2: Choice_6_6_2 + Choice_6_8_1 <= 1
DifferentPair_6_8_1_7_3: Choice_6_7_3 + Choice_6_8_1 <= 1
DifferentPair_6_8_1_9_3: Choice_6_8_1 + Choice_6_9_3 <= 1
DifferentPair_6_8_2_6_1: Choice_6_6_1 + Choice_6_8_2 <= 1
DifferentPair_6_8_2_6_3: Choice_6_6_3 + Choice_6_8_2 <= 1
DifferentPair_6_8_2_7_4: Choice_6_7_4 + Choice_6_8_2 <= 1
DifferentPair_6_8_2_9_4: Choice_6_8_2 + Choice_6_9_4 <= 1
DifferentPair_6_8_3_6_2: Choice_6_6_2 + Choice_6_8_3 <= 1
DifferentPair_6_8_3_6_4: Choice_6_6_4 + Choice_6_8_3 <= 1
DifferentPair_6_8_3_7_1: Choice_6_7_1 + Choice_6_8_3 <= 1
DifferentPair_6_8_3_7_5: Choice_6_7_5 + Choice_6_8_3 <= 1
DifferentPair_6_8_3_9_1: Choice_6_8_3 + Choice_6_9_1 <= 1
DifferentPair_6_8_3_9_5: Choice_6_8_3 + Choice_6_9_5 <= 1
DifferentPair_6_8_4_6_3: Choice_6_6_3 + Choice_6_8_4 <= 1
DifferentPair_6_8_4_6_5: Choice_6_6_5 + Choice_6_8_4 <= 1
DifferentPair_6_8_4_7_2: Choice_6_7_2 + Choice_6_8_4 <= 1
DifferentPair_6_8_4_7_6: Choice_6_7_6 + Choice_6_8_4 <= 1
DifferentPair_6_8_4_9_2: Choice_6_8_4 + Choice_6_9_2 <= 1
DifferentPair_6_8_4_9_6: Choice_6_8_4 + Choice_6_9_6 <= 1
DifferentPair_6_8_5_6_4: Choice_6_6_4 + Choice_6_8_5 <= 1
DifferentPair_6_8_5_6_6: Choice_6_6_6 + Choice_6_8_5 <= 1
DifferentPair_6_8_5_7_3: Choice_6_7_3 + Choice_6_8_5 <= 1
DifferentPair_6_8_5_7_7: Choice_6_7_7 + Choice_6_8_5 <= 1
DifferentPair_6_8_5_9_3: Choice_6_8_5 + Choice_6_9_3 <= 1
DifferentPair_6_8_5_9_7: Choice_6_8_5 + Choice_6_9_7 <= 1
DifferentPair_6_8_6_6_5: Choice_6_6_5 + Choice_6_8_6 <= 1
DifferentPair_6_8_6_6_7: Choice_6_6_7 + Choice_6_8_6 <= 1
DifferentPair_6_8_6_7_4: Choice_6_7_4 + Choice_6_8_6 <= 1
DifferentPair_6_8_6_7_8: Choice_6_7_8 + Choice_6_8_6 <= 1
DifferentPair_6_8_6_9_4: Choice_6_8_6 + Choice_6_9_4 <= 1
DifferentPair_6_8_6_9_8: Choice_6_8_6 + Choice_6_9_8 <= 1
DifferentPair_6_8_7_6_6: Choice_6_6_6 + Choice_6_8_7 <= 1
DifferentPair_6_8_7_6_8: Choice_6_6_8 + Choice_6_8_7 <= 1
DifferentPair_6_8_7_7_5: Choice_6_7_5 + Choice_6_8_7 <= 1
DifferentPair_6_8_7_7_9: Choice_6_7_9 + Choice_6_8_7 <= 1
DifferentPair_6_8_7_9_5: Choice_6_8_7 + Choice_6_9_5 <= 1
DifferentPair_6_8_7_9_9: Choice_6_8_7 + Choice_6_9_9 <= 1
DifferentPair_6_8_8_6_7: Choice_6_6_7 + Choice_6_8_8 <= 1
DifferentPair_6_8_8_6_9: Choice_6_6_9 + Choice_6_8_8 <= 1
DifferentPair_6_8_8_7_6: Choice_6_7_6 + Choice_6_8_8 <= 1
DifferentPair_6_8_8_9_6: Choice_6_8_8 + Choice_6_9_6 <= 1
DifferentPair_6_8_9_6_8: Choice_6_6_8 + Choice_6_8_9 <= 1
DifferentPair_6_8_9_7_7: Choice_6_7_7 + Choice_6_8_9 <= 1
DifferentPair_6_8_9_9_7: Choice_6_8_9 + Choice_6_9_7 <= 1
DifferentPair_6_9_1_7_2: Choice_6_7_2 + Choice_6_9_1 <= 1
DifferentPair_6_9_1_8_3: Choice_6_8_3 + Choice_6_9_1 <= 1
DifferentPair_6_9_2_7_1: Choice_6_7_1 + Choice_6_9_2 <= 1
DifferentPair_6_9_2_7_3: Choice_6_7_3 + Choice_6_9_2 <= 1
DifferentPair_6_9_2_8_4: Choice_6_8_4 + Choice_6_9_2 <= 1
DifferentPair_6_9_3_7_2: Choice_6_7_2 + Choice_6_9_3 <= 1
DifferentPair_6_9_3_7_4: Choice_6_7_4 + Choice_6_9_3 <= 1
DifferentPair_6_9_3_8_1: Choice_6_8_1 + Choice_6_9_3 <= 1
DifferentPair_6_9_3_8_5: Choice_6_8_5 + Choice_6_9_3 <= 1
DifferentPair_6_9_4_7_3: Choice_6_7_3 + Choice_6_9_4 <= 1
DifferentPair_6_9_4_7_5: Choice_6_7_5 + Choice_6_9_4 <= 1
DifferentPair_6_9_4_8_2: Choice_6_8_2 + Choice_6_9_4 <= 1
DifferentPair_6_9_4_8_6: Choice_6_8_6 + Choice_6_9_4 <= 1
DifferentPair_6_9_5_7_4: Choice_6_7_4 + Choice_6_9_5 <= 1
DifferentPair_6_9_5_7_6: Choice_6_7_6 + Choice_6_9_5 <= 1
DifferentPair_6_9_5_8_3: Choice_6_8_3 + Choice_6_9_5 <= 1
DifferentPair_6_9_5_8_7: Choice_6_8_7 + Choice_6_9_5 <= 1
DifferentPair_6_9_6_7_5: Choice_6_7_5 + Choice_6_9_6 <= 1
DifferentPair_6_9_6_7_7: Choice_6_7_7 + Choice_6_9_6 <= 1
DifferentPair_6_9_6_8_4: Choice_6_8_4 + Choice_6_9_6 <= 1
DifferentPair_6_9_6_8_8: Choice_6_8_8 + Choice_6_9_6 <= 1
DifferentPair_6_9_7_7_6: Choice_6_7_6 + Choice_6_9_7 <= 1
DifferentPair_6_9_7_7_8: Choice_6_7_8 + Choice_6_9_7 <= 1
DifferentPair_6_9_7_8_5: Choice_6_8_5 + Choice_6_9_7 <= 1
DifferentPair_6_9_7_8_9: Choice_6_8_9 + Choice_6_9_7 <= 1
DifferentPair_6_9_8_7_7: Choice_6_7_7 + Choice_6_9_8 <= 1
DifferentPair_6_9_8_7_9: Choice_6_7_9 + Choice_6_9_8 <= 1
DifferentPair_6_9_8_8_6: Choice_6_8_6 + Choice_6_9_8 <= 1
DifferentPair_6_9_9_7_8: Choice_6_7_8 + Choice_6_9_9 <= 1
DifferentPair_6_9_9_8_7: Choice_6_8_7 + Choice_6_9_9 <= 1
DifferentPair_7_1_1_2_3: Choice_7_1_1 + Choice_7_2_3 <= 1
DifferentPair_7_1_1_3_2: Choice_7_1_1 + Choice_7_3_2 <= 1
DifferentPair_7_1_2_2_4: Choice_7_1_2 + Choice_7_2_4 <= 1
DifferentPair_7_1_2_3_1: Choice_7_1_2 + Choice_7_3_1 <= 1
DifferentPair_7_1_2_3_3: Choice_7_1_2 + Choice_7_3_3 <= 1
DifferentPair_7_1_3_2_1: Choice_7_1_3 + Choice_7_2_1 <= 1
DifferentPair_7_1_3_2_5: Choice_7_1_3 + Choice_7_2_5 <= 1
DifferentPair_7_1_3_3_2: Choice_7_1_3 + Choice_7_3_2 <= 1
DifferentPair_7_1_3_3_4: Choice_7_1_3 + Choice_7_3_4 <= 1
DifferentPair_7_1_4_2_2: Choice_7_1_4 + Choice_7_2_2 <= 1
DifferentPair_7_1_4_2_6: Choice_7_1_4 + Choice_7_2_6 <= 1
DifferentPair_7_1_4_3_3: Choice_7_1_4 + Choice_7_3_3 <= 1
DifferentPair_7_1_4_3_5: Choice_7_1_4 + Choice_7_3_5 <= 1
DifferentPair_7_1_5_2_3: Choice_7_1_5 + Choice_7_2_3 <= 1
DifferentPair_7_1_5_2_7: Choice_7_1_5 + Choice_7_2_7 <= 1
DifferentPair_7_1_5_3_4: Choice_7_1_5 + Choice_7_3_4 <= 1
DifferentPair_7_1_5_3_6: Choice_7_1_5 + Choice_7_3_6 <= 1
DifferentPair_7_1_6_2_4: Choice_7_1_6 + Choice_7_2_4 <= 1
DifferentPair_7_1_6_2_8: Choice_7_1_6 + Choice_7_2_8 <= 1
DifferentPair_7_1_6_3_5: Choice_7_1_6 + Choice_7_3_5 <= 1
DifferentPair_7_1_6_3_7: Choice_7_1_6 + Choice_7_3_7 <= 1
DifferentPair_7_1_7_2_5: Choice_7_1_7 + Choice_7_2_5 <= 1
DifferentPair_7_1_7_2_9: Choice_7_1_7 + Choice_7_2_9 <= 1
DifferentPair_7_1_7_3_6: Choice_7_1_7 + Choice_7_3_6 <= 1
DifferentPair_7_1_7_3_8: Choice_7_1_7 + Choice_7_3_8 <= 1
DifferentPair_7_1_8_2_6: Choice_7_1_8 + Choice_7_2_6 <= 1
DifferentPair_7_1_8_3_7: Choice_7_1_8 + Choice_7_3_7 <= 1
DifferentPair_7_1_8_3_9: Choice_7_1_8 + Choice_7_3_9 <= 1
DifferentPair_7_1_9_2_7: Choice_7_1_9 + Choice_7_2_7 <= 1
DifferentPair_7_1_9_3_8: Choice_7_1_9 + Choice_7_3_8 <= 1
DifferentPair_7_2_1_1_3: Choice_7_1_3 + Choice_7_2_1 <= 1
DifferentPair_7_2_1_3_3: Choice_7_2_1 + Choice_7_3_3 <= 1
DifferentPair_7_2_1_4_2: Choice_7_2_1 + Choice_7_4_2 <= 1
DifferentPair_7_2_2_1_4: Choice_7_1_4 + Choice_7_2_2 <= 1
DifferentPair_7_2_2_3_4: Choice_7_2_2 + Choice_7_3_4 <= 1
DifferentPair_7_2_2_4_1: Choice_7_2_2 + Choice_7_4_1 <= 1
DifferentPair_7_2_2_4_3: Choice_7_2_2 + Choice_7_4_3 <= 1
DifferentPair_7_2_3_1_1: Choice_7_1_1 + Choice_7_2_3 <= 1
DifferentPair_7_2_3_1_5: Choice_7_1_5 + Choice_7_2_3 <= 1
DifferentPair_7_2_3_3_1: Choice_7_2_3 + Choice_7_3_1 <= 1
DifferentPair_7_2_3_3_5: Choice_7_2_3 + Choice_7_3_5 <= 1
DifferentPair_7_2_3_4_2: Choice_7_2_3 + Choice_7_4_2 <= 1
DifferentPair_7_2_3_4_4: Choice_7_2_3 + Choice_7_4_4 <= 1
DifferentPair_7_2_4_1_2: Choice_7_1_2 + Choice_7_2_4 <= 1
DifferentPair_7_2_4_1_6: Choice_7_1_6 + Choice_7_2_4 <= 1
DifferentPair_7_2_4_3_2: Choice_7_2_4 + Choice_7_3_2 <= 1
DifferentPair_7_2_4_3_6: Choice_7_2_4 + Choice_7_3_6 <= 1
DifferentPair_7_2_4_4_3: Choice_7_2_4 + Choice_7_4_3 <= 1
DifferentPair_7_2_4_4_5: Choice_7_2_4 + Choice_7_4_5 <= 1
DifferentPair_7_2_5_1_3: Choice_7_1_3 + Choice_7_2_5 <= 1
DifferentPair_7_2_5_1_7: Choice_7_1_7 + Choice_7_2_5 <= 1
DifferentPair_7_2_5_3_3: Choice_7_2_5 + Choice_7_3_3 <= 1
DifferentPair_7_2_5_3_7: Choice_7_2_5 + Choice_7_3_7 <= 1
DifferentPair_7_2_5_4_4: Choice_7_2_5 + Choice_7_4_4 <= 1
DifferentPair_7_2_5_4_6: Choice_7_2_5 + Choice_7_4_6 <= 1
DifferentPair_7_2_6_1_4: Choice_7_1_4 + Choice_7_2_6 <= 1
DifferentPair_7_2_6_1_8: Choice_7_1_8 + Choice_7_2_6 <= 1
DifferentPair_7_2_6_3_4: Choice_7_2_6 + Choice_7_3_4 <= 1
DifferentPair_7_2_6_3_8: Choice_7_2_6 + Choice_7_3_8 <= 1
DifferentPair_7_2_6_4_5: Choice_7_2_6 + Choice_7_4_5 <= 1
DifferentPair_7_2_6_4_7: Choice_7_2_6 + Choice_7_4_7 <= 1
DifferentPair_7_2_7_1_5: Choice_7_1_5 + Choice_7_2_7 <= 1
DifferentPair_7_2_7_1_9: Choice_7_1_9 + Choice_7_2_7 <= 1
DifferentPair_7_2_7_3_5: Choice_7_2_7 + Choice_7_3_5 <= 1
DifferentPair_7_2_7_3_9: Choice_7_2_7 + Choice_7_3_9 <= 1
DifferentPair_7_2_7_4_6: Choice_7_2_7 + Choice_7_4_6 <= 1
DifferentPair_7_2_7_4_8: Choice_7_2_7 + Choice_7_4_8 <= 1
DifferentPair_7_2_8_1_6: Choice_7_1_6 + Choice_7_2_8 <= 1
DifferentPair_7_2_8_3_6: Choice_7_2_8 + Choice_7_3_6 <= 1
DifferentPair_7_2_8_4_7: Choice_7_2_8 + Choice_7_4_7 <= 1
DifferentPair_7_2_8_4_9: Choice_7_2_8 + Choice_7_4_9 <= 1
DifferentPair_7_2_9_1_7: Choice_7_1_7 + Choice_7_2_9 <= 1
DifferentPair_7_2_9_3_7: Choice_7_2_9 + Choice_7_3_7 <= 1
DifferentPair_7_2_9_4_8: Choice_7_2_9 + Choice_7_4_8 <= 1
DifferentPair_7_3_1_1_2: Choice_7_1_2 + Choice_7_3_1 <= 1
DifferentPair_7_3_1_2_3: Choice_7_2_3 + Choice_7_3_1 <= 1
DifferentPair_7_3_1_4_3: Choice_7_3_1 + Choice_7_4_3 <= 1
DifferentPair_7_3_1_5_2: Choice_7_3_1 + Choice_7_5_2 <= 1
DifferentPair_7_3_2_1_1: Choice_7_1_1 + Choice_7_3_2 <= 1
DifferentPair_7_3_2_1_3: Choice_7_1_3 + Choice_7_3_2 <= 1
DifferentPair_7_3_2_2_4: Choice_7_2_4 + Choice_7_3_2 <= 1
DifferentPair_7_3_2_4_4: Choice_7_3_2 + Choice_7_4_4 <= 1
DifferentPair_7_3_2_5_1: Choice_7_3_2 + Choice_7_5_1 <= 1
DifferentPair_7_3_2_5_3: Choice_7_3_2 + Choice_7_5_3 <= 1
DifferentPair_7_3_3_1_2: Choice_7_1_2 + Choice_7_3_3 <= 1
DifferentPair_7_3_3_1_4: Choice_7_1_4 + Choice_7_3_3 <= 1
DifferentPair_7_3_3_2_1: Choice_7_2_1 + Choice_7_3_3 <= 1
DifferentPair_7_3_3_2_5: Choice_7_2_5 + Choice_7_3_3 <= 1
DifferentPair_7_3_3_4_1: Choice_7_3_3 + Choice_7_4_1 <= 1
DifferentPair_7_3_3_4_5: Choice_7_3_3 + Choice_7_4_5 <= 1
DifferentPair_7_3_3_5_2: Choice_7_3_3 + Choice_7_5_2 <= 1
DifferentPair_7_3_3_5_4: Choice_7_3_3 + Choice_7_5_4 <= 1
DifferentPair_7_3_4_1_3: Choice_7_1_3 + Choice_7_3_4 <= 1
DifferentPair_7_3_4_1_5: Choice_7_1_5 + Choice_7_3_4 <= 1
DifferentPair_7_3_4_2_2: Choice_7_2_2 + Choice_7_3_4 <= 1
DifferentPair_7_3_4_2_6: Choice_7_2_6 + Choice_7_3_4 <= 1
DifferentPair_7_3_4_4_2: Choice_7_3_4 + Choice_7_4_2 <= 1
DifferentPair_7_3_4_4_6: Choice_7_3_4 + Choice_7_4_6 <= 1
DifferentPair_7_3_4_5_3: Choice_7_3_4 + Choice_7_5_3 <= 1
DifferentPair_7_3_4_5_5: Choice_7_3_4 + Choice_7_5_5 <= 1
DifferentPair_7_3_5_1_4: Choice_7_1_4 + Choice_7_3_5 <= 1
DifferentPair_7_3_5_1_6: Choice_7_1_6 + Choice_7_3_5 <= 1
DifferentPair_7_3_5_2_3: Choice_7_2_3 + Choice_7_3_5 <= 1
DifferentPair_7_3_5_2_7: Choice_7_2_7 + Choice_7_3_5 <= 1
DifferentPair_7_3_5_4_3: Choice_7_3_5 + Choice_7_4_3 <= 1
DifferentPair_7_3_5_4_7: Choice_7_3_5 + Choice_7_4_7 <= 1
DifferentPair_7_3_5_5_4: Choice_7_3_5 + Choice_7_5_4 <= 1
DifferentPair_7_3_5_5_6: Choice_7_3_5 + Choice_7_5_6 <= 1
DifferentPair_7_3_6_1_5: Choice_7_1_5 + Choice_7_3_6 <= 1
DifferentPair_7_3_6_1_7: Choice_7_1_7 + Choice_7_3_6 <= 1
DifferentPair_7_3_6_2_4: Choice_7_2_4 + Choice_7_3_6 <= 1
DifferentPair_7_3_6_2_8: Choice_7_2_8 + Choice_7_3_6 <= 1
DifferentPair_7_3_6_4_4: Choice_7_3_6 + Choice_7_4_4 <= 1
DifferentPair_7_3_6_4_8: Choice_7_3_6 + Choice_7_4_8 <= 1
DifferentPair_7_3_6_5_5: Choice_7_3_6 + Choice_7_5_5 <= 1
DifferentPair_7_3_6_5_7: Choice_7_3_6 + Choice_7_5_7 <= 1
DifferentPair_7_3_7_1_6: Choice_7_1_6 + Choice_7_3_7 <= 1
DifferentPair_7_3_7_1_8: Choice_7_1_8 + Choice_7_3_7 <= 1
DifferentPair_7_3_7_2_5: Choice_7_2_5 + Choice_7_3_7 <= 1
DifferentPair_7_3_7_2_9: Choice_7_2_9 + Choice_7_3_7 <= 1
DifferentPair_7_3_7_4_5: Choice_7_3_7 + Choice_7_4_5 <= 1
DifferentPair_7_3_7_4_9: Choice_7_3_7 + Choice_7_4_9 <= 1
DifferentPair_7_3_7_5_6: Choice_7_3_7 + Choice_7_5_6 <= 1
DifferentPair_7_3_7_5_8: Choice_7_3_7 + Choice_7_5_8 <= 1
DifferentPair_7_3_8_1_7: Choice_7_1_7 + Choice_7_3_8 <= 1
DifferentPair_7_3_8_1_9: Choice_7_1_9 + Choice_7_3_8 <= 1
DifferentPair_7_3_8_2_6: Choice_7_2_6 + Choice_7_3_8 <= 1
DifferentPair_7_3_8_4_6: Choice_7_3_8 + Choice_7_4_6 <= 1
DifferentPair_7_3_8_5_7: Choice_7_3_8 + Choice_7_5_7 <= 1
DifferentPair_7_3_8_5_9: Choice_7_3_8 + Choice_7_5_9 <= 1
DifferentPair_7_3_9_1_8: Choice_7_1_8 + Choice_7_3_9 <= 1
DifferentPair_7_3_9_2_7: Choice_7_2_7 + Choice_7_3_9 <= 1
DifferentPair_7_3_9_4_7: Choice_7_3_9 + Choice_7_4_7 <= 1
DifferentPair_7_3_9_5_8: Choice_7_3_9 + Choice_7_5_8 <= 1
DifferentPair_7_4_1_2_2: Choice_7_2_2 + Choice_7_4_1 <= 1
DifferentPair_7_4_1_3_3: Choice_7_3_3 + Choice_7_4_1 <= 1
DifferentPair_7_4_1_5_3: Choice_7_4_1 + Choice_7_5_3 <= 1
DifferentPair_7_4_1_6_2: Choice_7_4_1 + Choice_7_6_2 <= 1
DifferentPair_7_4_2_2_1: Choice_7_2_1 + Choice_7_4_2 <= 1
DifferentPair_7_4_2_2_3: Choice_7_2_3 + Choice_7_4_2 <= 1
DifferentPair_7_4_2_3_4: Choice_7_3_4 + Choice_7_4_2 <= 1
DifferentPair_7_4_2_5_4: Choice_7_4_2 + Choice_7_5_4 <= 1
DifferentPair_7_4_2_6_1: Choice_7_4_2 + Choice_7_6_1 <= 1
DifferentPair_7_4_2_6_3: Choice_7_4_2 + Choice_7_6_3 <= 1
DifferentPair_7_4_3_2_2: Choice_7_2_2 + Choice_7_4_3 <= 1
DifferentPair_7_4_3_2_4: Choice_7_2_4 + Choice_7_4_3 <= 1
DifferentPair_7_4_3_3_1: Choice_7_3_1 + Choice_7_4_3 <= 1
DifferentPair_7_4_3_3_5: Choice_7_3_5 + Choice_7_4_3 <= 1
DifferentPair_7_4_3_5_1: Choice_7_4_3 + Choice_7_5_1 <= 1
DifferentPair_7_4_3_5_5: Choice_7_4_3 + Choice_7_5_5 <= 1
DifferentPair_7_4_3_6_2: Choice_7_4_3 + Choice_7_6_2 <= 1
DifferentPair_7_4_3_6_4: Choice_7_4_3 + Choice_7_6_4 <= 1
DifferentPair_7_4_4_2_3: Choice_7_2_3 + Choice_7_4_4 <= 1
DifferentPair_7_4_4_2_5: Choice_7_2_5 + Choice_7_4_4 <= 1
DifferentPair_7_4_4_3_2: Choice_7_3_2 + Choice_7_4_4 <= 1
DifferentPair_7_4_4_3_6: Choice_7_3_6 + Choice_7_4_4 <= 1
DifferentPair_7_4_4_5_2: Choice_7_4_4 + Choice_7_5_2 <= 1
DifferentPair_7_4_4_5_6: Choice_7_4_4 + Choice_7_5_6 <= 1
DifferentPair_7_4_4_6_3: Choice_7_4_4 + Choice_7_6_3 <= 1
DifferentPair_7_4_4_6_5: Choice_7_4_4 + Choice_7_6_5 <= 1
DifferentPair_7_4_5_2_4: Choice_7_2_4 + Choice_7_4_5 <= 1
DifferentPair_7_4_5_2_6: Choice_7_2_6 + Choice_7_4_5 <= 1
DifferentPair_7_4_5_3_3: Choice_7_3_3 + Choice_7_4_5 <= 1
DifferentPair_7_4_5_3_7: Choice_7_3_7 + Choice_7_4_5 <= 1
DifferentPair_7_4_5_5_3: Choice_7_4_5 + Choice_7_5_3 <= 1
DifferentPair_7_4_5_5_7: Choice_7_4_5 + Choice_7_5_7 <= 1
DifferentPair_7_4_5_6_4: Choice_7_4_5 + Choice_7_6_4 <= 1
DifferentPair_7_4_5_6_6: Choice_7_4_5 + Choice_7_6_6 <= 1
DifferentPair_7_4_6_2_5: Choice_7_2_5 + Choice_7_4_6 <= 1
DifferentPair_7_4_6_2_7: Choice_7_2_7 + Choice_7_4_6 <= 1
DifferentPair_7_4_6_3_4: Choice_7_3_4 + Choice_7_4_6 <= 1
DifferentPair_7_4_6_3_8: Choice_7_3_8 + Choice_7_4_6 <= 1
DifferentPair_7_4_6_5_4: Choice_7_4_6 + Choice_7_5_4 <= 1
DifferentPair_7_4_6_5_8: Choice_7_4_6 + Choice_7_5_8 <= 1
DifferentPair_7_4_6_6_5: Choice_7_4_6 + Choice_7_6_5 <= 1
DifferentPair_7_4_6_6_7: Choice_7_4_6 + Choice_7_6_7 <= 1
DifferentPair_7_4_7_2_6: Choice_7_2_6 + Choice_7_4_7 <= 1
DifferentPair_7_4_7_2_8: Choice_7_2_8 + Choice_7_4_7 <= 1
DifferentPair_7_4_7_3_5: Choice_7_3_5 + Choice_7_4_7 <= 1
DifferentPair_7_4_7_3_9: Choice_7_3_9 + Choice_7_4_7 <= 1
DifferentPair_7_4_7_5_5: Choice_7_4_7 + Choice_7_5_5 <= 1
DifferentPair_7_4_7_5_9: Choice_7_4_7 + Choice_7_5_9 <= 1
DifferentPair_7_4_7_6_6: Choice_7_4_7 + Choice_7_6_6 <= 1
DifferentPair_7_4_7_6_8: Choice_7_4_7 + Choice_7_6_8 <= 1
DifferentPair_7_4_8_2_7: Choice_7_2_7 + Choice_7_4_8 <= 1
DifferentPair_7_4_8_2_9: Choice_7_2_9 + Choice_7_4_8 <= 1
DifferentPair_7_4_8_3_6: Choice_7_3_6 + Choice_7_4_8 <= 1
DifferentPair_7_4_8_5_6: Choice_7_4_8 + Choice_7_5_6 <= 1
DifferentPair_7_4_8_6_7: Choice_7_4_8 + Choice_7_6_7 <= 1
DifferentPair_7_4_8_6_9: Choice_7_4_8 + Choice_7_6_9 <= 1
DifferentPair_7_4_9_2_8: Choice_7_2_8 + Choice_7_4_9 <= 1
DifferentPair_7_4_9_3_7: Choice_7_3_7 + Choice_7_4_9 <= 1
DifferentPair_7_4_9_5_7: Choice_7_4_9 + Choice_7_5_7 <= 1
DifferentPair_7_4_9_6_8: Choice_7_4_9 + Choice_7_6_8 <= 1
DifferentPair_7_5_1_3_2: Choice_7_3_2 + Choice_7_5_1 <= 1
DifferentPair_7_5_1_4_3: Choice_7_4_3 + Choice_7_5_1 <= 1
DifferentPair_7_5_1_6_3: Choice_7_5_1 + Choice_7_6_3 <= 1
DifferentPair_7_5_1_7_2: Choice_7_5_1 + Choice_7_7_2 <= 1
DifferentPair_7_5_2_3_1: Choice_7_3_1 + Choice_7_5_2 <= 1
DifferentPair_7_5_2_3_3: Choice_7_3_3 + Choice_7_5_2 <= 1
DifferentPair_7_5_2_4_4: Choice_7_4_4 + Choice_7_5_2 <= 1
DifferentPair_7_5_2_6_4: Choice_7_5_2 + Choice_7_6_4 <= 1
DifferentPair_7_5_2_7_1: Choice_7_5_2 + Choice_7_7_1 <= 1
DifferentPair_7_5_2_7_3: Choice_7_5_2 + Choice_7_7_3 <= 1
DifferentPair_7_5_3_3_2: Choice_7_3_2 + Choice_7_5_3 <= 1
DifferentPair_7_5_3_3_4: Choice_7_3_4 + Choice_7_5_3 <= 1
DifferentPair_7_5_3_4_1: Choice_7_4_1 + Choice_7_5_3 <= 1
DifferentPair_7_5_3_4_5: Choice_7_4_5 + Choice_7_5_3 <= 1
DifferentPair_7_5_3_6_1: Choice_7_5_3 + Choice_7_6_1 <= 1
DifferentPair_7_5_3_6_5: Choice_7_5_3 + Choice_7_6_5 <= 1
DifferentPair_7_5_3_7_2: Choice_7_5_3 + Choice_7_7_2 <= 1
DifferentPair_7_5_3_7_4: Choice_7_5_3 + Choice_7_7_4 <= 1
DifferentPair_7_5_4_3_3: Choice_7_3_3 + Choice_7_5_4 <= 1
DifferentPair_7_5_4_3_5: Choice_7_3_5 + Choice_7_5_4 <= 1
DifferentPair_7_5_4_4_2: Choice_7_4_2 + Choice_7_5_4 <= 1
DifferentPair_7_5_4_4_6: Choice_7_4_6 + Choice_7_5_4 <= 1
DifferentPair_7_5_4_6_2: Choice_7_5_4 + Choice_7_6_2 <= 1
DifferentPair_7_5_4_6_6: Choice_7_5_4 + Choice_7_6_6 <= 1
DifferentPair_7_5_4_7_3: Choice_7_5_4 + Choice_7_7_3 <= 1
DifferentPair_7_5_4_7_5: Choice_7_5_4 + Choice_7_7_5 <= 1
DifferentPair_7_5_5_3_4: Choice_7_3_4 + Choice_7_5_5 <= 1
DifferentPair_7_5_5_3_6: Choice_7_3_6 + Choice_7_5_5 <= 1
DifferentPair_7_5_5_4_3: Choice_7_4_3 + Choice_7_5_5 <= 1
DifferentPair_7_5_5_4_7: Choice_7_4_7 + Choice_7_5_5 <= 1
DifferentPair_7_5_5_6_3: Choice_7_5_5 + Choice_7_6_3 <= 1
DifferentPair_7_5_5_6_7: Choice_7_5_5 + Choice_7_6_7 <= 1
DifferentPair_7_5_5_7_4: Choice_7_5_5 + Choice_7_7_4 <= 1
DifferentPair_7_5_5_7_6: Choice_7_5_5 + Choice_7_7_6 <= 1
DifferentPair_7_5_6_3_5: Choice_7_3_5 + Choice_7_5_6 <= 1
DifferentPair_7_5_6_3_7: Choice_7_3_7 + Choice_7_5_6 <= 1
DifferentPair_7_5_6_4_4: Choice_7_4_4 + Choice_7_5_6 <= 1
DifferentPair_7_5_6_4_8: Choice_7_4_8 + Choice_7_5_6 <= 1
DifferentPair_7_5_6_6_4: Choice_7_5_6 + Choice_7_6_4 <= 1
DifferentPair_7_5_6_6_8: Choice_7_5_6 + Choice_7_6_8 <= 1
DifferentPair_7_5_6_7_5: Choice_7_5_6 + Choice_7_7_5 <= 1
DifferentPair_7_5_6_7_7: Choice_7_5_6 + Choice_7_7_7 <= 1
DifferentPair_7_5_7_3_6: Choice_7_3_6 + Choice_7_5_7 <= 1
DifferentPair_7_5_7_3_8: Choice_7_3_8 + Choice_7_5_7 <= 1
DifferentPair_7_5_7_4_5: Choice_7_4_5 + Choice_7_5_7 <= 1
DifferentPair_7_5_7_4_9: Choice_7_4_9 + Choice_7_5_7 <= 1
DifferentPair_7_5_7_6_5: Choice_7_5_7 + Choice_7_6_5 <= 1
DifferentPair_7_5_7_6_9: Choice_7_5_7 + Choice_7_6_9 <= 1
DifferentPair_7_5_7_7_6: Choice_7_5_7 + Choice_7_7_6 <= 1
DifferentPair_7_5_7_7_8: Choice_7_5_7 + Choice_7_7_8 <= 1
DifferentPair_7_5_8_3_7: Choice_7_3_7 + Choice_7_5_8 <= 1
DifferentPair_7_5_8_3_9: Choice_7_3_9 + Choice_7_5_8 <= 1
DifferentPair_7_5_8_4_6: Choice_7_4_6 + Choice_7_5_8 <= 1
DifferentPair_7_5_8_6_6: Choice_7_5_8 + Choice_7_6_6 <= 1
DifferentPair_7_5_8_7_7: Choice_7_5_8 + Choice_7_7_7 <= 1
DifferentPair_7_5_8_7_9: Choice_7_5_8 + Choice_7_7_9 <= 1
DifferentPair_7_5_9_3_8: Choice_7_3_8 + Choice_7_5_9 <= 1
DifferentPair_7_5_9_4_7: Choice_7_4_7 + Choice_7_5_9 <= 1
DifferentPair_7_5_9_6_7: Choice_7_5_9 + Choice_7_6_7 <= 1
DifferentPair_7_5_9_7_8: Choice_7_5_9 + Choice_7_7_8 <= 1
DifferentPair_7_6_1_4_2: Choice_7_4_2 + Choice_7_6_1 <= 1
DifferentPair_7_6_1_5_3: Choice_7_5_3 + Choice_7_6_1 <= 1
DifferentPair_7_6_1_7_3: Choice_7_6_1 + Choice_7_7_3 <= 1
DifferentPair_7_6_1_8_2: Choice_7_6_1 + Choice_7_8_2 <= 1
DifferentPair_7_6_2_4_1: Choice_7_4_1 + Choice_7_6_2 <= 1
DifferentPair_7_6_2_4_3: Choice_7_4_3 + Choice_7_6_2 <= 1
DifferentPair_7_6_2_5_4: Choice_7_5_4 + Choice_7_6_2 <= 1
DifferentPair_7_6_2_7_4: Choice_7_6_2 + Choice_7_7_4 <= 1
DifferentPair_7_6_2_8_1: Choice_7_6_2 + Choice_7_8_1 <= 1
DifferentPair_7_6_2_8_3: Choice_7_6_2 + Choice_7_8_3 <= 1
DifferentPair_7_6_3_4_2: Choice_7_4_2 + Choice_7_6_3 <= 1
DifferentPair_7_6_3_4_4: Choice_7_4_4 + Choice_7_6_3 <= 1
DifferentPair_7_6_3_5_1: Choice_7_5_1 + Choice_7_6_3 <= 1
DifferentPair_7_6_3_5_5: Choice_7_5_5 + Choice_7_6_3 <= 1
DifferentPair_7_6_3_7_1: Choice_7_6_3 + Choice_7_7_1 <= 1
DifferentPair_7_6_3_7_5: Choice_7_6_3 + Choice_7_7_5 <= 1
DifferentPair_7_6_3_8_2: Choice_7_6_3 + Choice_7_8_2 <= 1
DifferentPair_7_6_3_8_4: Choice_7_6_3 + Choice_7_8_4 <= 1
DifferentPair_7_6_4_4_3: Choice_7_4_3 + Choice_7_6_4 <= 1
DifferentPair_7_6_4_4_5: Choice_7_4_5 + Choice_7_6_4 <= 1
DifferentPair_7_6_4_5_2: Choice_7_5_2 + Choice_7_6_4 <= 1
DifferentPair_7_6_4_5_6: Choice_7_5_6 + Choice_7_6_4 <= 1
DifferentPair_7_6_4_7_2: Choice_7_6_4 + Choice_7_7_2 <= 1
DifferentPair_7_6_4_7_6: Choice_7_6_4 + Choice_7_7_6 <= 1
DifferentPair_7_6_4_8_3: Choice_7_6_4 + Choice_7_8_3 <= 1
DifferentPair_7_6_4_8_5: Choice_7_6_4 + Choice_7_8_5 <= 1
DifferentPair_7_6_5_4_4: Choice_7_4_4 + Choice_7_6_5 <= 1
DifferentPair_7_6_5_4_6: Choice_7_4_6 + Choice_7_6_5 <= 1
DifferentPair_7_6_5_5_3: Choice_7_5_3 + Choice_7_6_5 <= 1
DifferentPair_7_6_5_5_7: Choice_7_5_7 + Choice_7_6_5 <= 1
DifferentPair_7_6_5_7_3: Choice_7_6_5 + Choice_7_7_3 <= 1
DifferentPair_7_6_5_7_7: Choice_7_6_5 + Choice_7_7_7 <= 1
DifferentPair_7_6_5_8_4: Choice_7_6_5 + Choice_7_8_4 <= 1
DifferentPair_7_6_5_8_6: Choice_7_6_5 + Choice_7_8_6 <= 1
DifferentPair_7_6_6_4_5: Choice_7_4_5 + Choice_7_6_6 <= 1
DifferentPair_7_6_6_4_7: Choice_7_4_7 + Choice_7_6_6 <= 1
DifferentPair_7_6_6_5_4: Choice_7_5_4 + Choice_7_6_6 <= 1
DifferentPair_7_6_6_5_8: Choice_7_5_8 + Choice_7_6_6 <= 1
DifferentPair_7_6_6_7_4: Choice_7_6_6 + Choice_7_7_4 <= 1
DifferentPair_7_6_6_7_8: Choice_7_6_6 + Choice_7_7_8 <= 1
DifferentPair_7_6_6_8_5: Choice_7_6_6 + Choice_7_8_5 <= 1
DifferentPair_7_6_6_8_7: Choice_7_6_6 + Choice_7_8_7 <= 1
DifferentPair_7_6_7_4_6: Choice_7_4_6 + Choice_7_6_7 <= 1
DifferentPair_7_6_7_4_8: Choice_7_4_8 + Choice_7_6_7 <= 1
DifferentPair_7_6_7_5_5: Choice_7_5_5 + Choice_7_6_7 <= 1
DifferentPair_7_6_7_5_9: Choice_7_5_9 + Choice_7_6_7 <= 1
DifferentPair_7_6_7_7_5: Choice_7_6_7 + Choice_7_7_5 <= 1
DifferentPair_7_6_7_7_9: Choice_7_6_7 + Choice_7_7_9 <= 1
DifferentPair_7_6_7_8_6: Choice_7_6_7 + Choice_7_8_6 <= 1
DifferentPair_7_6_7_8_8: Choice_7_6_7 + Choice_7_8_8 <= 1
DifferentPair_7_6_8_4_7: Choice_7_4_7 + Choice_7_6_8 <= 1
DifferentPair_7_6_8_4_9: Choice_7_4_9 + Choice_7_6_8 <= 1
DifferentPair_7_6_8_5_6: Choice_7_5_6 + Choice_7_6_8 <= 1
DifferentPair_7_6_8_7_6: Choice_7_6_8 + Choice_7_7_6 <= 1
DifferentPair_7_6_8_8_7: Choice_7_6_8 + Choice_7_8_7 <= 1
DifferentPair_7_6_8_8_9: Choice_7_6_8 + Choice_7_8_9 <= 1
DifferentPair_7_6_9_4_8: Choice_7_4_8 + Choice_7_6_9 <= 1
DifferentPair_7_6_9_5_7: Choice_7_5_7 + Choice_7_6_9 <= 1
DifferentPair_7_6_9_7_7: Choice_7_6_9 + Choice_7_7_7 <= 1
DifferentPair_7_6_9_8_8: Choice_7_6_9 + Choice_7_8_8 <= 1
DifferentPair_7_7_1_5_2: Choice_7_5_2 + Choice_7_7_1 <= 1
DifferentPair_7_7_1_6_3: Choice_7_6_3 + Choice_7_7_1 <= 1
DifferentPair_7_7_1_8_3: Choice_7_7_1 + Choice_7_8_3 <= 1
DifferentPair_7_7_1_9_2: Choice_7_7_1 + Choice_7_9_2 <= 1
DifferentPair_7_7_2_5_1: Choice_7_5_1 + Choice_7_7_2 <= 1
DifferentPair_7_7_2_5_3: Choice_7_5_3 + Choice_7_7_2 <= 1
DifferentPair_7_7_2_6_4: Choice_7_6_4 + Choice_7_7_2 <= 1
DifferentPair_7_7_2_8_4: Choice_7_7_2 + Choice_7_8_4 <= 1
DifferentPair_7_7_2_9_1: Choice_7_7_2 + Choice_7_9_1 <= 1
DifferentPair_7_7_2_9_3: Choice_7_7_2 + Choice_7_9_3 <= 1
DifferentPair_7_7_3_5_2: Choice_7_5_2 + Choice_7_7_3 <= 1
DifferentPair_7_7_3_5_4: Choice_7_5_4 + Choice_7_7_3 <= 1
DifferentPair_7_7_3_6_1: Choice_7_6_1 + Choice_7_7_3 <= 1
DifferentPair_7_7_3_6_5: Choice_7_6_5 + Choice_7_7_3 <= 1
DifferentPair_7_7_3_8_1: Choice_7_7_3 + Choice_7_8_1 <= 1
DifferentPair_7_7_3_8_5: Choice_7_7_3 + Choice_7_8_5 <= 1
DifferentPair_7_7_3_9_2: Choice_7_7_3 + Choice_7_9_2 <= 1
DifferentPair_7_7_3_9_4: Choice_7_7_3 + Choice_7_9_4 <= 1
DifferentPair_7_7_4_5_3: Choice_7_5_3 + Choice_7_7_4 <= 1
DifferentPair_7_7_4_5_5: Choice_7_5_5 + Choice_7_7_4 <= 1
DifferentPair_7_7_4_6_2: Choice_7_6_2 + Choice_7_7_4 <= 1
DifferentPair_7_7_4_6_6: Choice_7_6_6 + Choice_7_7_4 <= 1
DifferentPair_7_7_4_8_2: Choice_7_7_4 + Choice_7_8_2 <= 1
DifferentPair_7_7_4_8_6: Choice_7_7_4 + Choice_7_8_6 <= 1
DifferentPair_7_7_4_9_3: Choice_7_7_4 + Choice_7_9_3 <= 1
DifferentPair_7_7_4_9_5: Choice_7_7_4 + Choice_7_9_5 <= 1
DifferentPair_7_7_5_5_4: Choice_7_5_4 + Choice_7_7_5 <= 1
DifferentPair_7_7_5_5_6: Choice_7_5_6 + Choice_7_7_5 <= 1
DifferentPair_7_7_5_6_3: Choice_7_6_3 + Choice_7_7_5 <= 1
DifferentPair_7_7_5_6_7: Choice_7_6_7 + Choice_7_7_5 <= 1
DifferentPair_7_7_5_8_3: Choice_7_7_5 + Choice_7_8_3 <= 1
DifferentPair_7_7_5_8_7: Choice_7_7_5 + Choice_7_8_7 <= 1
DifferentPair_7_7_5_9_4: Choice_7_7_5 + Choice_7_9_4 <= 1
DifferentPair_7_7_5_9_6: Choice_7_7_5 + Choice_7_9_6 <= 1
DifferentPair_7_7_6_5_5: Choice_7_5_5 + Choice_7_7_6 <= 1
DifferentPair_7_7_6_5_7: Choice_7_5_7 + Choice_7_7_6 <= 1
DifferentPair_7_7_6_6_4: Choice_7_6_4 + Choice_7_7_6 <= 1
DifferentPair_7_7_6_6_8: Choice_7_6_8 + Choice_7_7_6 <= 1
DifferentPair_7_7_6_8_4: Choice_7_7_6 + Choice_7_8_4 <= 1
DifferentPair_7_7_6_8_8: Choice_7_7_6 + Choice_7_8_8 <= 1
DifferentPair_7_7_6_9_5: Choice_7_7_6 + Choice_7_9_5 <= 1
DifferentPair_7_7_6_9_7: Choice_7_7_6 + Choice_7_9_7 <= 1
DifferentPair_7_7_7_5_6: Choice_7_5_6 + Choice_7_7_7 <= 1
DifferentPair_7_7_7_5_8: Choice_7_5_8 + Choice_7_7_7 <= 1
DifferentPair_7_7_7_6_5: Choice_7_6_5 + Choice_7_7_7 <= 1
DifferentPair_7_7_7_6_9: Choice_7_6_9 + Choice_7_7_7 <= 1
DifferentPair_7_7_7_8_5: Choice_7_7_7 + Choice_7_8_5 <= 1
DifferentPair_7_7_7_8_9: Choice_7_7_7 + Choice_7_8_9 <= 1
DifferentPair_7_7_7_9_6: Choice_7_7_7 + Choice_7_9_6 <= 1
DifferentPair_7_7_7_9_8: Choice_7_7_7 + Choice_7_9_8 <= 1
DifferentPair_7_7_8_5_7: Choice_7_5_7 + Choice_7_7_8 <= 1
DifferentPair_7_7_8_5_9: Choice_7_5_9 + Choice_7_7_8 <= 1
DifferentPair_7_7_8_6_6: Choice_7_6_6 + Choice_7_7_8 <= 1
DifferentPair_7_7_8_8_6: Choice_7_7_8 + Choice_7_8_6 <= 1
DifferentPair_7_7_8_9_7: Choice_7_7_8 + Choice_7_9_7 <= 1
DifferentPair_7_7_8_9_9: Choice_7_7_8 + Choice_7_9_9 <= 1
DifferentPair_7_7_9_5_8: Choice_7_5_8 + Choice_7_7_9 <= 1
DifferentPair_7_7_9_6_7: Choice_7_6_7 + Choice_7_7_9 <= 1
DifferentPair_7_7_9_8_7: Choice_7_7_9 + Choice_7_8_7 <= 1
DifferentPair_7_7_9_9_8: Choice_7_7_9 + Choice_7_9_8 <= 1
DifferentPair_7_8_1_6_2: Choice_7_6_2 + Choice_7_8_1 <= 1
DifferentPair_7_8_1_7_3: Choice_7_7_3 + Choice_7_8_1 <= 1
DifferentPair_7_8_1_9_3: Choice_7_8_1 + Choice_7_9_3 <= 1
DifferentPair_7_8_2_6_1: Choice_7_6_1 + Choice_7_8_2 <= 1
DifferentPair_7_8_2_6_3: Choice_7_6_3 + Choice_7_8_2 <= 1
DifferentPair_7_8_2_7_4: Choice_7_7_4 + Choice_7_8_2 <= 1
DifferentPair_7_8_2_9_4: Choice_7_8_2 + Choice_7_9_4 <= 1
DifferentPair_7_8_3_6_2: Choice_7_6_2 + Choice_7_8_3 <= 1
DifferentPair_7_8_3_6_4: Choice_7_6_4 + Choice_7_8_3 <= 1
DifferentPair_7_8_3_7_1: Choice_7_7_1 + Choice_7_8_3 <= 1
DifferentPair_7_8_3_7_5: Choice_7_7_5 + Choice_7_8_3 <= 1
DifferentPair_7_8_3_9_1: Choice_7_8_3 + Choice_7_9_1 <= 1
DifferentPair_7_8_3_9_5: Choice_7_8_3 + Choice_7_9_5 <= 1
DifferentPair_7_8_4_6_3: Choice_7_6_3 + Choice_7_8_4 <= 1
DifferentPair_7_8_4_6_5: Choice_7_6_5 + Choice_7_8_4 <= 1
DifferentPair_7_8_4_7_2: Choice_7_7_2 + Choice_7_8_4 <= 1
DifferentPair_7_8_4_7_6: Choice_7_7_6 + Choice_7_8_4 <= 1
DifferentPair_7_8_4_9_2: Choice_7_8_4 + Choice_7_9_2 <= 1
DifferentPair_7_8_4_9_6: Choice_7_8_4 + Choice_7_9_6 <= 1
DifferentPair_7_8_5_6_4: Choice_7_6_4 + Choice_7_8_5 <= 1
DifferentPair_7_8_5_6_6: Choice_7_6_6 + Choice_7_8_5 <= 1
DifferentPair_7_8_5_7_3: Choice_7_7_3 + Choice_7_8_5 <= 1
DifferentPair_7_8_5_7_7: Choice_7_7_7 + Choice_7_8_5 <= 1
DifferentPair_7_8_5_9_3: Choice_7_8_5 + Choice_7_9_3 <= 1
DifferentPair_7_8_5_9_7: Choice_7_8_5 + Choice_7_9_7 <= 1
DifferentPair_7_8_6_6_5: Choice_7_6_5 + Choice_7_8_6 <= 1
DifferentPair_7_8_6_6_7: Choice_7_6_7 + Choice_7_8_6 <= 1
DifferentPair_7_8_6_7_4: Choice_7_7_4 + Choice_7_8_6 <= 1
DifferentPair_7_8_6_7_8: Choice_7_7_8 + Choice_7_8_6 <= 1
DifferentPair_7_8_6_9_4: Choice_7_8_6 + Choice_7_9_4 <= 1
DifferentPair_7_8_6_9_8: Choice_7_8_6 + Choice_7_9_8 <= 1
DifferentPair_7_8_7_6_6: Choice_7_6_6 + Choice_7_8_7 <= 1
DifferentPair_7_8_7_6_8: Choice_7_6_8 + Choice_7_8_7 <= 1
DifferentPair_7_8_7_7_5: Choice_7_7_5 + Choice_7_8_7 <= 1
DifferentPair_7_8_7_7_9: Choice_7_7_9 + Choice_7_8_7 <= 1
DifferentPair_7_8_7_9_5: Choice_7_8_7 + Choice_7_9_5 <= 1
DifferentPair_7_8_7_9_9: Choice_7_8_7 + Choice_7_9_9 <= 1
DifferentPair_7_8_8_6_7: Choice_7_6_7 + Choice_7_8_8 <= 1
DifferentPair_7_8_8_6_9: Choice_7_6_9 + Choice_7_8_8 <= 1
DifferentPair_7_8_8_7_6: Choice_7_7_6 + Choice_7_8_8 <= 1
DifferentPair_7_8_8_9_6: Choice_7_8_8 + Choice_7_9_6 <= 1
DifferentPair_7_8_9_6_8: Choice_7_6_8 + Choice_7_8_9 <= 1
DifferentPair_7_8_9_7_7: Choice_7_7_7 + Choice_7_8_9 <= 1
DifferentPair_7_8_9_9_7: Choice_7_8_9 + Choice_7_9_7 <= 1
DifferentPair_7_9_1_7_2: Choice_7_7_2 + Choice_7_9_1 <= 1
DifferentPair_7_9_1_8_3: Choice_7_8_3 + Choice_7_9_1 <= 1
DifferentPair_7_9_2_7_1: Choice_7_7_1 + Choice_7_9_2 <= 1
DifferentPair_7_9_2_7_3: Choice_7_7_3 + Choice_7_9_2 <= 1
DifferentPair_7_9_2_8_4: Choice_7_8_4 + Choice_7_9_2 <= 1
DifferentPair_7_9_3_7_2: Choice_7_7_2 + Choice_7_9_3 <= 1
DifferentPair_7_9_3_7_4: Choice_7_7_4 + Choice_7_9_3 <= 1
DifferentPair_7_9_3_8_1: Choice_7_8_1 + Choice_7_9_3 <= 1
DifferentPair_7_9_3_8_5: Choice_7_8_5 + Choice_7_9_3 <= 1
DifferentPair_7_9_4_7_3: Choice_7_7_3 + Choice_7_9_4 <= 1
DifferentPair_7_9_4_7_5: Choice_7_7_5 + Choice_7_9_4 <= 1
DifferentPair_7_9_4_8_2: Choice_7_8_2 + Choice_7_9_4 <= 1
DifferentPair_7_9_4_8_6: Choice_7_8_6 + Choice_7_9_4 <= 1
DifferentPair_7_9_5_7_4: Choice_7_7_4 + Choice_7_9_5 <= 1
DifferentPair_7_9_5_7_6: Choice_7_7_6 + Choice_7_9_5 <= 1
DifferentPair_7_9_5_8_3: Choice_7_8_3 + Choice_7_9_5 <= 1
DifferentPair_7_9_5_8_7: Choice_7_8_7 + Choice_7_9_5 <= 1
DifferentPair_7_9_6_7_5: Choice_7_7_5 + Choice_7_9_6 <= 1
DifferentPair_7_9_6_7_7: Choice_7_7_7 + Choice_7_9_6 <= 1
DifferentPair_7_9_6_8_4: Choice_7_8_4 + Choice_7_9_6 <= 1
DifferentPair_7_9_6_8_8: Choice_7_8_8 + Choice_7_9_6 <= 1
DifferentPair_7_9_7_7_6: Choice_7_7_6 + Choice_7_9_7 <= 1
DifferentPair_7_9_7_7_8: Choice_7_7_8 + Choice_7_9_7 <= 1
DifferentPair_7_9_7_8_5: Choice_7_8_5 + Choice_7_9_7 <= 1
DifferentPair_7_9_7_8_9: Choice_7_8_9 + Choice_7_9_7 <= 1
DifferentPair_7_9_8_7_7: Choice_7_7_7 + Choice_7_9_8 <= 1
DifferentPair_7_9_8_7_9: Choice_7_7_9 + Choice_7_9_8 <= 1
DifferentPair_7_9_8_8_6: Choice_7_8_6 + Choice_7_9_8 <= 1
DifferentPair_7_9_9_7_8: Choice_7_7_8 + Choice_7_9_9 <= 1
DifferentPair_7_9_9_8_7: Choice_7_8_7 + Choice_7_9_9 <= 1
DifferentPair_8_1_1_2_3: Choice_8_1_1 + Choice_8_2_3 <= 1
DifferentPair_8_1_1_3_2: Choice_8_1_1 + Choice_8_3_2 <= 1
DifferentPair_8_1_2_2_4: Choice_8_1_2 + Choice_8_2_4 <= 1
DifferentPair_8_1_2_3_1: Choice_8_1_2 + Choice_8_3_1 <= 1
DifferentPair_8_1_2_3_3: Choice_8_1_2 + Choice_8_3_3 <= 1
DifferentPair_8_1_3_2_1: Choice_8_1_3 + Choice_8_2_1 <= 1
DifferentPair_8_1_3_2_5: Choice_8_1_3 + Choice_8_2_5 <= 1
DifferentPair_8_1_3_3_2: Choice_8_1_3 + Choice_8_3_2 <= 1
DifferentPair_8_1_3_3_4: Choice_8_1_3 + Choice_8_3_4 <= 1
DifferentPair_8_1_4_2_2: Choice_8_1_4 + Choice_8_2_2 <= 1
DifferentPair_8_1_4_2_6: Choice_8_1_4 + Choice_8_2_6 <= 1
DifferentPair_8_1_4_3_3: Choice_8_1_4 + Choice_8_3_3 <= 1
DifferentPair_8_1_4_3_5: Choice_8_1_4 + Choice_8_3_5 <= 1
DifferentPair_8_1_5_2_3: Choice_8_1_5 + Choice_8_2_3 <= 1
DifferentPair_8_1_5_2_7: Choice_8_1_5 + Choice_8_2_7 <= 1
DifferentPair_8_1_5_3_4: Choice_8_1_5 + Choice_8_3_4 <= 1
DifferentPair_8_1_5_3_6: Choice_8_1_5 + Choice_8_3_6 <= 1
DifferentPair_8_1_6_2_4: Choice_8_1_6 + Choice_8_2_4 <= 1
DifferentPair_8_1_6_2_8: Choice_8_1_6 + Choice_8_2_8 <= 1
DifferentPair_8_1_6_3_5: Choice_8_1_6 + Choice_8_3_5 <= 1
DifferentPair_8_1_6_3_7: Choice_8_1_6 + Choice_8_3_7 <= 1
DifferentPair_8_1_7_2_5: Choice_8_1_7 + Choice_8_2_5 <= 1
DifferentPair_8_1_7_2_9: Choice_8_1_7 + Choice_8_2_9 <= 1
DifferentPair_8_1_7_3_6: Choice_8_1_7 + Choice_8_3_6 <= 1
DifferentPair_8_1_7_3_8: Choice_8_1_7 + Choice_8_3_8 <= 1
DifferentPair_8_1_8_2_6: Choice_8_1_8 + Choice_8_2_6 <= 1
DifferentPair_8_1_8_3_7: Choice_8_1_8 + Choice_8_3_7 <= 1
DifferentPair_8_1_8_3_9: Choice_8_1_8 + Choice_8_3_9 <= 1
DifferentPair_8_1_9_2_7: Choice_8_1_9 + Choice_8_2_7 <= 1
DifferentPair_8_1_9_3_8: Choice_8_1_9 + Choice_8_3_8 <= 1
DifferentPair_8_2_1_1_3: Choice_8_1_3 + Choice_8_2_1 <= 1
DifferentPair_8_2_1_3_3: Choice_8_2_1 + Choice_8_3_3 <= 1
DifferentPair_8_2_1_4_2: Choice_8_2_1 + Choice_8_4_2 <= 1
DifferentPair_8_2_2_1_4: Choice_8_1_4 + Choice_8_2_2 <= 1
DifferentPair_8_2_2_3_4: Choice_8_2_2 + Choice_8_3_4 <= 1
DifferentPair_8_2_2_4_1: Choice_8_2_2 + Choice_8_4_1 <= 1
DifferentPair_8_2_2_4_3: Choice_8_2_2 + Choice_8_4_3 <= 1
DifferentPair_8_2_3_1_1: Choice_8_1_1 + Choice_8_2_3 <= 1
DifferentPair_8_2_3_1_5: Choice_8_1_5 + Choice_8_2_3 <= 1
DifferentPair_8_2_3_3_1: Choice_8_2_3 + Choice_8_3_1 <= 1
DifferentPair_8_2_3_3_5: Choice_8_2_3 + Choice_8_3_5 <= 1
DifferentPair_8_2_3_4_2: Choice_8_2_3 + Choice_8_4_2 <= 1
DifferentPair_8_2_3_4_4: Choice_8_2_3 + Choice_8_4_4 <= 1
DifferentPair_8_2_4_1_2: Choice_8_1_2 + Choice_8_2_4 <= 1
DifferentPair_8_2_4_1_6: Choice_8_1_6 + Choice_8_2_4 <= 1
DifferentPair_8_2_4_3_2: Choice_8_2_4 + Choice_8_3_2 <= 1
DifferentPair_8_2_4_3_6: Choice_8_2_4 + Choice_8_3_6 <= 1
DifferentPair_8_2_4_4_3: Choice_8_2_4 + Choice_8_4_3 <= 1
DifferentPair_8_2_4_4_5: Choice_8_2_4 + Choice_8_4_5 <= 1
DifferentPair_8_2_5_1_3: Choice_8_1_3 + Choice_8_2_5 <= 1
DifferentPair_8_2_5_1_7: Choice_8_1_7 + Choice_8_2_5 <= 1
DifferentPair_8_2_5_3_3: Choice_8_2_5 + Choice_8_3_3 <= 1
DifferentPair_8_2_5_3_7: Choice_8_2_5 + Choice_8_3_7 <= 1
DifferentPair_8_2_5_4_4: Choice_8_2_5 + Choice_8_4_4 <= 1
DifferentPair_8_2_5_4_6: Choice_8_2_5 + Choice_8_4_6 <= 1
DifferentPair_8_2_6_1_4: Choice_8_1_4 + Choice_8_2_6 <= 1
DifferentPair_8_2_6_1_8: Choice_8_1_8 + Choice_8_2_6 <= 1
DifferentPair_8_2_6_3_4: Choice_8_2_6 + Choice_8_3_4 <= 1
DifferentPair_8_2_6_3_8: Choice_8_2_6 + Choice_8_3_8 <= 1
DifferentPair_8_2_6_4_5: Choice_8_2_6 + Choice_8_4_5 <= 1
DifferentPair_8_2_6_4_7: Choice_8_2_6 + Choice_8_4_7 <= 1
DifferentPair_8_2_7_1_5: Choice_8_1_5 + Choice_8_2_7 <= 1
DifferentPair_8_2_7_1_9: Choice_8_1_9 + Choice_8_2_7 <= 1
DifferentPair_8_2_7_3_5: Choice_8_2_7 + Choice_8_3_5 <= 1
DifferentPair_8_2_7_3_9: Choice_8_2_7 + Choice_8_3_9 <= 1
DifferentPair_8_2_7_4_6: Choice_8_2_7 + Choice_8_4_6 <= 1
DifferentPair_8_2_7_4_8: Choice_8_2_7 + Choice_8_4_8 <= 1
DifferentPair_8_2_8_1_6: Choice_8_1_6 + Choice_8_2_8 <= 1
DifferentPair_8_2_8_3_6: Choice_8_2_8 + Choice_8_3_6 <= 1
DifferentPair_8_2_8_4_7: Choice_8_2_8 + Choice_8_4_7 <= 1
DifferentPair_8_2_8_4_9: Choice_8_2_8 + Choice_8_4_9 <= 1
DifferentPair_8_2_9_1_7: Choice_8_1_7 + Choice_8_2_9 <= 1
DifferentPair_8_2_9_3_7: Choice_8_2_9 + Choice_8_3_7 <= 1
DifferentPair_8_2_9_4_8: Choice_8_2_9 + Choice_8_4_8 <= 1
DifferentPair_8_3_1_1_2: Choice_8_1_2 + Choice_8_3_1 <= 1
DifferentPair_8_3_1_2_3: Choice_8_2_3 + Choice_8_3_1 <= 1
DifferentPair_8_3_1_4_3: Choice_8_3_1 + Choice_8_4_3 <= 1
DifferentPair_8_3_1_5_2: Choice_8_3_1 + Choice_8_5_2 <= 1
DifferentPair_8_3_2_1_1: Choice_8_1_1 + Choice_8_3_2 <= 1
DifferentPair_8_3_2_1_3: Choice_8_1_3 + Choice_8_3_2 <= 1
DifferentPair_8_3_2_2_4: Choice_8_2_4 + Choice_8_3_2 <= 1
DifferentPair_8_3_2_4_4: Choice_8_3_2 + Choice_8_4_4 <= 1
DifferentPair_8_3_2_5_1: Choice_8_3_2 + Choice_8_5_1 <= 1
DifferentPair_8_3_2_5_3: Choice_8_3_2 + Choice_8_5_3 <= 1
DifferentPair_8_3_3_1_2: Choice_8_1_2 + Choice_8_3_3 <= 1
DifferentPair_8_3_3_1_4: Choice_8_1_4 + Choice_8_3_3 <= 1
DifferentPair_8_3_3_2_1: Choice_8_2_1 + Choice_8_3_3 <= 1
DifferentPair_8_3_3_2_5: Choice_8_2_5 + Choice_8_3_3 <= 1
DifferentPair_8_3_3_4_1: Choice_8_3_3 + Choice_8_4_1 <= 1
DifferentPair_8_3_3_4_5: Choice_8_3_3 + Choice_8_4_5 <= 1
DifferentPair_8_3_3_5_2: Choice_8_3_3 + Choice_8_5_2 <= 1
DifferentPair_8_3_3_5_4: Choice_8_3_3 + Choice_8_5_4 <= 1
DifferentPair_8_3_4_1_3: Choice_8_1_3 + Choice_8_3_4 <= 1
DifferentPair_8_3_4_1_5: Choice_8_1_5 + Choice_8_3_4 <= 1
DifferentPair_8_3_4_2_2: Choice_8_2_2 + Choice_8_3_4 <= 1
DifferentPair_8_3_4_2_6: Choice_8_2_6 + Choice_8_3_4 <= 1
DifferentPair_8_3_4_4_2: Choice_8_3_4 + Choice_8_4_2 <= 1
DifferentPair_8_3_4_4_6: Choice_8_3_4 + Choice_8_4_6 <= 1
DifferentPair_8_3_4_5_3: Choice_8_3_4 + Choice_8_5_3 <= 1
DifferentPair_8_3_4_5_5: Choice_8_3_4 + Choice_8_5_5 <= 1
DifferentPair_8_3_5_1_4: Choice_8_1_4 + Choice_8_3_5 <= 1
DifferentPair_8_3_5_1_6: Choice_8_1_6 + Choice_8_3_5 <= 1
DifferentPair_8_3_5_2_3: Choice_8_2_3 + Choice_8_3_5 <= 1
DifferentPair_8_3_5_2_7: Choice_8_2_7 + Choice_8_3_5 <= 1
DifferentPair_8_3_5_4_3: Choice_8_3_5 + Choice_8_4_3 <= 1
DifferentPair_8_3_5_4_7: Choice_8_3_5 + Choice_8_4_7 <= 1
DifferentPair_8_3_5_5_4: Choice_8_3_5 + Choice_8_5_4 <= 1
DifferentPair_8_3_5_5_6: Choice_8_3_5 + Choice_8_5_6 <= 1
DifferentPair_8_3_6_1_5: Choice_8_1_5 + Choice_8_3_6 <= 1
DifferentPair_8_3_6_1_7: Choice_8_1_7 + Choice_8_3_6 <= 1
DifferentPair_8_3_6_2_4: Choice_8_2_4 + Choice_8_3_6 <= 1
DifferentPair_8_3_6_2_8: Choice_8_2_8 + Choice_8_3_6 <= 1
DifferentPair_8_3_6_4_4: Choice_8_3_6 + Choice_8_4_4 <= 1
DifferentPair_8_3_6_4_8: Choice_8_3_6 + Choice_8_4_8 <= 1
DifferentPair_8_3_6_5_5: Choice_8_3_6 + Choice_8_5_5 <= 1
DifferentPair_8_3_6_5_7: Choice_8_3_6 + Choice_8_5_7 <= 1
DifferentPair_8_3_7_1_6: Choice_8_1_6 + Choice_8_3_7 <= 1
DifferentPair_8_3_7_1_8: Choice_8_1_8 + Choice_8_3_7 <= 1
DifferentPair_8_3_7_2_5: Choice_8_2_5 + Choice_8_3_7 <= 1
DifferentPair_8_3_7_2_9: Choice_8_2_9 + Choice_8_3_7 <= 1
DifferentPair_8_3_7_4_5: Choice_8_3_7 + Choice_8_4_5 <= 1
DifferentPair_8_3_7_4_9: Choice_8_3_7 + Choice_8_4_9 <= 1
DifferentPair_8_3_7_5_6: Choice_8_3_7 + Choice_8_5_6 <= 1
DifferentPair_8_3_7_5_8: Choice_8_3_7 + Choice_8_5_8 <= 1
DifferentPair_8_3_8_1_7: Choice_8_1_7 + Choice_8_3_8 <= 1
DifferentPair_8_3_8_1_9: Choice_8_1_9 + Choice_8_3_8 <= 1
DifferentPair_8_3_8_2_6: Choice_8_2_6 + Choice_8_3_8 <= 1
DifferentPair_8_3_8_4_6: Choice_8_3_8 + Choice_8_4_6 <= 1
DifferentPair_8_3_8_5_7: Choice_8_3_8 + Choice_8_5_7 <= 1
DifferentPair_8_3_8_5_9: Choice_8_3_8 + Choice_8_5_9 <= 1
DifferentPair_8_3_9_1_8: Choice_8_1_8 + Choice_8_3_9 <= 1
DifferentPair_8_3_9_2_7: Choice_8_2_7 + Choice_8_3_9 <= 1
DifferentPair_8_3_9_4_7: Choice_8_3_9 + Choice_8_4_7 <= 1
DifferentPair_8_3_9_5_8: Choice_8_3_9 + Choice_8_5_8 <= 1
DifferentPair_8_4_1_2_2: Choice_8_2_2 + Choice_8_4_1 <= 1
DifferentPair_8_4_1_3_3: Choice_8_3_3 + Choice_8_4_1 <= 1
DifferentPair_8_4_1_5_3: Choice_8_4_1 + Choice_8_5_3 <= 1
DifferentPair_8_4_1_6_2: Choice_8_4_1 + Choice_8_6_2 <= 1
DifferentPair_8_4_2_2_1: Choice_8_2_1 + Choice_8_4_2 <= 1
DifferentPair_8_4_2_2_3: Choice_8_2_3 + Choice_8_4_2 <= 1
DifferentPair_8_4_2_3_4: Choice_8_3_4 + Choice_8_4_2 <= 1
DifferentPair_8_4_2_5_4: Choice_8_4_2 + Choice_8_5_4 <= 1
DifferentPair_8_4_2_6_1: Choice_8_4_2 + Choice_8_6_1 <= 1
DifferentPair_8_4_2_6_3: Choice_8_4_2 + Choice_8_6_3 <= 1
DifferentPair_8_4_3_2_2: Choice_8_2_2 + Choice_8_4_3 <= 1
DifferentPair_8_4_3_2_4: Choice_8_2_4 + Choice_8_4_3 <= 1
DifferentPair_8_4_3_3_1: Choice_8_3_1 + Choice_8_4_3 <= 1
DifferentPair_8_4_3_3_5: Choice_8_3_5 + Choice_8_4_3 <= 1
DifferentPair_8_4_3_5_1: Choice_8_4_3 + Choice_8_5_1 <= 1
DifferentPair_8_4_3_5_5: Choice_8_4_3 + Choice_8_5_5 <= 1
DifferentPair_8_4_3_6_2: Choice_8_4_3 + Choice_8_6_2 <= 1
DifferentPair_8_4_3_6_4: Choice_8_4_3 + Choice_8_6_4 <= 1
DifferentPair_8_4_4_2_3: Choice_8_2_3 + Choice_8_4_4 <= 1
DifferentPair_8_4_4_2_5: Choice_8_2_5 + Choice_8_4_4 <= 1
DifferentPair_8_4_4_3_2: Choice_8_3_2 + Choice_8_4_4 <= 1
DifferentPair_8_4_4_3_6: Choice_8_3_6 + Choice_8_4_4 <= 1
DifferentPair_8_4_4_5_2: Choice_8_4_4 + Choice_8_5_2 <= 1
DifferentPair_8_4_4_5_6: Choice_8_4_4 + Choice_8_5_6 <= 1
DifferentPair_8_4_4_6_3: Choice_8_4_4 + Choice_8_6_3 <= 1
DifferentPair_8_4_4_6_5: Choice_8_4_4 + Choice_8_6_5 <= 1
DifferentPair_8_4_5_2_4: Choice_8_2_4 + Choice_8_4_5 <= 1
DifferentPair_8_4_5_2_6: Choice_8_2_6 + Choice_8_4_5 <= 1
DifferentPair_8_4_5_3_3: Choice_8_3_3 + Choice_8_4_5 <= 1
DifferentPair_8_4_5_3_7: Choice_8_3_7 + Choice_8_4_5 <= 1
DifferentPair_8_4_5_5_3: Choice_8_4_5 + Choice_8_5_3 <= 1
DifferentPair_8_4_5_5_7: Choice_8_4_5 + Choice_8_5_7 <= 1
DifferentPair_8_4_5_6_4: Choice_8_4_5 + Choice_8_6_4 <= 1
DifferentPair_8_4_5_6_6: Choice_8_4_5 + Choice_8_6_6 <= 1
DifferentPair_8_4_6_2_5: Choice_8_2_5 + Choice_8_4_6 <= 1
DifferentPair_8_4_6_2_7: Choice_8_2_7 + Choice_8_4_6 <= 1
DifferentPair_8_4_6_3_4: Choice_8_3_4 + Choice_8_4_6 <= 1
DifferentPair_8_4_6_3_8: Choice_8_3_8 + Choice_8_4_6 <= 1
DifferentPair_8_4_6_5_4: Choice_8_4_6 + Choice_8_5_4 <= 1
DifferentPair_8_4_6_5_8: Choice_8_4_6 + Choice_8_5_8 <= 1
DifferentPair_8_4_6_6_5: Choice_8_4_6 + Choice_8_6_5 <= 1
DifferentPair_8_4_6_6_7: Choice_8_4_6 + Choice_8_6_7 <= 1
DifferentPair_8_4_7_2_6: Choice_8_2_6 + Choice_8_4_7 <= 1
DifferentPair_8_4_7_2_8: Choice_8_2_8 + Choice_8_4_7 <= 1
DifferentPair_8_4_7_3_5: Choice_8_3_5 + Choice_8_4_7 <= 1
DifferentPair_8_4_7_3_9: Choice_8_3_9 + Choice_8_4_7 <= 1
DifferentPair_8_4_7_5_5: Choice_8_4_7 + Choice_8_5_5 <= 1
DifferentPair_8_4_7_5_9: Choice_8_4_7 + Choice_8_5_9 <= 1
DifferentPair_8_4_7_6_6: Choice_8_4_7 + Choice_8_6_6 <= 1
DifferentPair_8_4_7_6_8: Choice_8_4_7 + Choice_8_6_8 <= 1
DifferentPair_8_4_8_2_7: Choice_8_2_7 + Choice_8_4_8 <= 1
DifferentPair_8_4_8_2_9: Choice_8_2_9 + Choice_8_4_8 <= 1
DifferentPair_8_4_8_3_6: Choice_8_3_6 + Choice_8_4_8 <= 1
DifferentPair_8_4_8_5_6: Choice_8_4_8 + Choice_8_5_6 <= 1
DifferentPair_8_4_8_6_7: Choice_8_4_8 + Choice_8_6_7 <= 1
DifferentPair_8_4_8_6_9: Choice_8_4_8 + Choice_8_6_9 <= 1
DifferentPair_8_4_9_2_8: Choice_8_2_8 + Choice_8_4_9 <= 1
DifferentPair_8_4_9_3_7: Choice_8_3_7 + Choice_8_4_9 <= 1
DifferentPair_8_4_9_5_7: Choice_8_4_9 + Choice_8_5_7 <= 1
DifferentPair_8_4_9_6_8: Choice_8_4_9 + Choice_8_6_8 <= 1
DifferentPair_8_5_1_3_2: Choice_8_3_2 + Choice_8_5_1 <= 1
DifferentPair_8_5_1_4_3: Choice_8_4_3 + Choice_8_5_1 <= 1
DifferentPair_8_5_1_6_3: Choice_8_5_1 + Choice_8_6_3 <= 1
DifferentPair_8_5_1_7_2: Choice_8_5_1 + Choice_8_7_2 <= 1
DifferentPair_8_5_2_3_1: Choice_8_3_1 + Choice_8_5_2 <= 1
DifferentPair_8_5_2_3_3: Choice_8_3_3 + Choice_8_5_2 <= 1
DifferentPair_8_5_2_4_4: Choice_8_4_4 + Choice_8_5_2 <= 1
DifferentPair_8_5_2_6_4: Choice_8_5_2 + Choice_8_6_4 <= 1
DifferentPair_8_5_2_7_1: Choice_8_5_2 + Choice_8_7_1 <= 1
DifferentPair_8_5_2_7_3: Choice_8_5_2 + Choice_8_7_3 <= 1
DifferentPair_8_5_3_3_2: Choice_8_3_2 + Choice_8_5_3 <= 1
DifferentPair_8_5_3_3_4: Choice_8_3_4 + Choice_8_5_3 <= 1
DifferentPair_8_5_3_4_1: Choice_8_4_1 + Choice_8_5_3 <= 1
DifferentPair_8_5_3_4_5: Choice_8_4_5 + Choice_8_5_3 <= 1
DifferentPair_8_5_3_6_1: Choice_8_5_3 + Choice_8_6_1 <= 1
DifferentPair_8_5_3_6_5: Choice_8_5_3 + Choice_8_6_5 <= 1
DifferentPair_8_5_3_7_2: Choice_8_5_3 + Choice_8_7_2 <= 1
DifferentPair_8_5_3_7_4: Choice_8_5_3 + Choice_8_7_4 <= 1
DifferentPair_8_5_4_3_3: Choice_8_3_3 + Choice_8_5_4 <= 1
DifferentPair_8_5_4_3_5: Choice_8_3_5 + Choice_8_5_4 <= 1
DifferentPair_8_5_4_4_2: Choice_8_4_2 + Choice_8_5_4 <= 1
DifferentPair_8_5_4_4_6: Choice_8_4_6 + Choice_8_5_4 <= 1
DifferentPair_8_5_4_6_2: Choice_8_5_4 + Choice_8_6_2 <= 1
DifferentPair_8_5_4_6_6: Choice_8_5_4 + Choice_8_6_6 <= 1
DifferentPair_8_5_4_7_3: Choice_8_5_4 + Choice_8_7_3 <= 1
DifferentPair_8_5_4_7_5: Choice_8_5_4 + Choice_8_7_5 <= 1
DifferentPair_8_5_5_3_4: Choice_8_3_4 + Choice_8_5_5 <= 1
DifferentPair_8_5_5_3_6: Choice_8_3_6 + Choice_8_5_5 <= 1
DifferentPair_8_5_5_4_3: Choice_8_4_3 + Choice_8_5_5 <= 1
DifferentPair_8_5_5_4_7: Choice_8_4_7 + Choice_8_5_5 <= 1
DifferentPair_8_5_5_6_3: Choice_8_5_5 + Choice_8_6_3 <= 1
DifferentPair_8_5_5_6_7: Choice_8_5_5 + Choice_8_6_7 <= 1
DifferentPair_8_5_5_7_4: Choice_8_5_5 + Choice_8_7_4 <= 1
DifferentPair_8_5_5_7_6: Choice_8_5_5 + Choice_8_7_6 <= 1
DifferentPair_8_5_6_3_5: Choice_8_3_5 + Choice_8_5_6 <= 1
DifferentPair_8_5_6_3_7: Choice_8_3_7 + Choice_8_5_6 <= 1
DifferentPair_8_5_6_4_4: Choice_8_4_4 + Choice_8_5_6 <= 1
DifferentPair_8_5_6_4_8: Choice_8_4_8 + Choice_8_5_6 <= 1
DifferentPair_8_5_6_6_4: Choice_8_5_6 + Choice_8_6_4 <= 1
DifferentPair_8_5_6_6_8: Choice_8_5_6 + Choice_8_6_8 <= 1
DifferentPair_8_5_6_7_5: Choice_8_5_6 + Choice_8_7_5 <= 1
DifferentPair_8_5_6_7_7: Choice_8_5_6 + Choice_8_7_7 <= 1
DifferentPair_8_5_7_3_6: Choice_8_3_6 + Choice_8_5_7 <= 1
DifferentPair_8_5_7_3_8: Choice_8_3_8 + Choice_8_5_7 <= 1
DifferentPair_8_5_7_4_5: Choice_8_4_5 + Choice_8_5_7 <= 1
DifferentPair_8_5_7_4_9: Choice_8_4_9 + Choice_8_5_7 <= 1
DifferentPair_8_5_7_6_5: Choice_8_5_7 + Choice_8_6_5 <= 1
DifferentPair_8_5_7_6_9: Choice_8_5_7 + Choice_8_6_9 <= 1
DifferentPair_8_5_7_7_6: Choice_8_5_7 + Choice_8_7_6 <= 1
DifferentPair_8_5_7_7_8: Choice_8_5_7 + Choice_8_7_8 <= 1
DifferentPair_8_5_8_3_7: Choice_8_3_7 + Choice_8_5_8 <= 1
DifferentPair_8_5_8_3_9: Choice_8_3_9 + Choice_8_5_8 <= 1
DifferentPair_8_5_8_4_6: Choice_8_4_6 + Choice_8_5_8 <= 1
DifferentPair_8_5_8_6_6: Choice_8_5_8 + Choice_8_6_6 <= 1
DifferentPair_8_5_8_7_7: Choice_8_5_8 + Choice_8_7_7 <= 1
DifferentPair_8_5_8_7_9: Choice_8_5_8 + Choice_8_7_9 <= 1
DifferentPair_8_5_9_3_8: Choice_8_3_8 + Choice_8_5_9 <= 1
DifferentPair_8_5_9_4_7: Choice_8_4_7 + Choice_8_5_9 <= 1
DifferentPair_8_5_9_6_7: Choice_8_5_9 + Choice_8_6_7 <= 1
DifferentPair_8_5_9_7_8: Choice_8_5_9 + Choice_8_7_8 <= 1
DifferentPair_8_6_1_4_2: Choice_8_4_2 + Choice_8_6_1 <= 1
DifferentPair_8_6_1_5_3: Choice_8_5_3 + Choice_8_6_1 <= 1
DifferentPair_8_6_1_7_3: Choice_8_6_1 + Choice_8_7_3 <= 1
DifferentPair_8_6_1_8_2: Choice_8_6_1 + Choice_8_8_2 <= 1
DifferentPair_8_6_2_4_1: Choice_8_4_1 + Choice_8_6_2 <= 1
DifferentPair_8_6_2_4_3: Choice_8_4_3 + Choice_8_6_2 <= 1
DifferentPair_8_6_2_5_4: Choice_8_5_4 + Choice_8_6_2 <= 1
DifferentPair_8_6_2_7_4: Choice_8_6_2 + Choice_8_7_4 <= 1
DifferentPair_8_6_2_8_1: Choice_8_6_2 + Choice_8_8_1 <= 1
DifferentPair_8_6_2_8_3: Choice_8_6_2 + Choice_8_8_3 <= 1
DifferentPair_8_6_3_4_2: Choice_8_4_2 + Choice_8_6_3 <= 1
DifferentPair_8_6_3_4_4: Choice_8_4_4 + Choice_8_6_3 <= 1
DifferentPair_8_6_3_5_1: Choice_8_5_1 + Choice_8_6_3 <= 1
DifferentPair_8_6_3_5_5: Choice_8_5_5 + Choice_8_6_3 <= 1
DifferentPair_8_6_3_7_1: Choice_8_6_3 + Choice_8_7_1 <= 1
DifferentPair_8_6_3_7_5: Choice_8_6_3 + Choice_8_7_5 <= 1
DifferentPair_8_6_3_8_2: Choice_8_6_3 + Choice_8_8_2 <= 1
DifferentPair_8_6_3_8_4: Choice_8_6_3 + Choice_8_8_4 <= 1
DifferentPair_8_6_4_4_3: Choice_8_4_3 + Choice_8_6_4 <= 1
DifferentPair_8_6_4_4_5: Choice_8_4_5 + Choice_8_6_4 <= 1
DifferentPair_8_6_4_5_2: Choice_8_5_2 + Choice_8_6_4 <= 1
DifferentPair_8_6_4_5_6: Choice_8_5_6 + Choice_8_6_4 <= 1
DifferentPair_8_6_4_7_2: Choice_8_6_4 + Choice_8_7_2 <= 1
DifferentPair_8_6_4_7_6: Choice_8_6_4 + Choice_8_7_6 <= 1
DifferentPair_8_6_4_8_3: Choice_8_6_4 + Choice_8_8_3 <= 1
DifferentPair_8_6_4_8_5: Choice_8_6_4 + Choice_8_8_5 <= 1
DifferentPair_8_6_5_4_4: Choice_8_4_4 + Choice_8_6_5 <= 1
DifferentPair_8_6_5_4_6: Choice_8_4_6 + Choice_8_6_5 <= 1
DifferentPair_8_6_5_5_3: Choice_8_5_3 + Choice_8_6_5 <= 1
DifferentPair_8_6_5_5_7: Choice_8_5_7 + Choice_8_6_5 <= 1
DifferentPair_8_6_5_7_3: Choice_8_6_5 + Choice_8_7_3 <= 1
DifferentPair_8_6_5_7_7: Choice_8_6_5 + Choice_8_7_7 <= 1
DifferentPair_8_6_5_8_4: Choice_8_6_5 + Choice_8_8_4 <= 1
DifferentPair_8_6_5_8_6: Choice_8_6_5 + Choice_8_8_6 <= 1
DifferentPair_8_6_6_4_5: Choice_8_4_5 + Choice_8_6_6 <= 1
DifferentPair_8_6_6_4_7: Choice_8_4_7 + Choice_8_6_6 <= 1
DifferentPair_8_6_6_5_4: Choice_8_5_4 + Choice_8_6_6 <= 1
DifferentPair_8_6_6_5_8: Choice_8_5_8 + Choice_8_6_6 <= 1
DifferentPair_8_6_6_7_4: Choice_8_6_6 + Choice_8_7_4 <= 1
DifferentPair_8_6_6_7_8: Choice_8_6_6 + Choice_8_7_8 <= 1
DifferentPair_8_6_6_8_5: Choice_8_6_6 + Choice_8_8_5 <= 1
DifferentPair_8_6_6_8_7: Choice_8_6_6 + Choice_8_8_7 <= 1
DifferentPair_8_6_7_4_6: Choice_8_4_6 + Choice_8_6_7 <= 1
DifferentPair_8_6_7_4_8: Choice_8_4_8 + Choice_8_6_7 <= 1
DifferentPair_8_6_7_5_5: Choice_8_5_5 + Choice_8_6_7 <= 1
DifferentPair_8_6_7_5_9: Choice_8_5_9 + Choice_8_6_7 <= 1
DifferentPair_8_6_7_7_5: Choice_8_6_7 + Choice_8_7_5 <= 1
DifferentPair_8_6_7_7_9: Choice_8_6_7 + Choice_8_7_9 <= 1
DifferentPair_8_6_7_8_6: Choice_8_6_7 + Choice_8_8_6 <= 1
DifferentPair_8_6_7_8_8: Choice_8_6_7 + Choice_8_8_8 <= 1
DifferentPair_8_6_8_4_7: Choice_8_4_7 + Choice_8_6_8 <= 1
DifferentPair_8_6_8_4_9: Choice_8_4_9 + Choice_8_6_8 <= 1
DifferentPair_8_6_8_5_6: Choice_8_5_6 + Choice_8_6_8 <= 1
DifferentPair_8_6_8_7_6: Choice_8_6_8 + Choice_8_7_6 <= 1
DifferentPair_8_6_8_8_7: Choice_8_6_8 + Choice_8_8_7 <= 1
DifferentPair_8_6_8_8_9: Choice_8_6_8 + Choice_8_8_9 <= 1
DifferentPair_8_6_9_4_8: Choice_8_4_8 + Choice_8_6_9 <= 1
DifferentPair_8_6_9_5_7: Choice_8_5_7 + Choice_8_6_9 <= 1
DifferentPair_8_6_9_7_7: Choice_8_6_9 + Choice_8_7_7 <= 1
DifferentPair_8_6_9_8_8: Choice_8_6_9 + Choice_8_8_8 <= 1
DifferentPair_8_7_1_5_2: Choice_8_5_2 + Choice_8_7_1 <= 1
DifferentPair_8_7_1_6_3: Choice_8_6_3 + Choice_8_7_1 <= 1
DifferentPair_8_7_1_8_3: Choice_8_7_1 + Choice_8_8_3 <= 1
DifferentPair_8_7_1_9_2: Choice_8_7_1 + Choice_8_9_2 <= 1
DifferentPair_8_7_2_5_1: Choice_8_5_1 + Choice_8_7_2 <= 1
DifferentPair_8_7_2_5_3: Choice_8_5_3 + Choice_8_7_2 <= 1
DifferentPair_8_7_2_6_4: Choice_8_6_4 + Choice_8_7_2 <= 1
DifferentPair_8_7_2_8_4: Choice_8_7_2 + Choice_8_8_4 <= 1
DifferentPair_8_7_2_9_1: Choice_8_7_2 + Choice_8_9_1 <= 1
DifferentPair_8_7_2_9_3: Choice_8_7_2 + Choice_8_9_3 <= 1
DifferentPair_8_7_3_5_2: Choice_8_5_2 + Choice_8_7_3 <= 1
DifferentPair_8_7_3_5_4: Choice_8_5_4 + Choice_8_7_3 <= 1
DifferentPair_8_7_3_6_1: Choice_8_6_1 + Choice_8_7_3 <= 1
DifferentPair_8_7_3_6_5: Choice_8_6_5 + Choice_8_7_3 <= 1
DifferentPair_8_7_3_8_1: Choice_8_7_3 + Choice_8_8_1 <= 1
DifferentPair_8_7_3_8_5: Choice_8_7_3 + Choice_8_8_5 <= 1
DifferentPair_8_7_3_9_2: Choice_8_7_3 + Choice_8_9_2 <= 1
DifferentPair_8_7_3_9_4: Choice_8_7_3 + Choice_8_9_4 <= 1
DifferentPair_8_7_4_5_3: Choice_8_5_3 + Choice_8_7_4 <= 1
DifferentPair_8_7_4_5_5: Choice_8_5_5 + Choice_8_7_4 <= 1
DifferentPair_8_7_4_6_2: Choice_8_6_2 + Choice_8_7_4 <= 1
DifferentPair_8_7_4_6_6: Choice_8_6_6 + Choice_8_7_4 <= 1
DifferentPair_8_7_4_8_2: Choice_8_7_4 + Choice_8_8_2 <= 1
DifferentPair_8_7_4_8_6: Choice_8_7_4 + Choice_8_8_6 <= 1
DifferentPair_8_7_4_9_3: Choice_8_7_4 + Choice_8_9_3 <= 1
DifferentPair_8_7_4_9_5: Choice_8_7_4 + Choice_8_9_5 <= 1
DifferentPair_8_7_5_5_4: Choice_8_5_4 + Choice_8_7_5 <= 1
DifferentPair_8_7_5_5_6: Choice_8_5_6 + Choice_8_7_5 <= 1
DifferentPair_8_7_5_6_3: Choice_8_6_3 + Choice_8_7_5 <= 1
DifferentPair_8_7_5_6_7: Choice_8_6_7 + Choice_8_7_5 <= 1
DifferentPair_8_7_5_8_3: Choice_8_7_5 + Choice_8_8_3 <= 1
DifferentPair_8_7_5_8_7: Choice_8_7_5 + Choice_8_8_7 <= 1
DifferentPair_8_7_5_9_4: Choice_8_7_5 + Choice_8_9_4 <= 1
DifferentPair_8_7_5_9_6: Choice_8_7_5 + Choice_8_9_6 <= 1
DifferentPair_8_7_6_5_5: Choice_8_5_5 + Choice_8_7_6 <= 1
DifferentPair_8_7_6_5_7: Choice_8_5_7 + Choice_8_7_6 <= 1
DifferentPair_8_7_6_6_4: Choice_8_6_4 + Choice_8_7_6 <= 1
DifferentPair_8_7_6_6_8: Choice_8_6_8 + Choice_8_7_6 <= 1
DifferentPair_8_7_6_8_4: Choice_8_7_6 + Choice_8_8_4 <= 1
DifferentPair_8_7_6_8_8: Choice_8_7_6 + Choice_8_8_8 <= 1
DifferentPair_8_7_6_9_5: Choice_8_7_6 + Choice_8_9_5 <= 1
DifferentPair_8_7_6_9_7: Choice_8_7_6 + Choice_8_9_7 <= 1
DifferentPair_8_7_7_5_6: Choice_8_5_6 + Choice_8_7_7 <= 1
DifferentPair_8_7_7_5_8: Choice_8_5_8 + Choice_8_7_7 <= 1
DifferentPair_8_7_7_6_5: Choice_8_6_5 + Choice_8_7_7 <= 1
DifferentPair_8_7_7_6_9: Choice_8_6_9 + Choice_8_7_7 <= 1
DifferentPair_8_7_7_8_5: Choice_8_7_7 + Choice_8_8_5 <= 1
DifferentPair_8_7_7_8_9: Choice_8_7_7 + Choice_8_8_9 <= 1
DifferentPair_8_7_7_9_6: Choice_8_7_7 + Choice_8_9_6 <= 1
DifferentPair_8_7_7_9_8: Choice_8_7_7 + Choice_8_9_8 <= 1
DifferentPair_8_7_8_5_7: Choice_8_5_7 + Choice_8_7_8 <= 1
DifferentPair_8_7_8_5_9: Choice_8_5_9 + Choice_8_7_8 <= 1
DifferentPair_8_7_8_6_6: Choice_8_6_6 + Choice_8_7_8 <= 1
DifferentPair_8_7_8_8_6: Choice_8_7_8 + Choice_8_8_6 <= 1
DifferentPair_8_7_8_9_7: Choice_8_7_8 + Choice_8_9_7 <= 1
DifferentPair_8_7_8_9_9: Choice_8_7_8 + Choice_8_9_9 <= 1
DifferentPair_8_7_9_5_8: Choice_8_5_8 + Choice_8_7_9 <= 1
DifferentPair_8_7_9_6_7: Choice_8_6_7 + Choice_8_7_9 <= 1
DifferentPair_8_7_9_8_7: Choice_8_7_9 + Choice_8_8_7 <= 1
DifferentPair_8_7_9_9_8: Choice_8_7_9 + Choice_8_9_8 <= 1
DifferentPair_8_8_1_6_2: Choice_8_6_2 + Choice_8_8_1 <= 1
DifferentPair_8_8_1_7_3: Choice_8_7_3 + Choice_8_8_1 <= 1
DifferentPair_8_8_1_9_3: Choice_8_8_1 + Choice_8_9_3 <= 1
DifferentPair_8_8_2_6_1: Choice_8_6_1 + Choice_8_8_2 <= 1
DifferentPair_8_8_2_6_3: Choice_8_6_3 + Choice_8_8_2 <= 1
DifferentPair_8_8_2_7_4: Choice_8_7_4 + Choice_8_8_2 <= 1
DifferentPair_8_8_2_9_4: Choice_8_8_2 + Choice_8_9_4 <= 1
DifferentPair_8_8_3_6_2: Choice_8_6_2 + Choice_8_8_3 <= 1
DifferentPair_8_8_3_6_4: Choice_8_6_4 + Choice_8_8_3 <= 1
DifferentPair_8_8_3_7_1: Choice_8_7_1 + Choice_8_8_3 <= 1
DifferentPair_8_8_3_7_5: Choice_8_7_5 + Choice_8_8_3 <= 1
DifferentPair_8_8_3_9_1: Choice_8_8_3 + Choice_8_9_1 <= 1
DifferentPair_8_8_3_9_5: Choice_8_8_3 + Choice_8_9_5 <= 1
DifferentPair_8_8_4_6_3: Choice_8_6_3 + Choice_8_8_4 <= 1
DifferentPair_8_8_4_6_5: Choice_8_6_5 + Choice_8_8_4 <= 1
DifferentPair_8_8_4_7_2: Choice_8_7_2 + Choice_8_8_4 <= 1
DifferentPair_8_8_4_7_6: Choice_8_7_6 + Choice_8_8_4 <= 1
DifferentPair_8_8_4_9_2: Choice_8_8_4 + Choice_8_9_2 <= 1
DifferentPair_8_8_4_9_6: Choice_8_8_4 + Choice_8_9_6 <= 1
DifferentPair_8_8_5_6_4: Choice_8_6_4 + Choice_8_8_5 <= 1
DifferentPair_8_8_5_6_6: Choice_8_6_6 + Choice_8_8_5 <= 1
DifferentPair_8_8_5_7_3: Choice_8_7_3 + Choice_8_8_5 <= 1
DifferentPair_8_8_5_7_7: Choice_8_7_7 + Choice_8_8_5 <= 1
DifferentPair_8_8_5_9_3: Choice_8_8_5 + Choice_8_9_3 <= 1
DifferentPair_8_8_5_9_7: Choice_8_8_5 + Choice_8_9_7 <= 1
DifferentPair_8_8_6_6_5: Choice_8_6_5 + Choice_8_8_6 <= 1
DifferentPair_8_8_6_6_7: Choice_8_6_7 + Choice_8_8_6 <= 1
DifferentPair_8_8_6_7_4: Choice_8_7_4 + Choice_8_8_6 <= 1
DifferentPair_8_8_6_7_8: Choice_8_7_8 + Choice_8_8_6 <= 1
DifferentPair_8_8_6_9_4: Choice_8_8_6 + Choice_8_9_4 <= 1
DifferentPair_8_8_6_9_8: Choice_8_8_6 + Choice_8_9_8 <= 1
DifferentPair_8_8_7_6_6: Choice_8_6_6 + Choice_8_8_7 <= 1
DifferentPair_8_8_7_6_8: Choice_8_6_8 + Choice_8_8_7 <= 1
DifferentPair_8_8_7_7_5: Choice_8_7_5 + Choice_8_8_7 <= 1
DifferentPair_8_8_7_7_9: Choice_8_7_9 + Choice_8_8_7 <= 1
DifferentPair_8_8_7_9_5: Choice_8_8_7 + Choice_8_9_5 <= 1
DifferentPair_8_8_7_9_9: Choice_8_8_7 + Choice_8_9_9 <= 1
DifferentPair_8_8_8_6_7: Choice_8_6_7 + Choice_8_8_8 <= 1
DifferentPair_8_8_8_6_9: Choice_8_6_9 + Choice_8_8_8 <= 1
DifferentPair_8_8_8_7_6: Choice_8_7_6 + Choice_8_8_8 <= 1
DifferentPair_8_8_8_9_6: Choice_8_8_8 + Choice_8_9_6 <= 1
DifferentPair_8_8_9_6_8: Choice_8_6_8 + Choice_8_8_9 <= 1
DifferentPair_8_8_9_7_7: Choice_8_7_7 + Choice_8_8_9 <= 1
DifferentPair_8_8_9_9_7: Choice_8_8_9 + Choice_8_9_7 <= 1
DifferentPair_8_9_1_7_2: Choice_8_7_2 + Choice_8_9_1 <= 1
DifferentPair_8_9_1_8_3: Choice_8_8_3 + Choice_8_9_1 <= 1
DifferentPair_8_9_2_7_1: Choice_8_7_1 + Choice_8_9_2 <= 1
DifferentPair_8_9_2_7_3: Choice_8_7_3 + Choice_8_9_2 <= 1
DifferentPair_8_9_2_8_4: Choice_8_8_4 + Choice_8_9_2 <= 1
DifferentPair_8_9_3_7_2: Choice_8_7_2 + Choice_8_9_3 <= 1
DifferentPair_8_9_3_7_4: Choice_8_7_4 + Choice_8_9_3 <= 1
DifferentPair_8_9_3_8_1: Choice_8_8_1 + Choice_8_9_3 <= 1
DifferentPair_8_9_3_8_5: Choice_8_8_5 + Choice_8_9_3 <= 1
DifferentPair_8_9_4_7_3: Choice_8_7_3 + Choice_8_9_4 <= 1
DifferentPair_8_9_4_7_5: Choice_8_7_5 + Choice_8_9_4 <= 1
DifferentPair_8_9_4_8_2: Choice_8_8_2 + Choice_8_9_4 <= 1
DifferentPair_8_9_4_8_6: Choice_8_8_6 + Choice_8_9_4 <= 1
DifferentPair_8_9_5_7_4: Choice_8_7_4 + Choice_8_9_5 <= 1
DifferentPair_8_9_5_7_6: Choice_8_7_6 + Choice_8_9_5 <= 1
DifferentPair_8_9_5_8_3: Choice_8_8_3 + Choice_8_9_5 <= 1
DifferentPair_8_9_5_8_7: Choice_8_8_7 + Choice_8_9_5 <= 1
DifferentPair_8_9_6_7_5: Choice_8_7_5 + Choice_8_9_6 <= 1
DifferentPair_8_9_6_7_7: Choice_8_7_7 + Choice_8_9_6 <= 1
DifferentPair_8_9_6_8_4: Choice_8_8_4 + Choice_8_9_6 <= 1
DifferentPair_8_9_6_8_8: Choice_8_8_8 + Choice_8_9_6 <= 1
DifferentPair_8_9_7_7_6: Choice_8_7_6 + Choice_8_9_7 <= 1
DifferentPair_8_9_7_7_8: Choice_8_7_8 + Choice_8_9_7 <= 1
DifferentPair_8_9_7_8_5: Choice_8_8_5 + Choice_8_9_7 <= 1
DifferentPair_8_9_7_8_9: Choice_8_8_9 + Choice_8_9_7 <= 1
DifferentPair_8_9_8_7_7: Choice_8_7_7 + Choice_8_9_8 <= 1
DifferentPair_8_9_8_7_9: Choice_8_7_9 + Choice_8_9_8 <= 1
DifferentPair_8_9_8_8_6: Choice_8_8_6 + Choice_8_9_8 <= 1
DifferentPair_8_9_9_7_8: Choice_8_7_8 + Choice_8_9_9 <= 1
DifferentPair_8_9_9_8_7: Choice_8_8_7 + Choice_8_9_9 <= 1
DifferentPair_9_1_1_2_3: Choice_9_1_1 + Choice_9_2_3 <= 1
DifferentPair_9_1_1_3_2: Choice_9_1_1 + Choice_9_3_2 <= 1
DifferentPair_9_1_2_2_4: Choice_9_1_2 + Choice_9_2_4 <= 1
DifferentPair_9_1_2_3_1: Choice_9_1_2 + Choice_9_3_1 <= 1
DifferentPair_9_1_2_3_3: Choice_9_1_2 + Choice_9_3_3 <= 1
DifferentPair_9_1_3_2_1: Choice_9_1_3 + Choice_9_2_1 <= 1
DifferentPair_9_1_3_2_5: Choice_9_1_3 + Choice_9_2_5 <= 1
DifferentPair_9_1_3_3_2: Choice_9_1_3 + Choice_9_3_2 <= 1
DifferentPair_9_1_3_3_4: Choice_9_1_3 + Choice_9_3_4 <= 1
DifferentPair_9_1_4_2_2: Choice_9_1_4 + Choice_9_2_2 <= 1
DifferentPair_9_1_4_2_6: Choice_9_1_4 + Choice_9_2_6 <= 1
DifferentPair_9_1_4_3_3: Choice_9_1_4 + Choice_9_3_3 <= 1
DifferentPair_9_1_4_3_5: Choice_9_1_4 + Choice_9_3_5 <= 1
DifferentPair_9_1_5_2_3: Choice_9_1_5 + Choice_9_2_3 <= 1
DifferentPair_9_1_5_2_7: Choice_9_1_5 + Choice_9_2_7 <= 1
DifferentPair_9_1_5_3_4: Choice_9_1_5 + Choice_9_3_4 <= 1
DifferentPair_9_1_5_3_6: Choice_9_1_5 + Choice_9_3_6 <= 1
DifferentPair_9_1_6_2_4: Choice_9_1_6 + Choice_9_2_4 <= 1
DifferentPair_9_1_6_2_8: Choice_9_1_6 + Choice_9_2_8 <= 1
DifferentPair_9_1_6_3_5: Choice_9_1_6 + Choice_9_3_5 <= 1
DifferentPair_9_1_6_3_7: Choice_9_1_6 + Choice_9_3_7 <= 1
DifferentPair_9_1_7_2_5: Choice_9_1_7 + Choice_9_2_5 <= 1
DifferentPair_9_1_7_2_9: Choice_9_1_7 + Choice_9_2_9 <= 1
DifferentPair_9_1_7_3_6: Choice_9_1_7 + Choice_9_3_6 <= 1
DifferentPair_9_1_7_3_8: Choice_9_1_7 + Choice_9_3_8 <= 1
DifferentPair_9_1_8_2_6: Choice_9_1_8 + Choice_9_2_6 <= 1
DifferentPair_9_1_8_3_7: Choice_9_1_8 + Choice_9_3_7 <= 1
DifferentPair_9_1_8_3_9: Choice_9_1_8 + Choice_9_3_9 <= 1
DifferentPair_9_1_9_2_7: Choice_9_1_9 + Choice_9_2_7 <= 1
DifferentPair_9_1_9_3_8: Choice_9_1_9 + Choice_9_3_8 <= 1
DifferentPair_9_2_1_1_3: Choice_9_1_3 + Choice_9_2_1 <= 1
DifferentPair_9_2_1_3_3: Choice_9_2_1 + Choice_9_3_3 <= 1
DifferentPair_9_2_1_4_2: Choice_9_2_1 + Choice_9_4_2 <= 1
DifferentPair_9_2_2_1_4: Choice_9_1_4 + Choice_9_2_2 <= 1
DifferentPair_9_2_2_3_4: Choice_9_2_2 + Choice_9_3_4 <= 1
DifferentPair_9_2_2_4_1: Choice_9_2_2 + Choice_9_4_1 <= 1
DifferentPair_9_2_2_4_3: Choice_9_2_2 + Choice_9_4_3 <= 1
DifferentPair_9_2_3_1_1: Choice_9_1_1 + Choice_9_2_3 <= 1
DifferentPair_9_2_3_1_5: Choice_9_1_5 + Choice_9_2_3 <= 1
DifferentPair_9_2_3_3_1: Choice_9_2_3 + Choice_9_3_1 <= 1
DifferentPair_9_2_3_3_5: Choice_9_2_3 + Choice_9_3_5 <= 1
DifferentPair_9_2_3_4_2: Choice_9_2_3 + Choice_9_4_2 <= 1
DifferentPair_9_2_3_4_4: Choice_9_2_3 + Choice_9_4_4 <= 1
DifferentPair_9_2_4_1_2: Choice_9_1_2 + Choice_9_2_4 <= 1
DifferentPair_9_2_4_1_6: Choice_9_1_6 + Choice_9_2_4 <= 1
DifferentPair_9_2_4_3_2: Choice_9_2_4 + Choice_9_3_2 <= 1
DifferentPair_9_2_4_3_6: Choice_9_2_4 + Choice_9_3_6 <= 1
DifferentPair_9_2_4_4_3: Choice_9_2_4 + Choice_9_4_3 <= 1
DifferentPair_9_2_4_4_5: Choice_9_2_4 + Choice_9_4_5 <= 1
DifferentPair_9_2_5_1_3: Choice_9_1_3 + Choice_9_2_5 <= 1
DifferentPair_9_2_5_1_7: Choice_9_1_7 + Choice_9_2_5 <= 1
DifferentPair_9_2_5_3_3: Choice_9_2_5 + Choice_9_3_3 <= 1
DifferentPair_9_2_5_3_7: Choice_9_2_5 + Choice_9_3_7 <= 1
DifferentPair_9_2_5_4_4: Choice_9_2_5 + Choice_9_4_4 <= 1
DifferentPair_9_2_5_4_6: Choice_9_2_5 + Choice_9_4_6 <= 1
DifferentPair_9_2_6_1_4: Choice_9_1_4 + Choice_9_2_6 <= 1
DifferentPair_9_2_6_1_8: Choice_9_1_8 + Choice_9_2_6 <= 1
DifferentPair_9_2_6_3_4: Choice_9_2_6 + Choice_9_3_4 <= 1
DifferentPair_9_2_6_3_8: Choice_9_2_6 + Choice_9_3_8 <= 1
DifferentPair_9_2_6_4_5: Choice_9_2_6 + Choice_9_4_5 <= 1
DifferentPair_9_2_6_4_7: Choice_9_2_6 + Choice_9_4_7 <= 1
DifferentPair_9_2_7_1_5: Choice_9_1_5 + Choice_9_2_7 <= 1
DifferentPair_9_2_7_1_9: Choice_9_1_9 + Choice_9_2_7 <= 1
DifferentPair_9_2_7_3_5: Choice_9_2_7 + Choice_9_3_5 <= 1
DifferentPair_9_2_7_3_9: Choice_9_2_7 + Choice_9_3_9 <= 1
DifferentPair_9_2_7_4_6: Choice_9_2_7 + Choice_9_4_6 <= 1
DifferentPair_9_2_7_4_8: Choice_9_2_7 + Choice_9_4_8 <= 1
DifferentPair_9_2_8_1_6: Choice_9_1_6 + Choice_9_2_8 <= 1
DifferentPair_9_2_8_3_6: Choice_9_2_8 + Choice_9_3_6 <= 1
DifferentPair_9_2_8_4_7: Choice_9_2_8 + Choice_9_4_7 <= 1
DifferentPair_9_2_8_4_9: Choice_9_2_8 + Choice_9_4_9 <= 1
DifferentPair_9_2_9_1_7: Choice_9_1_7 + Choice_9_2_9 <= 1
DifferentPair_9_2_9_3_7: Choice_9_2_9 + Choice_9_3_7 <= 1
DifferentPair_9_2_9_4_8: Choice_9_2_9 + Choice_9_4_8 <= 1
DifferentPair_9_3_1_1_2: Choice_9_1_2 + Choice_9_3_1 <= 1
DifferentPair_9_3_1_2_3: Choice_9_2_3 + Choice_9_3_1 <= 1
DifferentPair_9_3_1_4_3: Choice_9_3_1 + Choice_9_4_3 <= 1
DifferentPair_9_3_1_5_2: Choice_9_3_1 + Choice_9_5_2 <= 1
DifferentPair_9_3_2_1_1: Choice_9_1_1 + Choice_9_3_2 <= 1
DifferentPair_9_3_2_1_3: Choice_9_1_3 + Choice_9_3_2 <= 1
DifferentPair_9_3_2_2_4: Choice_9_2_4 + Choice_9_3_2 <= 1
DifferentPair_9_3_2_4_4: Choice_9_3_2 + Choice_9_4_4 <= 1
DifferentPair_9_3_2_5_1: Choice_9_3_2 + Choice_9_5_1 <= 1
DifferentPair_9_3_2_5_3: Choice_9_3_2 + Choice_9_5_3 <= 1
DifferentPair_9_3_3_1_2: Choice_9_1_2 + Choice_9_3_3 <= 1
DifferentPair_9_3_3_1_4: Choice_9_1_4 + Choice_9_3_3 <= 1
DifferentPair_9_3_3_2_1: Choice_9_2_1 + Choice_9_3_3 <= 1
DifferentPair_9_3_3_2_5: Choice_9_2_5 + Choice_9_3_3 <= 1
DifferentPair_9_3_3_4_1: Choice_9_3_3 + Choice_9_4_1 <= 1
DifferentPair_9_3_3_4_5: Choice_9_3_3 + Choice_9_4_5 <= 1
DifferentPair_9_3_3_5_2: Choice_9_3_3 + Choice_9_5_2 <= 1
DifferentPair_9_3_3_5_4: Choice_9_3_3 + Choice_9_5_4 <= 1
DifferentPair_9_3_4_1_3: Choice_9_1_3 + Choice_9_3_4 <= 1
DifferentPair_9_3_4_1_5: Choice_9_1_5 + Choice_9_3_4 <= 1
DifferentPair_9_3_4_2_2: Choice_9_2_2 + Choice_9_3_4 <= 1
DifferentPair_9_3_4_2_6: Choice_9_2_6 + Choice_9_3_4 <= 1
DifferentPair_9_3_4_4_2: Choice_9_3_4 + Choice_9_4_2 <= 1
DifferentPair_9_3_4_4_6: Choice_9_3_4 + Choice_9_4_6 <= 1
DifferentPair_9_3_4_5_3: Choice_9_3_4 + Choice_9_5_3 <= 1
DifferentPair_9_3_4_5_5: Choice_9_3_4 + Choice_9_5_5 <= 1
DifferentPair_9_3_5_1_4: Choice_9_1_4 + Choice_9_3_5 <= 1
DifferentPair_9_3_5_1_6: Choice_9_1_6 + Choice_9_3_5 <= 1
DifferentPair_9_3_5_2_3: Choice_9_2_3 + Choice_9_3_5 <= 1
DifferentPair_9_3_5_2_7: Choice_9_2_7 + Choice_9_3_5 <= 1
DifferentPair_9_3_5_4_3: Choice_9_3_5 + Choice_9_4_3 <= 1
DifferentPair_9_3_5_4_7: Choice_9_3_5 + Choice_9_4_7 <= 1
DifferentPair_9_3_5_5_4: Choice_9_3_5 + Choice_9_5_4 <= 1
DifferentPair_9_3_5_5_6: Choice_9_3_5 + Choice_9_5_6 <= 1
DifferentPair_9_3_6_1_5: Choice_9_1_5 + Choice_9_3_6 <= 1
DifferentPair_9_3_6_1_7: Choice_9_1_7 + Choice_9_3_6 <= 1
DifferentPair_9_3_6_2_4: Choice_9_2_4 + Choice_9_3_6 <= 1
DifferentPair_9_3_6_2_8: Choice_9_2_8 + Choice_9_3_6 <= 1
DifferentPair_9_3_6_4_4: Choice_9_3_6 + Choice_9_4_4 <= 1
DifferentPair_9_3_6_4_8: Choice_9_3_6 + Choice_9_4_8 <= 1
DifferentPair_9_3_6_5_5: Choice_9_3_6 + Choice_9_5_5 <= 1
DifferentPair_9_3_6_5_7: Choice_9_3_6 + Choice_9_5_7 <= 1
DifferentPair_9_3_7_1_6: Choice_9_1_6 + Choice_9_3_7 <= 1
DifferentPair_9_3_7_1_8: Choice_9_1_8 + Choice_9_3_7 <= 1
DifferentPair_9_3_7_2_5: Choice_9_2_5 + Choice_9_3_7 <= 1
DifferentPair_9_3_7_2_9: Choice_9_2_9 + Choice_9_3_7 <= 1
DifferentPair_9_3_7_4_5: Choice_9_3_7 + Choice_9_4_5 <= 1
DifferentPair_9_3_7_4_9: Choice_9_3_7 + Choice_9_4_9 <= 1
DifferentPair_9_3_7_5_6: Choice_9_3_7 + Choice_9_5_6 <= 1
DifferentPair_9_3_7_5_8: Choice_9_3_7 + Choice_9_5_8 <= 1
DifferentPair_9_3_8_1_7: Choice_9_1_7 + Choice_9_3_8 <= 1
DifferentPair_9_3_8_1_9: Choice_9_1_9 + Choice_9_3_8 <= 1
DifferentPair_9_3_8_2_6: Choice_9_2_6 + Choice_9_3_8 <= 1
DifferentPair_9_3_8_4_6: Choice_9_3_8 + Choice_9_4_6 <= 1
DifferentPair_9_3_8_5_7: Choice_9_3_8 + Choice_9_5_7 <= 1
DifferentPair_9_3_8_5_9: Choice_9_3_8 + Choice_9_5_9 <= 1
DifferentPair_9_3_9_1_8: Choice_9_1_8 + Choice_9_3_9 <= 1
DifferentPair_9_3_9_2_7: Choice_9_2_7 + Choice_9_3_9 <= 1
DifferentPair_9_3_9_4_7: Choice_9_3_9 + Choice_9_4_7 <= 1
DifferentPair_9_3_9_5_8: Choice_9_3_9 + Choice_9_5_8 <= 1
DifferentPair_9_4_1_2_2: Choice_9_2_2 + Choice_9_4_1 <= 1
DifferentPair_9_4_1_3_3: Choice_9_3_3 + Choice_9_4_1 <= 1
DifferentPair_9_4_1_5_3: Choice_9_4_1 + Choice_9_5_3 <= 1
DifferentPair_9_4_1_6_2: Choice_9_4_1 + Choice_9_6_2 <= 1
DifferentPair_9_4_2_2_1: Choice_9_2_1 + Choice_9_4_2 <= 1
DifferentPair_9_4_2_2_3: Choice_9_2_3 + Choice_9_4_2 <= 1
DifferentPair_9_4_2_3_4: Choice_9_3_4 + Choice_9_4_2 <= 1
DifferentPair_9_4_2_5_4: Choice_9_4_2 + Choice_9_5_4 <= 1
DifferentPair_9_4_2_6_1: Choice_9_4_2 + Choice_9_6_1 <= 1
DifferentPair_9_4_2_6_3: Choice_9_4_2 + Choice_9_6_3 <= 1
DifferentPair_9_4_3_2_2: Choice_9_2_2 + Choice_9_4_3 <= 1
DifferentPair_9_4_3_2_4: Choice_9_2_4 + Choice_9_4_3 <= 1
DifferentPair_9_4_3_3_1: Choice_9_3_1 + Choice_9_4_3 <= 1
DifferentPair_9_4_3_3_5: Choice_9_3_5 + Choice_9_4_3 <= 1
DifferentPair_9_4_3_5_1: Choice_9_4_3 + Choice_9_5_1 <= 1
DifferentPair_9_4_3_5_5: Choice_9_4_3 + Choice_9_5_5 <= 1
DifferentPair_9_4_3_6_2: Choice_9_4_3 + Choice_9_6_2 <= 1
DifferentPair_9_4_3_6_4: Choice_9_4_3 + Choice_9_6_4 <= 1
DifferentPair_9_4_4_2_3: Choice_9_2_3 + Choice_9_4_4 <= 1
DifferentPair_9_4_4_2_5: Choice_9_2_5 + Choice_9_4_4 <= 1
DifferentPair_9_4_4_3_2: Choice_9_3_2 + Choice_9_4_4 <= 1
DifferentPair_9_4_4_3_6: Choice_9_3_6 + Choice_9_4_4 <= 1
DifferentPair_9_4_4_5_2: Choice_9_4_4 + Choice_9_5_2 <= 1
DifferentPair_9_4_4_5_6: Choice_9_4_4 + Choice_9_5_6 <= 1
DifferentPair_9_4_4_6_3: Choice_9_4_4 + Choice_9_6_3 <= 1
DifferentPair_9_4_4_6_5: Choice_9_4_4 + Choice_9_6_5 <= 1
DifferentPair_9_4_5_2_4: Choice_9_2_4 + Choice_9_4_5 <= 1
DifferentPair_9_4_5_2_6: Choice_9_2_6 + Choice_9_4_5 <= 1
DifferentPair_9_4_5_3_3: Choice_9_3_3 + Choice_9_4_5 <= 1
DifferentPair_9_4_5_3_7: Choice_9_3_7 + Choice_9_4_5 <= 1
DifferentPair_9_4_5_5_3: Choice_9_4_5 + Choice_9_5_3 <= 1
DifferentPair_9_4_5_5_7: Choice_9_4_5 + Choice_9_5_7 <= 1
DifferentPair_9_4_5_6_4: Choice_9_4_5 + Choice_9_6_4 <= 1
DifferentPair_9_4_5_6_6: Choice_9_4_5 + Choice_9_6_6 <= 1
DifferentPair_9_4_6_2_5: Choice_9_2_5 + Choice_9_4_6 <= 1
DifferentPair_9_4_6_2_7: Choice_9_2_7 + Choice_9_4_6 <= 1
DifferentPair_9_4_6_3_4: Choice_9_3_4 + Choice_9_4_6 <= 1
DifferentPair_9_4_6_3_8: Choice_9_3_8 + Choice_9_4_6 <= 1
DifferentPair_9_4_6_5_4: Choice_9_4_6 + Choice_9_5_4 <= 1
DifferentPair_9_4_6_5_8: Choice_9_4_6 + Choice_9_5_8 <= 1
DifferentPair_9_4_6_6_5: Choice_9_4_6 + Choice_9_6_5 <= 1
DifferentPair_9_4_6_6_7: Choice_9_4_6 + Choice_9_6_7 <= 1
DifferentPair_9_4_7_2_6: Choice_9_2_6 + Choice_9_4_7 <= 1
DifferentPair_9_4_7_2_8: Choice_9_2_8 + Choice_9_4_7 <= 1
DifferentPair_9_4_7_3_5: Choice_9_3_5 + Choice_9_4_7 <= 1
DifferentPair_9_4_7_3_9: Choice_9_3_9 + Choice_9_4_7 <= 1
DifferentPair_9_4_7_5_5: Choice_9_4_7 + Choice_9_5_5 <= 1
DifferentPair_9_4_7_5_9: Choice_9_4_7 + Choice_9_5_9 <= 1
DifferentPair_9_4_7_6_6: Choice_9_4_7 + Choice_9_6_6 <= 1
DifferentPair_9_4_7_6_8: Choice_9_4_7 + Choice_9_6_8 <= 1
DifferentPair_9_4_8_2_7: Choice_9_2_7 + Choice_9_4_8 <= 1
DifferentPair_9_4_8_2_9: Choice_9_2_9 + Choice_9_4_8 <= 1
DifferentPair_9_4_8_3_6: Choice_9_3_6 + Choice_9_4_8 <= 1
DifferentPair_9_4_8_5_6: Choice_9_4_8 + Choice_9_5_6 <= 1
DifferentPair_9_4_8_6_7: Choice_9_4_8 + Choice_9_6_7 <= 1
DifferentPair_9_4_8_6_9: Choice_9_4_8 + Choice_9_6_9 <= 1
DifferentPair_9_4_9_2_8: Choice_9_2_8 + Choice_9_4_9 <= 1
DifferentPair_9_4_9_3_7: Choice_9_3_7 + Choice_9_4_9 <= 1
DifferentPair_9_4_9_5_7: Choice_9_4_9 + Choice_9_5_7 <= 1
DifferentPair_9_4_9_6_8: Choice_9_4_9 + Choice_9_6_8 <= 1
DifferentPair_9_5_1_3_2: Choice_9_3_2 + Choice_9_5_1 <= 1
DifferentPair_9_5_1_4_3: Choice_9_4_3 + Choice_9_5_1 <= 1
DifferentPair_9_5_1_6_3: Choice_9_5_1 + Choice_9_6_3 <= 1
DifferentPair_9_5_1_7_2: Choice_9_5_1 + Choice_9_7_2 <= 1
DifferentPair_9_5_2_3_1: Choice_9_3_1 + Choice_9_5_2 <= 1
DifferentPair_9_5_2_3_3: Choice_9_3_3 + Choice_9_5_2 <= 1
DifferentPair_9_5_2_4_4: Choice_9_4_4 + Choice_9_5_2 <= 1
DifferentPair_9_5_2_6_4: Choice_9_5_2 + Choice_9_6_4 <= 1
DifferentPair_9_5_2_7_1: Choice_9_5_2 + Choice_9_7_1 <= 1
DifferentPair_9_5_2_7_3: Choice_9_5_2 + Choice_9_7_3 <= 1
DifferentPair_9_5_3_3_2: Choice_9_3_2 + Choice_9_5_3 <= 1
DifferentPair_9_5_3_3_4: Choice_9_3_4 + Choice_9_5_3 <= 1
DifferentPair_9_5_3_4_1: Choice_9_4_1 + Choice_9_5_3 <= 1
DifferentPair_9_5_3_4_5: Choice_9_4_5 + Choice_9_5_3 <= 1
DifferentPair_9_5_3_6_1: Choice_9_5_3 + Choice_9_6_1 <= 1
DifferentPair_9_5_3_6_5: Choice_9_5_3 + Choice_9_6_5 <= 1
DifferentPair_9_5_3_7_2: Choice_9_5_3 + Choice_9_7_2 <= 1
DifferentPair_9_5_3_7_4: Choice_9_5_3 + Choice_9_7_4 <= 1
DifferentPair_9_5_4_3_3: Choice_9_3_3 + Choice_9_5_4 <= 1
DifferentPair_9_5_4_3_5: Choice_9_3_5 + Choice_9_5_4 <= 1
DifferentPair_9_5_4_4_2: Choice_9_4_2 + Choice_9_5_4 <= 1
DifferentPair_9_5_4_4_6: Choice_9_4_6 + Choice_9_5_4 <= 1
DifferentPair_9_5_4_6_2: Choice_9_5_4 + Choice_9_6_2 <= 1
DifferentPair_9_5_4_6_6: Choice_9_5_4 + Choice_9_6_6 <= 1
DifferentPair_9_5_4_7_3: Choice_9_5_4 + Choice_9_7_3 <= 1
DifferentPair_9_5_4_7_5: Choice_9_5_4 + Choice_9_7_5 <= 1
DifferentPair_9_5_5_3_4: Choice_9_3_4 + Choice_9_5_5 <= 1
DifferentPair_9_5_5_3_6: Choice_9_3_6 + Choice_9_5_5 <= 1
DifferentPair_9_5_5_4_3: Choice_9_4_3 + Choice_9_5_5 <= 1
DifferentPair_9_5_5_4_7: Choice_9_4_7 + Choice_9_5_5 <= 1
DifferentPair_9_5_5_6_3: Choice_9_5_5 + Choice_9_6_3 <= 1
DifferentPair_9_5_5_6_7: Choice_9_5_5 + Choice_9_6_7 <= 1
DifferentPair_9_5_5_7_4: Choice_9_5_5 + Choice_9_7_4 <= 1
DifferentPair_9_5_5_7_6: Choice_9_5_5 + Choice_9_7_6 <= 1
DifferentPair_9_5_6_3_5: Choice_9_3_5 + Choice_9_5_6 <= 1
DifferentPair_9_5_6_3_7: Choice_9_3_7 + Choice_9_5_6 <= 1
DifferentPair_9_5_6_4_4: Choice_9_4_4 + Choice_9_5_6 <= 1
DifferentPair_9_5_6_4_8: Choice_9_4_8 + Choice_9_5_6 <= 1
DifferentPair_9_5_6_6_4: Choice_9_5_6 + Choice_9_6_4 <= 1
DifferentPair_9_5_6_6_8: Choice_9_5_6 + Choice_9_6_8 <= 1
DifferentPair_9_5_6_7_5: Choice_9_5_6 + Choice_9_7_5 <= 1
DifferentPair_9_5_6_7_7: Choice_9_5_6 + Choice_9_7_7 <= 1
DifferentPair_9_5_7_3_6: Choice_9_3_6 + Choice_9_5_7 <= 1
DifferentPair_9_5_7_3_8: Choice_9_3_8 + Choice_9_5_7 <= 1
DifferentPair_9_5_7_4_5: Choice_9_4_5 + Choice_9_5_7 <= 1
DifferentPair_9_5_7_4_9: Choice_9_4_9 + Choice_9_5_7 <= 1
DifferentPair_9_5_7_6_5: Choice_9_5_7 + Choice_9_6_5 <= 1
DifferentPair_9_5_7_6_9: Choice_9_5_7 + Choice_9_6_9 <= 1
DifferentPair_9_5_7_7_6: Choice_9_5_7 + Choice_9_7_6 <= 1
DifferentPair_9_5_7_7_8: Choice_9_5_7 + Choice_9_7_8 <= 1
DifferentPair_9_5_8_3_7: Choice_9_3_7 + Choice_9_5_8 <= 1
DifferentPair_9_5_8_3_9: Choice_9_3_9 + Choice_9_5_8 <= 1
DifferentPair_9_5_8_4_6: Choice_9_4_6 + Choice_9_5_8 <= 1
DifferentPair_9_5_8_6_6: Choice_9_5_8 + Choice_9_6_6 <= 1
DifferentPair_9_5_8_7_7: Choice_9_5_8 + Choice_9_7_7 <= 1
DifferentPair_9_5_8_7_9: Choice_9_5_8 + Choice_9_7_9 <= 1
DifferentPair_9_5_9_3_8: Choice_9_3_8 + Choice_9_5_9 <= 1
DifferentPair_9_5_9_4_7: Choice_9_4_7 + Choice_9_5_9 <= 1
DifferentPair_9_5_9_6_7: Choice_9_5_9 + Choice_9_6_7 <= 1
DifferentPair_9_5_9_7_8: Choice_9_5_9 + Choice_9_7_8 <= 1
DifferentPair_9_6_1_4_2: Choice_9_4_2 + Choice_9_6_1 <= 1
DifferentPair_9_6_1_5_3: Choice_9_5_3 + Choice_9_6_1 <= 1
DifferentPair_9_6_1_7_3: Choice_9_6_1 + Choice_9_7_3 <= 1
DifferentPair_9_6_1_8_2: Choice_9_6_1 + Choice_9_8_2 <= 1
DifferentPair_9_6_2_4_1: Choice_9_4_1 + Choice_9_6_2 <= 1
DifferentPair_9_6_2_4_3: Choice_9_4_3 + Choice_9_6_2 <= 1
DifferentPair_9_6_2_5_4: Choice_9_5_4 + Choice_9_6_2 <= 1
DifferentPair_9_6_2_7_4: Choice_9_6_2 + Choice_9_7_4 <= 1
DifferentPair_9_6_2_8_1: Choice_9_6_2 + Choice_9_8_1 <= 1
DifferentPair_9_6_2_8_3: Choice_9_6_2 + Choice_9_8_3 <= 1
DifferentPair_9_6_3_4_2: Choice_9_4_2 + Choice_9_6_3 <= 1
DifferentPair_9_6_3_4_4: Choice_9_4_4 + Choice_9_6_3 <= 1
DifferentPair_9_6_3_5_1: Choice_9_5_1 + Choice_9_6_3 <= 1
DifferentPair_9_6_3_5_5: Choice_9_5_5 + Choice_9_6_3 <= 1
DifferentPair_9_6_3_7_1: Choice_9_6_3 + Choice_9_7_1 <= 1
DifferentPair_9_6_3_7_5: Choice_9_6_3 + Choice_9_7_5 <= 1
DifferentPair_9_6_3_8_2: Choice_9_6_3 + Choice_9_8_2 <= 1
DifferentPair_9_6_3_8_4: Choice_9_6_3 + Choice_9_8_4 <= 1
DifferentPair_9_6_4_4_3: Choice_9_4_3 + Choice_9_6_4 <= 1
DifferentPair_9_6_4_4_5: Choice_9_4_5 + Choice_9_6_4 <= 1
DifferentPair_9_6_4_5_2: Choice_9_5_2 + Choice_9_6_4 <= 1
DifferentPair_9_6_4_5_6: Choice_9_5_6 + Choice_9_6_4 <= 1
DifferentPair_9_6_4_7_2: Choice_9_6_4 + Choice_9_7_2 <= 1
DifferentPair_9_6_4_7_6: Choice_9_6_4 + Choice_9_7_6 <= 1
DifferentPair_9_6_4_8_3: Choice_9_6_4 + Choice_9_8_3 <= 1
DifferentPair_9_6_4_8_5: Choice_9_6_4 + Choice_9_8_5 <= 1
DifferentPair_9_6_5_4_4: Choice_9_4_4 + Choice_9_6_5 <= 1
DifferentPair_9_6_5_4_6: Choice_9_4_6 + Choice_9_6_5 <= 1
DifferentPair_9_6_5_5_3: Choice_9_5_3 + Choice_9_6_5 <= 1
DifferentPair_9_6_5_5_7: Choice_9_5_7 + Choice_9_6_5 <= 1
DifferentPair_9_6_5_7_3: Choice_9_6_5 + Choice_9_7_3 <= 1
DifferentPair_9_6_5_7_7: Choice_9_6_5 + Choice_9_7_7 <= 1
DifferentPair_9_6_5_8_4: Choice_9_6_5 + Choice_9_8_4 <= 1
DifferentPair_9_6_5_8_6: Choice_9_6_5 + Choice_9_8_6 <= 1
DifferentPair_9_6_6_4_5: Choice_9_4_5 + Choice_9_6_6 <= 1
DifferentPair_9_6_6_4_7: Choice_9_4_7 + Choice_9_6_6 <= 1
DifferentPair_9_6_6_5_4: Choice_9_5_4 + Choice_9_6_6 <= 1
DifferentPair_9_6_6_5_8: Choice_9_5_8 + Choice_9_6_6 <= 1
DifferentPair_9_6_6_7_4: Choice_9_6_6 + Choice_9_7_4 <= 1
DifferentPair_9_6_6_7_8: Choice_9_6_6 + Choice_9_7_8 <= 1
DifferentPair_9_6_6_8_5: Choice_9_6_6 + Choice_9_8_5 <= 1
DifferentPair_9_6_6_8_7: Choice_9_6_6 + Choice_9_8_7 <= 1
DifferentPair_9_6_7_4_6: Choice_9_4_6 + Choice_9_6_7 <= 1
DifferentPair_9_6_7_4_8: Choice_9_4_8 + Choice_9_6_7 <= 1
DifferentPair_9_6_7_5_5: Choice_9_5_5 + Choice_9_6_7 <= 1
DifferentPair_9_6_7_5_9: Choice_9_5_9 + Choice_9_6_7 <= 1
DifferentPair_9_6_7_7_5: Choice_9_6_7 + Choice_9_7_5 <= 1
DifferentPair_9_6_7_7_9: Choice_9_6_7 + Choice_9_7_9 <= 1
DifferentPair_9_6_7_8_6: Choice_9_6_7 + Choice_9_8_6 <= 1
DifferentPair_9_6_7_8_8: Choice_9_6_7 + Choice_9_8_8 <= 1
DifferentPair_9_6_8_4_7: Choice_9_4_7 + Choice_9_6_8 <= 1
DifferentPair_9_6_8_4_9: Choice_9_4_9 + Choice_9_6_8 <= 1
DifferentPair_9_6_8_5_6: Choice_9_5_6 + Choice_9_6_8 <= 1
DifferentPair_9_6_8_7_6: Choice_9_6_8 + Choice_9_7_6 <= 1
DifferentPair_9_6_8_8_7: Choice_9_6_8 + Choice_9_8_7 <= 1
DifferentPair_9_6_8_8_9: Choice_9_6_8 + Choice_9_8_9 <= 1
DifferentPair_9_6_9_4_8: Choice_9_4_8 + Choice_9_6_9 <= 1
DifferentPair_9_6_9_5_7: Choice_9_5_7 + Choice_9_6_9 <= 1
DifferentPair_9_6_9_7_7: Choice_9_6_9 + Choice_9_7_7 <= 1
DifferentPair_9_6_9_8_8: Choice_9_6_9 + Choice_9_8_8 <= 1
DifferentPair_9_7_1_5_2: Choice_9_5_2 + Choice_9_7_1 <= 1
DifferentPair_9_7_1_6_3: Choice_9_6_3 + Choice_9_7_1 <= 1
DifferentPair_9_7_1_8_3: Choice_9_7_1 + Choice_9_8_3 <= 1
DifferentPair_9_7_1_9_2: Choice_9_7_1 + Choice_9_9_2 <= 1
DifferentPair_9_7_2_5_1: Choice_9_5_1 + Choice_9_7_2 <= 1
DifferentPair_9_7_2_5_3: Choice_9_5_3 + Choice_9_7_2 <= 1
DifferentPair_9_7_2_6_4: Choice_9_6_4 + Choice_9_7_2 <= 1
DifferentPair_9_7_2_8_4: Choice_9_7_2 + Choice_9_8_4 <= 1
DifferentPair_9_7_2_9_1: Choice_9_7_2 + Choice_9_9_1 <= 1
DifferentPair_9_7_2_9_3: Choice_9_7_2 + Choice_9_9_3 <= 1
DifferentPair_9_7_3_5_2: Choice_9_5_2 + Choice_9_7_3 <= 1
DifferentPair_9_7_3_5_4: Choice_9_5_4 + Choice_9_7_3 <= 1
DifferentPair_9_7_3_6_1: Choice_9_6_1 + Choice_9_7_3 <= 1
DifferentPair_9_7_3_6_5: Choice_9_6_5 + Choice_9_7_3 <= 1
DifferentPair_9_7_3_8_1: Choice_9_7_3 + Choice_9_8_1 <= 1
DifferentPair_9_7_3_8_5: Choice_9_7_3 + Choice_9_8_5 <= 1
DifferentPair_9_7_3_9_2: Choice_9_7_3 + Choice_9_9_2 <= 1
DifferentPair_9_7_3_9_4: Choice_9_7_3 + Choice_9_9_4 <= 1
DifferentPair_9_7_4_5_3: Choice_9_5_3 + Choice_9_7_4 <= 1
DifferentPair_9_7_4_5_5: Choice_9_5_5 + Choice_9_7_4 <= 1
DifferentPair_9_7_4_6_2: Choice_9_6_2 + Choice_9_7_4 <= 1
DifferentPair_9_7_4_6_6: Choice_9_6_6 + Choice_9_7_4 <= 1
DifferentPair_9_7_4_8_2: Choice_9_7_4 + Choice_9_8_2 <= 1
DifferentPair_9_7_4_8_6: Choice_9_7_4 + Choice_9_8_6 <= 1
DifferentPair_9_7_4_9_3: Choice_9_7_4 + Choice_9_9_3 <= 1
DifferentPair_9_7_4_9_5: Choice_9_7_4 + Choice_9_9_5 <= 1
DifferentPair_9_7_5_5_4: Choice_9_5_4 + Choice_9_7_5 <= 1
DifferentPair_9_7_5_5_6: Choice_9_5_6 + Choice_9_7_5 <= 1
DifferentPair_9_7_5_6_3: Choice_9_6_3 + Choice_9_7_5 <= 1
DifferentPair_9_7_5_6_7: Choice_9_6_7 + Choice_9_7_5 <= 1
DifferentPair_9_7_5_8_3: Choice_9_7_5 + Choice_9_8_3 <= 1
DifferentPair_9_7_5_8_7: Choice_9_7_5 + Choice_9_8_7 <= 1
DifferentPair_9_7_5_9_4: Choice_9_7_5 + Choice_9_9_4 <= 1
DifferentPair_9_7_5_9_6: Choice_9_7_5 + Choice_9_9_6 <= 1
DifferentPair_9_7_6_5_5: Choice_9_5_5 + Choice_9_7_6 <= 1
DifferentPair_9_7_6_5_7: Choice_9_5_7 + Choice_9_7_6 <= 1
DifferentPair_9_7_6_6_4: Choice_9_6_4 + Choice_9_7_6 <= 1
DifferentPair_9_7_6_6_8: Choice_9_6_8 + Choice_9_7_6 <= 1
DifferentPair_9_7_6_8_4: Choice_9_7_6 + Choice_9_8_4 <= 1
DifferentPair_9_7_6_8_8: Choice_9_7_6 + Choice_9_8_8 <= 1
DifferentPair_9_7_6_9_5: Choice_9_7_6 + Choice_9_9_5 <= 1
DifferentPair_9_7_6_9_7: Choice_9_7_6 + Choice_9_9_7 <= 1
DifferentPair_9_7_7_5_6: Choice_9_5_6 + Choice_9_7_7 <= 1
DifferentPair_9_7_7_5_8: Choice_9_5_8 + Choice_9_7_7 <= 1
DifferentPair_9_7_7_6_5: Choice_9_6_5 + Choice_9_7_7 <= 1
DifferentPair_9_7_7_6_9: Choice_9_6_9 + Choice_9_7_7 <= 1
DifferentPair_9_7_7_8_5: Choice_9_7_7 + Choice_9_8_5 <= 1
DifferentPair_9_7_7_8_9: Choice_9_7_7 + Choice_9_8_9 <= 1
DifferentPair_9_7_7_9_6: Choice_9_7_7 + Choice_9_9_6 <= 1
DifferentPair_9_7_7_9_8: Choice_9_7_7 + Choice_9_9_8 <= 1
DifferentPair_9_7_8_5_7: Choice_9_5_7 + Choice_9_7_8 <= 1
DifferentPair_9_7_8_5_9: Choice_9_5_9 + Choice_9_7_8 <= 1
DifferentPair_9_7_8_6_6: Choice_9_6_6 + Choice_9_7_8 <= 1
DifferentPair_9_7_8_8_6: Choice_9_7_8 + Choice_9_8_6 <= 1
DifferentPair_9_7_8_9_7: Choice_9_7_8 + Choice_9_9_7 <= 1
DifferentPair_9_7_8_9_9: Choice_9_7_8 + Choice_9_9_9 <= 1
DifferentPair_9_7_9_5_8: Choice_9_5_8 + Choice_9_7_9 <= 1
DifferentPair_9_7_9_6_7: Choice_9_6_7 + Choice_9_7_9 <= 1
DifferentPair_9_7_9_8_7: Choice_9_7_9 + Choice_9_8_7 <= 1
DifferentPair_9_7_9_9_8: Choice_9_7_9 + Choice_9_9_8 <= 1
DifferentPair_9_8_1_6_2: Choice_9_6_2 + Choice_9_8_1 <= 1
DifferentPair_9_8_1_7_3: Choice_9_7_3 + Choice_9_8_1 <= 1
DifferentPair_9_8_1_9_3: Choice_9_8_1 + Choice_9_9_3 <= 1
DifferentPair_9_8_2_6_1: Choice_9_6_1 + Choice_9_8_2 <= 1
DifferentPair_9_8_2_6_3: Choice_9_6_3 + Choice_9_8_2 <= 1
DifferentPair_9_8_2_7_4: Choice_9_7_4 + Choice_9_8_2 <= 1
DifferentPair_9_8_2_9_4: Choice_9_8_2 + Choice_9_9_4 <= 1
DifferentPair_9_8_3_6_2: Choice_9_6_2 + Choice_9_8_3 <= 1
DifferentPair_9_8_3_6_4: Choice_9_6_4 + Choice_9_8_3 <= 1
DifferentPair_9_8_3_7_1: Choice_9_7_1 + Choice_9_8_3 <= 1
DifferentPair_9_8_3_7_5: Choice_9_7_5 + Choice_9_8_3 <= 1
DifferentPair_9_8_3_9_1: Choice_9_8_3 + Choice_9_9_1 <= 1
DifferentPair_9_8_3_9_5: Choice_9_8_3 + Choice_9_9_5 <= 1
DifferentPair_9_8_4_6_3: Choice_9_6_3 + Choice_9_8_4 <= 1
DifferentPair_9_8_4_6_5: Choice_9_6_5 + Choice_9_8_4 <= 1
DifferentPair_9_8_4_7_2: Choice_9_7_2 + Choice_9_8_4 <= 1
DifferentPair_9_8_4_7_6: Choice_9_7_6 + Choice_9_8_4 <= 1
DifferentPair_9_8_4_9_2: Choice_9_8_4 + Choice_9_9_2 <= 1
DifferentPair_9_8_4_9_6: Choice_9_8_4 + Choice_9_9_6 <= 1
DifferentPair_9_8_5_6_4: Choice_9_6_4 + Choice_9_8_5 <= 1
DifferentPair_9_8_5_6_6: Choice_9_6_6 + Choice_9_8_5 <= 1
DifferentPair_9_8_5_7_3: Choice_9_7_3 + Choice_9_8_5 <= 1
DifferentPair_9_8_5_7_7: Choice_9_7_7 + Choice_9_8_5 <= 1
DifferentPair_9_8_5_9_3: Choice_9_8_5 + Choice_9_9_3 <= 1
DifferentPair_9_8_5_9_7: Choice_9_8_5 + Choice_9_9_7 <= 1
DifferentPair_9_8_6_6_5: Choice_9_6_5 + Choice_9_8_6 <= 1
DifferentPair_9_8_6_6_7: Choice_9_6_7 + Choice_9_8_6 <= 1
DifferentPair_9_8_6_7_4: Choice_9_7_4 + Choice_9_8_6 <= 1
DifferentPair_9_8_6_7_8: Choice_9_7_8 + Choice_9_8_6 <= 1
DifferentPair_9_8_6_9_4: Choice_9_8_6 + Choice_9_9_4 <= 1
DifferentPair_9_8_6_9_8: Choice_9_8_6 + Choice_9_9_8 <= 1
DifferentPair_9_8_7_6_6: Choice_9_6_6 + Choice_9_8_7 <= 1
DifferentPair_9_8_7_6_8: Choice_9_6_8 + Choice_9_8_7 <= 1
DifferentPair_9_8_7_7_5: Choice_9_7_5 + Choice_9_8_7 <= 1
DifferentPair_9_8_7_7_9: Choice_9_7_9 + Choice_9_8_7 <= 1
DifferentPair_9_8_7_9_5: Choice_9_8_7 + Choice_9_9_5 <= 1
DifferentPair_9_8_7_9_9: Choice_9_8_7 + Choice_9_9_9 <= 1
DifferentPair_9_8_8_6_7: Choice_9_6_7 + Choice_9_8_8 <= 1
DifferentPair_9_8_8_6_9: Choice_9_6_9 + Choice_9_8_8 <= 1
DifferentPair_9_8_8_7_6: Choice_9_7_6 + Choice_9_8_8 <= 1
DifferentPair_9_8_8_9_6: Choice_9_8_8 + Choice_9_9_6 <= 1
DifferentPair_9_8_9_6_8: Choice_9_6_8 + Choice_9_8_9 <= 1
DifferentPair_9_8_9_7_7: Choice_9_7_7 + Choice_9_8_9 <= 1
DifferentPair_9_8_9_9_7: Choice_9_8_9 + Choice_9_9_7 <= 1
DifferentPair_9_9_1_7_2: Choice_9_7_2 + Choice_9_9_1 <= 1
DifferentPair_9_9_1_8_3: Choice_9_8_3 + Choice_9_9_1 <= 1
DifferentPair_9_9_2_7_1: Choice_9_7_1 + Choice_9_9_2 <= 1
DifferentPair_9_9_2_7_3: Choice_9_7_3 + Choice_9_9_2 <= 1
DifferentPair_9_9_2_8_4: Choice_9_8_4 + Choice_9_9_2 <= 1
DifferentPair_9_9_3_7_2: Choice_9_7_2 + Choice_9_9_3 <= 1
DifferentPair_9_9_3_7_4: Choice_9_7_4 + Choice_9_9_3 <= 1
DifferentPair_9_9_3_8_1: Choice_9_8_1 + Choice_9_9_3 <= 1
DifferentPair_9_9_3_8_5: Choice_9_8_5 + Choice_9_9_3 <= 1
DifferentPair_9_9_4_7_3: Choice_9_7_3 + Choice_9_9_4 <= 1
DifferentPair_9_9_4_7_5: Choice_9_7_5 + Choice_9_9_4 <= 1
DifferentPair_9_9_4_8_2: Choice_9_8_2 + Choice_9_9_4 <= 1
DifferentPair_9_9_4_8_6: Choice_9_8_6 + Choice_9_9_4 <= 1
DifferentPair_9_9_5_7_4: Choice_9_7_4 + Choice_9_9_5 <= 1
DifferentPair_9_9_5_7_6: Choice_9_7_6 + Choice_9_9_5 <= 1
DifferentPair_9_9_5_8_3: Choice_9_8_3 + Choice_9_9_5 <= 1
DifferentPair_9_9_5_8_7: Choice_9_8_7 + Choice_9_9_5 <= 1
DifferentPair_9_9_6_7_5: Choice_9_7_5 + Choice_9_9_6 <= 1
DifferentPair_9_9_6_7_7: Choice_9_7_7 + Choice_9_9_6 <= 1
DifferentPair_9_9_6_8_4: Choice_9_8_4 + Choice_9_9_6 <= 1
DifferentPair_9_9_6_8_8: Choice_9_8_8 + Choice_9_9_6 <= 1
DifferentPair_9_9_7_7_6: Choice_9_7_6 + Choice_9_9_7 <= 1
DifferentPair_9_9_7_7_8: Choice_9_7_8 + Choice_9_9_7 <= 1
DifferentPair_9_9_7_8_5: Choice_9_8_5 + Choice_9_9_7 <= 1
DifferentPair_9_9_7_8_9: Choice_9_8_9 + Choice_9_9_7 <= 1
DifferentPair_9_9_8_7_7: Choice_9_7_7 + Choice_9_9_8 <= 1
DifferentPair_9_9_8_7_9: Choice_9_7_9 + Choice_9_9_8 <= 1
DifferentPair_9_9_8_8_6: Choice_9_8_6 + Choice_9_9_8 <= 1
DifferentPair_9_9_9_7_8: Choice_9_7_8 + Choice_9_9_9 <= 1
DifferentPair_9_9_9_8_7: Choice_9_8_7 + Choice_9_9_9 <= 1
Imposible_1_1_1: Choice_1_1_1 = 0
Imposible_1_1_2: Choice_1_1_2 = 0
Imposible_1_1_3: Choice_1_1_3 = 0
Imposible_1_1_4: Choice_1_1_4 = 0
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
Imposible_1_2_7: Choice_1_2_7 = 0
Imposible_1_2_8: Choice_1_2_8 = 0
Imposible_1_2_9: Choice_1_2_9 = 0
Imposible_1_3_1: Choice_1_3_1 = 0
Imposible_1_3_2: Choice_1_3_2 = 0
Imposible_1_3_3: Choice_1_3_3 = 0
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
Imposible_1_4_9: Choice_1_4_9 = 0
Imposible_1_5_1: Choice_1_5_1 = 0
Imposible_1_5_2: Choice_1_5_2 = 0
Imposible_1_5_3: Choice_1_5_3 = 0
Imposible_1_5_4: Choice_1_5_4 = 0
Imposible_1_5_5: Choice_1_5_5 = 0
Imposible_1_5_6: Choice_1_5_6 = 0
Imposible_1_5_7: Choice_1_5_7 = 0
Imposible_1_5_8: Choice_1_5_8 = 0
Imposible_1_5_9: Choice_1_5_9 = 0
Imposible_1_6_1: Choice_1_6_1 = 0
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
Imposible_1_7_8: Choice_1_7_8 = 0
Imposible_1_7_9: Choice_1_7_9 = 0
Imposible_1_8_1: Choice_1_8_1 = 0
Imposible_1_8_2: Choice_1_8_2 = 0
Imposible_1_8_3: Choice_1_8_3 = 0
Imposible_1_8_4: Choice_1_8_4 = 0
Imposible_1_8_5: Choice_1_8_5 = 0
Imposible_1_8_6: Choice_1_8_6 = 0
Imposible_1_8_7: Choice_1_8_7 = 0
Imposible_1_8_8: Choice_1_8_8 = 0
Imposible_1_8_9: Choice_1_8_9 = 0
Imposible_1_9_1: Choice_1_9_1 = 0
Imposible_1_9_2: Choice_1_9_2 = 0
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
Imposible_2_1_8: Choice_2_1_8 = 0
Imposible_2_1_9: Choice_2_1_9 = 0
Imposible_2_2_1: Choice_2_2_1 = 0
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
Imposible_2_3_4: Choice_2_3_4 = 0
Imposible_2_3_5: Choice_2_3_5 = 0
Imposible_2_3_6: Choice_2_3_6 = 0
Imposible_2_3_7: Choice_2_3_7 = 0
Imposible_2_3_8: Choice_2_3_8 = 0
Imposible_2_3_9: Choice_2_3_9 = 0
Imposible_2_4_1: Choice_2_4_1 = 0
Imposible_2_4_2: Choice_2_4_2 = 0
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
Imposible_2_5_5: Choice_2_5_5 = 0
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
Imposible_2_6_7: Choice_2_6_7 = 0
Imposible_2_6_8: Choice_2_6_8 = 0
Imposible_2_6_9: Choice_2_6_9 = 0
Imposible_2_7_1: Choice_2_7_1 = 0
Imposible_2_7_2: Choice_2_7_2 = 0
Imposible_2_7_3: Choice_2_7_3 = 0
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
Imposible_2_8_9: Choice_2_8_9 = 0
Imposible_2_9_1: Choice_2_9_1 = 0
Imposible_2_9_2: Choice_2_9_2 = 0
Imposible_2_9_3: Choice_2_9_3 = 0
Imposible_2_9_4: Choice_2_9_4 = 0
Imposible_2_9_5: Choice_2_9_5 = 0
Imposible_2_9_6: Choice_2_9_6 = 0
Imposible_2_9_7: Choice_2_9_7 = 0
Imposible_2_9_8: Choice_2_9_8 = 0
Imposible_2_9_9: Choice_2_9_9 = 0
Imposible_3_1_1: Choice_3_1_1 = 0
Imposible_3_1_2: Choice_3_1_2 = 0
Imposible_3_1_3: Choice_3_1_3 = 0
Imposible_3_1_4: Choice_3_1_4 = 0
Imposible_3_1_5: Choice_3_1_5 = 0
Imposible_3_1_6: Choice_3_1_6 = 0
Imposible_3_1_7: Choice_3_1_7 = 0
Imposible_3_1_8: Choice_3_1_8 = 0
Imposible_3_1_9: Choice_3_1_9 = 0
Imposible_3_2_1: Choice_3_2_1 = 0
Imposible_3_2_2: Choice_3_2_2 = 0
Imposible_3_2_3: Choice_3_2_3 = 0
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
Imposible_3_3_7: Choice_3_3_7 = 0
Imposible_3_3_8: Choice_3_3_8 = 0
Imposible_3_3_9: Choice_3_3_9 = 0
Imposible_3_4_1: Choice_3_4_1 = 0
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
Imposible_3_5_8: Choice_3_5_8 = 0
Imposible_3_5_9: Choice_3_5_9 = 0
Imposible_3_6_1: Choice_3_6_1 = 0
Imposible_3_6_2: Choice_3_6_2 = 0
Imposible_3_6_3: Choice_3_6_3 = 0
Imposible_3_6_4: Choice_3_6_4 = 0
Imposible_3_6_5: Choice_3_6_5 = 0
Imposible_3_6_6: Choice_3_6_6 = 0
Imposible_3_6_7: Choice_3_6_7 = 0
Imposible_3_6_8: Choice_3_6_8 = 0
Imposible_3_6_9: Choice_3_6_9 = 0
Imposible_3_7_1: Choice_3_7_1 = 0
Imposible_3_7_2: Choice_3_7_2 = 0
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
Imposible_3_8_4: Choice_3_8_4 = 0
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
Imposible_3_9_9: Choice_3_9_9 = 0
Imposible_4_1_1: Choice_4_1_1 = 0
Imposible_4_1_2: Choice_4_1_2 = 0
Imposible_4_1_3: Choice_4_1_3 = 0
Imposible_4_1_4: Choice_4_1_4 = 0
Imposible_4_1_5: Choice_4_1_5 = 0
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
Imposible_4_2_8: Choice_4_2_8 = 0
Imposible_4_2_9: Choice_4_2_9 = 0
Imposible_4_3_1: Choice_4_3_1 = 0
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
Imposible_4_4_7: Choice_4_4_7 = 0
Imposible_4_4_8: Choice_4_4_8 = 0
Imposible_4_4_9: Choice_4_4_9 = 0
Imposible_4_5_1: Choice_4_5_1 = 0
Imposible_4_5_2: Choice_4_5_2 = 0
Imposible_4_5_3: Choice_4_5_3 = 0
Imposible_4_5_4: Choice_4_5_4 = 0
Imposible_4_5_5: Choice_4_5_5 = 0
Imposible_4_5_6: Choice_4_5_6 = 0
Imposible_4_5_7: Choice_4_5_7 = 0
Imposible_4_5_8: Choice_4_5_8 = 0
Imposible_4_5_9: Choice_4_5_9 = 0
Imposible_4_6_1: Choice_4_6_1 = 0
Imposible_4_6_2: Choice_4_6_2 = 0
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
Imposible_4_7_9: Choice_4_7_9 = 0
Imposible_4_8_1: Choice_4_8_1 = 0
Imposible_4_8_2: Choice_4_8_2 = 0
Imposible_4_8_3: Choice_4_8_3 = 0
Imposible_4_8_4: Choice_4_8_4 = 0
Imposible_4_8_5: Choice_4_8_5 = 0
Imposible_4_8_6: Choice_4_8_6 = 0
Imposible_4_8_7: Choice_4_8_7 = 0
Imposible_4_8_8: Choice_4_8_8 = 0
Imposible_4_8_9: Choice_4_8_9 = 0
Imposible_4_9_1: Choice_4_9_1 = 0
Imposible_4_9_2: Choice_4_9_2 = 0
Imposible_4_9_3: Choice_4_9_3 = 0
Imposible_4_9_4: Choice_4_9_4 = 0
Imposible_4_9_5: Choice_4_9_5 = 0
Imposible_4_9_6: Choice_4_9_6 = 0
Imposible_4_9_7: Choice_4_9_7 = 0
Imposible_4_9_8: Choice_4_9_8 = 0
Imposible_4_9_9: Choice_4_9_9 = 0
Imposible_5_1_1: Choice_5_1_1 = 0
Imposible_5_1_2: Choice_5_1_2 = 0
Imposible_5_1_3: Choice_5_1_3 = 0
Imposible_5_1_4: Choice_5_1_4 = 0
Imposible_5_1_5: Choice_5_1_5 = 0
Imposible_5_1_6: Choice_5_1_6 = 0
Imposible_5_1_7: Choice_5_1_7 = 0
Imposible_5_1_8: Choice_5_1_8 = 0
Imposible_5_1_9: Choice_5_1_9 = 0
Imposible_5_2_1: Choice_5_2_1 = 0
Imposible_5_2_2: Choice_5_2_2 = 0
Imposible_5_2_3: Choice_5_2_3 = 0
Imposible_5_2_4: Choice_5_2_4 = 0
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
Imposible_5_3_8: Choice_5_3_8 = 0
Imposible_5_3_9: Choice_5_3_9 = 0
Imposible_5_4_1: Choice_5_4_1 = 0
Imposible_5_4_2: Choice_5_4_2 = 0
Imposible_5_4_3: Choice_5_4_3 = 0
Imposible_5_4_4: Choice_5_4_4 = 0
Imposible_5_4_5: Choice_5_4_5 = 0
Imposible_5_4_6: Choice_5_4_6 = 0
Imposible_5_4_7: Choice_5_4_7 = 0
Imposible_5_4_8: Choice_5_4_8 = 0
Imposible_5_4_9: Choice_5_4_9 = 0
Imposible_5_5_1: Choice_5_5_1 = 0
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
Imposible_5_6_9: Choice_5_6_9 = 0
Imposible_5_7_1: Choice_5_7_1 = 0
Imposible_5_7_2: Choice_5_7_2 = 0
Imposible_5_7_3: Choice_5_7_3 = 0
Imposible_5_7_4: Choice_5_7_4 = 0
Imposible_5_7_5: Choice_5_7_5 = 0
Imposible_5_7_6: Choice_5_7_6 = 0
Imposible_5_7_7: Choice_5_7_7 = 0
Imposible_5_7_8: Choice_5_7_8 = 0
Imposible_5_7_9: Choice_5_7_9 = 0
Imposible_5_8_1: Choice_5_8_1 = 0
Imposible_5_8_2: Choice_5_8_2 = 0
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
Imposible_5_9_5: Choice_5_9_5 = 0
Imposible_5_9_6: Choice_5_9_6 = 0
Imposible_5_9_7: Choice_5_9_7 = 0
Imposible_5_9_8: Choice_5_9_8 = 0
Imposible_5_9_9: Choice_5_9_9 = 0
Imposible_6_1_1: Choice_6_1_1 = 0
Imposible_6_1_2: Choice_6_1_2 = 0
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
Imposible_6_2_5: Choice_6_2_5 = 0
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
Imposible_6_3_9: Choice_6_3_9 = 0
Imposible_6_4_1: Choice_6_4_1 = 0
Imposible_6_4_2: Choice_6_4_2 = 0
Imposible_6_4_3: Choice_6_4_3 = 0
Imposible_6_4_4: Choice_6_4_4 = 0
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
Imposible_6_5_7: Choice_6_5_7 = 0
Imposible_6_5_8: Choice_6_5_8 = 0
Imposible_6_5_9: Choice_6_5_9 = 0
Imposible_6_6_1: Choice_6_6_1 = 0
Imposible_6_6_2: Choice_6_6_2 = 0
Imposible_6_6_3: Choice_6_6_3 = 0
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
Imposible_6_7_6: Choice_6_7_6 = 0
Imposible_6_7_7: Choice_6_7_7 = 0
Imposible_6_7_8: Choice_6_7_8 = 0
Imposible_6_7_9: Choice_6_7_9 = 0
Imposible_6_8_1: Choice_6_8_1 = 0
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
Imposible_6_9_8: Choice_6_9_8 = 0
Imposible_6_9_9: Choice_6_9_9 = 0
Imposible_7_1_1: Choice_7_1_1 = 0
Imposible_7_1_2: Choice_7_1_2 = 0
Imposible_7_1_3: Choice_7_1_3 = 0
Imposible_7_1_4: Choice_7_1_4 = 0
Imposible_7_1_5: Choice_7_1_5 = 0
Imposible_7_1_6: Choice_7_1_6 = 0
Imposible_7_1_7: Choice_7_1_7 = 0
Imposible_7_1_8: Choice_7_1_8 = 0
Imposible_7_1_9: Choice_7_1_9 = 0
Imposible_7_2_1: Choice_7_2_1 = 0
Imposible_7_2_2: Choice_7_2_2 = 0
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
Imposible_7_3_5: Choice_7_3_5 = 0
Imposible_7_3_6: Choice_7_3_6 = 0
Imposible_7_3_7: Choice_7_3_7 = 0
Imposible_7_3_8: Choice_7_3_8 = 0
Imposible_7_3_9: Choice_7_3_9 = 0
Imposible_7_4_1: Choice_7_4_1 = 0
Imposible_7_4_2: Choice_7_4_2 = 0
Imposible_7_4_3: Choice_7_4_3 = 0
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
Imposible_7_5_9: Choice_7_5_9 = 0
Imposible_7_6_1: Choice_7_6_1 = 0
Imposible_7_6_2: Choice_7_6_2 = 0
Imposible_7_6_3: Choice_7_6_3 = 0
Imposible_7_6_4: Choice_7_6_4 = 0
Imposible_7_6_5: Choice_7_6_5 = 0
Imposible_7_6_6: Choice_7_6_6 = 0
Imposible_7_6_7: Choice_7_6_7 = 0
Imposible_7_6_8: Choice_7_6_8 = 0
Imposible_7_6_9: Choice_7_6_9 = 0
Imposible_7_7_1: Choice_7_7_1 = 0
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
Imposible_7_8_8: Choice_7_8_8 = 0
Imposible_7_8_9: Choice_7_8_9 = 0
Imposible_7_9_1: Choice_7_9_1 = 0
Imposible_7_9_2: Choice_7_9_2 = 0
Imposible_7_9_3: Choice_7_9_3 = 0
Imposible_7_9_4: Choice_7_9_4 = 0
Imposible_7_9_5: Choice_7_9_5 = 0
Imposible_7_9_6: Choice_7_9_6 = 0
Imposible_7_9_7: Choice_7_9_7 = 0
Imposible_7_9_8: Choice_7_9_8 = 0
Imposible_7_9_9: Choice_7_9_9 = 0
Imposible_8_1_1: Choice_8_1_1 = 0
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
Imposible_8_2_9: Choice_8_2_9 = 0
Imposible_8_3_1: Choice_8_3_1 = 0
Imposible_8_3_2: Choice_8_3_2 = 0
Imposible_8_3_3: Choice_8_3_3 = 0
Imposible_8_3_4: Choice_8_3_4 = 0
Imposible_8_3_5: Choice_8_3_5 = 0
Imposible_8_3_6: Choice_8_3_6 = 0
Imposible_8_3_7: Choice_8_3_7 = 0
Imposible_8_3_8: Choice_8_3_8 = 0
Imposible_8_3_9: Choice_8_3_9 = 0
Imposible_8_4_1: Choice_8_4_1 = 0
Imposible_8_4_2: Choice_8_4_2 = 0
Imposible_8_4_3: Choice_8_4_3 = 0
Imposible_8_4_4: Choice_8_4_4 = 0
Imposible_8_4_5: Choice_8_4_5 = 0
Imposible_8_4_6: Choice_8_4_6 = 0
Imposible_8_4_7: Choice_8_4_7 = 0
Imposible_8_4_8: Choice_8_4_8 = 0
Imposible_8_4_9: Choice_8_4_9 = 0
Imposible_8_5_1: Choice_8_5_1 = 0
Imposible_8_5_2: Choice_8_5_2 = 0
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
Imposible_8_6_8: Choice_8_6_8 = 0
Imposible_8_6_9: Choice_8_6_9 = 0
Imposible_8_7_1: Choice_8_7_1 = 0
Imposible_8_7_2: Choice_8_7_2 = 0
Imposible_8_7_3: Choice_8_7_3 = 0
Imposible_8_7_4: Choice_8_7_4 = 0
Imposible_8_7_5: Choice_8_7_5 = 0
Imposible_8_7_6: Choice_8_7_6 = 0
Imposible_8_7_7: Choice_8_7_7 = 0
Imposible_8_7_8: Choice_8_7_8 = 0
Imposible_8_7_9: Choice_8_7_9 = 0
Imposible_8_8_1: Choice_8_8_1 = 0
Imposible_8_8_2: Choice_8_8_2 = 0
Imposible_8_8_3: Choice_8_8_3 = 0
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
Imposible_8_9_7: Choice_8_9_7 = 0
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
Imposible_9_1_9: Choice_9_1_9 = 0
Imposible_9_2_1: Choice_9_2_1 = 0
Imposible_9_2_2: Choice_9_2_2 = 0
Imposible_9_2_3: Choice_9_2_3 = 0
Imposible_9_2_4: Choice_9_2_4 = 0
Imposible_9_2_5: Choice_9_2_5 = 0
Imposible_9_2_6: Choice_9_2_6 = 0
Imposible_9_2_7: Choice_9_2_7 = 0
Imposible_9_2_8: Choice_9_2_8 = 0
Imposible_9_2_9: Choice_9_2_9 = 0
Imposible_9_3_1: Choice_9_3_1 = 0
Imposible_9_3_2: Choice_9_3_2 = 0
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
Imposible_9_4_8: Choice_9_4_8 = 0
Imposible_9_4_9: Choice_9_4_9 = 0
Imposible_9_5_1: Choice_9_5_1 = 0
Imposible_9_5_2: Choice_9_5_2 = 0
Imposible_9_5_3: Choice_9_5_3 = 0
Imposible_9_5_4: Choice_9_5_4 = 0
Imposible_9_5_5: Choice_9_5_5 = 0
Imposible_9_5_6: Choice_9_5_6 = 0
Imposible_9_5_7: Choice_9_5_7 = 0
Imposible_9_5_8: Choice_9_5_8 = 0
Imposible_9_5_9: Choice_9_5_9 = 0
Imposible_9_6_1: Choice_9_6_1 = 0
Imposible_9_6_2: Choice_9_6_2 = 0
Imposible_9_6_3: Choice_9_6_3 = 0
Imposible_9_6_4: Choice_9_6_4 = 0
Imposible_9_6_5: Choice_9_6_5 = 0
Imposible_9_6_6: Choice_9_6_6 = 0
Imposible_9_6_7: Choice_9_6_7 = 0
Imposible_9_6_8: Choice_9_6_8 = 0
Imposible_9_6_9: Choice_9_6_9 = 0
Imposible_9_7_1: Choice_9_7_1 = 0
Imposible_9_7_2: Choice_9_7_2 = 0
Imposible_9_7_3: Choice_9_7_3 = 0
Imposible_9_7_4: Choice_9_7_4 = 0
Imposible_9_7_5: Choice_9_7_5 = 0
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
Imposible_9_8_7: Choice_9_8_7 = 0
Imposible_9_8_8: Choice_9_8_8 = 0
Imposible_9_8_9: Choice_9_8_9 = 0
Imposible_9_9_1: Choice_9_9_1 = 0
Imposible_9_9_2: Choice_9_9_2 = 0
Imposible_9_9_3: Choice_9_9_3 = 0
Imposible_9_9_4: Choice_9_9_4 = 0
Imposible_9_9_5: Choice_9_9_5 = 0
Imposible_9_9_6: Choice_9_9_6 = 0
Imposible_9_9_7: Choice_9_9_7 = 0
Imposible_9_9_8: Choice_9_9_8 = 0
Imposible_9_9_9: Choice_9_9_9 = 0
Row_131600_Unique_1: Choice_1_1_1 + Choice_1_1_2 + Choice_1_1_3 + Choice_1_1_4
 + Choice_1_1_5 + Choice_1_1_6 + Choice_1_1_7 + Choice_1_1_8 + Choice_1_1_9
 = 1
Row_131600_Unique_2: Choice_2_1_1 + Choice_2_1_2 + Choice_2_1_3 + Choice_2_1_4
 + Choice_2_1_5 + Choice_2_1_6 + Choice_2_1_7 + Choice_2_1_8 + Choice_2_1_9
 = 1
Row_131600_Unique_3: Choice_3_1_1 + Choice_3_1_2 + Choice_3_1_3 + Choice_3_1_4
 + Choice_3_1_5 + Choice_3_1_6 + Choice_3_1_7 + Choice_3_1_8 + Choice_3_1_9
 = 1
Row_131600_Unique_4: Choice_4_1_1 + Choice_4_1_2 + Choice_4_1_3 + Choice_4_1_4
 + Choice_4_1_5 + Choice_4_1_6 + Choice_4_1_7 + Choice_4_1_8 + Choice_4_1_9
 = 1
Row_131600_Unique_5: Choice_5_1_1 + Choice_5_1_2 + Choice_5_1_3 + Choice_5_1_4
 + Choice_5_1_5 + Choice_5_1_6 + Choice_5_1_7 + Choice_5_1_8 + Choice_5_1_9
 = 1
Row_131600_Unique_6: Choice_6_1_1 + Choice_6_1_2 + Choice_6_1_3 + Choice_6_1_4
 + Choice_6_1_5 + Choice_6_1_6 + Choice_6_1_7 + Choice_6_1_8 + Choice_6_1_9
 = 1
Row_131600_Unique_7: Choice_7_1_1 + Choice_7_1_2 + Choice_7_1_3 + Choice_7_1_4
 + Choice_7_1_5 + Choice_7_1_6 + Choice_7_1_7 + Choice_7_1_8 + Choice_7_1_9
 = 1
Row_131600_Unique_8: Choice_8_1_1 + Choice_8_1_2 + Choice_8_1_3 + Choice_8_1_4
 + Choice_8_1_5 + Choice_8_1_6 + Choice_8_1_7 + Choice_8_1_8 + Choice_8_1_9
 = 1
Row_131600_Unique_9: Choice_9_1_1 + Choice_9_1_2 + Choice_9_1_3 + Choice_9_1_4
 + Choice_9_1_5 + Choice_9_1_6 + Choice_9_1_7 + Choice_9_1_8 + Choice_9_1_9
 = 1
Row_131601_Unique_1: Choice_1_2_1 + Choice_1_2_2 + Choice_1_2_3 + Choice_1_2_4
 + Choice_1_2_5 + Choice_1_2_6 + Choice_1_2_7 + Choice_1_2_8 + Choice_1_2_9
 = 1
Row_131601_Unique_2: Choice_2_2_1 + Choice_2_2_2 + Choice_2_2_3 + Choice_2_2_4
 + Choice_2_2_5 + Choice_2_2_6 + Choice_2_2_7 + Choice_2_2_8 + Choice_2_2_9
 = 1
Row_131601_Unique_3: Choice_3_2_1 + Choice_3_2_2 + Choice_3_2_3 + Choice_3_2_4
 + Choice_3_2_5 + Choice_3_2_6 + Choice_3_2_7 + Choice_3_2_8 + Choice_3_2_9
 = 1
Row_131601_Unique_4: Choice_4_2_1 + Choice_4_2_2 + Choice_4_2_3 + Choice_4_2_4
 + Choice_4_2_5 + Choice_4_2_6 + Choice_4_2_7 + Choice_4_2_8 + Choice_4_2_9
 = 1
Row_131601_Unique_5: Choice_5_2_1 + Choice_5_2_2 + Choice_5_2_3 + Choice_5_2_4
 + Choice_5_2_5 + Choice_5_2_6 + Choice_5_2_7 + Choice_5_2_8 + Choice_5_2_9
 = 1
Row_131601_Unique_6: Choice_6_2_1 + Choice_6_2_2 + Choice_6_2_3 + Choice_6_2_4
 + Choice_6_2_5 + Choice_6_2_6 + Choice_6_2_7 + Choice_6_2_8 + Choice_6_2_9
 = 1
Row_131601_Unique_7: Choice_7_2_1 + Choice_7_2_2 + Choice_7_2_3 + Choice_7_2_4
 + Choice_7_2_5 + Choice_7_2_6 + Choice_7_2_7 + Choice_7_2_8 + Choice_7_2_9
 = 1
Row_131601_Unique_8: Choice_8_2_1 + Choice_8_2_2 + Choice_8_2_3 + Choice_8_2_4
 + Choice_8_2_5 + Choice_8_2_6 + Choice_8_2_7 + Choice_8_2_8 + Choice_8_2_9
 = 1
Row_131601_Unique_9: Choice_9_2_1 + Choice_9_2_2 + Choice_9_2_3 + Choice_9_2_4
 + Choice_9_2_5 + Choice_9_2_6 + Choice_9_2_7 + Choice_9_2_8 + Choice_9_2_9
 = 1
Row_131602_Unique_1: Choice_1_3_1 + Choice_1_3_2 + Choice_1_3_3 + Choice_1_3_4
 + Choice_1_3_5 + Choice_1_3_6 + Choice_1_3_7 + Choice_1_3_8 + Choice_1_3_9
 = 1
Row_131602_Unique_2: Choice_2_3_1 + Choice_2_3_2 + Choice_2_3_3 + Choice_2_3_4
 + Choice_2_3_5 + Choice_2_3_6 + Choice_2_3_7 + Choice_2_3_8 + Choice_2_3_9
 = 1
Row_131602_Unique_3: Choice_3_3_1 + Choice_3_3_2 + Choice_3_3_3 + Choice_3_3_4
 + Choice_3_3_5 + Choice_3_3_6 + Choice_3_3_7 + Choice_3_3_8 + Choice_3_3_9
 = 1
Row_131602_Unique_4: Choice_4_3_1 + Choice_4_3_2 + Choice_4_3_3 + Choice_4_3_4
 + Choice_4_3_5 + Choice_4_3_6 + Choice_4_3_7 + Choice_4_3_8 + Choice_4_3_9
 = 1
Row_131602_Unique_5: Choice_5_3_1 + Choice_5_3_2 + Choice_5_3_3 + Choice_5_3_4
 + Choice_5_3_5 + Choice_5_3_6 + Choice_5_3_7 + Choice_5_3_8 + Choice_5_3_9
 = 1
Row_131602_Unique_6: Choice_6_3_1 + Choice_6_3_2 + Choice_6_3_3 + Choice_6_3_4
 + Choice_6_3_5 + Choice_6_3_6 + Choice_6_3_7 + Choice_6_3_8 + Choice_6_3_9
 = 1
Row_131602_Unique_7: Choice_7_3_1 + Choice_7_3_2 + Choice_7_3_3 + Choice_7_3_4
 + Choice_7_3_5 + Choice_7_3_6 + Choice_7_3_7 + Choice_7_3_8 + Choice_7_3_9
 = 1
Row_131602_Unique_8: Choice_8_3_1 + Choice_8_3_2 + Choice_8_3_3 + Choice_8_3_4
 + Choice_8_3_5 + Choice_8_3_6 + Choice_8_3_7 + Choice_8_3_8 + Choice_8_3_9
 = 1
Row_131602_Unique_9: Choice_9_3_1 + Choice_9_3_2 + Choice_9_3_3 + Choice_9_3_4
 + Choice_9_3_5 + Choice_9_3_6 + Choice_9_3_7 + Choice_9_3_8 + Choice_9_3_9
 = 1
Row_131603_Unique_1: Choice_1_4_1 + Choice_1_4_2 + Choice_1_4_3 + Choice_1_4_4
 + Choice_1_4_5 + Choice_1_4_6 + Choice_1_4_7 + Choice_1_4_8 + Choice_1_4_9
 = 1
Row_131603_Unique_2: Choice_2_4_1 + Choice_2_4_2 + Choice_2_4_3 + Choice_2_4_4
 + Choice_2_4_5 + Choice_2_4_6 + Choice_2_4_7 + Choice_2_4_8 + Choice_2_4_9
 = 1
Row_131603_Unique_3: Choice_3_4_1 + Choice_3_4_2 + Choice_3_4_3 + Choice_3_4_4
 + Choice_3_4_5 + Choice_3_4_6 + Choice_3_4_7 + Choice_3_4_8 + Choice_3_4_9
 = 1
Row_131603_Unique_4: Choice_4_4_1 + Choice_4_4_2 + Choice_4_4_3 + Choice_4_4_4
 + Choice_4_4_5 + Choice_4_4_6 + Choice_4_4_7 + Choice_4_4_8 + Choice_4_4_9
 = 1
Row_131603_Unique_5: Choice_5_4_1 + Choice_5_4_2 + Choice_5_4_3 + Choice_5_4_4
 + Choice_5_4_5 + Choice_5_4_6 + Choice_5_4_7 + Choice_5_4_8 + Choice_5_4_9
 = 1
Row_131603_Unique_6: Choice_6_4_1 + Choice_6_4_2 + Choice_6_4_3 + Choice_6_4_4
 + Choice_6_4_5 + Choice_6_4_6 + Choice_6_4_7 + Choice_6_4_8 + Choice_6_4_9
 = 1
Row_131603_Unique_7: Choice_7_4_1 + Choice_7_4_2 + Choice_7_4_3 + Choice_7_4_4
 + Choice_7_4_5 + Choice_7_4_6 + Choice_7_4_7 + Choice_7_4_8 + Choice_7_4_9
 = 1
Row_131603_Unique_8: Choice_8_4_1 + Choice_8_4_2 + Choice_8_4_3 + Choice_8_4_4
 + Choice_8_4_5 + Choice_8_4_6 + Choice_8_4_7 + Choice_8_4_8 + Choice_8_4_9
 = 1
Row_131603_Unique_9: Choice_9_4_1 + Choice_9_4_2 + Choice_9_4_3 + Choice_9_4_4
 + Choice_9_4_5 + Choice_9_4_6 + Choice_9_4_7 + Choice_9_4_8 + Choice_9_4_9
 = 1
Row_131604_Unique_1: Choice_1_5_1 + Choice_1_5_2 + Choice_1_5_3 + Choice_1_5_4
 + Choice_1_5_5 + Choice_1_5_6 + Choice_1_5_7 + Choice_1_5_8 + Choice_1_5_9
 = 1
Row_131604_Unique_2: Choice_2_5_1 + Choice_2_5_2 + Choice_2_5_3 + Choice_2_5_4
 + Choice_2_5_5 + Choice_2_5_6 + Choice_2_5_7 + Choice_2_5_8 + Choice_2_5_9
 = 1
Row_131604_Unique_3: Choice_3_5_1 + Choice_3_5_2 + Choice_3_5_3 + Choice_3_5_4
 + Choice_3_5_5 + Choice_3_5_6 + Choice_3_5_7 + Choice_3_5_8 + Choice_3_5_9
 = 1
Row_131604_Unique_4: Choice_4_5_1 + Choice_4_5_2 + Choice_4_5_3 + Choice_4_5_4
 + Choice_4_5_5 + Choice_4_5_6 + Choice_4_5_7 + Choice_4_5_8 + Choice_4_5_9
 = 1
Row_131604_Unique_5: Choice_5_5_1 + Choice_5_5_2 + Choice_5_5_3 + Choice_5_5_4
 + Choice_5_5_5 + Choice_5_5_6 + Choice_5_5_7 + Choice_5_5_8 + Choice_5_5_9
 = 1
Row_131604_Unique_6: Choice_6_5_1 + Choice_6_5_2 + Choice_6_5_3 + Choice_6_5_4
 + Choice_6_5_5 + Choice_6_5_6 + Choice_6_5_7 + Choice_6_5_8 + Choice_6_5_9
 = 1
Row_131604_Unique_7: Choice_7_5_1 + Choice_7_5_2 + Choice_7_5_3 + Choice_7_5_4
 + Choice_7_5_5 + Choice_7_5_6 + Choice_7_5_7 + Choice_7_5_8 + Choice_7_5_9
 = 1
Row_131604_Unique_8: Choice_8_5_1 + Choice_8_5_2 + Choice_8_5_3 + Choice_8_5_4
 + Choice_8_5_5 + Choice_8_5_6 + Choice_8_5_7 + Choice_8_5_8 + Choice_8_5_9
 = 1
Row_131604_Unique_9: Choice_9_5_1 + Choice_9_5_2 + Choice_9_5_3 + Choice_9_5_4
 + Choice_9_5_5 + Choice_9_5_6 + Choice_9_5_7 + Choice_9_5_8 + Choice_9_5_9
 = 1
Row_131605_Unique_1: Choice_1_6_1 + Choice_1_6_2 + Choice_1_6_3 + Choice_1_6_4
 + Choice_1_6_5 + Choice_1_6_6 + Choice_1_6_7 + Choice_1_6_8 + Choice_1_6_9
 = 1
Row_131605_Unique_2: Choice_2_6_1 + Choice_2_6_2 + Choice_2_6_3 + Choice_2_6_4
 + Choice_2_6_5 + Choice_2_6_6 + Choice_2_6_7 + Choice_2_6_8 + Choice_2_6_9
 = 1
Row_131605_Unique_3: Choice_3_6_1 + Choice_3_6_2 + Choice_3_6_3 + Choice_3_6_4
 + Choice_3_6_5 + Choice_3_6_6 + Choice_3_6_7 + Choice_3_6_8 + Choice_3_6_9
 = 1
Row_131605_Unique_4: Choice_4_6_1 + Choice_4_6_2 + Choice_4_6_3 + Choice_4_6_4
 + Choice_4_6_5 + Choice_4_6_6 + Choice_4_6_7 + Choice_4_6_8 + Choice_4_6_9
 = 1
Row_131605_Unique_5: Choice_5_6_1 + Choice_5_6_2 + Choice_5_6_3 + Choice_5_6_4
 + Choice_5_6_5 + Choice_5_6_6 + Choice_5_6_7 + Choice_5_6_8 + Choice_5_6_9
 = 1
Row_131605_Unique_6: Choice_6_6_1 + Choice_6_6_2 + Choice_6_6_3 + Choice_6_6_4
 + Choice_6_6_5 + Choice_6_6_6 + Choice_6_6_7 + Choice_6_6_8 + Choice_6_6_9
 = 1
Row_131605_Unique_7: Choice_7_6_1 + Choice_7_6_2 + Choice_7_6_3 + Choice_7_6_4
 + Choice_7_6_5 + Choice_7_6_6 + Choice_7_6_7 + Choice_7_6_8 + Choice_7_6_9
 = 1
Row_131605_Unique_8: Choice_8_6_1 + Choice_8_6_2 + Choice_8_6_3 + Choice_8_6_4
 + Choice_8_6_5 + Choice_8_6_6 + Choice_8_6_7 + Choice_8_6_8 + Choice_8_6_9
 = 1
Row_131605_Unique_9: Choice_9_6_1 + Choice_9_6_2 + Choice_9_6_3 + Choice_9_6_4
 + Choice_9_6_5 + Choice_9_6_6 + Choice_9_6_7 + Choice_9_6_8 + Choice_9_6_9
 = 1
Row_131606_Unique_1: Choice_1_7_1 + Choice_1_7_2 + Choice_1_7_3 + Choice_1_7_4
 + Choice_1_7_5 + Choice_1_7_6 + Choice_1_7_7 + Choice_1_7_8 + Choice_1_7_9
 = 1
Row_131606_Unique_2: Choice_2_7_1 + Choice_2_7_2 + Choice_2_7_3 + Choice_2_7_4
 + Choice_2_7_5 + Choice_2_7_6 + Choice_2_7_7 + Choice_2_7_8 + Choice_2_7_9
 = 1
Row_131606_Unique_3: Choice_3_7_1 + Choice_3_7_2 + Choice_3_7_3 + Choice_3_7_4
 + Choice_3_7_5 + Choice_3_7_6 + Choice_3_7_7 + Choice_3_7_8 + Choice_3_7_9
 = 1
Row_131606_Unique_4: Choice_4_7_1 + Choice_4_7_2 + Choice_4_7_3 + Choice_4_7_4
 + Choice_4_7_5 + Choice_4_7_6 + Choice_4_7_7 + Choice_4_7_8 + Choice_4_7_9
 = 1
Row_131606_Unique_5: Choice_5_7_1 + Choice_5_7_2 + Choice_5_7_3 + Choice_5_7_4
 + Choice_5_7_5 + Choice_5_7_6 + Choice_5_7_7 + Choice_5_7_8 + Choice_5_7_9
 = 1
Row_131606_Unique_6: Choice_6_7_1 + Choice_6_7_2 + Choice_6_7_3 + Choice_6_7_4
 + Choice_6_7_5 + Choice_6_7_6 + Choice_6_7_7 + Choice_6_7_8 + Choice_6_7_9
 = 1
Row_131606_Unique_7: Choice_7_7_1 + Choice_7_7_2 + Choice_7_7_3 + Choice_7_7_4
 + Choice_7_7_5 + Choice_7_7_6 + Choice_7_7_7 + Choice_7_7_8 + Choice_7_7_9
 = 1
Row_131606_Unique_8: Choice_8_7_1 + Choice_8_7_2 + Choice_8_7_3 + Choice_8_7_4
 + Choice_8_7_5 + Choice_8_7_6 + Choice_8_7_7 + Choice_8_7_8 + Choice_8_7_9
 = 1
Row_131606_Unique_9: Choice_9_7_1 + Choice_9_7_2 + Choice_9_7_3 + Choice_9_7_4
 + Choice_9_7_5 + Choice_9_7_6 + Choice_9_7_7 + Choice_9_7_8 + Choice_9_7_9
 = 1
Row_131607_Unique_1: Choice_1_8_1 + Choice_1_8_2 + Choice_1_8_3 + Choice_1_8_4
 + Choice_1_8_5 + Choice_1_8_6 + Choice_1_8_7 + Choice_1_8_8 + Choice_1_8_9
 = 1
Row_131607_Unique_2: Choice_2_8_1 + Choice_2_8_2 + Choice_2_8_3 + Choice_2_8_4
 + Choice_2_8_5 + Choice_2_8_6 + Choice_2_8_7 + Choice_2_8_8 + Choice_2_8_9
 = 1
Row_131607_Unique_3: Choice_3_8_1 + Choice_3_8_2 + Choice_3_8_3 + Choice_3_8_4
 + Choice_3_8_5 + Choice_3_8_6 + Choice_3_8_7 + Choice_3_8_8 + Choice_3_8_9
 = 1
Row_131607_Unique_4: Choice_4_8_1 + Choice_4_8_2 + Choice_4_8_3 + Choice_4_8_4
 + Choice_4_8_5 + Choice_4_8_6 + Choice_4_8_7 + Choice_4_8_8 + Choice_4_8_9
 = 1
Row_131607_Unique_5: Choice_5_8_1 + Choice_5_8_2 + Choice_5_8_3 + Choice_5_8_4
 + Choice_5_8_5 + Choice_5_8_6 + Choice_5_8_7 + Choice_5_8_8 + Choice_5_8_9
 = 1
Row_131607_Unique_6: Choice_6_8_1 + Choice_6_8_2 + Choice_6_8_3 + Choice_6_8_4
 + Choice_6_8_5 + Choice_6_8_6 + Choice_6_8_7 + Choice_6_8_8 + Choice_6_8_9
 = 1
Row_131607_Unique_7: Choice_7_8_1 + Choice_7_8_2 + Choice_7_8_3 + Choice_7_8_4
 + Choice_7_8_5 + Choice_7_8_6 + Choice_7_8_7 + Choice_7_8_8 + Choice_7_8_9
 = 1
Row_131607_Unique_8: Choice_8_8_1 + Choice_8_8_2 + Choice_8_8_3 + Choice_8_8_4
 + Choice_8_8_5 + Choice_8_8_6 + Choice_8_8_7 + Choice_8_8_8 + Choice_8_8_9
 = 1
Row_131607_Unique_9: Choice_9_8_1 + Choice_9_8_2 + Choice_9_8_3 + Choice_9_8_4
 + Choice_9_8_5 + Choice_9_8_6 + Choice_9_8_7 + Choice_9_8_8 + Choice_9_8_9
 = 1
Row_131608_Unique_1: Choice_1_9_1 + Choice_1_9_2 + Choice_1_9_3 + Choice_1_9_4
 + Choice_1_9_5 + Choice_1_9_6 + Choice_1_9_7 + Choice_1_9_8 + Choice_1_9_9
 = 1
Row_131608_Unique_2: Choice_2_9_1 + Choice_2_9_2 + Choice_2_9_3 + Choice_2_9_4
 + Choice_2_9_5 + Choice_2_9_6 + Choice_2_9_7 + Choice_2_9_8 + Choice_2_9_9
 = 1
Row_131608_Unique_3: Choice_3_9_1 + Choice_3_9_2 + Choice_3_9_3 + Choice_3_9_4
 + Choice_3_9_5 + Choice_3_9_6 + Choice_3_9_7 + Choice_3_9_8 + Choice_3_9_9
 = 1
Row_131608_Unique_4: Choice_4_9_1 + Choice_4_9_2 + Choice_4_9_3 + Choice_4_9_4
 + Choice_4_9_5 + Choice_4_9_6 + Choice_4_9_7 + Choice_4_9_8 + Choice_4_9_9
 = 1
Row_131608_Unique_5: Choice_5_9_1 + Choice_5_9_2 + Choice_5_9_3 + Choice_5_9_4
 + Choice_5_9_5 + Choice_5_9_6 + Choice_5_9_7 + Choice_5_9_8 + Choice_5_9_9
 = 1
Row_131608_Unique_6: Choice_6_9_1 + Choice_6_9_2 + Choice_6_9_3 + Choice_6_9_4
 + Choice_6_9_5 + Choice_6_9_6 + Choice_6_9_7 + Choice_6_9_8 + Choice_6_9_9
 = 1
Row_131608_Unique_7: Choice_7_9_1 + Choice_7_9_2 + Choice_7_9_3 + Choice_7_9_4
 + Choice_7_9_5 + Choice_7_9_6 + Choice_7_9_7 + Choice_7_9_8 + Choice_7_9_9
 = 1
Row_131608_Unique_8: Choice_8_9_1 + Choice_8_9_2 + Choice_8_9_3 + Choice_8_9_4
 + Choice_8_9_5 + Choice_8_9_6 + Choice_8_9_7 + Choice_8_9_8 + Choice_8_9_9
 = 1
Row_131608_Unique_9: Choice_9_9_1 + Choice_9_9_2 + Choice_9_9_3 + Choice_9_9_4
 + Choice_9_9_5 + Choice_9_9_6 + Choice_9_9_7 + Choice_9_9_8 + Choice_9_9_9
 = 1
Total_Box_131610: Values_1_1 + Values_1_2 + Values_1_3 + Values_2_1
 + Values_2_2 + Values_2_3 + Values_3_1 + Values_3_2 + Values_3_3 = 45
Total_Box_131611: Values_4_1 + Values_4_2 + Values_4_3 + Values_5_1
 + Values_5_2 + Values_5_3 + Values_6_1 + Values_6_2 + Values_6_3 = 45
Total_Box_131612: Values_7_1 + Values_7_2 + Values_7_3 + Values_8_1
 + Values_8_2 + Values_8_3 + Values_9_1 + Values_9_2 + Values_9_3 = 45
Total_Box_131613: Values_1_4 + Values_1_5 + Values_1_6 + Values_2_4
 + Values_2_5 + Values_2_6 + Values_3_4 + Values_3_5 + Values_3_6 = 45
Total_Box_131614: Values_4_4 + Values_4_5 + Values_4_6 + Values_5_4
 + Values_5_5 + Values_5_6 + Values_6_4 + Values_6_5 + Values_6_6 = 45
Total_Box_131615: Values_7_4 + Values_7_5 + Values_7_6 + Values_8_4
 + Values_8_5 + Values_8_6 + Values_9_4 + Values_9_5 + Values_9_6 = 45
Total_Box_131616: Values_1_7 + Values_1_8 + Values_1_9 + Values_2_7
 + Values_2_8 + Values_2_9 + Values_3_7 + Values_3_8 + Values_3_9 = 45
Total_Box_131617: Values_4_7 + Values_4_8 + Values_4_9 + Values_5_7
 + Values_5_8 + Values_5_9 + Values_6_7 + Values_6_8 + Values_6_9 = 45
Total_Box_131618: Values_7_7 + Values_7_8 + Values_7_9 + Values_8_7
 + Values_8_8 + Values_8_9 + Values_9_7 + Values_9_8 + Values_9_9 = 45
Total_Column_131590: Values_1_1 + Values_2_1 + Values_3_1 + Values_4_1
 + Values_5_1 + Values_6_1 + Values_7_1 + Values_8_1 + Values_9_1 = 45
Total_Column_131591: Values_1_2 + Values_2_2 + Values_3_2 + Values_4_2
 + Values_5_2 + Values_6_2 + Values_7_2 + Values_8_2 + Values_9_2 = 45
Total_Column_131592: Values_1_3 + Values_2_3 + Values_3_3 + Values_4_3
 + Values_5_3 + Values_6_3 + Values_7_3 + Values_8_3 + Values_9_3 = 45
Total_Column_131593: Values_1_4 + Values_2_4 + Values_3_4 + Values_4_4
 + Values_5_4 + Values_6_4 + Values_7_4 + Values_8_4 + Values_9_4 = 45
Total_Column_131594: Values_1_5 + Values_2_5 + Values_3_5 + Values_4_5
 + Values_5_5 + Values_6_5 + Values_7_5 + Values_8_5 + Values_9_5 = 45
Total_Column_131595: Values_1_6 + Values_2_6 + Values_3_6 + Values_4_6
 + Values_5_6 + Values_6_6 + Values_7_6 + Values_8_6 + Values_9_6 = 45
Total_Column_131596: Values_1_7 + Values_2_7 + Values_3_7 + Values_4_7
 + Values_5_7 + Values_6_7 + Values_7_7 + Values_8_7 + Values_9_7 = 45
Total_Column_131597: Values_1_8 + Values_2_8 + Values_3_8 + Values_4_8
 + Values_5_8 + Values_6_8 + Values_7_8 + Values_8_8 + Values_9_8 = 45
Total_Column_131598: Values_1_9 + Values_2_9 + Values_3_9 + Values_4_9
 + Values_5_9 + Values_6_9 + Values_7_9 + Values_8_9 + Values_9_9 = 45
Total_Row_131600: Values_1_1 + Values_1_2 + Values_1_3 + Values_1_4
 + Values_1_5 + Values_1_6 + Values_1_7 + Values_1_8 + Values_1_9 = 45
Total_Row_131601: Values_2_1 + Values_2_2 + Values_2_3 + Values_2_4
 + Values_2_5 + Values_2_6 + Values_2_7 + Values_2_8 + Values_2_9 = 45
Total_Row_131602: Values_3_1 + Values_3_2 + Values_3_3 + Values_3_4
 + Values_3_5 + Values_3_6 + Values_3_7 + Values_3_8 + Values_3_9 = 45
Total_Row_131603: Values_4_1 + Values_4_2 + Values_4_3 + Values_4_4
 + Values_4_5 + Values_4_6 + Values_4_7 + Values_4_8 + Values_4_9 = 45
Total_Row_131604: Values_5_1 + Values_5_2 + Values_5_3 + Values_5_4
 + Values_5_5 + Values_5_6 + Values_5_7 + Values_5_8 + Values_5_9 = 45
Total_Row_131605: Values_6_1 + Values_6_2 + Values_6_3 + Values_6_4
 + Values_6_5 + Values_6_6 + Values_6_7 + Values_6_8 + Values_6_9 = 45
Total_Row_131606: Values_7_1 + Values_7_2 + Values_7_3 + Values_7_4
 + Values_7_5 + Values_7_6 + Values_7_7 + Values_7_8 + Values_7_9 = 45
Total_Row_131607: Values_8_1 + Values_8_2 + Values_8_3 + Values_8_4
 + Values_8_5 + Values_8_6 + Values_8_7 + Values_8_8 + Values_8_9 = 45
Total_Row_131608: Values_9_1 + Values_9_2 + Values_9_3 + Values_9_4
 + Values_9_5 + Values_9_6 + Values_9_7 + Values_9_8 + Values_9_9 = 45
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
