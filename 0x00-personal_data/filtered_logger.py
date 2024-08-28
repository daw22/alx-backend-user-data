#!/usr/bin/env python3
"""
filter for logeer
"""
import re
from typing import List
import logging


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Returns a log message obfuscated
    """
    for field in fields:
        start_delimeter = field + '='
        end_delimeter = separator
        pattern = rf"({start_delimeter})(.*?)({end_delimeter})"
        new_text = re.sub(pattern, fr"\1{redaction}\3", message)
        message = new_text
    return new_text


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters values from the log record"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
