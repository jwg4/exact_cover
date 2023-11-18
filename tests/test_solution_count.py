import numpy as np

from exact_cover_impl import get_solution_count
from exact_cover.io import DTYPE_FOR_ARRAY

from .problems import small_trimino_problem
from .problems import detailed_wikipedia_problem
from .problems import bruteforce_problem1, bruteforce_problem2, bruteforce_problem3


def test_solution_count():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 2


def test_solution_count_zero_rows():
    """
        Blank rows are ignored - we don't count extra solutions
        which include some collection of blank rows.
    """
    data = np.array([[1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 0], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 2


def test_solution_count_duplicate_rows():
    """
        Duplicate rows mean that all the solutions including
        those rows are counted multiple times.

        Here we have a basic problem involving rows
        A, B, C, and D, and two distinct solutions, A+C and A+B+D

        By adding another copy of A and another copy of C, we
        get 6 different solutions:
        A1 + C1, A1 + C2, A2 + C1, A2 + C2, A1 + B + D, A2 + B + D
    """
    data = np.array([[1, 0, 0], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 6


def test_solution_count_single_solution():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 1


def test_solution_count_no_solutions():
    data = np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0]], dtype=DTYPE_FOR_ARRAY
    )
    result = get_solution_count(data)
    assert result == 0


def test_small_trimino_problem():
    problem = small_trimino_problem()
    data = problem["data"]
    result = get_solution_count(data)
    assert result == problem["solution_count"]


def test_detailed_wikipedia_problem():
    problem = detailed_wikipedia_problem()
    data = problem["data"]
    result = get_solution_count(data)
    assert result == problem["solution_count"]


def test_bruteforce_problem1():
    problem = bruteforce_problem1()
    data = problem["data"]
    result = get_solution_count(data)
    assert result == problem["solution_count"]


def test_bruteforce_problem2():
    problem = bruteforce_problem2()
    data = problem["data"]
    result = get_solution_count(data)
    assert result == problem["solution_count"]


def test_bruteforce_problem3():
    problem = bruteforce_problem3()
    data = problem["data"]
    result = get_solution_count(data)
    assert result == problem["solution_count"]
