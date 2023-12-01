Finding Exact Covers in NumPy
=============================

[![PyPI version](https://badge.fury.io/py/exact-cover.svg)](https://badge.fury.io/py/exact-cover)
![Deploy wheels to pypi](https://github.com/jwg4/exact_cover/workflows/Deploy%20wheels%20to%20pypi/badge.svg)
![Run Python tests](https://github.com/jwg4/exact_cover/workflows/Run%20Python%20tests/badge.svg)

This is a Python 3 package to solve exact cover problems using Numpy. It is based on https://github.com/moygit/exact_cover_np by Moy Easwaran. Jack Grahl ported it to Python 3, fixed some bugs and made lots of small improvements to the packaging.

The original package by Moy was designed to solve sudoku. Now this package is only designed to solve exact cover problems given as boolean arrays. It can be used to solve sudoku and a variety of combinatorial problems. However the code to reduce a sudoku to an exact cover problem is no longer part of this project. It can be found at:
 - https://pypi.org/project/xudoku/
 - https://github.com/jwg4/xudoku

Another project, 'polyomino' by Jack Grahl uses this algorithm to solve polyomino tiling problems. It can be found at:
 - https://pypi.org/project/polyomino/
 - https://github.com/jwg4/polyomino

Summary
-------

The exact cover problem is as follows: given a set X and a
collection S of subsets of X, we want to find a subcollection S*
of S that is an exact cover or partition of X.  In other words,
S* is a bunch of subsets of X whose union is X, and which have
empty intersection with each other.  (Example below; more details [on
wikipedia](https://en.wikipedia.org/wiki/Exact_cover).)

This NumPy module uses Donald Knuth's Algorithm X
(also known as Dancing Links) to find
exact covers of sets.
For details on Algorithm X please see either
[the Wikipedia page](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)
or [Knuth's paper](http://arxiv.org/pdf/cs/0011047v1).
Specifically, we use the Knuth/Hitotsumatsu/Noshita method of
Dancing Links for efficient backtracking.  Please see
[Knuth's paper](http://arxiv.org/pdf/cs/0011047v1)
for details.

How to Use It
-------------

Suppose X = {0,1,2,3,4}, and suppose S = {A,B,C,D}, where

    A = {0, 3}
    B = {0, 1, 2}
    C = {1, 2}
    D = {4}.

Here we can just eyeball these sets and conclude that S* = {A,C,D} forms an
exact cover: each element of X is in one of these sets (i.e. is
"covered" by one of these sets), and no element of X is in more than
one.

We'd use `exact_cover` to solve the problem as follows:
using 1 to denote that a particular member of X is in a subset and 0 to
denote that it's not, we can represent the sets as

    A = 1,0,0,1,0    # The 0th and 3rd entries are 1 since 0 and 3 are in A; the rest are 0.
    B = 1,1,1,0,0    # The 0th, 1st, and 2nd entries are 1, and the rest are 0,
    C = 0,1,1,0,0    # etc.
    D = 0,0,0,0,1

Now we can call `exact_cover`:

    >>> import numpy as np
    >>> import exact_cover as ec
    >>> S = np.array([[1,0,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,1]], dtype=bool)
    >>> print(ec.get_exact_cover(S))
    [0 2 3]

This is telling us that the 0th row (i.e. A), the 2nd row (i.e. C),
and the 3rd row (i.e. D) together form an exact cover.

To see the total number of distinct solutions, we can use the function get_solution_count:

    >>> ec.get_solution_count(S)
    1

See the file examples.md for more detailed examples of use.


Implementation Overview
-----------------------

The NumPy module (`exact_cover`) is implemented in four pieces:

- The lowest level is `quad_linked_list`, which implements a circular
  linked-list with left-, right-, up-, and down-links.
- This is used in `sparse_matrix` to implement the type of sparse
  representation of matrices that Knuth describes in his paper (in
  brief, each column contains all its non-zero entries, and each
  non-zero cell also points to the (horizontally) next non-zero cell
  in either direction).
- Sparse matrices are used in `dlx` to implement Knuth's Dancing
  Links version of his Algorithm X, which calculates exact covers.
- `exact_cover` provides the glue code letting us invoke
  `dlx` on NumPy arrays.

The package now has some pure Python modules for helper functions, with the main algorithm in the C-only package `exact_cover_impl`.

How to develop
--------------

The package uses poetry and most of the setup for development uses that tool.

To install locally (as an editable package):
`poetry install`

To build:
`poetry build`

To run tests:
`poetry run test` or `poetry run doctest`

To open a Python shell with the package available:
`poetry run python`

The exception is running the C unit tests:
`make c_tests`

Repository
----------

- build/ The location where files are built.
- dist/ The location for fully prepared files.
- exact_cover/ The Python code.
- obj/ Where the compiled C code is going to be output.
- src/ The C sources.
- tests/ Tests for both the Python package and the C code.
- tools/ Code used in analysing and working with the library. This is not distributed with the package.

Acknowledgements
----------------

Thanks very much to Moy Easwaran (https://github.com/moygit) for his inspiring work!

Munit aka µnit (https://nemequ.github.io/munit/) is a wonderful unit testing framework for C code.
