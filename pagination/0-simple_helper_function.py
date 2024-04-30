#!/usr/bin/env python3
"""Return a tuple of page and page size."""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Returns the start and end indexes for pagination."""
    start_index = (page - 1) * page_size  # (page - 1) permet de traduire les numéros de page en indices de liste (qui sont basés sur zéro)
    end_index = start_index + page_size

    return start_index, end_index
