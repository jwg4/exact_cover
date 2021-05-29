#include "munit.h"

extern MunitSuite sparse_matrix_test_suite;
extern MunitSuite sparse_matrix_test_suite_2;
extern MunitSuite dlx_test_suite;
extern MunitSuite legacy_dlx_test_suite;
extern MunitSuite quad_linked_list_test_suite;

MunitSuite all_test_suites[5];


int main(int argc, char* argv[MUNIT_ARRAY_PARAM(argc + 1)]) {
  all_test_suites[0] = sparse_matrix_test_suite;
  all_test_suites[1] = sparse_matrix_test_suite_2;
  all_test_suites[2] = dlx_test_suite;
  all_test_suites[3] = legacy_dlx_test_suite;
  all_test_suites[4] = quad_linked_list_test_suite;

  const MunitSuite test_suite = {
    (char*) "all_tests/",
    NULL,
    all_test_suites,
    1,
    MUNIT_SUITE_OPTION_NONE
  };

  return munit_suite_main(&test_suite, (void*) "µnit", argc, argv);
}
