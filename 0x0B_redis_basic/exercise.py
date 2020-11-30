#!/usr/bin/env python3

""" Cache class
"""

import redis
from typing import Union
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
