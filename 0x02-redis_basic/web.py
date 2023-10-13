#!/usr/bin/env python3
"""
Web Cache and Tracker
"""
import redis
import requests


store = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """ get a page and cach value"""
    store.set(f"cached:{url}", count)
    resp = requests.get(url)
    store.incr(f"count:{url}")
    store.setex(f"cached:{url}", 10, store.get(f"cached:{url}"))
    return resp.text
