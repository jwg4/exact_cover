# Examples

Importing the package:

    >>> import exact_cover as ec

Input and output to the package are using the numpy array type:

    >>> import numpy as np

This example is explained in README.md
    >>> S = np.array([[1,0,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,1]], dtype=np.int32)
    >>> print(ec.get_exact_cover(S))
    [0 2 3]

The numpy type to use is defined in the package for convenience and compatibility:
    >>> from exact_cover.io import DTYPE_FOR_ARRAY
    >>> T = np.array([[1,0,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,1]], dtype=DTYPE_FOR_ARRAY)
    >>> print(ec.get_exact_cover(T))
    [0 2 3]

It's also possible to retrieve the total number of solutions to an exact cover problem:
    >>> ec.get_solution_count(T)
    1

This function (experimental) returns a set of all the solutions to a problem:
    >>> U = np.array([[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 0, 0, 1]])
    >>> ec.get_all_solutions(U)
    {(2, 3), (0, 4), (0, 1, 5)}

You can pass in a max number of solutions that you would like the function to find.
    >>> ec.get_all_solutions(U, 2)
    {(0, 4), (0, 1, 5)}
    >>> ec.get_all_solutions(U, 3)
    {(2, 3), (0, 4), (0, 1, 5)}
    >>> ec.get_all_solutions(U, 5)
    {(2, 3), (0, 4), (0, 1, 5)}
