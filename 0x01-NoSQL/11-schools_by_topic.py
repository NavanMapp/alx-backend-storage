#!/usr/bin/env python3
"""
Script to list schools with a specific topic in the "school" collection
"""

import sys
import pymongo

def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.

    """
    query = {"topics": topic}
    schools = list(mongo_collection.find(query))
    return schools

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 11-schools_by_topic.py <database_name>")
        sys.exit(1)

    database_name = sys.argv[1]

    # Create a MongoDB client
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    # Access the specified database
    db = client[database_name]

    # Access the "school" collection (modify the collection name as needed)
    school_collection = db.school

    # List schools with the topic "Python"
    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
