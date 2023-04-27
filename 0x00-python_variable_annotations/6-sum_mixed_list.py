#!/usr/bin/env python3
"""
Write a type-annotated function `sum_mixed_list` which takes a
list `mxd_lst` of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    return the sum of float items in a mixed list
    """
    sum_fl: float = 0
    for fl_item in mxd_list:
        sum_fl += fl_item
    return sum_fl
