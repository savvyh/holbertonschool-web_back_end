#!/usr/bin/env python3
"""
Redis basic
"""
import redis
import uuid


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Store an instance of redis client and flush it.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """
        Generate a random key and store input in Redis.
        Args:
            data: Data to store in Redis.
        Returns:
            The key of the stored data.
        """
        random_key = str(uuid.uuid1())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key, fn=None):
        """
        Get a value from Redis.
        Args:
            key: The key to get the value from.
            fn: A function to convert the value to a specific type.
        Returns:
            The value of the key.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            value = fn(value)
        return value

    def get_str(self, key):
        """
        Get a value from Redis and convert it to a string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """
        Get a value from Redis and convert it to an integer.
        """
        return self.get(key, int)
