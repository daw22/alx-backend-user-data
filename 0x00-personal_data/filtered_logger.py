#!/usr/bin/env python3
"""
filter for logeer
"""
import re
from typing import List


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
