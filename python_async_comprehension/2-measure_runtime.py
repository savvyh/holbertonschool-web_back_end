#!/usr/bin/env python3
"""Run time 4 parallel comprehensions."""
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Asynch coroutine that will execute async_comprehension
    4 times in parallel using asyncio.gather, the return the running time."""
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = perf_counter()
    total_runtime = end_time - start_time

    return total_runtime
