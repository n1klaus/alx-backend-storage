#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""

if __name__ == "__main__":
    from pymongo import MongoClient
    from pymongo.collection import Collection

    with MongoClient() as client:
        db = client.logs
        collection = Collection(db, "nginx")
        print("{} logs".format(collection.count_documents({})))
        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for m in methods:
            c = collection.count_documents({"method": m})
            print("\tmethod {}: {}".format(m, c))
        s = collection.count_documents({"method": "GET", "path": "/status"})
        print("{} status check".format(s))
        print("IPs:")
        ip_occurence = collection.aggregate([
            {
                "$group": {
                    "_id": "$ip",
                    "occurence": {
                        "$sum": 1
                    }
                }
            },
            {
                "$sort": {
                    "occurence": -1
                }
            },
            {
                "$limit": 10
            }
        ])
        for ip in ip_occurence:
            print(f"\t{ip.get('_id')}: {ip.get('occurence')}")
