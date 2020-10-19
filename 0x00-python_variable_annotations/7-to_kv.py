#!/usr/bin/env python3

'''
Complex types - string and int/float to tuple
'''

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    '''
    Returns string representation of float
    '''
    return (k, v ** 2)
