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
        self.mru_key = 0

    def put(self, key, item):
        """
        Add an item in the cache
        """
        self.cache_data[key] = item
        if key is None or item is None:
            return
        self.mru_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.mru_key
            print(f"DISCARD: {discard_key}")
            self.cache_data.pop(discard_key)

    def get(self, key):
        """
        Get an item in the cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.mru_key = key

        return self.cache_data[key]
