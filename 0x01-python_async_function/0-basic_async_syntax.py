#!/usr/bin/env python3
'''an asynchronous coroutine'''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds (inclusive).

    Parameters:
    - max_delay (float): The maximum delay in seconds. Defaults to 10.

    Returns:
    - float: The actual delay waited.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    asyncio.run(main())
