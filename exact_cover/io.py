import numpy as np


def load_problem(filename):
    return np.genfromtxt(filename, dtype=np.int32)


def save_problem(filename, array):
    np.savetxt(filename, array)
