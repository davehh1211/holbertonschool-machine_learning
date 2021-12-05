#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Henao
"""


def add_matrices2D(mat1, mat2):
    """
    Function that adds two matrices element-wise.
    Parameters:
    - mat1 (ints/floats list of lists): first matrix.
    - mat2 (ints/floats list of lists): second matrix.
    Return:
     A new matrix with first add second matrix,
     if mat1 and mat2 are not the same shape, return None.
    """

    if len(mat1) != len(mat2):
        return None

    new_add_matrix = []
    for r in range(len(mat1)):
        if len(mat1[r]) != len(mat2[r]):
            return None
        else:
            column = []
            for c in range(len(mat1[r])):
                column.append(mat1[r][c] + mat2[r][c])
            new_add_matrix.append(column)

    return new_add_matrix
