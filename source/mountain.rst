Mountain
========

In mountain sudoku, we have a line that forms a zig-zag that looks like a mountain. Cells that are higher up the
mountaint have a higher value.

.. image:: images/mountain.svg

Implementation
--------------

Just check the row of each cell on the mountain, if the row is higher than the neighbouring cell on the line, add
a greater than constraint.

YAML
----

.. code-block:: yaml

    Constraints:
      - Mountain: 21, 12, 23, 34, 25, 16, 27, 18, 29

Where the cells on the mountain are specified as rc for row column.