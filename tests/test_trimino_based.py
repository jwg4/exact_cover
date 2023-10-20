import pytest
import numpy as np

from exact_cover import get_exact_cover
from exact_cover.error import NoSolution
from exact_cover.io import DTYPE_FOR_ARRAY

# from exact_cover.helpers import is_solution

DTYPE = dict(dtype=DTYPE_FOR_ARRAY)

# from exact_cover.io import load_problem

# from tests.config import GLOBAL_CONFIG


# one specific problem that I had trouble with
# originally based on solving the trivial problem
# of arranging 2 identical triminos on a 3x3 board

#    +--+
#    |  |
# +--+--+
# |  |  |
# +--+--+

# +--+--+--+
# |xx|  |xx|
# +--+--+--+
# |  |  |  |
# +--+--+--+
# |xx|  |  |
# +--+--+--+


# the exact cover matrix built manually
def input1():
    to_cover = [
        [1, 0, 0, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0],  # <- 5
        [1, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1],  # <- 13
    ]
    return np.array(to_cover, **DTYPE)


def input2():
    return np.load("tests/files/small_trimino_problem.npy")


def test_inputs_are_equal():
    m1 = input1()
    m2 = input2()

    # really equal, including their dtype
    assert (
        np.all(np.equal(m1, m2)) and (m1.dtype is m2.dtype) and (m1.shape == m2.shape)
    )


def run_on_input(array, expected):
    try:
        solution = get_exact_cover(array)
        assert np.all(solution == expected)
    except NoSolution:
        pytest.fail(f"no solution found for {array}")


def test_input1():
    run_on_input(input1(), [5, 13])


def test_input2():
    run_on_input(input2(), [5, 13])
