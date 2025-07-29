#!/usr/bin/env python3
"""
Redis basic
"""
import redis
import uuid
from typing import Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Counts number of calls to a class method
    Args:
        method: The method to count the calls of.
        Callable: The class method to count the calls of.
    Returns:
        The number of calls to the method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Wrapper function to count the calls to a method.
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Store the history of inputs and outputs for a particular function.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """
        Wrapper function to store the history of inputs and outputs for a
        particular function.
        """
        self._redis.rpush(key + ":inputs", str(args))
        result = method(self, *args)
        self._redis.rpush(key + ":outputs", str(result))
        return result
    return wrapper


def replay(method: Callable):
    """
    Display the history of calls of a particular function.
    """
    key = method.__qualname__

    count_calls = method.__self__._redis.get(key)
    if count_calls is None:
        print(f"Cache.store was called 0 times.")
        return

    count_calls = int(count_calls)
    print(f"Cache.store {key} was called {count_calls} times:")

    inputs = method.__self__._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = method.__self__._redis.lrange(f"{key}:outputs", 0, -1)

    for input_data, output_data in zip(inputs, outputs):
        input_str = input_data.decode('utf-8')
        output_str = output_data.decode('utf-8')
        print(f"{key}(*{input_str}) -> {output_str}")


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

    @count_calls
    @call_history
    def store(self, data):
        """
        Generate a random key and store input in Redis.
        Args:
            data: Data to store in Redis.
        Returns:
            The key of the stored data.
        """
        random_key = str(uuid.uuid4())
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
