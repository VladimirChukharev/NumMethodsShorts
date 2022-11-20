#!/usr/bin/env python
# -*- coding: utf8 -*-

"""A function to invert a matrix. Mostly it will be dealing with 3x3 or 4x4 matrices.
Let's start with ordinary Python lists of lists. Then we'll go with numpy ndarray...
"""

# from inspect import currentframe, stack
import sys


def invert(matrix):
    """Invert the matrix by Gauss method with full selection of the pivot element."""
    rows, columns = len(matrix), len(matrix[0])
    assert rows == columns and all((columns == len(row) for row in matrix[1:])), f"{rows=}, {columns=}, {matrix=}."
    row_order, columns_order = [i for i in range(rows)], [i for i in range(columns)]
    determinant, sign = 1.0, 1
    min_pivot = sys.float_info.max
    todo = rows
    print(f"{rows=}, {columns=}, {matrix=}.")
    print(f"{row_order=}, {columns_order=}, {determinant=}, {sign=}.")
    print(f"{min_pivot=}, {todo=}.")


if __name__ == '__main__':
    mat = [
        [3.0, 2.0, 1.0],
        [1.0, 2.0, 1.0],
        [3.0, 2.0, 3.0],
    ]
    print({invert(mat)})
