import numpy as np

from exact_cover_impl import get_solution_count
from exact_cover.io import DTYPE_FOR_ARRAY

from .data import small_trimino_problem
from .data import detailed_wikipedia_problem

def test_solution_count():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 2


def test_solution_count_single_solution():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 1


def test_solution_count_no_solutions():
    data = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 0

def test_small_trimino_problem():
    problem = small_trimino_problem()
    data = problem['data']
    result = get_solution_count(data)
    assert result == problem['solution_count']

def test_detailed_wikipedia_problem():
    problem = detailed_wikipedia_problem()
    data = problem['data']
    result = get_solution_count(data)
    assert result == problem['solution_count']
