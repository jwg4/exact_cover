import logging

import numpy as np

import pytest

from hypothesis import given, settings
from hypothesis.strategies import integers

from exact_cover import get_exact_cover
from exact_cover.helpers import reduce, split_problem, is_solution
from exact_cover.error import NoSolution, CannotSplitFurther

from .config import GLOBAL_CONFIG
from .test_exact_cover_problems import (
    all_problems,
    array_with_solution,
    array_without_solution,
    large_problems_with_solution,
    large_problems_without_solution,
)


def test_reduce():
    d = [[0, 1, 0], [1, 1, 1], [1, 1, 1]]
    a = np.array(d)
    result = reduce(a)
    np.testing.assert_array_equal(result, a)


@given(array_with_solution)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_reduce_with_solution(a):
    result = reduce(a)
    assert result.shape[0] <= a.shape[0]
    assert result.shape[1] <= a.shape[1]


@settings(deadline=None)
@given(array_without_solution)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_reduce_without_solution(a):
    try:
        result = reduce(a)
        assert result.shape[0] <= a.shape[0]
        assert result.shape[1] <= a.shape[1]
    except NoSolution:
        assert True


def test_split_problem():
    d = [[0, 1, 0], [1, 1, 1], [1, 1, 1]]
    a = np.array(d)
    result = list(split_problem(a, 2))
    assert len(result) >= 2
    for sub in result:
        assert isinstance(sub, np.ndarray)
        assert sub.shape == a.shape


@given(all_problems)
@settings(deadline=None)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_split_arbitrary_problem(a):
    try:
        result = list(split_problem(a, 2))
        assert len(result) >= 2
        for sub in result:
            assert isinstance(sub, np.ndarray)
            assert sub.shape == a.shape
    except NoSolution:
        assert True
    except CannotSplitFurther:
        assert True


@given(all_problems, integers(2, 100))
@settings(deadline=None)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_correct_number_of_splits(a, n):
    try:
        result = list(split_problem(a, n))
        assert len(result) >= n
        assert len(result) < n * a.shape[0]
    except NoSolution:
        assert True
    except CannotSplitFurther:
        assert True


@given(large_problems_without_solution)
@settings(deadline=None)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_many_splits_without_solution(a):
    n = 1000
    try:
        result = list(split_problem(a, n))
        assert len(result) >= n
        assert len(result) < n * a.shape[0]
    except NoSolution:
        assert True


@given(array=large_problems_with_solution)
@settings(deadline=None)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_many_splits_with_solution(caplog, array):
    n = 1000
    # We count a list with the same number of elements, but each
    # is None. This is so that we don't flood our memory with
    # more than 1000 large numpy arrays.
    with caplog.at_level(logging.INFO):
        result = list(None for x in split_problem(array, n))
    assert len(result) >= n
    assert len(result) < n * array.shape[0]


@given(all_problems, integers(2, 30))
@settings(deadline=None)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_solution_to_split_problem_solves_original_problem(a, n):
    try:
        result = list(split_problem(a, n))
        for sub in result:
            s = get_exact_cover(sub)
            if s.size > 0:
                assert is_solution(s, sub)
                assert is_solution(s, a)
    except NoSolution:
        assert True
    except CannotSplitFurther:
        assert True


@given(array_with_solution)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_is_solution(a):
    s = get_exact_cover(a)
    assert is_solution(s, a)


@given(array_with_solution)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_list_is_solution(a):
    s = list(get_exact_cover(a))
    assert is_solution(s, a)


@given(array_with_solution, integers(0, 100))
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_is_solution_fails_for_extra_rows(a, x):
    s = get_exact_cover(a)
    assert not is_solution(list(s) + [x], a)


@given(array_with_solution)
@pytest.mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_is_solution_fails_for_proper_subset(a):
    s = get_exact_cover(a)
    assert not is_solution(s[:-1], a)
