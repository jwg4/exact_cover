#ifndef _QUAD_LINKED_LIST_H_
#define _QUAD_LINKED_LIST_H_

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*--------------------------------------------------------------------
 * These are the only pieces that need to be changed if the payload
 * data changes:
 */

typedef struct {
    int data;
    struct node *list_data;
} *data_type;

data_type create_data(int, struct node *);
void delete_data(data_type);

/*------------------------------------------------------------------*/

typedef struct node {
    data_type data;
    struct node *left;
    struct node *right;
    struct node *up;
    struct node *down;
} node, *node_ptr, *list;

list create_empty_list(void);
node_ptr create_node(data_type);

bool is_empty(list);
bool not_empty(list);

void set_data(node_ptr N, data_type data);
void set_left(node_ptr N, node_ptr left);
void set_right(node_ptr N, node_ptr right);
void set_up(node_ptr N, node_ptr up);
void set_down(node_ptr N, node_ptr down);

data_type get_data(node_ptr);
struct node *get_left(node_ptr);
struct node *get_right(node_ptr);
struct node *get_up(node_ptr);
struct node *get_down(node_ptr);

list insert_horizontally(list, node_ptr);
list insert_horizontally_after(list, node_ptr);
list insert_vertically(list, node_ptr);
list insert_vertically_after(list, node_ptr);

node_ptr cover_horizontally(node_ptr);
node_ptr cover_vertically(node_ptr);
void cover_column(list);
void uncover_column(list);
void uncover_horizontally(node_ptr);
void uncover_vertically(node_ptr);

node_ptr delete_return_right(node_ptr);
node_ptr delete_return_down(node_ptr);
void destroy_column_unsafely (list);
void destroy_entire_grid (list);

#endif


