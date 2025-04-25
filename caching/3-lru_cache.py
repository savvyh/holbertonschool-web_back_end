"""
Module for implementing a LRU caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and is a caching system
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
            least_recently_item = self.cache_data.popitem(last=False)
            print(f"DISCARD: {least_recently_item}")

    def get(self, key):
        """
        Get an item in the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
