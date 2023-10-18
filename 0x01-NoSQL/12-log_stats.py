#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB
"""

import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("localhost", 27017)
db = client["logs"]
collection = db["nginx"]

# Count the number of documents in the collection
count = collection.count_documents({})

# Get the number of documents for each HTTP method
methods = collection.aggregate([
    {"$group": {"_id": "$method", "count": {"$sum": 1}}},
])

# Get the number of documents with the GET method and the path /status
status_checks = collection.count_documents({"method": "GET", "path": "/status"})

# Print the stats
print(f"{count} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method['_id']}: {method['count']}")
print(f"{status_checks} status check")
