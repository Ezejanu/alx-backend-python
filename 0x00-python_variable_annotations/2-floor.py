#!/usr/bin/env python3
''' a type-annotated function floor '''

from math import floor as math_floor


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Parameters:
    - n (float): The input float number.

    Returns:
    int: The floor of the input float.

    """

    return math_floor(n)
