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
