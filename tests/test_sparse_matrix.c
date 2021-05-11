#include <assert.h>

#include "munit.h"

#include "sparse_matrix.h"


#define HSIZE 9
#define VSIZE 15
 

static MunitResult test_choose_column_with_min_data(const MunitParameter params[], void* data)
{
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

    // The min value is guaranteed to be less than VSIZE + 1
    column = choose_column_with_min_data(sparse_matrix, VSIZE + 1);
    munit_assert_int(get_data(column)->data, ==, 5);

    return MUNIT_OK;
}

static MunitResult test_matrix(const MunitParameter params[], void* data)
{
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

    column = get_right(sparse_matrix);
    cover_column(column);
    munit_assert_int(get_data(get_right(sparse_matrix))->data, ==, 5);              // sum for first column
    munit_assert_int(get_data(get_left(sparse_matrix))->data, ==, 2);               // sum for last column
    munit_assert_int(get_data(get_right(get_right(sparse_matrix)))->data, ==, 1);   // sum for second column
    munit_assert_int(get_data(get_left(get_left(sparse_matrix)))->data, ==, 1);     // sum for 2nd-last column

    uncover_column(column);
    munit_assert_int(get_data(get_right(sparse_matrix))->data, ==, 8);              // sum for first column
    munit_assert_int(get_data(get_left(sparse_matrix))->data, ==, 5);               // sum for last column
    munit_assert_int(get_data(get_right(get_right(sparse_matrix)))->data, ==, 9);   // sum for second column
    munit_assert_int(get_data(get_left(get_left(sparse_matrix)))->data, ==, 5);     // sum for 2nd-last column

    destroy_entire_grid(sparse_matrix);
    return MUNIT_OK;
}

static MunitTest test_suite_tests[] = {
  { (char*) "test_covering_and_uncovering", test_matrix, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "test_choose_column_with_min_data", test_choose_column_with_min_data, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { NULL, NULL, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL }
};


static const MunitSuite test_suite = {
  (char*) "test_sparse_matrix",
  test_suite_tests,
  NULL,
  1,
  MUNIT_SUITE_OPTION_NONE
};


int main(int argc, char* argv[MUNIT_ARRAY_PARAM(argc + 1)]) {
  return munit_suite_main(&test_suite, (void*) "µnit", argc, argv);
}
