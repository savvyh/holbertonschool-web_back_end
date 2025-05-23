#!/usr/bin/env python3
"""
filtered logger module
"""

import re
import logging


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format function
        """
        return self.filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
            )

    def filter_datum(self, fields, redaction, message, separator):
        """
        filter_datum function
        """
        return re.sub(r'{}'.format(fields, separator), redaction, message)
