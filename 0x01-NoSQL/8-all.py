#!/usr/bin/env python3
"""
Function that list all documents
"""
import pymongo


def list_all(mongo_collection):
    """
    list all collections
    """
    if not mongo_collection:
        return []
