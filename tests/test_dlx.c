#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "debug.h"
#include "dlx.h"
#include "munit.h"

#define VSIZE 729
#define HSIZE 324


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

static MunitResult
test_simple_example(const MunitParameter params[], void* data) {
    int matrix[6*7] =  // Knuth's example
            {
              0, 0, 1, 0, 1, 1, 0,
              1, 0, 0, 1, 0, 0, 1,
              0, 1, 1, 0, 0, 1, 0,
              1, 0, 0, 1, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 1,
              0, 0, 0, 1, 1, 0, 1
            };

    int *solution = malloc(VSIZE * sizeof(*solution));
    int result = dlx_get_exact_cover(6,7,matrix,solution);
    munit_assert(result == 3);
    munit_assert(solution[0] == 3);
    munit_assert(solution[1] == 0);
    munit_assert(solution[2] == 4);

    return MUNIT_OK;
}


static MunitTest test_suite_tests[] = {
  { (char*) "example_from_Knuth_paper", test_simple_example, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { NULL, NULL, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL }
};


static const MunitSuite test_suite = {
  (char*) "legacy_dlx_tests",
  test_suite_tests,
  NULL,
  1,
  MUNIT_SUITE_OPTION_NONE
};

int main(int argc, char* argv[MUNIT_ARRAY_PARAM(argc + 1)]) {

    int *solution = malloc(VSIZE * sizeof(*solution));
    int matrix2[6*7] =
            {
              1, 0, 1, 1, 1, 1, 1,
              1, 0, 0, 1, 0, 0, 1,
              0, 1, 1, 0, 0, 1, 0,
              1, 0, 0, 1, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 1,
              0, 0, 0, 1, 1, 0, 1
            };
    int result = dlx_get_exact_cover(6,7,matrix2,solution);
    // sparse_matrix = create_sparse(6, 7, matrix2);
    // result = search(sparse_matrix, 0, 6, solution);
    assert(result == 0);
    assert((solution[0] == 0) && (solution[1] == 0));

    int matrix3[9*9] =
        {
          1, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 1, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 1, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 1, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 1, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 1, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 1, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 1, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 1
        };
    result = dlx_get_exact_cover(9,9,matrix3,solution);
    assert(result == 9);
    assert((solution[0] != 0) || (solution[1] != 0));
    // sparse_matrix = create_sparse(9, 9, matrix3);
    // result = search(sparse_matrix, 0, 9, solution);

    int matrix4[64*64];
    char filename[] = "tests/con4.csv";
    read_csv(filename, 64, 64, matrix4);
    result = dlx_get_exact_cover(64,64,matrix4,solution);
    assert(result == 16);
    assert((solution[0] == 0) && (solution[1] == 26) && (solution[2] == 37) && (solution[3] == 23) && (solution[15] == 57));
    // printf("%d\n", result);
    // sparse_matrix = create_sparse(64, 64, matrix4);
    // result = search(sparse_matrix, 0, 64, solution);
    // int i;
    // for (i = 0; i < result; ++i) printf("%d, ", solution[i]);
    // printf("\n");

    int matrix5[VSIZE*HSIZE];
    char filename2[] = "tests/con2.csv";
    read_csv(filename2, VSIZE, HSIZE, matrix5);
    result = dlx_get_exact_cover(VSIZE,HSIZE,matrix5,solution);
    assert(result == 81);
    assert((solution[0] == 11) && (solution[1] == 22) && (solution[2] == 28) && (solution[3] == 44) && (solution[80] == 725));
    // sparse_matrix = create_sparse(VSIZE, HSIZE, matrix5);
    // result = search(sparse_matrix, 0, VSIZE, solution);
    // int i;
    // for (i = 0; i < 81; ++i) printf("%d, ", solution[i]);
    // printf("\n");
    // printf("%lu\n", sizeof(solution));

    DEBUG_PRINT(0, "Passed all tests!\n");
    free(solution);

    return munit_suite_main(&test_suite, (void*) "µnit", argc, argv);

    return 0;
}


