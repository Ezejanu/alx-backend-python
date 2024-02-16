#!/usr/bin/env python3
'''More involved type annotations'''

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')
'''Type variable for the value in the dictionary'''


def safely_get_value(dct: Mapping, key: Any, default: 
        Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets the value associated with the specified key in the dictionary.
    If the key is not present, returns the default value.

    Parameters:
    - dct (Dict[K, V]): The input dictionary with keys of type K
    and values of type V.
    - key (K): The key to look for in the dictionary.
    - default (V, optional): The default value to return
    if the key is not present.
    Defaults to None.

    Returns:
    V: The value associated with the key in the dictionary,
    or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
