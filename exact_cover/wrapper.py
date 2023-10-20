from exact_cover_impl import get_exact_cover as raw_get_exact_cover

from .error import NoSolution
from .io import DTYPE_FOR_ARRAY

import numpy as np


def get_exact_cover(matrix):
    transformed = np.require(
        matrix, dtype=DTYPE_FOR_ARRAY, requirements=["C_CONTIGUOUS"]
    )
    assert (
        transformed.flags.c_contiguous
    ), "We depend on the input array being C contiguous for raw goodness."
    result = raw_get_exact_cover(transformed)
    if result.size == 0:
        raise NoSolution("No solutions found by the C code.")
    return result
