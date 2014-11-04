#include "debug.h"
#include <assert.h>

#include "quad_linked_list.h"


int main(void) {
    int item1 = 1, item2 = 2, item3 = 3;
    list save_list, my_list = create_empty_list();
    // New list should be empty:
    
    // Horizontal tests:
    DEBUG_PRINT(1, "Starting horizontal tests.\n");

    DEBUG_PRINT(1, "Check: emptiness.\n");
    assert(is_empty(my_list));
    my_list = insert_horizontally(my_list, create_node(create_data(item3, NULL)));
    // Inserted one item; list should not be empty:
    assert(not_empty(my_list));
    // We just inserted 3, so the items should match:
    DEBUG_PRINT(1, "Check: insertion match.\n");
    assert(get_data(my_list)->data == 3);

    save_list = my_list;
    my_list = cover_horizontally(my_list);
    // We covered the sole item, so remaining list should be empty:
    DEBUG_PRINT(1, "Check: covering, test 1.\n");
    assert(is_empty(my_list));
    uncover_horizontally(save_list);
    my_list = save_list;
    // We uncovered and restored it, so it should no longer be empty:
    assert(not_empty(my_list));

    my_list = insert_horizontally(my_list, create_node(create_data(item2, NULL)));
    my_list = insert_horizontally(my_list, create_node(create_data(item1, NULL)));
    DEBUG_PRINT(1, "Check: get data.\n");
    // First item (last inserted) should be 1:
    assert(get_data(my_list)->data == 1);
    // Second item (second inserted) should be 2:
    assert(get_data(get_right(my_list))->data == 2);
    // Last item (first inserted) should be 3:
    assert(get_data(get_right(get_right(my_list)))->data == 3);

    // Going to cover the first item (which is 1):
    DEBUG_PRINT(1, "Check: covering, test 2.\n");
    save_list = my_list;
    my_list = cover_horizontally(my_list);
    // Covered first item; new first should be 2:
    assert(get_data(my_list)->data == 2);
    uncover_horizontally(save_list);
    my_list = save_list;
    // We uncovered and restored it, so it should no longer be empty:
    assert(not_empty(my_list));
    // We uncovered and restored it, so the new first should again be 1:
    assert(get_data(my_list)->data == 1);

    DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the first item, so the new first should be 2:
    assert(get_data(my_list)->data == 2);

    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the second item, so the new first should be 3:
    assert(get_data(my_list)->data == 3);

    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the last item, so the list should be empty
    assert(is_empty(my_list));

    DEBUG_PRINT(1, "Check: insert after.\n");
    save_list = my_list = insert_horizontally_after(my_list, create_node(create_data(item1, NULL)));
    my_list = insert_horizontally_after(my_list, create_node(create_data(item2, NULL)));
    my_list = insert_horizontally_after(my_list, create_node(create_data(item3, NULL)));
    // First item (first inserted) should be 1:
    assert(get_data(save_list)->data == 1);
    // Second item (second inserted) should be 2:
    assert(get_data(get_right(save_list))->data == 2);
    // Last item (last inserted) should be 3:
    assert(get_data(get_right(get_right(save_list)))->data == 3);

    DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = save_list;
    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the first item, so the new first should be 2:
    assert(get_data(my_list)->data == 2);

    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the second item, so the new first should be 3:
    assert(get_data(my_list)->data == 3);

    my_list = delete_return_right(my_list);
    //  We delete_return_rightd the last item, so the list should be empty
    assert(is_empty(my_list));


    // Vertical tests:
    DEBUG_PRINT(1, "\n");
    DEBUG_PRINT(1, "Starting vertical tests.\n");

    item1 = 1; item2 = 2; item3 = 3;
    my_list = create_empty_list();
    // New list should be empty:
    
    DEBUG_PRINT(1, "Check: emptiness.\n");
    assert(is_empty(my_list));
    my_list = insert_vertically(my_list, create_node(create_data(item3, NULL)));
    // Inserted one item; list should not be empty:
    assert(not_empty(my_list));
    // We just inserted 3, so the items should match:
    DEBUG_PRINT(1, "Check: insertion match.\n");
    assert(get_data(my_list)->data == 3);

    save_list = my_list;
    my_list = cover_vertically(my_list);
    // We covered the sole item, so remaining list should be empty:
    DEBUG_PRINT(1, "Check: covering, test 1.\n");
    assert(is_empty(my_list));
    uncover_vertically(save_list);
    my_list = save_list;
    // We uncovered and restored it, so it should no longer be empty:
    assert(not_empty(my_list));

    my_list = insert_vertically(my_list, create_node(create_data(item2, NULL)));
    my_list = insert_vertically(my_list, create_node(create_data(item1, NULL)));
    DEBUG_PRINT(1, "Check: get data.\n");
    // First item (last inserted) should be 1:
    assert(get_data(my_list)->data == 1);
    // Second item (second inserted) should be 2:
    assert(get_data(get_down(my_list))->data == 2);
    // Last item (first inserted) should be 3:
    assert(get_data(get_down(get_down(my_list)))->data == 3);

    // Going to cover the first item (which is 1):
    DEBUG_PRINT(1, "Check: covering, test 2.\n");
    save_list = my_list;
    my_list = cover_vertically(my_list);
    // Covered first item; new first should be 2:
    assert(get_data(my_list)->data == 2);
    assert(get_data(get_down(my_list))->data == 3);
    uncover_vertically(save_list);
    my_list = save_list;
    // We uncovered and restored it, so it should no longer be empty:
    assert(not_empty(my_list));
    // We uncovered and restored it, so the new first should again be 1:
    assert(get_data(my_list)->data == 1);
    assert(get_data(get_down(my_list))->data == 2);
    assert(get_data(get_down(get_down(my_list)))->data == 3);

    DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = delete_return_down(my_list);
    //  We delete_return_down the first item, so the new first should be 2:
    assert(get_data(my_list)->data == 2);

    my_list = delete_return_down(my_list);
    //  We delete_return_down the second item, so the new first should be 3:
    assert(get_data(my_list)->data == 3);

    DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = delete_return_down(my_list);
    //  We delete_return_down the last item, so the list should be empty
    assert(is_empty(my_list));

    DEBUG_PRINT(1, "Check: insert after.\n");
    save_list = my_list = insert_vertically_after(my_list, create_node(create_data(item1, NULL)));
    my_list = insert_vertically_after(my_list, create_node(create_data(item2, NULL)));
    my_list = insert_vertically_after(my_list, create_node(create_data(item3, NULL)));
    // First item (first inserted) should be 1:
    assert(get_data(save_list)->data == 1);
    // Second item (second inserted) should be 2:
    assert(get_data(get_down(save_list))->data == 2);
    // Last item (last inserted) should be 3:
    assert(get_data(get_down(get_down(save_list)))->data == 3);

    DEBUG_PRINT(1, "Check: deleting.\n");
    my_list = save_list;
    my_list = delete_return_down(my_list);
    //  We delete_return_down the first item, so the new first should be 2:
    assert(get_data(my_list)->data == 2);

    my_list = delete_return_down(my_list);
    //  We delete_return_down the second item, so the new first should be 3:
    assert(get_data(my_list)->data == 3);

    my_list = delete_return_down(my_list);
    //  We delete_return_down the last item, so the list should be empty
    assert(is_empty(my_list));

    DEBUG_PRINT(1, "\n");
    DEBUG_PRINT(0, "Passed all tests!\n");
    return 0;
}

