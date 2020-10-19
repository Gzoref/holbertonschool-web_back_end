#!/usr/bin/env python3

'''
Duck Typing
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Return element length
    '''
    return [(i, len(i)) for i in lst]
