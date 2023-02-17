#!/usr/bin/env python3
"""Cache class model for Redis"""

import json
import redis
from typing import Any, Callable
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
        if not isinstance(data, (int, str, bytes)):
            data = json.dumps(data)
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> Any:
        """Returns obj stored using provided key"""
        value: Any = self._redis.get(key)
        if value:
            if fn == str:
                return self.get_str(value, fn)
            elif fn == int:
                return self.get_int(value, fn)
            elif fn is not None:
                return fn(value)
            else:
                return value
        return None

    def get_str(self, value: Any, fn: Callable) -> str:
        """Returns str from raw value"""
        return fn(value)

    def get_int(self, value: Any, fn: Callable) -> int:
        """Returns int from raw value"""
        return fn(value)
