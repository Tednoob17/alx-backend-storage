#!/usr/bin/env python3
"""
Returns all students sorted by average score
"""


def top_students(mongo_collection):
    """Get Top Students"""
    return mongo_collection.aggregate([
        {

        {
            "$sort": {"averageScore": -1}
        }
    ])
