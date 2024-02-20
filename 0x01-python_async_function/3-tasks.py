#!/usr/bin/env python3
'''a function that returns asyncio.Task'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random
    function with the specified max_delay.

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: An asyncio task for wait_random.
    """

    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
