#!/usr/bin/env python3

'''
Async Generator
'''

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
     Yield a random number between 0 and 10.
    '''
    random_number = random.random() * 10

    for count in range(10):
        await asyncio.sleep(1)
        yield random_number
