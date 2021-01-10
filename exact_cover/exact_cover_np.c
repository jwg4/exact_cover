#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <numpy/arrayobject.h>
#include <math.h>

#include <stdlib.h>
#include <stdbool.h>

#include "dlx.h"

#define _EXACT_COVER_NP_DIM_ERROR_ "get_exact_cover(...) needs a 2-dimensional (m x n) matrix."
#define _EXACT_COVER_NP_TYPE_ERROR_ "get_exact_cover(...) needs a matrix of dtype 'int32'."


static bool not_2d_int_array(PyArrayObject *);
static PyObject* get_exact_cover(PyObject*, PyObject*);


static bool not_2d_int_array(PyArrayObject *in_array) {
    if (PyArray_NDIM(in_array) != 2) {
        PyErr_SetString(PyExc_ValueError, _EXACT_COVER_NP_DIM_ERROR_);
        return 1;
    }
    if (PyArray_TYPE(in_array) != NPY_INT32) { 
        PyErr_SetString(PyExc_TypeError, _EXACT_COVER_NP_TYPE_ERROR_);
        return 1;
    }
    return 0;
}

static PyObject* get_exact_cover(PyObject* self, PyObject* args)
{

    PyArrayObject *in_array;
    PyObject      *out_array;
    npy_intp      *dims;
    int           *in_array_data, rows, cols, result;

    /*  Parse single numpy array argument */
    if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &in_array)) return NULL;

    /*  Construct the output array, like the input array */
    out_array = PyArray_NewLikeArray(in_array, NPY_ANYORDER, NULL, 0);
    if (out_array == NULL) return NULL;

    /*  Check that we got a 2-dimensional array of dtype='int32'. */
    if (not_2d_int_array(in_array)) return NULL;

    /*  Get the data. */
    dims = PyArray_DIMS(in_array);
    rows = (int) dims[0],  cols = (int) dims[1];
    in_array_data = (int*) PyArray_DATA(in_array);

    /*  Calculate the exact cover. */
    int nd = 1, *solution = malloc(rows * sizeof(*solution));
    result = dlx_get_exact_cover(rows, cols, in_array_data, solution);

    dims = malloc(nd * sizeof(*dims));
    dims[0] = result;
    PyObject *return_solution = PyArray_SimpleNewFromData(nd, dims, NPY_INT32, (void*)solution);
    Py_INCREF(return_solution);
    return return_solution;
}

static PyMethodDef ExactCoverMethods[] =
{
     {"get_exact_cover", get_exact_cover, METH_VARARGS, "Calculate an exact cover of a set."},
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
	"exact_cover",
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
PyInit_exact_cover(void)
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


