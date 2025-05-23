#!/usr/bin/env python3
"""
filtered logger module
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    filter_datum function
    fields: list of strings representing all fields to obfuscate
    redaction: string representing by what the field will be obfuscated
    message: string representing the log line
    separator: str representing by which char is separating each field
    """

    for field in fields:
        message = re.sub(r'{}'.format(field, separator), redaction, message)
    return message
