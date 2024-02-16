#!/usr/bin/env python3
'''Duck typing - first element of a sequence'''

from typing import Any, Sequence, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the sequence if it is not empty,
    otherwise returns None.

    Parameters:
    - lst (Sequence[Any]): The input sequence with elements of any type.

    Returns:
    Union[Any, None]: The first element of the sequence if not empty,
    otherwise None.
    """

    if lst:
        return lst[0]
    else:
        return None
