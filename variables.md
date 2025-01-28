# Sets

For a 9x9 sudoku, we have the following sets

$$rows = \{1,2,3,4,5,6,7,8,9\}$$

$$columns = \{1,2,3,4,5,6,7,8,9\}$$

$$digits = \{1,2,3,4,5,6,7,8,9\}$$

$$parity = \{odd, even\}$$

$$modulo = \{mod0, mod1, mod2\}$$

$$entropy = \{low, mid, high\}$$

# Choices

In the Sudoku solver, we need a set of booleans where we can use them for choices.

$$ Choice_{rcd} = \{0,1\} $$

where $ r \in rows $, $ c \in columns $ and $ d \in digits $

# Numbers

To make writing some constraints simpler add in some new variables for the values in a given cell. Since this is
a derived value it can be any positive integer value.

$$ Number_{rc} = \sum_{d \in digits} Choice_{rcd} * d $$

# Restrictions

For any cell, we only have one number allowed.

$$ \sum_{d \in digits} Choice_{rcd} = 1, \forall r \in rows, \forall c \in columns $$

# Uniqueness

For any region we can enforce uniqueness.

$$ \sum_{(r,c) \in region} Choice_{rcd} \leq 1, \forall d \in digits $$

Since rows, columns and boxes are all regions, we can enforce uniqueness for them using the rule.

The $\le$ condition needs an explanation as to why it us not $=$. If the region has 9 cells,
then all the sums will be 1. However we can have regions with less than 9 cells, so the $\le$ condition
needs to be applied. For a 9 cell region, the only way the condition can be met is that all the sums are 1.

