#!/usr/bin/env python3

""" Cache class
"""

import redis
from typing import Callable, Optional, Union
from uuid import uuid4
from functools import wraps


def count_calls(func: Callable) -> Callable:
    """ Counts how many times methods of Cache class are called
    """
    method_name = func.__qualname__

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """ Increment method call number
        """
        self._redis.incr(method_name)
        return func(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Stores history of inputs and outputs for a particular function
    """


class Cache:
    """ Cache class stores instance of the Redic client
    """

    def __init__(self):
        """ Initalizee for Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random uuid
        """
        unique_id = str(uuid4)
        self._redis.set(unique_id, data)
        return unique_id

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """ Converts data back to desired format
        """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, int, float]:
        """ Converts data back to desired string format
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        """ Converts data back to desired int format
        """
        return self.get(key, int)
