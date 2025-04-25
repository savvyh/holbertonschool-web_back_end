#!/usr/bin/env python3
"""
Module for implementing a LIFO caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        self.cache_data[key] = item
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_element = self.cache_data.pop(self.cache_data[-1])
            print(f"DISCARD: {last_element}")

    def get(self, key):
        """
        Get an item in the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
