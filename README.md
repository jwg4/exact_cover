Finding Exact Covers in NumPy (and Solving Sudoku!)
===================================================


Summary
-------

This NumPy module uses Donald Knuth's Algorithm X to find
[exact covers of sets](https://en.wikipedia.org/wiki/Exact_cover).
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



