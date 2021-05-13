import numpy as np

from exact_cover import get_exact_cover
from exact_cover.helpers import is_solution


def test_small_sudoku_problem():
    matrix = np.genfromtxt("tests/files/small_sudoku.csv", dtype=np.int32)
    assert matrix.shape == (64, 64)
    col_sums = np.sum(matrix, axis=0)
    assert all(col_sums <= 4)
    row_sums = np.sum(matrix, axis=1)
    assert all(row_sums == 0 or row_sums == 4)


def test_solve_small_sudoku_problem():
    matrix = np.genfromtxt("tests/files/small_sudoku.csv", dtype=np.int32)
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)
