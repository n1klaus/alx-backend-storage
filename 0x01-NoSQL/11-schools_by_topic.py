#!/usr/bin/env python3
"""Finds a list of schools having a specific topic in a collection"""


def schools_by_topic(mongo_collection, topic):
    """
    Args:
        mongo_collection: pymongo collection object
        topic (str): topic searched
    Returns:
        list of schools having the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
