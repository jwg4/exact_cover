import io
import sys

import numpy as np

from sudoku_solver import sudoku


def check(con_matrix):
    sum = 0
    for i in range(len(con_matrix)):
        for j in range(len(con_matrix[i])):
            if con_matrix[i][j] == 1:
                sum += 2**j
    return sum


def test_solving_mini_sudoku():
    sudo = sudoku.Sudoku(4)
    sudo.read(io.StringIO("1,0,0,0\n0,0,3,0\n0,2,0,0\n0,0,0,4\n"), False)    # 4 in bottom-right essential (tests overflow)
    con_matrix = sudo._translate_into_constraint_matrix()
    # checking the whole 64x64 constraint-matrix is a PITA, so just compute a checksum.
    assert(check(con_matrix) == 64726160598999529785)


def test_solving_empty_mini_sudoku():
    sudo = sudoku.Sudoku(4)
    sudo._sudo = np.zeros((4,4), dtype='int')
    con_matrix = sudo._translate_into_constraint_matrix()
    # checking the whole 64x64 constraint-matrix is a PITA, so just compute a checksum.
    assert(check(con_matrix) == 73786976294838206460)


def test_solving_trivial_sudoku():
    sudo = sudoku.Sudoku(9)
    sudo.read(io.StringIO("0,3,5,2,9,0,8,6,4\n0,8,2,4,1,0,7,0,3\n7,6,4,3,8,0,0,9,0\n2,1,8,7,3,9,0,4,0\n0,0,0,8,0,4,2,3,0\n0,4,3,0,5,2,9,7,0\n4,0,6,5,7,1,0,0,9\n3,5,9,0,2,8,4,1,7\n8,0,0,9,0,0,5,2,6\n"), False)
    sol = sudo.solve()
    assert(sol._sudo.tolist() == [[1,3,5,2,9,7,8,6,4],[9,8,2,4,1,6,7,5,3],[7,6,4,3,8,5,1,9,2],[2,1,8,7,3,9,6,4,5],[5,9,7,8,6,4,2,3,1],[6,4,3,1,5,2,9,7,8],[4,2,6,5,7,1,3,8,9],[3,5,9,6,2,8,4,1,7],[8,7,1,9,4,3,5,2,6]])


def test_solving_easy_sudoku():
    sudo = sudoku.Sudoku(9)
    sudo.read(io.StringIO("0,0,0,0,7,4,5,6,0\n5,0,0,2,1,8,3,0,0\n0,4,0,0,6,0,2,7,1\n6,9,0,3,2,5,1,8,0\n0,5,0,0,8,0,9,3,6\n0,7,0,6,0,1,4,2,5\n0,0,3,0,5,0,6,0,0\n0,0,0,8,0,0,0,0,0\n9,2,0,0,0,6,0,1,0\n"), False)
    sol = sudo.solve()
    assert(sol._sudo.tolist() == [[1,3,2,9,7,4,5,6,8],[5,6,7,2,1,8,3,4,9],[8,4,9,5,6,3,2,7,1],[6,9,4,3,2,5,1,8,7],[2,5,1,4,8,7,9,3,6],[3,7,8,6,9,1,4,2,5],[7,8,3,1,5,2,6,9,4],[4,1,6,8,3,9,7,5,2],[9,2,5,7,4,6,8,1,3]])
    assert(sudo._hardness == "Easy")


def test_solving_medium_sudoku():
    sudo = sudoku.Sudoku(9)
    sudo.read(io.StringIO("9,0,5,2,0,0,0,3,0\n0,0,0,1,0,3,0,0,6\n0,0,0,4,5,6,0,9,0\n0,4,0,0,8,0,6,0,0\n0,5,0,3,0,1,0,4,0\n0,0,2,0,6,0,0,1,0\n0,2,0,6,1,7,0,0,0\n3,0,0,5,0,9,0,0,0\n0,9,0,0,0,2,7,0,4\n"), False)
    sol = sudo.solve()
    assert(sol._sudo.tolist() == [[9,6,5,2,7,8,4,3,1],[2,8,4,1,9,3,5,7,6],[7,1,3,4,5,6,2,9,8],[1,4,7,9,8,5,6,2,3],[6,5,9,3,2,1,8,4,7],[8,3,2,7,6,4,9,1,5],[4,2,8,6,1,7,3,5,9],[3,7,6,5,4,9,1,8,2],[5,9,1,8,3,2,7,6,4]])
    assert(sudo._hardness == "Medium")


def test_solving_hard_sudoku():
    sudo = sudoku.Sudoku(9)
    sudo.read(io.StringIO("0,3,0,0,0,8,0,0,0\n0,5,0,9,0,0,3,0,1\n2,0,7,0,0,0,0,4,0\n0,0,0,0,7,0,1,0,0\n5,0,8,0,3,0,4,0,9\n0,0,1,0,8,0,0,0,0\n0,8,0,0,0,0,7,0,6\n7,0,3,0,0,6,0,2,0\n0,0,0,4,0,0,0,3,0\n"), False)
    sol = sudo.solve()
    assert(sol._sudo.tolist() == [[1,3,4,7,5,8,6,9,2],[8,5,6,9,4,2,3,7,1],[2,9,7,1,6,3,8,4,5],[9,6,2,5,7,4,1,8,3],[5,7,8,2,3,1,4,6,9],[3,4,1,6,8,9,2,5,7],[4,8,9,3,2,5,7,1,6],[7,1,3,8,9,6,5,2,4],[6,2,5,4,1,7,9,3,8]])
    assert(sudo._hardness == "Hard")


def test_solving_very_hard_sudoku():
    sudo = sudoku.Sudoku(9)
    sudo.read(io.StringIO("8,1,9,0,7,0,0,0,6\n0,0,0,9,0,0,5,0,0\n0,0,0,0,0,4,0,8,0\n0,5,2,6,0,0,0,0,0\n3,0,0,0,0,0,0,0,5\n0,0,0,0,0,9,2,1,0\n0,7,0,8,0,0,0,0,0\n0,0,6,0,0,3,0,0,0\n2,0,0,0,6,0,9,4,7\n"), False)
    sol = sudo.solve()
    assert(sol._sudo.tolist() == [[8,1,9,2,7,5,4,3,6],[7,4,3,9,8,6,5,2,1],[6,2,5,1,3,4,7,8,9],[9,5,2,6,1,8,3,7,4],[3,8,1,4,2,7,6,9,5],[4,6,7,3,5,9,2,1,8],[5,7,4,8,9,2,1,6,3],[1,9,6,7,4,3,8,5,2],[2,3,8,5,6,1,9,4,7]])
    assert(sudo._hardness == "Very hard")


def test_solving_impossible_sudoku():
    sudo = sudoku.Sudoku(4)
    sudo.read(io.StringIO("1,1,1,1\n1,1,1,1\n1,1,1,1\n1,1,1,1\n"), False)
    sol = sudo.solve()
    assert(sol is None)

