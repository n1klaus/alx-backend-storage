#!/usr/bin/env python3
"""Cache class model for Redis"""

from functools import wraps
import json
import redis
from typing import Any, Callable, Union
import uuid


def count_calls(method: Callable) -> Callable:
    """Decorator function to count number of calls to method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Callable:
        """Increments the number of calls made to a function on each call"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator function to store input and ouput of a method"""

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Callable:
        """Pushes input and output to the end of a list"""
        self._redis.rpush(f"{method.__qualname__}:inputs", str(*args))
        result = self.__call__(method, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(result))
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable, cache: Any) -> None:
    """Displays the history of calls of a function"""
    counter = cache.get(method.__qualname__).decode("utf-8")
    print(f"{method.__qualname__} was called {counter} times:")
    inputs = list(cache.lrange(f"{method.__qualname__}:inputs", 0, -1))
    outputs = list(cache.lrange(f"{method.__qualname__}:outputs", 0, -1))
    for i, o in zip(inputs, outputs):
        print("{0}(*({1},)) -> {2}"
              .format(method.__qualname__, repr(i.decode('utf-8')),
                      o.decode('utf-8')))


class Cache:
    """Cache model for Redis"""

    def __init__(self):
        """Constructor method for new instances"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def __call__(self, method, *args, **kwargs):
        """Caller method to execute instance method"""
        return method(self, *args, **kwargs)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the input data using the key"""
        key: str = str(uuid.uuid4())
        if not isinstance(data, (str, bytes, int, float)):
            data = json.dumps(data)
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Union[Callable, None] = None) -> Any:
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
