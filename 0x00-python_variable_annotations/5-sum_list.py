#!/usr/bin/env python3
"""
Write a type-annotated function `sum_list` which takes a list
`input_list` of floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum_fl: float = 0
    for fl_item in input_list:
        sum_fl += fl_item
    return sum_fl
