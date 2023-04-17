#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

import redis
import requests
import time
from functools import wraps
from multiprocessing import Process
from typing import Any, Callable, List

cache = redis.Redis()


def run(tasks: List[Callable]) -> None:
    """Run CPU work tasks in parallel"""
    running_tasks = [Process(target=task) for task in tasks]
    [task.start() for task in running_tasks]
    [task.join() for task in running_tasks]


def count_calls(wrapped: Callable) -> Callable:
    """Decorator function to count number of calls to method"""
    @wraps(wrapped)
    def wrapper(*args, **kwargs) -> Callable:
        """Increments the number of calls made to a specific url"""
        url = str(args[0])
        key = f"count:{url}"
        cache.incr(key)
        cached = cache.get(url)
        if cached:
            return cached
        print(cache.get(key))
        cache.setex(url, 10, wrapped(url))
        return wrapped(*args, **kwargs)
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """Returns the obtained content of a particular URL"""
    resp = requests.get(url)
    content: str = resp.text
    return content


if __name__ == "__main__":
    url = "http://google.com"
    # [run([lambda: get_page(url), lambda: time.sleep(2)]) for _ in range(10)]
    get_page(url)
