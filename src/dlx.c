#include "dlx.h"


/*
 * This program uses Donald Knuth's Algorithm X to find exact covers
 * of sets.  For details on Algorithm X please see either
 * <https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X>
 * or
 * <http://arxiv.org/pdf/cs/0011047v1>.
 *
 * Specifically, we use the Knuth/Hitotsumatsu/Noshita method of
 * Dancing Links for efficient backtracking.  Please see Knuth's
 * paper above for details.
 */


int search(list sparse_matrix, int k, int max, int *solution) {
    list col, row, next;
    int result = 0;

    // Base cases:
    // 1. There are no columns left; we've found a solution.
    if (get_right(sparse_matrix) == sparse_matrix) return k;
    // 2. There's a column with only zeros. This branch of the search
    //    tree has no solutions and we need to backtrack.
    col = choose_column_with_min_data(sparse_matrix, max);
    if (get_data(col)->data == 0) return 0;

    // Main algorithm:
    cover_column(col);
    for (row = col; (row = get_down(row)) != col; ) {
        solution[k] = get_data(row)->data;  // save the row number
        for (next = row; (next = get_right(next)) != row; )
            cover_column(get_data(next)->list_data);
        result = search(sparse_matrix, k+1, max, solution);
        // If result > 0 we're done, but we should still clean up.
        for (next = row; (next = get_left(next)) != row; )
            uncover_column(get_data(next)->list_data);
        if (result > 0) break;
    }
    uncover_column(col);
    return result;
}

int count(list sparse_matrix, int k, int max, int *solution) {
    list col, row, next;
    int result = 0;
    int c = 0;

    // Base cases:
    // 1. There are no columns left; we've found a solution.
    if (get_right(sparse_matrix) == sparse_matrix) return 1;
    // 2. There's a column with only zeros. This branch of the search
    //    tree has no solutions and we need to backtrack.
    col = choose_column_with_min_data(sparse_matrix, max);
    if (get_data(col)->data == 0) return 0;

    // Main algorithm:
    cover_column(col);
    for (row = col; (row = get_down(row)) != col; ) {
        solution[k] = get_data(row)->data;  // save the row number
        for (next = row; (next = get_right(next)) != row; )
            cover_column(get_data(next)->list_data);
        result = count(sparse_matrix, k+1, max, solution);
        c += result;
        // If result > 0 we're done, but we should still clean up.
        for (next = row; (next = get_left(next)) != row; )
            uncover_column(get_data(next)->list_data);
    }
    uncover_column(col);
    return c;
}

int dlx_get_exact_cover(int rows, int cols, char matrix[], int *solution) {
    list sparse_matrix;
    int solution_length;

    sparse_matrix = create_sparse(rows, cols, matrix);
    solution_length = search(sparse_matrix, 0, rows, solution);
    destroy_entire_grid(sparse_matrix);

    while (rows > solution_length) {
        solution[--rows] = 0;  // Zero out everything above position i.  Caller
                               // can use this to determine if there is a solution.
    };

    return solution_length;
}

int dlx_get_solution_count(int rows, int cols, char matrix[]) {
    list sparse_matrix;
    // int solution_length;
    int solution_count = 0;
    int *solution = malloc(rows * sizeof(*solution));

    sparse_matrix = create_sparse(rows, cols, matrix);
    solution_count = count(sparse_matrix, 0, rows, solution);
    destroy_entire_grid(sparse_matrix);

    free(solution);
    return solution_count;
}

int enumerate(list sparse_matrix, int k, int max, int *solution, int *solutions, int solution_size) {
    list col, row, next;
    int result = 0;
    int c = 0;

    // Base cases:
    // 0. we have run out of space
    if (max < 1) {
        return 0;
    }
    // 1. There are no columns left; we've found a solution.
    if (get_right(sparse_matrix) == sparse_matrix) {
	for (int i=0; i < k; i++) {
            solutions[i] = solution[i];
	}
	for (int i=k; i < solution_size; i++) {
	    solutions[i] = 0;
	}
	return 1;
    }
    // 2. There's a column with only zeros. This branch of the search
    //    tree has no solutions and we need to backtrack.
    col = choose_column_with_min_data(sparse_matrix, solution_size);
    if (get_data(col)->data == 0) return 0;

    // Main algorithm:
    cover_column(col);
    for (row = col; (row = get_down(row)) != col; ) {
        solution[k] = get_data(row)->data;  // save the row number
        for (next = row; (next = get_right(next)) != row; )
            cover_column(get_data(next)->list_data);
        result = enumerate(sparse_matrix, k+1, max - c, solution, solutions + c * solution_size, solution_size);
        c += result;
        for (next = row; (next = get_left(next)) != row; )
            uncover_column(get_data(next)->list_data);
    }
    uncover_column(col);
    return c;
}

int dlx_get_all_solutions(int rows, int cols, char matrix[], int max_count, int* solutions) {
    list sparse_matrix;
    int solution_count = 0;
    int *solution = malloc(rows * sizeof(*solution));

    sparse_matrix = create_sparse(rows, cols, matrix);

    int count = enumerate(sparse_matrix, 0, max_count, solution, solutions, rows);

    destroy_entire_grid(sparse_matrix);

    free(solution);
    return count;

}
