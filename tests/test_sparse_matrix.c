#include "debug.h"
#include <assert.h>

#include "sparse_matrix.h"


#define HSIZE 9
#define VSIZE 15
#define ARRAYSIZE(x)  (sizeof(x)/sizeof(*(x)))
 
void read_csv(char filename[], int rows, int cols, int array[rows*cols]) {
    FILE *file = fopen(filename, "r");
    int i, j;
    char buffer[cols*5], *ptr;
    for ( i = 0; fgets(buffer, sizeof buffer, file); ++i )
       for ( j = 0, ptr = buffer; j < cols; ++j, ++ptr )
          array[(i*cols)+j] = (int)strtol(ptr, &ptr, 10);
    fclose(file);
}

void print_array(int rows, int columns, int array[rows*columns]) {
    int j, k;
    for (j = 0; j < rows; ++j) {
       for ( k = 0; k < columns; ++k )
          printf("%d,", array[(j*columns)+k]);
       printf("\b\n");
    }
}


int main(void)
{
    // char filename[] = "sudo2.csv";
    // int matrix[VSIZE][HSIZE];
    // read_csv(filename, matrix);

    int matrix[VSIZE*HSIZE] =
        {
 // sums: 8, 9, 8,11, 7,10, 8, 5, 5
          0, 1, 0, 1, 0, 0, 0, 1, 0,
          1, 1, 1, 1, 1, 1, 1, 0, 1,
          1, 0, 0, 1, 0, 1, 1, 1, 0,
          1, 0, 1, 1, 0, 1, 1, 1, 0,
          1, 1, 1, 1, 0, 0, 0, 1, 1,
          1, 0, 1, 1, 1, 0, 1, 1, 1,
          0, 1, 0, 1, 1, 1, 1, 0, 0,
          0, 1, 0, 0, 1, 0, 0, 0, 0,
          1, 1, 1, 0, 0, 0, 1, 0, 0,
          0, 1, 1, 1, 1, 1, 1, 0, 1,
          1, 1, 1, 0, 0, 1, 1, 0, 0,
          0, 1, 0, 1, 1, 1, 0, 0, 1,
          0, 0, 0, 1, 1, 1, 0, 0, 0,
          0, 0, 0, 0, 0, 1, 0, 0, 0,
          1, 0, 1, 1, 0, 1, 0, 0, 0
        };

    list sparse_matrix = create_sparse(VSIZE, HSIZE, matrix);
    list column;

    DEBUG_PRINT(1, "Check choosing column with min data.\n");
    column = choose_column_with_min_data(sparse_matrix, VSIZE + 1); // VSIZE + 1 is an arbitrary number >= min
    // print_sparse_matrix_transpose(sparse_matrix, VSIZE);
    // printf("----------\n");
    assert(get_data(column)->data == 5);                            // should have sum for 2nd-last column

    DEBUG_PRINT(1, "Check covering first column.\n");
    column = get_right(sparse_matrix);
    cover_column(column);
    // new column sums: 5,1,5,5,5,2,1,2
    // print_sparse_matrix_transpose(sparse_matrix, VSIZE);
    // printf("----------\n");
    assert(get_data(get_right(sparse_matrix))->data == 5);              // sum for first column
    assert(get_data(get_left(sparse_matrix))->data == 2);               // sum for last column
    assert(get_data(get_right(get_right(sparse_matrix)))->data == 1);   // sum for second column
    assert(get_data(get_left(get_left(sparse_matrix)))->data == 1);     // sum for 2nd-last column

    DEBUG_PRINT(1, "Check uncovering first column.\n");
    uncover_column(column);
    // print_sparse_matrix_transpose(sparse_matrix, VSIZE);
    assert(get_data(get_right(sparse_matrix))->data == 8);              // sum for first column
    assert(get_data(get_left(sparse_matrix))->data == 5);               // sum for last column
    assert(get_data(get_right(get_right(sparse_matrix)))->data == 9);   // sum for second column
    assert(get_data(get_left(get_left(sparse_matrix)))->data == 5);     // sum for 2nd-last column

    // printf("----------\n");
    // translate_into_constraint_matrix(matrix, constraints);
    // translate_into_sparse_constraints(constraints, sparse);
    // print_array(VSIZE, HSIZE, matrix);
    destroy_entire_grid(sparse_matrix);
    DEBUG_PRINT(0, "Passed all tests!\n");
    return 0;
}



