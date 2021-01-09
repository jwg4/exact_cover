from setuptools import setup, Extension
import numpy

# define the extension module
deps_dir = "../src/"
src_dir = "./"
exact_cover_np = Extension('exact_cover_np',
                           sources=[src_dir + 'exact_cover_np.c',
                                    deps_dir + 'dlx.c',
                                    deps_dir + 'sparse_matrix.c',
                                    deps_dir + 'quad_linked_list.c'],
                           include_dirs=[deps_dir, numpy.get_include()])

# run the setup
setup(
    name = 'exact_cover_np',
    description = "Use Donald Knuth's Algorithm X to calculate an exact cover of a set.",
    url = ("http://github.com/jwg4/exact_cover_np"),
    version = "0.2",
    license = 'GPL v2 or above',
    author = 'Moy Easwaran',
    maintainer = 'jwg4',
    packages = ['sudoku_solver'],
    ext_modules = [exact_cover_np]
)


