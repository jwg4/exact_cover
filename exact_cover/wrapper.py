from exact_cover_impl import get_exact_cover as raw_get_exact_cover

from .error import NoSolution
from .io import DTYPE_FOR_ARRAY


def get_exact_cover(matrix):
    if matrix.dtype == DTYPE_FOR_ARRAY:
        result = raw_get_exact_cover(matrix)
    else:
        result = raw_get_exact_cover(matrix.astype(DTYPE_FOR_ARRAY))
    if result.size == 0:
        raise NoSolution("No solutions found by the C code.")
    return result
