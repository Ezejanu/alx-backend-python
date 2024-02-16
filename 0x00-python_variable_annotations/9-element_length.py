#!/usr/bin/env python3
'''duck type an iterable object'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from
    the input iterable and its corresponding length.

    Parameters:
    - lst (Iterable[str]): The input iterable of strings.

    Returns:
    List[Tuple[str, int]]: A list of tuples where the first element is a
    string from the input iterable, and the second element is its length.
    """
    return [(i, len(i)) for i in lst]
