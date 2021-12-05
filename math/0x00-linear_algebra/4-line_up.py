#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Henao
"""

def add_arrays(arr1, arr2):
    """
    Function that adds two arrays element-wise.
    Parameters:
    - arr1 (list of ints/floats): first list.
    - arr2 (list of ints/floats): second list.
    Return:
     A new list with the first list added second list,
     if the shape of the lists are not the same, return None.
    """

    if len(arr1) != len(arr2):
        return None
    newList = []
    for i in range(len(arr1)):
        newList.append(arr1[i] + arr2[i])

    return newList
