Introduction
============

Problems are defined using yaml. There are three sections. First one to decribe the board. Then a section
that defines the constraints. Lastly an optional section for the known solution

.. image:: images/standard.svg


Board
-----

The first part is to define the board

.. code-block:: yaml

    Board:
      Title: She Makes The Numbers Dance!
      Author: Shye
      Video: https://www.youtube.com/watch?v=yMkwG_y5gpk&t=1685s
      Reference: https://app.crackingthecryptic.com/sudoku/TdBgH8fFdF
      Board: 9x9
      Boxes: 3x3


==========  ======== ==============================================================
Field       Optional Description
==========  ======== ==============================================================
Title       Yes      Name of the Sudoku
Author      Yes      Author
Video       Yes      URL for a video for the sudoku
Reference   Yes      URL for where you can play online
Board       No       RxC where R is the number of rows, C the number of columns
Boxes       Yes      RxC like the board but gives the shape of the boxes. Optional
==========  ======== ==============================================================

Constraints
-----------

Constraints are defined in a contraints section.
Here's a definition of a standard sudoku

.. code-block:: yaml

    Constraints:
      - Columns:
      - Rows:
      - Boxes:
      - Knowns:
          - 8..4.6..3
          - ..9....2.
          - ........1
          - ...8..4..
          - .6.....1.
          - ..3..2..9
          - 7.2.3....
          - .4....5..
          - 5..7.9..8


Constraints are a yaml list.

+ Columns makes the cells unique in each column.
+ Rows makes the cells unique in each row.
+ Boxes makes the cells unique in each box.
+ Knowns.  A number makes that cell equal to the given digit. A '.' can take any digit.

Solution
--------

You can give an optional solution. This will be used for testing and to present a view of the problem
and solution

.. code-block:: yaml

    Solution:
      - 815426973
      - 379158624
      - 624397851
      - 297813465
      - 468975312
      - 153642789
      - 782534196
      - 946281537
      - 531769248

It look just like the known section, but all numbers are given.






