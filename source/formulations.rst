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

.. _My target:
.. _formulations-logical-and:

Logical AND
-----------

The following are equivalent

.. math:: 

    d = d_1 \wedge d_2 \wedge ... \wedge d_n

.. math:: 

    d = \Pi_i d_i

.. math:: 

     d = minimum \{ d_1, d_2, ... d_n \}
     
     
Create d as a binary variable
     
Add the following constraints

.. math::

    d \leq d_i

.. math::

    d \geq \sum_i d_i - (n-1)

.. math::

    d \geq 0


.. _formulations-logical-or:

Logical OR
----------

The following are equivalent

.. math::

     d = max \{ d_i \}

.. math:: 

    d = d_1 \vee d_2 ... \vee d_n
		 
Add the following contraints

.. math::

   d \geq d_i
   
   d \leq \sum_i d_i
   
   d \leq 1
		 

.. _formulations-logical-not:

Logical NOT
-----------

.. math:: 

    d = \neg \; d_1
		
where both are binary variables

Add the following constraint

.. math::

    d = 1 - d_1
		

.. _formulations-product-binary-and-value:

Product binary and value
------------------------

We want

.. math:: 

    y = x \cdot d

where x is the variable and d the binary

We need that 

.. math:: 
	
    L \leq x \leq U

Add the following constraints

.. math::

    L \cdot d \leq y
	
.. math:: 

    y <= U \cdot d
	
.. math:: 

    L \cdot (1 - d) \leq x - y
	
.. math::

    x - y \leq U \cdot (1 - d)

Minimum
-------

We want

.. math:: y = minimum (x_i)

where we know that

.. math:: L \leq x_i \leq U


Add binary variables

.. math:: d_i

Add the following constraints

.. math::

    y \leq x_i

.. math::

    y \geq x_i - (U-L)(1-d_i)

.. math::
    \sum_i d_i = 1

the last being a SOS1 type constraint.

Maximum
-------

We want

.. math:: y = maximum (x_i)

where we know that

.. math:: L \leq x_i \leq U


Add binary variables

.. math:: d_i

Add the following constraints

.. math::

    y \geq x_i

.. math::

    y \leq x_i + (U-L)(1-d_i)

.. math::
    \sum_i d_i = 1

the last being a SOS1 type constraint.

Absolute
--------

We want

.. math:: y = | x_1 - x_2 |

where we know that

.. math:: 0 \leq x_i \leq U

Add binary variable

.. math:: d

Add these constraints

.. math:: 0 \leq y - (x_1 - x_2)
.. math:: y - (x_1 - x_2) \leq 2 \cdot U \cdot d
.. math:: 0 \leq y - (x_2 - x_1)
.. math:: y - (x_2 - x_1) \leq 2 \cdot U \cdot (1-d)


Disjunction
-----------
