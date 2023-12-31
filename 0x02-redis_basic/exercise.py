#!/usr/bin/env python3
"""Exercise for Redis"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """
    Count the number of times a method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        """


def call_history(method: Callable) -> Callable:
    """
    Store the history of inputs and outputs for a particular function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Call the method and store the history of inputs/outputs
        """
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ":outputs", str(result))
        return result
    return wrapper



class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """Get data from Redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Convert bytes to str"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Convert bytes to int"""
        return self.get(key, int)
