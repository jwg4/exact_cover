import numpy as np

DTYPE_FOR_ARRAY = np.bool_


def load_problem(filename):
    return np.array(np.genfromtxt(filename), dtype=DTYPE_FOR_ARRAY)


def save_problem(filename, array):
    np.savetxt(filename, np.array(array, dtype=np.int8))
