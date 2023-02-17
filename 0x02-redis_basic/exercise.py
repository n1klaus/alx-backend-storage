#!/usr/bin/env python3
"""Cache class model for Redis"""

import json
import redis
from typing import Any
import uuid


class Cache:
    """Cache model for Redis"""

    def __init__(self):
        """Constructor method for new instances"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Generates a random key and stores the input data using the key"""
        key: str = str(uuid.uuid4())
        if not isinstance(data, (str, bytes)):
            data = json.dumps(data)
        self._redis.set(key, data)
        return key
