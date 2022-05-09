Asterix
=======

In asterix sudoku, the values in the shaded cells must be unique. .

.. image:: images/asterix.svg

Implementation
--------------

Just apply the uniqueness constraint to the cells

YAML
----

.. code-block:: yaml

    Constraints:
      - Asterix:

