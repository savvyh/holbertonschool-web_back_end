#!/usr/bin/env python3
"""insert a new document based on kwargs"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert a new doc in a collection based on kwargs"""
    return mongo_collection.insert(kwargs)
