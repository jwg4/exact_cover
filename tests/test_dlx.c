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


static MunitResult
test_simple_negative_example(const MunitParameter params[], void* data) {
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
    munit_assert(result == 0);
    munit_assert((solution[0] == 0) && (solution[1] == 0));

    return MUNIT_OK;
}

static MunitResult
test_very_simple_large_example(const MunitParameter params[], void* data) {
    int result;
    int *solution = malloc(VSIZE * sizeof(*solution));
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
    munit_assert(result == 9);
    munit_assert((solution[0] != 0) || (solution[1] != 0));

    return MUNIT_OK;
}

static MunitResult
test_large_example_from_csv(const MunitParameter params[], void* data) {
    int result;
    int *solution = malloc(VSIZE * sizeof(*solution));

    int matrix4[64*64];
    char filename[] = "tests/con4.csv";
    read_csv(filename, 64, 64, matrix4);
    result = dlx_get_exact_cover(64,64,matrix4,solution);
    munit_assert(result == 16);
    munit_assert(solution[0] == 0);
    munit_assert(solution[1] == 26);
    munit_assert(solution[2] == 37);
    munit_assert(solution[3] == 23);
    munit_assert(solution[15] == 57);

    return MUNIT_OK;
}

static MunitResult
test_large_example_from_csv_2(const MunitParameter params[], void* data) {
    int result;
    int *solution = malloc(VSIZE * sizeof(*solution));

    int matrix5[VSIZE*HSIZE];
    char filename2[] = "tests/con2.csv";
    read_csv(filename2, VSIZE, HSIZE, matrix5);
    result = dlx_get_exact_cover(VSIZE,HSIZE,matrix5,solution);
    munit_assert(result == 81);
    munit_assert(solution[0] == 11);
    munit_assert(solution[1] == 22);
    munit_assert(solution[2] == 28);
    munit_assert(solution[3] == 44);
    munit_assert(solution[80] == 725);

    return MUNIT_OK;
}

static MunitTest test_suite_tests[] = {
  { (char*) "example_from_Knuth_paper", test_simple_example, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "negative_example_from_Knuth_paper", test_simple_negative_example, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "trivial_example", test_very_simple_large_example, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "large_example_from_csv", test_large_example_from_csv, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "large_example_from_csv_2", test_large_example_from_csv_2, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { NULL, NULL, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL }
};


static const MunitSuite test_suite = {
  (char*) "legacy_dlx_tests/",
  test_suite_tests,
  NULL,
  1,
  MUNIT_SUITE_OPTION_NONE
};

int main(int argc, char* argv[MUNIT_ARRAY_PARAM(argc + 1)]) {
    return munit_suite_main(&test_suite, (void*) "µnit", argc, argv);
}


