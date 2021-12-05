#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Henao
"""


def np_elementwise(mat1, mat2):
    """
    Function that performs element-wise addition, subtraction, multiplication,
    and division.
    Parameters:
    - mat1 (numpy.ndarray).
    - mat2 (numpy.ndarray).
    Return:
     A tuple containing the element-wise sum, difference, product,
     and quotient, respectively.
    """
    add = mat1 + mat2
    diff = mat1 - mat2
    prod = mat1 * mat2
    quot = mat1 / mat2
    return add, diff, prod, quot
