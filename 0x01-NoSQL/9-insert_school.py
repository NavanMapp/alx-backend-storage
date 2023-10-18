#!/usr/bin/env python3
"""
Script to insert a new school document in the "school" collection
"""

import sys
import pymongo
def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on keyword arguments.

    """
    return mongo_collection.insert_one(kwargs).inserted_id
