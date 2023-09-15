# Examples

Importing the package:

    >>> import exact_cover as ec

Input and output to the package are using the numpy array type:

    >>> import numpy as np

This example is explained in README.md
    >>> S = np.array([[1,0,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,1]], dtype=np.int32)
    >>> ec.get_exact_cover(S)
    array([0, 2, 3], dtype=int32)

The numpy type to use is defined in the package for convenience and compatibility:
    >>> from exact_cover.io import DTYPE_FOR_ARRAY
    >>> T = np.array([[1,0,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,1]], dtype=DTYPE_FOR_ARRAY)
    >>> ec.get_exact_cover(T)
    array([0, 2, 3], dtype=int32)
