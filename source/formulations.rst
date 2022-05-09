Formulations
============

It's not always obvious how to implement some constraints. There are known formulations
to implement different constraints. The mathematics is shown below

Comparison
==========

Equality
--------

Equality is easy. If two cells are equal either do

.. math::
    V_{r_1 c_1} = V_{r_2 c_2}

or

.. math::

    C_{d r_1 c_1} = C_{d r_2 c_2} \: \forall \: d\: \in Digits


Less than or equal
------------------

.. math::

    V_{r_1 c_1} \leq V_{r_2 c_2}

Less than
---------

LP cannot directly implement less than. However we are talking integers so its easy to convert into a
less than or equal to constraint by adding 1 to the smaller number

.. math::

    V_{r_1 c_1} + 1 \leq V_{r_2 c_2}

Not Equal To
------------

This turns out to be difficult. Think of it as two conditions,

.. math::

    x + 1 \leq y \vee y \leq x - 1.

You need to introduce a new binary variable.

.. math::
    x \leq y-1 + M \delta
.. math::
    x \geq y+1 + M (1 - \delta)
.. math::
    \delta \in {0,1}

The question of M is that it needs to be sufficently large to cover all cases. You don't want to make it
too large, or that causes solvers problems.

So if you are comparing two digits set M equal to the maximum digit.

Logical And
-----------

Logical Or
----------

Logical Not
-----------

Disjunction
-----------

Product values
--------------

Minimum and maximum
-------------------
