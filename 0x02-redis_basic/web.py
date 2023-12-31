#!/usr/bin/env python3
"""
Web Cache and Tracker
"""
import redis
import requests


store = redis.Redis()
count = 0


def get_page(url: str) -> str:

