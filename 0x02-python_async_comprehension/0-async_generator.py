#!/usr/bin/env python3
''' a coroutine called async_generator that takes no arguments'''

import asyncio
import random


async def async_generator():
    """
    Coroutine that loops 10 times, asynchronously waits 1 second,
    then yields a random number between 0 and 10.

    Yields:
        float: Random number between 0 and 10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
