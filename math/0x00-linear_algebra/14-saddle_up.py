#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Henao
"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    Function that performs matrix multiplication
    Parameters:
    - mat1 (numpy.ndarray): never empty
    - mat2 (numpy.ndarray): never empty
    Return:
     The product of the matrices in ndarray
    """

    return np.matmul(mat1, mat2)
