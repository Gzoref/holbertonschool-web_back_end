#!/usr/bin/python3

'''
MRU Caching
'''
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize
        """
        self.queued_item = deque()
        super().__init__()

    def put(self, key, item):
        """
       Print or discard the least recently used item (LRU algorithm)
        """
        if key and item:
            if key in self.cache_data:
                self.queued_item.remove(key)
            elif len(self.queued_item) > BaseCaching.MAX_ITEMS:
                popped_item = self.queued_item.pop()
                del self.cache_data[popped_item]
                print("DISCARD: " + str(popped_item))
            self.queued_item.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value of cache_data linked to key
        """
        if key in self.cache_data:
            self.queued_item.remove(key)
            self.queued_item.append(key)
            return self.cache_data.get(key)
