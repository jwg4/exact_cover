from exact_cover_impl import get_exact_cover as raw_get_exact_cover

from .error import NoSolution
from .io import DTYPE_FOR_ARRAY


def get_exact_cover(matrix):
    if matrix.dtype == DTYPE_FOR_ARRAY:
        assert matrix.flags.c_contiguous, "We depend on the input array being C contiguous as we access the internal data directly."
        result = raw_get_exact_cover(matrix)
    else:
        transformed = matrix.astype(DTYPE_FOR_ARRAY)
        assert transformed.flags.c_contiguous, "We depend on the input array being C contiguous as we access the internal data directly."
        result = raw_get_exact_cover(transformed)
    if result.size == 0:
        raise NoSolution("No solutions found by the C code.")
    return result
