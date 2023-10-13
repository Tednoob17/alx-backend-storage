#!/usr/bin/env python3
"""
Function that insert documents
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert a school
    """
    return mongo_collection.insert_one(kwargs).inserted_id
