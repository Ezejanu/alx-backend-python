#!/usr/bin/env python3
'''a coroutine called async_comprehension that takes no arguments.'''

import asyncio
from typing import List, AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over the async_generator coroutine.

    Returns:
        List[float]: List of 10 random numbers.
    """

    random_numbers = [number async for number in async_generator()]
    return random_numbers
