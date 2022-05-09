Disjoint Group
==============

In disjoint group sudoku, standard sudoku rules apply. 
In addition  cells with the same position in 3x3 boxes contains number from 1 to 9 i.e no number can repeat in the same position in 3x3 boxes

.. image:: images/disjoint_group.svg

Implementation
--------------

This is just an additional uniqueness constraint. Since there are 9 boxes, for each position in each box, the numbers must be unique

YAML
----

.. code-block:: yaml

    DisjointGroup:




