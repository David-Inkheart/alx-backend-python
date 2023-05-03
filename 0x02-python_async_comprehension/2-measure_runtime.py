#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime should measure the total runtime and return it.
    """
    s_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    e_time = time.perf_counter()
    return e_time - s_time

"""
The total runtime is roughly 10 seconds because the 4 coroutines are
running in parallel, so the total runtime is the runtime of longest one.
This is the beauty of async. One can use asyncio.gather to run multiple
coroutines at the same time.
"""
