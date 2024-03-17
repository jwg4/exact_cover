#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <numpy/arrayobject.h>
#include <math.h>

#include <stdlib.h>
#include <stdbool.h>

#include "dlx.h"

#define _EXACT_COVER_NP_DIM_ERROR_ "get_exact_cover(...) needs a 2-dimensional (m x n) matrix."
#define _EXACT_COVER_NP_TYPE_ERROR_ "get_exact_cover(...) needs a matrix of dtype 'bool'."
#define _EXACT_COVER_NP_ORDER_ERROR_ "get_exact_cover(...) needs a matrix which is 'C contiguous'"


static bool not_2d_int_array(PyArrayObject *);
static PyObject* get_exact_cover(PyObject*, PyObject*);
static PyObject* get_solution_count(PyObject*, PyObject*);


static bool not_2d_int_array(PyArrayObject *in_array) {
    if (PyArray_NDIM(in_array) != 2) {
        PyErr_SetString(PyExc_ValueError, _EXACT_COVER_NP_DIM_ERROR_);
        return 1;
    }
    if (PyArray_TYPE(in_array) != NPY_BOOL) {
        PyErr_SetString(PyExc_TypeError, _EXACT_COVER_NP_TYPE_ERROR_);
        return 1;
    }
    if (!(PyArray_FLAGS(in_array) & NPY_ARRAY_C_CONTIGUOUS)) {
        PyErr_SetString(PyExc_TypeError, _EXACT_COVER_NP_ORDER_ERROR_);
        return 1;
    }
    return 0;
}

static PyObject* get_exact_cover(PyObject* self, PyObject* args)
{

    PyArrayObject *in_array;
    npy_intp      *dims;
    char          *in_array_data;
    int           rows, cols, result;

    /*  Parse single numpy array argument */
    if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &in_array)) return NULL;

    /*  Check that we got a 2-dimensional array of dtype='bool'. */
    if (not_2d_int_array(in_array)) return NULL;

    /*  Get the data. */
    dims = PyArray_DIMS(in_array);
    rows = (int) dims[0],  cols = (int) dims[1];
    in_array_data = (char*) PyArray_DATA(in_array);

    /*  Calculate the exact cover. */
    int nd = 1, *solution = malloc(rows * sizeof(*solution));
    result = dlx_get_exact_cover(rows, cols, in_array_data, solution);

    dims = malloc(nd * sizeof(*dims));
    dims[0] = result;
    PyObject *return_solution = PyArray_SimpleNewFromData(nd, dims, NPY_INT32, (void*)solution);
    PyArray_ENABLEFLAGS((PyArrayObject*) return_solution, NPY_ARRAY_OWNDATA);
    free(dims);
    return return_solution;
}

static PyObject* get_all_solutions(PyObject* self, PyObject* args)
{

    PyArrayObject *in_array;
    npy_intp      *dims;
    char          *in_array_data;
    int           rows, cols, result;
    int           max_count;
    int           *solutions;

    /*  Parse single numpy array argument */
    if (!PyArg_ParseTuple(args, "O!I", &PyArray_Type, &in_array, &max_count)) return NULL;

    /*  Check that we got a 2-dimensional array of dtype='bool'. */
    if (not_2d_int_array(in_array)) return NULL;
    
    /*  Get the data. */
    dims = PyArray_DIMS(in_array);
    rows = (int) dims[0],  cols = (int) dims[1];
    in_array_data = (char*) PyArray_DATA(in_array);

    /*  Calculate the exact cover. */
    int nd = 2;
    solutions = malloc(max_count * rows * sizeof(int));
    result = dlx_get_all_solutions(rows, cols, in_array_data, max_count, solutions);

    dims = malloc(nd * sizeof(*dims));
    dims[0] = result;
    dims[1] = rows;
    PyObject *return_solution = PyArray_SimpleNewFromData(nd, dims, NPY_INT32, (void*)solutions);
    PyArray_ENABLEFLAGS((PyArrayObject*) return_solution, NPY_ARRAY_OWNDATA);
    free(dims);
    return return_solution;
}

static PyObject* get_solution_count(PyObject* self, PyObject* args)
{

    PyArrayObject *in_array;
    npy_intp      *dims;
    char          *in_array_data;
    int           rows, cols, result;

    /*  Parse single numpy array argument */
    if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &in_array)) return NULL;

    /*  Check that we got a 2-dimensional array of dtype='bool'. */
    if (not_2d_int_array(in_array)) return NULL;

    /*  Get the data. */
    dims = PyArray_DIMS(in_array);
    rows = (int) dims[0],  cols = (int) dims[1];
    in_array_data = (char*) PyArray_DATA(in_array);

    /*  Get the solution count. */
    result = dlx_get_solution_count(rows, cols, in_array_data);

    return PyLong_FromLong(result);
}

static PyMethodDef ExactCoverMethods[] =
{
     {"get_exact_cover", get_exact_cover, METH_VARARGS, "Calculate an exact cover of a set."},
     {"get_solution_count", get_solution_count, METH_VARARGS, "Get the number of distinct exact cover solutions."},
     {"get_all_solutions", get_all_solutions, METH_VARARGS, "Get an array of all solutions."},
     {NULL, NULL, 0, NULL}
};

struct module_state {
	PyObject *error;
};

static int exact_cover_traverse(PyObject *m, visitproc visit, void *arg) {
	Py_VISIT(((struct module_state*)PyModule_GetState(m))->error);
	return 0;
}

static int exact_cover_clear(PyObject *m) {
	Py_CLEAR(((struct module_state*)PyModule_GetState(m))->error);
	return 0;
}

static struct PyModuleDef moduledef = {
	PyModuleDef_HEAD_INIT,
	"exact_cover_impl",
	NULL,
	sizeof(struct module_state),
	ExactCoverMethods,
	NULL,
	exact_cover_traverse,
	exact_cover_clear,
	NULL
};


/* module initialization */
PyMODINIT_FUNC
PyInit_exact_cover_impl(void)
{
     PyObject *module = PyModule_Create(&moduledef);

     if (module == NULL)
	 return NULL;

     struct module_state *st = (struct module_state*)PyModule_GetState(module);
     st->error = PyErr_NewException("exact_cover.Error", NULL, NULL);
     if (st->error == NULL) {
	     Py_DECREF(module);
	     return NULL;
     }
     /* IMPORTANT: this must be called */
     import_array();

     return module;
}
