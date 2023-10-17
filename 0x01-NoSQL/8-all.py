#!/usr/bin/env python3
"""
Script to list all documents in a collection
"""

import sys
import pymongo

def list_all(mongo_collection):
    """
    List all documents in a collection.

    """
    documents = list(mongo_collection.find({}))
    return documents

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 8-all.py <database_name>")
        sys.exit(1)

    database_name = sys.argv[1]

    # Create a MongoDB client
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    # Access the specified database
    db = client[database_name]

    # Access the "school" collection (modify the collection name as needed)
    school_collection = db.school

    # List all documents in the collection
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
