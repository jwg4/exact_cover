from distutils.core import setup, Extension
import numpy

# define the extension module
deps_dir = "/home/moy/build/sudoku/src/"
src_dir = "/home/moy/build/sudoku/exact_cover_np/"
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
    url = ("https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X"),
    version = "0.1",
    license = 'GPL v2 or above',
    author = 'Moy Easwaran',
    ext_modules = [exact_cover_np]
)


