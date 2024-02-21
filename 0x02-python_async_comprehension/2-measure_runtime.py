#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''

import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: Total runtime in seconds.
    """

    start_time = asyncio.get_event_loop().time()

    # Use asyncio.gather to run async_comprehension four times in parallel

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            )

    end_time = asyncio.get_event_loop().time()
    total_runtime: float = end_time - start_time

    return total_runtime
