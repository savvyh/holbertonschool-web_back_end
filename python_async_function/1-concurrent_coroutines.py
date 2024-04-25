#!/usr/bin/env python3
"""
Defines an async routine wait_n.
That spawns wait_random n times with specified max_delay.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that spawns wait_random n times with a max_delay."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
