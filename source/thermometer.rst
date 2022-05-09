Thermometer
===========

In thermometer sudoku, we have a line with a bulb. There are two variants.
In a simple thermo the numbers must increase along the line.
In a frozen thermo, the numbers must not decrease towards the bulb. However with other constraints
taken into account, this changes. So if the two cells are within the same box, row or column, then
they must increase. If the leave a box, row and column, the number could be the same.

.. image:: images/mountain.svg

Implementation
--------------

Just check the row of each cell on the mountain, if the row is higher than the neighbouring cell on the line, add
a greater than constraint.

YAML
----

.. code-block:: yaml

    Constraints:
       - SimpleThermometer: 41, 31, 21, 11
       - FrozenThermometer: 11, 22, 13, 24, 15, 26, 17, 28, 19

Where the cells on the mountain are specified as rc for row column.