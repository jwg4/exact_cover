#include "munit.h"
#include "../src/sparse_matrix.h"


/* Tests are functions that return void, and take a single void*
 * parameter.  We'll get to what that parameter is later. */
static MunitResult
test_get_simple_result(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 1;
  int col_count = 1;
  int array[] = {1, 1, 1};

  list l = create_sparse(row_count, col_count, array);
  munit_assert_not_null(l);

  return MUNIT_OK;
}


/* Creating a test suite is pretty simple.  First, you'll need an
 * array of tests: */
static MunitTest test_suite_tests[] = {
  {
    (char*) "Very simple exact cover problem",
    test_get_simple_result,
    NULL,
    NULL,
    MUNIT_TEST_OPTION_NONE,
    NULL
  },
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
