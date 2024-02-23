#!/usr/bin/env python3
'''execute multiple coroutines at the same time with async'''

import asyncio
from typing import List

# Import the wait_random function from file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times
    with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        List[float]: List of delays in ascending order.
    """

    # Check for non-negative integer values for n and max_delay
    if not (isinstance(n, int) or isinstance(n, float)) or not\
            (isinstance(max_delay, int) or isinstance(max_delay, float))\
            or n < 0 or max_delay < 0:
        raise ValueError

    # Use gather to concurrently spawn wait_random n times
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Sort the delays in ascending order
    delays.sort()

    return delays

if __name__ == "__main__":
    # Run the main coroutine within the event loop
    asyncio.run(main())
