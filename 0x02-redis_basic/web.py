#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

import redis
import requests

cache = redis.Redis()


def get_page(url: str) -> str:
    """Returns the obtained html content of a particular URL"""
    resp = requests.get(url)
    html: str = resp.content.decode("utf-8")
    access_count = cache.incrby(f"count:{url}", 1)
    cache.expire(access_count, 10)
    return html
