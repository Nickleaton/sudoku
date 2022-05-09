Renban
======

On a renban line, the order of the digits is irrelevant, however they must form a continuous set of digits.
For example a 4 cell renban could contain the digits 4, 5, 6 and 7 in any order. An invalid choice
would be 1, 5, 6 and 7

.. image:: images/renban.svg

Implementation
--------------

We add two new variables, min and max

.. math::

    \min \leq V_{rc}, \forall\:rc\:\in\:line

and

.. math::

    \max \geq V_{rc}, \forall\:rc\:\in\:line

Now we need one more constraint

.. math::

    \max - min = length(line)

YAML
----

.. code-block:: yaml

    Constraints:
      - Renban: 12, 13, 23, 33



