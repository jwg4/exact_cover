#include <assert.h>

#include "munit.h"

#include "quad_linked_list.h"


static MunitResult test_new_list_is_empty(const MunitParameter params[], void* data)
{
    list my_list = create_empty_list();
    
    munit_assert(is_empty(my_list));
    return MUNIT_OK;
}

static MunitResult test_add_one_item(const MunitParameter params[], void* data)
{
    int item1 = 1;
    list my_list = create_empty_list();
    
    my_list = insert_horizontally(my_list, create_node(create_data(item1, NULL)));
    munit_assert(not_empty(my_list));
    return MUNIT_OK;
}

static MunitResult test_can_retrieve_one_item(const MunitParameter params[], void* data)
{
    int item1 = 1;
    list my_list = create_empty_list();
   
    my_list = insert_horizontally(my_list, create_node(create_data(item1, NULL)));
    munit_assert(get_data(my_list)->data == 1);
    return MUNIT_OK;
}

static MunitResult test_quad_linked_list(const MunitParameter params[], void* data)
{
    int item1 = 1, item2 = 2, item3 = 3;
    list save_list, my_list = create_empty_list();
    
    munit_assert(is_empty(my_list));
    my_list = insert_horizontally(my_list, create_node(create_data(item3, NULL)));
    // Inserted one item; list should not be empty:
    munit_assert(not_empty(my_list));
    // We just inserted 3, so the items should match:
    //DEBUG_PRINT(1, "Check: insertion match.\n");
    munit_assert(get_data(my_list)->data == 3);

    save_list = my_list;
    my_list = cover_horizontally(my_list);
    // We covered the sole item, so remaining list should be empty:
    //DEBUG_PRINT(1, "Check: covering, test 1.\n");
    munit_assert(is_empty(my_list));
    uncover_horizontally(save_list);
    my_list = save_list;
    // We uncovered and restored it, so it should no longer be empty:
    munit_assert(not_empty(my_list));

    my_list = insert_horizontally(my_list, create_node(create_data(item2, NULL)));
    my_list = insert_horizontally(my_list, create_node(create_data(item1, NULL)));
    //DEBUG_PRINT(1, "Check: get data.\n");
    // First item (last inserted) should be 1:
    munit_assert(get_data(my_list)->data == 1);
    // Second item (second inserted) should be 2:
    munit_assert(get_data(get_right(my_list))->data == 2);
    // Last item (first inserted) should be 3:
    munit_assert(get_data(get_right(get_right(my_list)))->data == 3);

    // Going to cover the first item (which is 1):
    //DEBUG_PRINT(1, "Check: covering, test 2.\n");
    save_list = my_list;
    my_list = cover_horizontally(my_list);
    // Covered first item; new first should be 2:
    munit_assert(get_data(my_list)->data == 2);
    uncover_horizontally(save_list);
    my_list = save_list;
    // We uncovered and restored it, so it should no longer be empty:
    munit_assert(not_empty(my_list));
    // We uncovered and restored it, so the new first should again be 1:
    munit_assert(get_data(my_list)->data == 1);

    //DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the first item, so the new first should be 2:
    munit_assert(get_data(my_list)->data == 2);

    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the second item, so the new first should be 3:
    munit_assert(get_data(my_list)->data == 3);

    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the last item, so the list should be empty
    munit_assert(is_empty(my_list));

    //DEBUG_PRINT(1, "Check: insert after.\n");
    save_list = my_list = insert_horizontally_after(my_list, create_node(create_data(item1, NULL)));
    my_list = insert_horizontally_after(my_list, create_node(create_data(item2, NULL)));
    my_list = insert_horizontally_after(my_list, create_node(create_data(item3, NULL)));
    // First item (first inserted) should be 1:
    munit_assert(get_data(save_list)->data == 1);
    // Second item (second inserted) should be 2:
    munit_assert(get_data(get_right(save_list))->data == 2);
    // Last item (last inserted) should be 3:
    munit_assert(get_data(get_right(get_right(save_list)))->data == 3);

    //DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = save_list;
    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the first item, so the new first should be 2:
    munit_assert(get_data(my_list)->data == 2);

    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the second item, so the new first should be 3:
    munit_assert(get_data(my_list)->data == 3);

    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the last item, so the list should be empty
    munit_assert(is_empty(my_list));


    // Vertical tests:
    //DEBUG_PRINT(1, "\n");
    //DEBUG_PRINT(1, "Starting vertical tests.\n");

    item1 = 1; item2 = 2; item3 = 3;
    my_list = create_empty_list();
    // New list should be empty:
    
    //DEBUG_PRINT(1, "Check: emptiness.\n");
    munit_assert(is_empty(my_list));
    my_list = insert_vertically(my_list, create_node(create_data(item3, NULL)));
    // Inserted one item; list should not be empty:
    munit_assert(not_empty(my_list));
    // We just inserted 3, so the items should match:
    //DEBUG_PRINT(1, "Check: insertion match.\n");
    munit_assert(get_data(my_list)->data == 3);

    save_list = my_list;
    my_list = cover_vertically(my_list);
    // We covered the sole item, so remaining list should be empty:
    //DEBUG_PRINT(1, "Check: covering, test 1.\n");
    munit_assert(is_empty(my_list));
    uncover_vertically(save_list);
    my_list = save_list;
    // We uncovered and restored it, so it should no longer be empty:
    munit_assert(not_empty(my_list));

    my_list = insert_vertically(my_list, create_node(create_data(item2, NULL)));
    my_list = insert_vertically(my_list, create_node(create_data(item1, NULL)));
    //DEBUG_PRINT(1, "Check: get data.\n");
    // First item (last inserted) should be 1:
    munit_assert(get_data(my_list)->data == 1);
    // Second item (second inserted) should be 2:
    munit_assert(get_data(get_down(my_list))->data == 2);
    // Last item (first inserted) should be 3:
    munit_assert(get_data(get_down(get_down(my_list)))->data == 3);

    // Going to cover the first item (which is 1):
    //DEBUG_PRINT(1, "Check: covering, test 2.\n");
    save_list = my_list;
    my_list = cover_vertically(my_list);
    // Covered first item; new first should be 2:
    munit_assert(get_data(my_list)->data == 2);
    munit_assert(get_data(get_down(my_list))->data == 3);
    uncover_vertically(save_list);
    my_list = save_list;
    // We uncovered and restored it, so it should no longer be empty:
    munit_assert(not_empty(my_list));
    // We uncovered and restored it, so the new first should again be 1:
    munit_assert(get_data(my_list)->data == 1);
    munit_assert(get_data(get_down(my_list))->data == 2);
    munit_assert(get_data(get_down(get_down(my_list)))->data == 3);

    //DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = delete_return_down(my_list);
    //  We delete_return_down the first item, so the new first should be 2:
    munit_assert(get_data(my_list)->data == 2);

    my_list = delete_return_down(my_list);
    //  We delete_return_down the second item, so the new first should be 3:
    munit_assert(get_data(my_list)->data == 3);

    //DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = delete_return_down(my_list);
    //  We delete_return_down the last item, so the list should be empty
    munit_assert(is_empty(my_list));

    //DEBUG_PRINT(1, "Check: insert after.\n");
    save_list = my_list = insert_vertically_after(my_list, create_node(create_data(item1, NULL)));
    my_list = insert_vertically_after(my_list, create_node(create_data(item2, NULL)));
    my_list = insert_vertically_after(my_list, create_node(create_data(item3, NULL)));
    // First item (first inserted) should be 1:
    munit_assert(get_data(save_list)->data == 1);
    // Second item (second inserted) should be 2:
    munit_assert(get_data(get_down(save_list))->data == 2);
    // Last item (last inserted) should be 3:
    munit_assert(get_data(get_down(get_down(save_list)))->data == 3);

    //DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = save_list;
    my_list = delete_return_down(my_list);
    //  We delete_return_down the first item, so the new first should be 2:
    munit_assert(get_data(my_list)->data == 2);

    my_list = delete_return_down(my_list);
    //  We delete_return_down the second item, so the new first should be 3:
    munit_assert(get_data(my_list)->data == 3);

    my_list = delete_return_down(my_list);
    //  We delete_return_down the last item, so the list should be empty
    munit_assert(is_empty(my_list));

    return MUNIT_OK;
}

static MunitTest test_suite_tests[] = {
  { (char*) "create empty list", test_new_list_is_empty, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "add one item", test_add_one_item, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "retrieve one item", test_can_retrieve_one_item, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { (char*) "test_linked_list_manipulation", test_quad_linked_list, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL },
  { NULL, NULL, NULL, NULL, MUNIT_TEST_OPTION_NONE, NULL }
};


const MunitSuite quad_linked_list_test_suite = {
  (char*) "test_quad_linked_list",
  test_suite_tests,
  NULL,
  1,
  MUNIT_SUITE_OPTION_NONE
};
