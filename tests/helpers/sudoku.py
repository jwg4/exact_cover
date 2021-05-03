# ---------------------------------------------------------------------
#
# Author: Moy Easwaran, 2014-11-03
# Exact Cover with application to Sudoku, ver 0.1
# License: GPL v2 or above (https://www.gnu.org/licenses/gpl-2.0.html)
#
# This program uses Donald Knuth's Algorithm X to find exact
# covers of sets.  For details on Algorithm X please see either
# <https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X>
# or
# <http://arxiv.org/pdf/cs/0011047v1>.
#
# Specifically, we use the Knuth/Hitotsumatsu/Noshita method of
# Dancing Links for efficient backtracking.  Please see Knuth's
# paper above for details.
#
# As an example, we use this NumPy module to solve Sudoku.  For
# details on this approach (exact covers), please see
# <https://en.wikipedia.org/wiki/Exact_cover#Sudoku>.
#
# ---------------------------------------------------------------------
# flake8: noqa

import logging
import math
import numpy as np
import sys
import exact_cover as ec
import getopt


class Sudoku:
    def __init__(self, size=9):
        self._sudo = None
        self._constraint_matrix = None
        self._hardness = None
        self._size = size
        self._base = int(math.sqrt(size))
        self._num_possibilities = self._size ** 3
        self._num_constraints = 4 * self._size ** 2

    def _print_usage(self):
        sys.stderr.write("Usage:\n")
        sys.stderr.write(
            "    To use this program to solve Sudoku puzzles, put the puzzle in a\n"
        )
        sys.stderr.write("    CSV file and then call the program as follows:\n")
        sys.stderr.write("    {progname} < filename.csv\n".format(progname=sys.argv[0]))

    def read(self, file_handle, want_rating):
        try:
            self._sudo = np.genfromtxt(
                file_handle, delimiter=",", loose=False, dtype="int32"
            )
        except IOError:
            sys.stderr.write("Error: Unable to read file, sorry.\n")
            sys.exit(1)
        except ValueError:
            sys.stderr.write(
                "Error: CSV file should have integers between 1 and 9, inclusive.\n\n"
            )
            self._print_usage()
            sys.exit(1)
        if self._sudo.shape != (self._size, self._size):
            sys.stderr.write("Error: Sudoku matrices are usually 9x9.\n")
            sys.exit(1)
        if np.max(self._sudo) > 9 or np.min(self._sudo) < 0:
            sys.stderr.write(
                "Error: CSV file should have integers between 1 and 9, inclusive.\n"
            )
            sys.exit(1)
        self._constraint_matrix = self._translate_into_constraint_matrix()
        self._calculate_hardness()
        if want_rating:
            print("Rating: " + self._hardness)

    def _calculate_hardness(self):
        # Roughly, the fewer choices the player has, the easier the puzzle.
        # This translates to the constraint matrix having more columns with low sums.
        # The total sum of the constraint matrix is a rough proxy for this quanitity.
        # Caveats: (a) "rough" appears twice in the above! (b) At this point we don't
        # even know if a solution exists. (c) We're depending on the ratings of
        # <http://www.websudoku.com/>.
        freedom = self._constraint_matrix.sum()
        if freedom < 1800:
            self._hardness = "Easy"
            return
        if freedom < 1950:
            self._hardness = "Medium"
            return
        if freedom < 2075:
            self._hardness = "Hard"
            return
        self._hardness = "Very hard"
        return

    def write(self, file_handle):
        np.savetxt(file_handle, self._sudo, fmt="%d", delimiter=",")

    def _set_constraint_row(self, constraints, row, col, entry):
        """
        Set the constraints for each possible entry in the matrix.
        For details of these constraints please see <https://en.wikipedia.org/wiki/Exact_cover#Sudoku>.
        """
        con_row = (row * self._size ** 2) + (col * self._size) + entry - 1
        cell_con_col = (0 * self._size ** 2) + (row * self._size) + col
        row_con_col = (1 * self._size ** 2) + (row * self._size) + entry - 1
        col_con_col = (2 * self._size ** 2) + (col * self._size) + entry - 1
        box_con_col = (
            (3 * self._size ** 2)
            + self._size * (self._base * (row // self._base) + (col // self._base))
            + entry
            - 1
        )
        # print row, col, entry, ":", con_row, cell_con_col, row_con_col, col_con_col, box_con_col
        constraints[con_row][cell_con_col] = 1
        constraints[con_row][row_con_col] = 1
        constraints[con_row][col_con_col] = 1
        constraints[con_row][box_con_col] = 1

    def _translate_into_constraint_matrix(self):
        """
        Translate a 9x9 Sudoku matrix into a 729x324 constraint matrix.
        For details of these constraints please see <https://en.wikipedia.org/wiki/Exact_cover#Sudoku>.
        """
        constraints = np.zeros(
            (self._num_possibilities, self._num_constraints), dtype="int32"
        )
        for row in range(self._size):
            for col in range(self._size):
                real_entry = self._sudo[row, col]
                # If we don't already have an entry then all entries are possible.
                if real_entry == 0:
                    possible_entries = range(1, self._size + 1)
                else:
                    # If we already have an entry then leave out all the otherrpossibilities.
                    possible_entries = range(real_entry, real_entry + 1)
                for entry in possible_entries:
                    self._set_constraint_row(constraints, row, col, entry)
        return constraints

    def _translate_exact_cover_into_sudoku(self, cover):
        cover.sort()
        return np.fromiter(map(lambda x: (x % self._size) + 1, cover), int).reshape(
            self._size, self._size
        )

    def solve(self):
        # NOTES:
        # 1.  No error-checking; data is clean at this point.
        # 2.  We translate the puzzle once into the constraint matrix below, and then we
        #     translate again into a sparse matrix in get_exact_cover.  This duplicates
        #     some work, but it allows get_exact_cover to be a more generally applicable
        #     function.
        logging.debug(self._constraint_matrix)
        cover = ec.get_exact_cover(self._constraint_matrix)
        logging.debug(cover)
        solution = None
        if cover.size > 0 and (
            (cover[0] != 0) or (cover[1] != 0)
        ):  # an array of 0's implies no solution.
            solution = Sudoku(self._size)
            solution._sudo = self._translate_exact_cover_into_sudoku(cover)
        return solution


def want_rating():
    optlist = []
    args = []
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "r")
    except getopt.GetoptError:
        pass
    if len(optlist) != 0 and optlist[0][0] == "-r":
        return True


def main():
    sudo = Sudoku()
    sudo.read(sys.stdin, want_rating())
    solution = sudo.solve()
    if solution is None:
        sys.stdout.write("No solutions!\n")
    else:
        solution.write(sys.stdout)


# What should we do if there are no solutions?

if __name__ == "__main__":
    main()
