#!/usr/bin/env python3
"""Function that return a tuple with the string k and the square of v as a float."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of v as a float."""
    return k, float(v ** 2)
