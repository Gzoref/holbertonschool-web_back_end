#!/usr/bin/env python3

'''
More involved type annotations
'''

from typing import Iterable, List, Sequence, Tuple, Union, Any, TypeVar, Mapping


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'), None]=None) -> Union[Any, TypeVar('T')]:
    '''
    return dictionary key
    '''
    if key in dct:
        return dct[key]
    else:
        return default
