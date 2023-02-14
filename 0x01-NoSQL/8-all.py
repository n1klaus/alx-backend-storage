#!/usr/bin/env python3
"""Lists all documents in MongoDb collection"""


def list_all(mongo_collection) -> list:
    """
    Args:
        mongo_collection: pymongo collection objectR
    Returns:
        A list of all documents in a mongodb collection
    """
    return [*mongo_collection.find()]
