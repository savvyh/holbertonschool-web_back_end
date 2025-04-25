#!/usr/bin/env python3
"""
BasicCache class that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching



class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
