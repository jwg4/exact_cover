import pytest
import numpy as np

from exact_cover import get_exact_cover
from exact_cover.error import NoSolution

from .data import (
    # the exact cover matrix built manually
    small_trimino_problem,
    # the same store in a file
    small_trimino_problem_from_file)


def input1():
    return small_trimino_problem()['data']

def input2():
    return small_trimino_problem_from_file()['data']

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
    expected = small_trimino_problem()['solution1']
    run_on_input(input1(), expected)


def test_input2():
    expected = small_trimino_problem_from_file()['solution1']
    run_on_input(input2(), expected)
