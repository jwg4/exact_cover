#---------------------------------------------------------------------
# 
# Author: Moy Easwaran, 2014-11-03
# Exact Cover with application to Sudoku, ver 0.1
# License: GPL v2 or above (https://www.gnu.org/licenses/gpl-2.0.html)
# 
# This NumPy module uses Donald Knuth's Algorithm X to find exact
# covers of sets.  For details on Algorithm X please see either
# <https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X>
# or
# <http://arxiv.org/pdf/cs/0011047v1>.
#
# Specifically, we use the Knuth/Hitotsumatsu/Noshita method of
# Dancing Links for efficient backtracking.  Please see Knuth's
# paper above for details.
# 
# As an example, we use this NumPy module to solve Sudoku.
# 
#---------------------------------------------------------------------
# P.S.  I'm not an expert on Make, so please forgive any Makefile
#  		ugliness.
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


#-----------------------------------------------------------------------------------------

c_tests: note \
	note_quad_linked_list run_test_quad_linked_list \
	note_sparse_matrix run_test_sparse_matrix \
	note_dlx run_test_dlx \
	run_munit

tests: c_tests py_tests

py_tests: test_exact_cover

note:
	@echo "**********************************************************************"
	@echo "* NOTE: THE DEFAULT MAKE TARGET IS 'make tests'.                     *"
	@echo "* THIS WILL ALSO BUILD ALL COMPONENTS AND INSTALL THE NUMPY MODULE.  *"
	@echo "**********************************************************************"
	@echo

note_quad_linked_list:
	@echo "**********************************************************************"
	@echo "* Test quad_linked_list.                                             *"
	@echo "**********************************************************************"

note_sparse_matrix:
	@echo "**********************************************************************"
	@echo "* Test sparse matrix.                                                *"
	@echo "**********************************************************************"

note_dlx:
	@echo "**********************************************************************"
	@echo "* Test dlx (Knuth's algorithm X implemented using Dancing Links.     *"
	@echo "**********************************************************************"

note_install_exact_cover:
	@echo "**********************************************************************"
	@echo "* Build and install NumPy exact cover module.                        *"
	@echo "**********************************************************************"

#-----------------------------------------------------------------------------------------

$(TEST_DIR)/test_quad_linked_list: $(OBJ_DIR)/quad_linked_list.o $(TEST_DIR)/test_quad_linked_list.c
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ $^

$(OBJ_DIR)/quad_linked_list.o: $(SRC_DIR)/quad_linked_list.c
	mkdir -pv $(OBJ_DIR)
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ -c $^

run_test_quad_linked_list: $(TEST_DIR)/test_quad_linked_list
	$^

#-----------------------------------------------------------------------------------------

$(OBJ_DIR)/munit.o: $(TEST_DIR)/munit.c
	mkdir -pv $(OBJ_DIR)
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ -c $^

$(TEST_DIR)/test_m_sparse_matrix: $(OBJ_DIR)/quad_linked_list.o $(OBJ_DIR)/sparse_matrix.o $(OBJ_DIR)/munit.o $(TEST_DIR)/test_m_sparse_matrix.c
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ $^

run_test_m_sparse_matrix: $(TEST_DIR)/test_m_sparse_matrix
	$^

$(TEST_DIR)/test_m_dlx: $(OBJ_DIR)/quad_linked_list.o $(OBJ_DIR)/sparse_matrix.o $(OBJ_DIR)/dlx.o $(OBJ_DIR)/munit.o $(TEST_DIR)/test_m_dlx.c
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ $^

run_test_m_dlx: $(TEST_DIR)/test_m_dlx
	$^

run_munit_test_dlx: $(TEST_DIR)/test_dlx
	$^

run_munit: run_test_m_sparse_matrix \
	run_test_m_dlx \
	run_munit_test_dlx

#-----------------------------------------------------------------------------------------

$(TEST_DIR)/test_sparse_matrix: $(OBJ_DIR)/quad_linked_list.o $(OBJ_DIR)/sparse_matrix.o $(TEST_DIR)/test_sparse_matrix.c
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ $^

$(OBJ_DIR)/sparse_matrix.o: $(SRC_DIR)/sparse_matrix.c
	mkdir -pv $(OBJ_DIR)
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ -c $^

run_test_sparse_matrix: $(TEST_DIR)/test_sparse_matrix
	$^

#-----------------------------------------------------------------------------------------

$(TEST_DIR)/test_dlx: $(OBJ_DIR)/quad_linked_list.o $(OBJ_DIR)/sparse_matrix.o $(OBJ_DIR)/dlx.o $(OBJ_DIR)/munit.o $(TEST_DIR)/test_dlx.c
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ $^

$(OBJ_DIR)/dlx.o: $(SRC_DIR)/dlx.c
	$(CC) $(CFLAGS) $(DEBUG_CFLAGS) -o $@ -c $^

run_test_dlx: $(TEST_DIR)/test_dlx
	$^

#-----------------------------------------------------------------------------------------

exact_cover:
	cd $(PY_DIR) ; python setup.py build_ext ; cd -

install_exact_cover: exact_cover
	cd $(PY_DIR) ; python setup.py install ; cd -

test_exact_cover: install_exact_cover
	pytest

#-----------------------------------------------------------------------------------------

clean:
	rm -rf $(OBJ_DIR)/*.o $(PY_DIR)/build $(PY_DIR)/exact_cover_np.so \
		$(TEST_DIR)/test_dlx $(TEST_DIR)/test_quad_linked_list $(TEST_DIR)/test_sparse_matrix \
		$(SRC_DIR)/*.pyc

vim_clean:
	find $(ROOT_DIR) -name '*~' -exec rm {} \;
	find $(ROOT_DIR) -name '.*~' -exec rm {} \;


