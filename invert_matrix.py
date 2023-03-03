#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
A function to invert a matrix. Mostly it will be dealing with 3x3 or 4x4 matrices.
Let's start with ordinary Python lists of lists. Then we'll go with numpy ndarray...
"""

# from inspect import currentframe, stack
# import sys
import numpy as np
from numpy import ndarray


def find_pivot(ind: int, matrix: ndarray) -> [int, int, float]:
    """
    Find the biggest by absolute value element in matrix starting from matrix[ind][ind].
    Return indices and value of the found element (column, row, pivot).
    Use NaN ('Not A Number' value) as pivot if all remaining elements are zeroes.
    """
    col_l: int = 0
    row_l: int = 0
    pivot_l: float = np.NaN
    abs_piv: float = 0.0
    for i_add, vect in enumerate(matrix[ind:]):
        for j_add, elem in enumerate(vect[ind:]):
            abs_elem: float = abs(elem)
            if abs_elem > abs_piv:
                row_l, col_l, pivot_l, abs_piv = i_add, j_add, elem, abs_elem
    return ind + col_l, ind + row_l, pivot_l


def swap_rows(ind1: int, ind2: int, matrix: ndarray, inverse: ndarray, order: ndarray) -> None:
    """Exchange the values in the given rows_l of both the matrices"""
    # print(f"Before: {matrix}, {ind1}, {ind2}.")
    if ind1 != ind2:
        # tmp = matrix[ind1].copy()
        matrix[ind1], matrix[ind2] = matrix[ind2].copy(), matrix[ind1].copy()
        # tmp = inverse[ind1].copy()
        inverse[ind1], inverse[ind2] = inverse[ind2].copy(), inverse[ind1].copy()
        order[ind1], order[ind2] = order[ind2], order[ind1]


def swap_cols(ind1: int, ind2: int, matrix: ndarray, inverse: ndarray, order: ndarray) -> None:
    """Exchange the values in the given colons of both the matrices"""
    if ind1 != ind2:
        # tmp = matrix[..., ind1].copy()
        matrix[..., ind1], matrix[..., ind2] = matrix[..., ind2].copy(), matrix[..., ind1].copy()
        # tmp = inverse[..., ind1].copy()
        inverse[..., ind1], inverse[..., ind2] = inverse[..., ind2].copy(), inverse[..., ind1].copy()
        order[ind1], order[ind2] = order[ind2], order[ind1]
    # print(f"After: {matrix}.")


def invert(mat: ndarray, row_order: ndarray, col_order: ndarray) -> (ndarray, ndarray, ndarray):
    """Invert the matrix by Gauss method with full selection of the pivot element."""
    rows_l: int = len(mat)
    cols_l: int = len(mat[0])
    assert rows_l == cols_l and all((cols_l == len(row_l) for row_l in mat[1:])), f"{rows_l=}, {cols_l=}, {mat=}."
    mat_0: ndarray = mat.copy()
    mat_inv: ndarray = np.eye(rows_l)
    for k in range(rows_l):
        print(f"Before: {mat=}.\n{mat_inv=}.")
        pivot: float  # = matrix[k, k]
        col, row, pivot = find_pivot(k, mat)
        swap_rows(row, k, mat, mat_inv, row_order)
        swap_cols(col, k, mat, mat_inv, col_order)
        if np.isnan(pivot):
            raise ValueError(f"Matrix size is {rows_l}x{cols_l}, rank is {k}, inverse matrix does not exist.")
        mat[k, :] /= pivot
        mat_inv[k, :] /= pivot
        for r in range(k):
            mrk = mat[r, k]
            mat_inv[r, :] -= mrk * mat_inv[k, :]
            mat[r, :] -= mrk * mat[k, :]
        for r in range(k + 1, rows_l):
            mrk = mat[r, k]
            mat_inv[r, :] -= mrk * mat_inv[k, :]
            mat[r, :] -= mrk * mat[k, :]
        print(f"After: {mat=}.\n{mat_inv=}.")
    print(f"{mat=}.")
    print(f"{mat_inv=}.")
    print(f"{row_order=}.")
    print(f"{col_order=}.\n")
    print(f"{np.matmul(mat_inv, mat_0)=}.")
    for i, j in enumerate(row_order):
        swap_rows(i, j, mat, mat_inv, row_order)
    for i, j in enumerate(col_order):
        swap_cols(i, j, mat, mat_inv, col_order)
    print(f"{np.matmul(mat_inv, mat_0)=}.")
    return mat_inv


if __name__ == '__main__':
    # matrix: ndarray = np.array([
    #     [8.0, 1.0],
    #     [1.0, 8.0],
    # ])
    matrixA: ndarray = np.array([
        [6.0, 2.0, 1.0],
        [7.0, 4.0, -8.0],
        [-0.5, -0.5, -4.5],
    ])
    mat0: ndarray = matrixA.copy()
    rows, columns = len(matrixA), len(matrixA[0])
    row_ord, columns_ord = np.arange(rows), np.arange(columns)
    matrixA_inv: ndarray = invert(matrixA, row_ord, columns_ord)
    print(f"{matrixA=}.")
    print(f"{matrixA_inv=}.")
    print(f"{row_ord=}.")
    print(f"{columns_ord=}.\n")

    print(f"{mat0=}.")
    print(f"{np.matmul(matrixA_inv, mat0)=}.")
    print(f"{np.dtype=}, {np.dtype.type=}, {matrixA_inv.dtype.type=}, {mat0[0, 0].dtype=}.")
    # m_inv: ndarray = np.array([
    #     [8.0 / 63.0, -1.0 / 63.0],
    #     [-1.0 / 63.0, 8.0 / 63.0]])
    # print(f"{m_inv=}.")
    # print(f"{np.matmul(m_inv, mat0)=}.")
