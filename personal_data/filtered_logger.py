#!/usr/bin/env python3
"""
filtered logger module
"""

import re
import logging
import os
import mysql.connector
from typing import List, Tuple, Any

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")

"""
Redacting Formatter class
"""


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION: str = "***"
    FORMAT: str = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]) -> None:
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format function
        """
        return self.filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
            )

    def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
        """
        filter_datum function
        """
        for field in fields:
            message = re.sub(f'{field}=[^{separator}]*',
                             f'{field}={redaction}', message)
        return message


def get_logger() -> logging.Logger:
    """
    get_logger function
    """
    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler: logging.StreamHandler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    get_db function that returns a connector to the database
    """
    username: str = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password: str = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host: str = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database: str = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main() -> None:
    """
    main function
    """
    db: mysql.connector.connection.MySQLConnection = get_db()
    sql_query: mysql.connector.cursor.MySQLCursor = db.cursor()
    sql_query.execute("SELECT * FROM users")
    logger: logging.Logger = get_logger()

    for row in sql_query:
        message: str = "; ".join([f"{field}={value}" for field,
                              value in zip(sql_query.column_names, row)])
        logger.info(message)

    sql_query.close()
    db.close()


if __name__ == "__main__":
    main()
