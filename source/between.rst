Between
=======

In between sudoku, we have a line with two circles at the end. The numbers not on the ends must lie
strictly between the numbers in the circles


.. image:: images/between.svg

Implementation
--------------

Todo

YAML
----

.. code-block:: yaml

    Constraints:
       - Between: 11, 22, 13, 24, 15, 26, 17, 28, 19

Where the cells on the line are specified as rc for row column.
The first and last cells are the end cells. The other cells for the interior