import numpy as np

from exact_cover import get_exact_cover
from exact_cover.helpers import is_solution


def test_small_sudoku_problem():
    matrix = np.genfromtxt("tests/files/small_sudoku.csv")
    assert matrix.shape == (64, 64)


def test_solve_small_sudoku_problem():
    matrix = np.genfromtxt("tests/files/small_sudoku.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)
