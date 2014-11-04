Finding Exact Covers in NumPy (and Solving Sudoku!)
===================================================


Summary
-------

The exact cover problem is as follows: given a set X and a
collection S of subsets of X, we want to find a subcollection S*
of S that is an exact cover or partition of X.  In other words,
S* is a bunch of subsets of X whose union is X, and which have
empty intersection with each other.  (Example below; more details [on
wikipedia](https://en.wikipedia.org/wiki/Exact_cover).)

This NumPy module uses Donald Knuth's Algorithm X to find
exact covers of sets.
For details on Algorithm X please see either
[the Wikipedia page](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)
or [Knuth's paper](http://arxiv.org/pdf/cs/0011047v1).
Specifically, we use the Knuth/Hitotsumatsu/Noshita method of
Dancing Links for efficient backtracking.  Please see
[Knuth's paper](http://arxiv.org/pdf/cs/0011047v1)
for details.

As an example, we use this NumPy module to
[solve Sudoku](https://en.wikipedia.org/wiki/Exact_cover#Sudoku).
As a bonus feature for the Sudoku piece, we also calculate an
approximate rating of the puzzle (easy, medium, hard, or very hard).


How to Try It
-------------

- `git clone https://github.com/moygit/exact_cover_np.git`
- `cd exact_cover_np`
- `make` will build everything, install the Python module
  `exact_cover_np`, and run all the tests.  It'll also show you some
  examples.
- To solve Sudoku, say: `sudoku.py < filename.csv`, where `filename.csv`
  contains the puzzle as a list of comma-separated values with 0's
  denoting the blank entries.


How to Use It (Example)
-----------------------

Suppose X = {0,1,2,3,4}, and suppose S = {A,B,C,D}, where

    A = {0, 3}
    B = {0, 1, 2}
    C = {2, 3}
    D = {4}.

Here we can just eyeball these sets and conclude that S* = {A,C,D} forms an
exact cover: each element of X is in one of these sets (i.e. is
"covered" by one of these sets), and no element of X is in more than
one.

We'd use `exact_cover_np` to solve the problem as follows:
using 1 to denote that a particular member of X is in a subset and 0 to
denote that it's not, we can represent the sets as

    A = 1,0,0,1,0    # The 0th and 3rd entries are 1 since 0 and 3 are in A; the rest are 0.
    B = 1,1,1,0,0    # The 0th, 1st, and 2nd entries are 1, and the rest are 0,
    C = 0,1,1,0,0    # etc.
    D = 0,0,0,0,1

Now we can call `exact_cover_np`:

    >>> import numpy as np
    >>> import exact_cover_np as ec
    >>> S = np.array([[1,0,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,1]], dtype='int32')
    >>> ec.get_exact_cover(S)
    array([0, 2, 3], dtype=int32)

This is telling us that the 0th row (i.e. A), the 2nd row (i.e. C),
and the 3rd row (i.e. D) together form an exact cover.


Implementation Overview
-----------------------

The NumPy module (`exact_cover_np`) is implemented in four pieces:

- The lowest level is `quad_linked_list`, which implements a circular
  linked-list with left-, right-, up-, and down-links.
- This is used in `sparse_matrix` to implement the type of sparse
  representation of matrices that Knuth describes in his paper (in
  brief, each column contains all its non-zero entries, and each
  non-zero cell also points to the (horizontally) next non-zero cell
  in either direction).
- Sparse matrices are used in `dlx` to implement Knuth's Dancing
  Links version of his Algorithm X, which calculates exact covers.
- `exact_cover_np` provides the glue code letting us invoke
  `dlx` on NumPy arrays.
- And finally, `sudoku.py` is the example application.



