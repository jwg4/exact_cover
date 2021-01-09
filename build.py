from setuptools import Extension

import numpy
import pytest


# define the extension module
deps_dir = "src/"
src_dir = "exact_cover/"
exact_cover = Extension('exact_cover',
                           sources=[src_dir + 'exact_cover_np.c',
                                    deps_dir + 'dlx.c',
                                    deps_dir + 'sparse_matrix.c',
                                    deps_dir + 'quad_linked_list.c'],
                           include_dirs=[deps_dir, numpy.get_include()])

def build(setup_kwargs):
    setup_kwargs.update(
        {
            "ext_modules": [exact_cover],
        }
    )


def test():
    pytest.main()

