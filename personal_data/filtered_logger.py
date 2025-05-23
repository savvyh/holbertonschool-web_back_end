#!/usr/bin/env python3
"""
filtered logger module
"""

import re
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "ip")

"""
Redacting Formatter class
"""


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

    def filter_datum(fields, redaction, message, separator):
        """
        filter_datum function
        """
        for field in fields:
            message = re.sub(f'{field}=[^{separator}]*',
                             f'{field}={redaction}', message)
        return message


def get_logger():
    """
    get_logger function
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db():
    """
    get_db function that returns a connector to the database
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

