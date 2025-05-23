#!/usr/bin/env python3
"""
filtered logger module
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    filter_datum function
    """
    return re.sub(r'{}'.format(fields, separator), redaction, message)
