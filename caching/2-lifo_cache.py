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
        self.last_key = None

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

    def get(self, key):
        """
        Get an item in the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
