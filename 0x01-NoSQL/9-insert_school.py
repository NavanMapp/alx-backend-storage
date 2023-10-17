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
    new_document = kwargs
    mongo_collection.insert_one(new_document)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 9-insert_school.py <database_name>")
        sys.exit(1)

    database_name = sys.argv[1]

    # Create a MongoDB client
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    # Access the specified database
    db = client[database_name]

    # Access the "school" collection
    school_collection = db.school

    # Insert a new school document
    insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
