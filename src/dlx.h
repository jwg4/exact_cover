#ifndef _DLX_H_
#define _DLX_H_

#include "quad_linked_list.h"
#include "sparse_matrix.h"

int search(list, int, int, int *);
int dlx_get_exact_cover(int, int, char [], int*);
int dlx_get_solution_count(int, int, char []);
int dlx_get_all_solutions(int, int, char [], int, int*);

#endif
