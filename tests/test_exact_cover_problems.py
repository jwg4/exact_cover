import numpy as np

from hypothesis import given, strategies
from hypothesis.strategies import integers, lists, booleans

from exact_cover_np import get_exact_cover


@given(
    integers(min_value=0, max_value=10).flatmap(
        lambda n: lists(
            lists(booleans(), min_size=n, max_size=n), min_size=1, max_size=30
        )
    )
)
def test_exact_cover(array_data):
    rowcount = len(array_data)
    data = np.array(array_data, dtype=np.int32)
    actual = get_exact_cover(data)
    assert actual.size <= rowcount
    assert all(actual < rowcount)
