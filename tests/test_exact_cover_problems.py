import numpy as np

from hypothesis import given, example
from hypothesis.strategies import integers, lists, booleans
from hypothesis.strategies import composite, one_of, permutations

from exact_cover_np import get_exact_cover


@composite
def exact_cover_problem(draw):
    width = draw(integers(min_value=1, max_value=15))
    data = draw(lists(lists(booleans(), min_size=width, max_size=width), min_size=1, max_size=30))
    return np.array(data, dtype=np.int32)


@given(exact_cover_problem())
def test_exact_cover(array_data):
    rowcount = len(array_data)
    actual = get_exact_cover(array_data)
    assert actual.size <= rowcount
    assert all(actual < rowcount)


@composite
def array_with_exact_cover(draw):
    width = draw(integers(min_value=1, max_value=15))
    dummy_data = draw(lists(lists(booleans(), min_size=width, max_size=width), min_size=1, max_size=30))
    cover_size = draw(integers(min_value=1, max_value=10))
    cover = draw(lists(integers(min_value=0, max_value=cover_size - 1), min_size=width, max_size=width))
    cover_data = [[a == i for a in cover] for i in range(0, cover_size)]
    data = cover_data + dummy_data
    shuffled_data = draw(permutations(data))
    return np.array(shuffled_data, dtype=np.int32)


@composite
def array_with_trivial_solution(draw):
    array = draw(exact_cover_problem())
    height, width = array.shape
    row = draw(integers(min_value=0, max_value=height-1))
    array[row] = 1
    return array


@example(np.array([[1, 1, 1]], dtype=np.int32))
@example(np.array([[1, 0, 0], [0, 1, 1]], dtype=np.int32))
@given(one_of(array_with_trivial_solution(), array_with_exact_cover()))
def test_exact_cover_with_solution(array_data):
    rowcount = len(array_data)
    actual = get_exact_cover(array_data)
    assert actual.size > 0
    assert actual.size <= rowcount
    assert all(actual < rowcount)
    check_cover = array_data[actual, :].sum(axis=0)
    assert all(check_cover == 1)


@composite
def exact_cover_problem_with_empty_col(draw):
    array = draw(exact_cover_problem())
    height, width = array.shape
    col = draw(integers(min_value=0, max_value=width-1))
    array[:, col] = 0
    return array


@composite
def exact_cover_problem_with_abc(draw):
    """
        A simple way of making cases without solution.
        col_a and col_b are never covered by the same row.
        col_c is only covered by rows which cover col_a OR col_b.
        Thus, to cover col_a and col_b, we would have to cover col_c twice.

        If col_a == col_b, col_b == col_c or col_a == col_c, 
        we get a grid with an empty column. So we don't have to 
        filter out those cases, since we just want a problem
        without a solution.
    """
    array = draw(exact_cover_problem())
    height, width = array.shape
    col_a = draw(integers(min_value=0, max_value=width-1))
    col_b = draw(integers(min_value=0, max_value=width-1))
    col_c = draw(integers(min_value=0, max_value=width-1))
    array[:, col_a] = array[:, col_a] * (1 - array[:, col_b])
    array[:, col_c] = array[:, col_a] & array[:, col_b]
    return array


@given(one_of(exact_cover_problem_with_empty_col(), exact_cover_problem_with_abc()))
def test_exact_cover_without_solution(array_data):
    rowcount = len(array_data)
    actual = get_exact_cover(array_data)
    assert actual.size == 0
