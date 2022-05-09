Diagonal
=======

In diagonal sudoku, the values on one or both diagonals must be unique.

.. image:: images/diagonal.svg

Implementation
--------------

Just apply the uniqueness constraint to the cells on the diagonals.
This then just means making a region with the appropriate cells and applying
a uniqueness contraint.

YAML
----

There are two variants. TLBR for top left to bottom right, and BLTR for bottom left to top right.

.. code-block:: yaml

    Constraints:
      - BLTR:
      - TLBR


