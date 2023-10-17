#!/usr/bin/env python3
"""
Script to display stats from Nginx logs in MongoDB
"""

import pymongo

def main():
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Total number of logs
    total_logs = logs_collection.count_documents({})

    print(f"{total_logs} logs")

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Status check
    status_check = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    top_ips = list(logs_collection.aggregate(pipeline))

    print("IPs:")
    for ip_data in top_ips:
        print(f"    {ip_data['_id']}: {ip_data['count']}")

if __name__ == "__main__":
    main()
