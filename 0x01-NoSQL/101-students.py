#!/usr/bin/python3
"""Top students by average score"""

from pymongo.collection import Collection


def top_students(mongo_collection: Collection) -> list:
    """
    Args:
        mongo_collection(Collection): mongo database collection of students
    Returns:
        (list) the top students sorted by average score
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
    return list(top_students)
