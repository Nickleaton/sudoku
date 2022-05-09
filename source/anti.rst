Anti
====

Typical associated with chess moves, but there are other variants.

As an example, taking an antiknight sudoku, if we have a 9 in a given cell, then you cannot have another 9 
in any cell that is a chess knight's move away

Implementation
--------------

For each move we have a set of offsets that represent the chess moves. 
For each cell, we calculate the squares we need to check, removing any if they are not on the board. 
Then for each digit, we add a rule, that bans the digit from appearing in both cells.

So if we are checking r1c1 and r2c2 for digit d, we add the constraint

.. math:: 

	\\C_{d r_1 c_1} + C_{d r_2 c_2} <= 1
	

AntiKing
--------

Here the check is just the same offsets as a king's move in chess. One square orthoganally or vertically. 
The orthogonal is redudant since it should be caught by the row and column constraints


AntiKnight
----------

The offsets are just chess knight's moves. 2 cells forward 1 to the side. 

AntiMonkey
----------

Similar to antiknight, but 3 cells forward, one to the side.

AntiQueen
---------

Any number of orthoganal or diagonal moves. Typically this is implemented for a restricted set of digits


YAML
----

.. code-block:: yaml

	Constraints:
       - Antiknight:
       - Antiking:
       - AntiMonkey:
       - AntiQueen: 9
    
It's possible to set digits in the constraint such as the AntiQueen above that only applies to the digit 9. 
If no digits are specified it will assume it applie to all digits