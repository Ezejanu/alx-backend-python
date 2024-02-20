#!/usr/bin/env python3
'''Measure the runtime'''

import asyncio
import time
from typing import List
# Import the wait_random function from file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per operation.

    Args:
        n (int): Number of times to execute wait_n.
        max_delay (int, optional): Maximum delay in seconds for wait_random.
        Default is 10.

    Returns:
        float: Average time per operation in seconds.

    Raises:
        ValueError: If n or max_delay is not a non-negative integer.
    """

    start_time = time.time()

    # Run the event loop to measure the execution time
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
