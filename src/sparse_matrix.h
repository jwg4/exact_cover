#ifndef _SPARSE_MATRIX_H_
#define _SPARSE_MATRIX_H_

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include "quad_linked_list.h"

list create_sparse (int, int, int []);
list create_headers_list(int);
list populate_sparse_matrix(list, int, int, int []);
list choose_column_with_min_data(list, int);
void print_sparse_matrix_transpose(list, int);
void print_column(list, int);

#endif

