#include "munit.h"
#include "../src/sparse_matrix.h"


static MunitResult
test_make_simple_matrix(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 1;
  int col_count = 3;
  int array[] = {1, 1, 1};

  list l = create_sparse(row_count, col_count, array);
  munit_assert_not_null(l);

  return MUNIT_OK;
}

static MunitResult
test_check_details_of_simple_matrix(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 1;
  int col_count = 3;
  int array[] = {1, 1, 1};

  list l = create_sparse(row_count, col_count, array);

  munit_assert_ptr_not_equal(get_right(l), l);
  munit_assert_ptr_not_equal(get_right(get_right(l)), l);
  munit_assert_ptr_not_equal(get_right(get_right(get_right(l))), l);
  munit_assert_ptr_equal(get_right(get_right(get_right(get_right(l)))), l);

  for (list col_head = get_right(l); col_head != l; col_head = get_right(col_head)){
	  munit_assert_ptr_not_equal(get_down(col_head), col_head);
	  munit_assert_ptr_equal(get_down(get_down(col_head)), col_head);

	  munit_assert_int(col_head->data->data, ==, 1);
	  //munit_assert_int(get_down(col_head)->data->data, ==, 1);

  }

  return MUNIT_OK;
}

static MunitResult
test_check_details_empty_table(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 1;
  int col_count = 0;
  int array[] = {};

  list l = create_sparse(row_count, col_count, array);
  munit_assert_ptr_equal(l, get_right(l));

  return MUNIT_OK;
}


static MunitResult
test_choose_column_with_min_data(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 1;
  int col_count = 3;
  int array[] = {1, 1, 1};

  list l = create_sparse(row_count, col_count, array);

  list min_col = choose_column_with_min_data(l, 1);
  munit_assert_not_null(min_col);
  // We don't know which column we get but we know it's data value.
  munit_assert_int(min_col->data->data, ==, 1);

  return MUNIT_OK;
}

static MunitResult
test_choose_column_with_min_data_2(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 1;
  int col_count = 3;
  int array[] = {0, 1, 1};

  list l = create_sparse(row_count, col_count, array);

  list min_col = choose_column_with_min_data(l, 1);
  munit_assert_not_null(min_col);
  munit_assert_ptr_equal(min_col, get_right(l));
  munit_assert_int(min_col->data->data, ==, 0);

  return MUNIT_OK;
}

static MunitResult
test_choose_column_with_min_data_empty_table(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 1;
  int col_count = 0;
  int array[] = {};

  list l = create_sparse(row_count, col_count, array);

  list min_col = choose_column_with_min_data(l, 1);
  munit_assert_null(min_col);

  return MUNIT_OK;
}




static MunitTest test_suite_tests[] = {
  { (char*) "simple_matrix_gets_created", test_make_simple_matrix, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "simple_matrix_makes_sense", test_check_details_of_simple_matrix, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "empty_matrix_makes_sense", test_check_details_empty_table, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "column_with_min_data", test_choose_column_with_min_data, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "column_with_min_data_2", test_choose_column_with_min_data_2, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "column_with_min_data_empty_table", test_choose_column_with_min_data_empty_table, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { NULL, NULL, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL }
};


/* Now we'll actually declare the test suite.  You could do this in
 * the main function, or on the heap, or whatever you want. */
static const MunitSuite test_suite = {
  (char*) "my tests",
  test_suite_tests,
  NULL,
  1,
  MUNIT_SUITE_OPTION_NONE
};

/* This is only necessary for EXIT_SUCCESS and EXIT_FAILURE, which you
 * *should* be using but probably aren't (no, zero and non-zero don't
 * always mean success and failure).  I guess my point is that nothing
 * about µnit requires it. */
#include <stdlib.h>

int main(int argc, char* argv[MUNIT_ARRAY_PARAM(argc + 1)]) {
  /* Finally, we'll actually run our test suite!  That second argument
   * is the user_data parameter which will be passed either to the
   * test or (if provided) the fixture setup function. */
  return munit_suite_main(&test_suite, (void*) "µnit", argc, argv);
}
