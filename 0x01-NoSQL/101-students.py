#!/usr/bin/env python3
"""Top students by average score"""

from pymongo.collection import Collection
from pymongo.command_cursor import CommandCursor


def top_students(mongo_collection: Collection) -> CommandCursor:
    """
    Args:
        mongo_collection(Collection): mongo database collection of students
    Returns:
        (CommandCursor) the top students sorted by average score
    """
    top_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                },
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
    return top_students
