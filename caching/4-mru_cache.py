#!/usr/bin/env python3
"""
Module for implementing a MRU caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.mru_key in self.cache_data:
                print(f"DISCARD: {self.mru_key}")
                self.cache_data.pop(self.mru_key)

        self.cache_data[key] = item
        self.mru_key = key

    def get(self, key):
        """
        Get an item in the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_key = key  # mise à jour à chaque accès
        return self.cache_data[key]
