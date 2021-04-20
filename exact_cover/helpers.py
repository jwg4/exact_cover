import numpy as np

from .error import NoSolution


def cut(a):
    """Reduces a problem by finding a column
    which can only be covered in one way,
    and removing it along with any row which
    touches it.

    If it can't find such a row, it raises.
    """
    sq = (np.sum(a, 0) == 1).nonzero()[0][0]
    shape = a[a[:, sq] == 1, :]
    print(shape.nonzero())
    d = a[:, shape[0] != 1]
    dd = d[np.sum(d, 1) == 4, :]
    return dd


def reduce(a):
    """
    Call cut() on an array as many times as is possible.
    """
    while True:
        try:
            b = cut(a)
        except Exception:
            return a
        print(b.shape)
        a = b


def create_numpy_array(a):
    """
    >>> create_numpy_array([[0, 1], [1, 0]])
    numpy.array([[0, 1], [1, 0]])
    """
    return np.array(a)


def split_problem(a, n):
    """
    Create several subproblems from a single problem.
    """
    m = np.argmax(a.sum(axis=0))
    x = a[:, m]
    if not a[x == 1].any():
        raise NoSolution
    for v in a[x == 1]:
        yield np.concatenate((a[x == 0], [v]))
