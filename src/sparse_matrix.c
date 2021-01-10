#include "sparse_matrix.h"


/*
 *  Given a 2-dimensional matrix represented as a single array,
 *      return a sparse representation of it.
 *  This will be quad-linked-list as follows:
 *
 *      <- L <-> C_1 <-> C_2 <-> ... <-> C_n ->
 *  Each C_i is a circular (vertical) list with nodes representing its
 *  non-zero entries.  Each node points to its nearest non-zero left-
 *  and right-neighbours.
 *
 *  For details please see either Knuth's paper 
 *  <http://arxiv.org/pdf/cs/0011047v1>.
 *  or this wikipedia page:
 *  <https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X>
 */


list create_sparse (int row_count, int col_count, int matrix[]) {
    list sparse_matrix = create_headers_list(col_count);
    if (not_empty(sparse_matrix))
        sparse_matrix = populate_sparse_matrix(sparse_matrix, row_count, col_count, matrix);
    return sparse_matrix;
}

list create_headers_list(int col_count) {
    node_ptr new_node;
    list column_header, sparse_matrix = NULL;
    int col_num;

    sparse_matrix = create_node(create_data(0, NULL));
    if (not_empty(sparse_matrix))
        for (col_num = 0, column_header = sparse_matrix; col_num < col_count; ++col_num) {
            new_node = create_node(create_data(0, NULL));
            if (is_empty(new_node)) {
                // Uh oh.  Couldn't create a new node.  We need to clean up and abort.
                destroy_entire_grid(sparse_matrix);
                sparse_matrix = NULL;
                break;
            } else
                column_header = insert_horizontally_after(column_header, new_node);
        }

    return sparse_matrix;
}

// Assumptions:
// sparse_matrix is not NULL
list populate_sparse_matrix(list sparse_matrix, int row_count, int col_count, int matrix[]) {
    int row_num, col_num;
    list col, row_list;
    node_ptr new_node;

    for (row_num = 0; row_num < row_count; ++row_num) {
        row_list = create_empty_list();
        for (col_num = 0, col = get_right(sparse_matrix); col_num < col_count; ++col_num, col = get_right(col)) {
            if (matrix[(row_num*col_count)+col_num] != 0) {
                new_node = create_node(create_data(row_num, col));
                // If we can't create a new node, abort!
                if (is_empty(new_node)) {
                    destroy_entire_grid(sparse_matrix);   // ABORT!
                    return NULL;
                }
                row_list = insert_horizontally_after(row_list, new_node);
                insert_vertically_after(get_up(col), new_node);
                get_data(col)->data += 1;
            }
        }
    }
    return sparse_matrix;
}
        
list choose_column_with_min_data(list sparse_matrix, int max) {
    int min = max;
    list col = sparse_matrix, min_col = NULL;
    while ((col = get_right(col)) != sparse_matrix) {
        if (get_data(col)->data < min || (get_data(col)->data == min && min_col == NULL)) {
            min_col = col;
            min = get_data(col)->data;
        }
    }
    return min_col;
}

void print_sparse_matrix_transpose(list sparse_matrix, int row_count) {
    list col = sparse_matrix;
    while ((col = get_right(col)) != sparse_matrix) {
        print_column(col, row_count);
    }
}

void print_column(list col, int row_count) {
    node_ptr row;
    int row_num;
    printf("%d:", get_data(col)->data);
    row = col;
    for (row_num = 0; (row = get_down(row)) != col; ) {
        for (; row_num < get_data(row)->data; ++row_num)
            printf("0,");
        printf("1,"), ++row_num;
    }
    for (; row_num < row_count; ++row_num) printf("0,");
    putchar('\n');
}


