.. Sudoku documentation master file, created by
   sphinx-quickstart on Wed Apr 20 16:22:27 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Variant Sudoku Solver
=====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



===============
Outside  Sudoku
===============

***************
Rules
***************

In this variant you are given some digits outside the grid. Those digits must appear in the first three cells
from that side.

***************
Example
***************

.. image:: problem046.svg
   :width: 600

***************
Constraints
***************

.. math::
    \sum_{d \in digits} C_{d}_{r}_{c} for (r,c) in Cells
