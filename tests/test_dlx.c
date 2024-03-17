#include "munit.h"
#include "../src/dlx.h"


static MunitResult
test_get_one_row_result(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 1;
  int col_count = 3;
  char array[] = {1, 1, 1};
  int solution[] = {0};

  int length = dlx_get_exact_cover(row_count, col_count, array, solution);
  munit_assert(length == 1);

  return MUNIT_OK;
}

static MunitResult
test_get_two_row_result(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 2;
  int col_count = 3;
  char array[] = {1, 0, 0, 0, 1, 1};
  int solution[] = {0, 0};

  int length = dlx_get_exact_cover(row_count, col_count, array, solution);
  munit_assert(length == 2);
  munit_assert_int(solution[0], ==, 0);
  munit_assert_int(solution[1], ==, 1);

  return MUNIT_OK;
}


static MunitResult
test_get_two_row_all_solutions(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 4;
  int col_count = 3;
  char array[] = {1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, };
  int solutions[] = {0, 0, 0, 0, 0, 0, 0, 0};

  int result = dlx_get_all_solutions(row_count, col_count, array, 2, solutions);
  munit_assert(result == 2);

  return MUNIT_OK;
}


static MunitResult
test_get_two_row_some_solutions(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 4;
  int col_count = 3;
  char array[] = {1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, };
  int solutions[] = {0, 0, 0, 0};

  int result = dlx_get_all_solutions(row_count, col_count, array, 1, solutions);
  munit_assert(result == 1);

  return MUNIT_OK;
}


static MunitResult
test_get_multiple_row_result(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 4;
  int col_count = 3;
  char array[] = {0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1};
  int solution[] = {0, 0, 0, 0};

  int length = dlx_get_exact_cover(row_count, col_count, array, solution);
  munit_assert(length == 3);
  munit_assert_int(solution[0], ==, 2);
  munit_assert_int(solution[1], ==, 1);
  munit_assert_int(solution[2], ==, 3);
  munit_assert_int(solution[3], ==, 0);

  return MUNIT_OK;
}

static MunitResult
test_get_solution_count(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 4;
  int col_count = 3;
  char array[] = {0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1};
  int solution[] = {0, 0, 0, 0};

  int count = dlx_get_solution_count(row_count, col_count, array);
  munit_assert(count == 1);

  return MUNIT_OK;
}

static MunitResult
test_correct_zeroing_out(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 4;
  int col_count = 3;
  char array[] = {0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1};
  int solution[] = {-1, -1, -1, -1};

  int length = dlx_get_exact_cover(row_count, col_count, array, solution);
  munit_assert(length == 3);
  munit_assert_int(solution[0], ==, 2);
  munit_assert_int(solution[1], ==, 1);
  munit_assert_int(solution[2], ==, 3);
  munit_assert_int(solution[3], ==, 0);

  return MUNIT_OK;
}

static MunitResult
test_correct_zeroing_out_2(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  int row_count = 4;
  int col_count = 3;
  char array[] = {0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1};
  int solution[] = {-1, -1, -1, -1};

  int length = dlx_get_exact_cover(row_count, col_count, array, solution);
  munit_assert(length == 2);
  munit_assert_int(solution[0], ==, 1);
  munit_assert_int(solution[1], ==, 3);
  munit_assert_int(solution[2], ==, 0);
  munit_assert_int(solution[3], ==, 0);

  return MUNIT_OK;
}

static MunitTest test_suite_tests[] = {
  //{ (char*) "one_row_problem", test_get_one_row_result, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  //{ (char*) "two_row_problem", test_get_two_row_result, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  //{ (char*) "get_all_solutions", test_get_two_row_all_solutions, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "get_some_solutions", test_get_two_row_some_solutions, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  //{ (char*) "bigger_simple_problem", test_get_multiple_row_result, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  //{ (char*) "count_single_solution", test_get_solution_count, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  //{ (char*) "zero_out_array_correctly", test_correct_zeroing_out, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  //{ (char*) "zero_out_array_start_and_end", test_correct_zeroing_out_2, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { NULL, NULL, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL }
};


const MunitSuite dlx_test_suite = {
  (char*) "test_search_for_cover/",
  test_suite_tests,
  NULL,
  1,
  MUNIT_SUITE_OPTION_NONE
};
