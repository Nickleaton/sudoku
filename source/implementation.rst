Implementation
==============

Sudokus can be solved with a Integer Linear Programming formulation.

Assumuming a 9x9 sudoku, it is easy to change to other sizes, we can implement in the following way.

Add 9 x 9 x 9 = 729 binary decision variables. For a given cell you get 9 decision variables, corresponding to each of the possible digits.

One Digit Per Cell
------------------

To ensure that you only have one digit per cell we implement this restriction. 

.. math::

	\sum_{d \in Digits} C_{drc} = 1 , \forall r \in Rows, \forall c \in Columns


Region Uniqueness
-----------------

To implement uniqueness in any region, such as a box, row or column, add this restriction.

.. math::

	\sum_{ (r,c) \in Region} C_{drc} \leq 1 , \forall d\in Digits

Known Digits
------------

To constrain a known digit, say d in cell rc

.. math::

    C_{drc} = 1

optionaly add these as well

.. math::

    C_{d_x rc} = 0, \forall d_x \in Digits \: such \: that \: d_x \ne d


Value
-----

There are two appoaches to values. One is to just a sum and rely on the expression handling to sort out the
model construction.  This leads to large expresions in the lp file and makes it difficult to debug.

The second is to create an intermediate variable. In practice the presolve should remove these variables. This
makes it easier to debug.

.. math::
    V_{rc} = d * C_{drc} \: \forall d \in Digits

This leads to an alternative formulation for known digits

.. math::

    V_{rc} = d


