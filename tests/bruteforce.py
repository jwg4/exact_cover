"""
bruteforce algorithm to compute the expected solutions
and help write tests
"""

from itertools import chain, combinations

import numpy as np

# from the itertools module documentation
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def bruteforce(data):
    """
    Brute-force generator of all exact cover solutions
    """
    for subset in powerset(range(data.shape[0])):
        if np.all(data[list(subset)].sum(axis=0) == 1):
            yield subset
