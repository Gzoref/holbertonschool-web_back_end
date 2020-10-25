#!/usr/bin/python3

'''
FIFO Caching
'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key or item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            pop_off = sorted(self.cache_data)[0]
            self.cache_data.pop(pop_off)
            print('DISCARD:', pop_off)

    def get(self, key):
        """
        Return value of cache_data linked to key
        """
        if key is None:
            return
        return self.cache_data.get(key, None)