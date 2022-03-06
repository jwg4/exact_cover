from exact_cover_impl import get_exact_cover as raw_get_exact_cover

from .error import NoSolution


def get_exact_cover(matrix):
    result = raw_get_exact_cover(matrix)
    if result.size == 0:
        raise NoSolution("No solutions found by the C code.")
    return result
