#!/usr/bin/env python3
'''a type-annotated function sum_mixed_list'''

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of integers and floats.

    Parameters:
    - mxd_lst (List[Union[int, float]]):
    The input list of integers and float numbers.

    Returns:
    float: The sum of the input list.
    """

    return sum(mxd_list)
