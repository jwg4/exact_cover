#---------------------------------------------------------------------
# 
# Author: Moy Easwaran, 2014-11-03
# Exact Cover with application to Sudoku, ver 0.1
# License: GPL v2 or above (https://www.gnu.org/licenses/gpl-2.0.html)
# 
#---------------------------------------------------------------------


ROOT_DIR = .

CC = gcc

SRC_DIR = $(ROOT_DIR)/src
OBJ_DIR = $(ROOT_DIR)/obj
TEST_DIR = $(ROOT_DIR)/tests
INCLUDES_DIR = $(SRC_DIR)
EXAMPLES_DIR = $(ROOT_DIR)/examples
PY_DIR = $(ROOT_DIR)/exact_cover_np


CFLAGS = -g -Wall -Wstrict-prototypes -I $(INCLUDES_DIR)
CFLAGS += -O0 -DDEBUG_LEVEL=0


$(OBJ_DIR):
	mkdir -pv $(OBJ_DIR)


$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(OBJ_DIR)
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ -c $^


$(OBJ_DIR)/munit.o: $(TEST_DIR)/munit.c $(OBJ_DIR)
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ -c $^


run_c_suite: $(TEST_DIR)/test_c_suite
	$^

$(TEST_DIR)/test_c_suite: $(OBJ_DIR)/quad_linked_list.o $(OBJ_DIR)/sparse_matrix.o $(OBJ_DIR)/dlx.o $(OBJ_DIR)/munit.o $(TEST_DIR)/test_sparse_matrix.o $(TEST_DIR)/test_dlx.o $(TEST_DIR)/test_legacy_dlx.o $(TEST_DIR)/test_quad_linked_list.o $(TEST_DIR)/test_sparse_matrix_2.o $(TEST_DIR)/test_c_suite.o
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ $^

all:
	echo "Make is used only for building and running C tests."
	echo "To build, install or test the Python package, use poetry."

clean:
	rm -rf $(OBJ_DIR)/*.o $(PY_DIR)/build $(PY_DIR)/exact_cover_np.so \
                $(TEST_DIR)/test_c_suite $(SRC_DIR)/*.pyc
