#!/usr/bin/env python3
from base_caching import BaseCaching
"""
BasicCache class that inherits from BaseCaching and is a caching system
"""


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
