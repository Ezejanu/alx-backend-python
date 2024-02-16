#!/usr/bin/env python3
'''a type-annotated function sum_mixed_list'''

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:

    return sum(mxd_list)
