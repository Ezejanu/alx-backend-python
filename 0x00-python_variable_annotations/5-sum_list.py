#!/usr/bin/env python3
'''a type-annotated function sum_list'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Parameters:
    - input_list (List[float]): The input list of float numbers.

    Returns:
    float: The sum of the input list.
    """

    return sum(input_list)
