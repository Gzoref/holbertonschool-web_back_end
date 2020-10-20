#!/usr/bin/env python3

'''
Let's execute multiple coroutines at the same time with async
'''

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Call wait_random n times
    '''

    result = []

    delays = [wait_random(max_delay) for time in range(n)]

    for sort in asyncio.as_completed(delays):
        val = await sort
        result.append(val)
    return result
