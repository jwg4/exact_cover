import numpy as np


def cut(a):
    """ Reduces a problem by finding a column
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
