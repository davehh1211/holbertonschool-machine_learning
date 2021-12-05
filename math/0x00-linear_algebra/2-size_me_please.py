#!/usr/bin/env python3
"""
@author: David Henao
"""


def matrix_shape(matrix):
    """
    Function that calculate the shape of a matrix.
    Parameters:
    - matrix (list of lists): matrix to calculate the shape.
    Return:
     The shape of the matrix as a list of integers.
    """
    shape = []
    while type(matrix) == list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
