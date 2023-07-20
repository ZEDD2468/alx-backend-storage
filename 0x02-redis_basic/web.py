#!/usr/bin/env python3

import requests
import time
from functools import wraps

cache = {}

def get_page(url: str) -> str:
    
    if url in cache and time.time() - cache[url]['timestamp'] < 10:
        cache[url]['count'] += 1
        return cache[url]['content']

    response = requests.get(url)
    content = response.text

    cache[url] = {'content': content, 'count': 1, 'timestamp': time.time()}

    return content

def cache_decorator(func):
    cache = {}

    @wraps(func)
    def wrapper(url):
        if url in cache and time.time() - cache[url]['timestamp'] < 10:
            cache[url]['count'] += 1
            return cache[url]['content']

        response = func(url)
        cache[url] = {'content': response, 'count': 1, 'timestamp': time.time()}
        return response

    return wrapper
