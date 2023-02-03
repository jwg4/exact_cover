import logging

from collections import deque

import numpy as np

from .error import NoSolution, CannotSplitFurther
from .io import DTYPE_FOR_ARRAY

logger = logging.getLogger(__name__)


def cut(a):
    """Reduces a problem by finding a column
    which can only be covered in one way,
    and removing it along with any row which
    touches it.

    If it can't find such a row, it raises.
    """
    sq = (np.sum(a, 0) == 1).nonzero()[0][0]
    shape = a[a[:, sq] == 1, :]
    logger.debug(shape.nonzero())
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
        logger.debug(b.shape)
        a = b


def create_numpy_array(a):
    """
    >>> create_numpy_array([[0, 1], [1, 0]])
    array([[False,  True],
           [ True, False]])
    """
    return np.array(a, dtype=DTYPE_FOR_ARRAY)


def split_problem(a, n):
    """
    Create several subproblems from a single problem.
    """
    queue = deque([a])
    while len(queue) < n:
        logger.debug("Length of queue %s, splitting a problem" % (len(queue),))
        try:
            to_expand = queue.popleft()
        except IndexError:
            raise NoSolution
        try:
            for sub in _split_problem_once(to_expand):
                queue.append(sub)
        except NoSolution:
            continue
    yield from queue


def _split_problem_once(a):
    colsums = a.sum(axis=0)
    if min(colsums) < 1:
        logger.debug("skipping %s because it doesn't have a solution", (colsums,))
        raise NoSolution
    m = np.argmax(colsums)
    x = a[:, m]
    if np.sum(x) < 2:
        raise CannotSplitFurther
    k = a.shape[0]
    for i in range(0, k):
        if a[i, m]:
            aa = a.copy()
            # Zero out all the rows with a 1 in column x, EXCEPT row i.
            aa[(x == 1) & ~np.identity(k, bool)[i], :] = 0
            yield aa


def is_solution(solution, problem):
    if len(solution) == 0:
        logger.debug("No rows in solution.")
        return False
    if len(solution) != len(set(solution)):
        logger.debug("There are repeated row indices in the solution.")
        return False
    try:
        cover = problem[solution, :]
    except IndexError:
        logger.debug("There are invalid row indices in the solution.")
        return False
    rowsums = np.sum(cover, axis=1)
    if min(rowsums) < 1:
        logger.debug("There are redundant (empty) rows in the solution.")
        return False
    count = np.sum(cover, axis=0)
    return min(count) == max(count) == 1
