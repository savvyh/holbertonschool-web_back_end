#!/usr/bin/env python3
"""Defines a function to measure the runtime of wait_n."""

import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int, func: Callable) -> float:
    """Measure the total execution time and return total_time / n."""
    start_time = time.time()
    func(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
