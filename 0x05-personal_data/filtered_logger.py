#!/usr/bin/env python3
"""
Filter personal information using a Regex, Environmental variables, etc
"""

import re
from typing import List
import logging
import mysql.connector
import os


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Filter values in incoming log records using filter_datum.
        Values for fields in fields should be filtered.
        """
        result = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            result,
            self.SEPARATOR)


PII_FIELDS = ('password', 'email', 'ssn', 'email', 'phone')


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    Connect to mysql server with environmental vars
    '''
    user = os.environ.get('PERSONAL_DATA_DB_USERNAME', None),
    db_host = os.environ.get('PERSONAL_DATA_DB_HOST', None),
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME', None),
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', None)

    return mysql.connector.connect(user=user,
                                   password=password,
                                   host=db_host,
                                   database=db_name)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    '''
    Returns the log message obfuscated with Regex
    '''
    for item in fields:
        pattern = item + "=.+?(?=abc)*\\" + ";"
        message = re.sub(pattern, item + "=" + redaction + separator, message)
    return message


def get_logger() -> logging.Logger:
    '''
    Returns a Logger object with a
    StreamHandler with RedactingFormatter
    as formatter
    '''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    target_handler = logging.StreamHandler()
    target_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(list(PII_FIELDS))
    target_handler.setFormatter(formatter)

    logger.addHandler(target_handler)

    return logger
