import pytest
import numpy as np

from exact_cover import get_exact_cover
from exact_cover.error import NoSolution
from exact_cover.helpers import is_solution
from exact_cover.io import load_problem

from tests.config import GLOBAL_CONFIG

# These problems were originally sudoku problems specified
# as values and blanks of the sudoku grid. Since this package
# doesn't include code for manipulating or building sudoku
# problems any more, the sudoku formulation was removed, but
# the underlying exact cover problems were kept, because they
# are good tests of the algorithm.


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


def test_solve_small_empty_sudoku_problem():
    matrix = load_problem("tests/files/small_empty_sudoku.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)


def test_solve_trivial_sudoku_problem():
    matrix = load_problem("tests/files/trivial_sudoku.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)


def test_solve_easy_sudoku_problem():
    matrix = load_problem("tests/files/easy_sudoku.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)


def test_solve_easy_sudoku_problem_2():
    matrix = load_problem("tests/files/easy_sudoku_2.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)


@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_solve_medium_sudoku_problem():
    matrix = load_problem("tests/files/medium_sudoku.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)


@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_solve_hard_sudoku_problem():
    matrix = load_problem("tests/files/hard_sudoku.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)


@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_solve_very_hard_sudoku_problem():
    matrix = load_problem("tests/files/very_hard_sudoku.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)


@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_solve_very_hard_sudoku_problem_2():
    matrix = load_problem("tests/files/very_hard_sudoku_2.csv")
    solution = get_exact_cover(matrix)
    assert is_solution(solution, matrix)


def test_solve_impossible_sudoku_problem():
    matrix = load_problem("tests/files/impossible_sudoku.csv")
    with pytest.raises(NoSolution):
        get_exact_cover(matrix)
