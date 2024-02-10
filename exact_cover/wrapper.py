from exact_cover_impl import get_exact_cover as raw_get_exact_cover
from exact_cover_impl import get_solution_count as raw_get_solution_count
from exact_cover_impl import get_all_solutions as raw_get_all_solutions

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


def get_all_solutions(matrix):
    transformed = np.require(
        matrix, dtype=DTYPE_FOR_ARRAY, requirements=["C_CONTIGUOUS"]
    )
    assert (
        transformed.flags.c_contiguous
    ), "We depend on the input array being C contiguous for raw goodness."
    count = raw_get_solution_count(transformed)
    result = raw_get_all_solutions(transformed, count)
    if result.size == 0:
        raise NoSolution("No solutions found by the C code.")
    return result
