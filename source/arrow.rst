Arrow
=====

In arrow sudoku, the value in the circle is the sum of the values on the arrow.

.. image:: images/arrow.svg

Implementation
--------------

Value in the first cell = sum of the other values on the arrow

YAML
----

.. code-block:: yaml

    Constraints:
      - Arrow: 12, 13, 23, 33

The first cell is for the total and cells are specified in standard rc [row column] format.


Bookkeeping
-----------

For a one cell on the shaft arrow, the condition is that the two cells must be the same.

For a two cell arrow the head must be at least 2. If the shaft cells are in the same region where
uniqueness applies, the restriction is greater than or equal to 3. ie. 1+2

There can be no 9s on a two cell shaft

Similary if that restiction applies for 3 cells it is greater than or equal to 6

The more general solution is proper bookkeeping.



