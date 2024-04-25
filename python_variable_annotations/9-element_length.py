#!/usr/bin/env python3
"""Return values with the appropriate types from a function."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each element of lst and its length."""
    return [(i, len(i)) for i in lst]
