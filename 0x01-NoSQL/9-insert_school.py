#!/usr/bin/env python3
"""Insert a document in a MongoDb collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Args:
        mongo_collection: pymongo collection object
        kwargs: key-value items
    Returns:
        the new `_id` of the created document
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
