#!/usr/bin/env python3
"""
filtered logger module
"""

import re

"""
fields: list of strings representing all fields to obfuscate
redaction: string representing by what the field will be obfuscated
message: string representing the log line
separator: str representing by which char is separating each field
"""

def filter_datum(fields, redaction, message, separator):
    """
    filter_datum function
    """
    return re.sub(r'{}'.format(fields, separator), redaction, message)
