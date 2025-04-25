#!/usr/bin/env python3
"""
Module for implementing a FIFO caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        Get an item in the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
