import numpy as np

from exact_cover import get_exact_cover
from exact_cover.helpers import is_solution
from exact_cover.io import load_problem


def test_small_sudoku_problem():
    matrix = load_problem("tests/files/small_sudoku.csv")
    assert matrix.shape == (64, 64)
    col_sums = np.sum(matrix, axis=0)
    assert all(col_sums <= 4)
    row_sums = np.sum(matrix, axis=1)
    assert np.isin(row_sums, [0, 4]).all()


def test_solve_small_sudoku_problem():
    matrix = load_problem("tests/files/small_sudoku.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)
