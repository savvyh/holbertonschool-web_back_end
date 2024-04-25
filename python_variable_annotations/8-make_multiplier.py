#!/usr/bin/env python3
"""Function that multiplies a float by the given multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiplier_function(number: float) -> float:
        """Multiply a float by the given multiplier."""
        return number * multiplier
    return multiplier_function
