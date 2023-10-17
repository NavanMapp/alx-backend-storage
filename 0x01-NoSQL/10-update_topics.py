#!/usr/bin/env python3
"""
Script to update topics of a school document based on the name.
"""

import sys
import pymongo

def update_topics(mongo_collection, name, topics):
    """
    Change the topics of a school document based on the name.

    """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, update)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <database_name>")
        sys.exit(1)

    database_name = sys.argv[1]

    # Create a MongoDB client
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    # Access the specified database
    db = client[database_name]

    # Access the "school" collection
    school_collection = db.school

    # Update topics for the "Holberton school" document
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])
