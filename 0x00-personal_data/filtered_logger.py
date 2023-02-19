#!/usr/bin/env python3
"""  Regex-ing module """

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ returns the log message obfuscated """
    for field in fields:
        pattern = field + "=.*?" + separator
        replacement = field + "=" + redaction + separator
        message = re.sub(pattern, replacement, message)
    return message
