#!/usr/bin/env python3

""" Cache class
"""

import redis
from typing import Callable, Optional, Union
from uuid import uuid4


class Cache:
    """ Cache class stores instance of the Redic client
    """

    def __init__(self):
        """ Initalizee for Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random uuid
        """
        unique_id = str(uuid4)
        self._redis.set(unique_id, data)
        return unique_id

    def get(self, key: str, fn: Optional[Callable]):
        """ Converts data back to desired format
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, int, float]:
        """ Converts data back to desired string format
        """
        return self._redis.get(key, str)

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        """ Converts data back to desired int format
        """
        return self._redis.get(key, int)
