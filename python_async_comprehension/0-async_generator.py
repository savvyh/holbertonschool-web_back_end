#!/usr/bin/env python3
"""Async  generator."""
import asyncio
import random
from types import NoneType
from typing import AsyncGenerator, Union, NoneType


async def async_generator() -> AsyncGenerator[float, Union[None, NoneType]]:
    """Coroutine that yields a random number after waiting for 1 second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
