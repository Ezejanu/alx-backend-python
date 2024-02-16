#!/usr/bin/env python3
''' a type-annotated function make_multiplier'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    Parameters:
    - multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float and returns the
    product.
    """

    def multiplier_function(x: float) -> float:
        """a function that multiplies a float by multiplier"""
        return x * multiplier

    return multiplier_function
