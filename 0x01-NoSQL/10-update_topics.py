#!/usr/bin/env python3
"""Modifies MongoDb collection document"""


def update_topics(mongo_collection, name, topics):
    """
    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics (List[str]): list of topics approached in the school
    Returs:
        Nothing
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
