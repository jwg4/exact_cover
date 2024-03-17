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


def get_solution_count(matrix):
    transformed = np.require(
        matrix, dtype=DTYPE_FOR_ARRAY, requirements=["C_CONTIGUOUS"]
    )
    assert (
        transformed.flags.c_contiguous
    ), "We depend on the input array being C contiguous for raw goodness."
    result = raw_get_solution_count(transformed)
    return result


def _solutions_array_to_set(a):
    def truncate(row):
        if all(x == 0 for x in row):
            return [0]
        else:
            if row[-1] == 0:
                return truncate(row[:-1])
            else:
                return row

    return set([tuple(truncate(row)) for row in a])


def get_all_solutions(matrix, max_count=None):
    transformed = np.require(
        matrix, dtype=DTYPE_FOR_ARRAY, requirements=["C_CONTIGUOUS"]
    )
    assert (
        transformed.flags.c_contiguous
    ), "We depend on the input array being C contiguous for raw goodness."
    if max_count is None:
        count = raw_get_solution_count(transformed)
    else:
        count = max_count
    result = raw_get_all_solutions(transformed, count)
    if result.size == 0:
        raise NoSolution("No solutions found by the C code.")
    return _solutions_array_to_set(result)
