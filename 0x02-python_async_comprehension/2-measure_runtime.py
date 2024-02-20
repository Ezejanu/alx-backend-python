#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
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
    total_runtime = end_time - start_time

    return total_runtime
