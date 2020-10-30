#!/usr/bin/env python3
"""
Filter personal information with Regex
"""

from re import sub
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    '''
    Returns the log message obfuscated with Regex
    '''
    for item in fields:
        pattern = item + "=.+?(?=abc)*\\" + ";"
        message = sub(pattern, item + "=" + redaction + separator, message)
    return message
