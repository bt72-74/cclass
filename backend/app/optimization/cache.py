import time

cache_store = {}


def set_cache(key, value, ttl=60):
    cache_store[key] = {
        "value": value,
        "expires": time.time() + ttl
    }


def get_cache(key):
    item = cache_store.get(key)
    if not item:
        return None

    if time.time() > item["expires"]:
        del cache_store[key]
        return None

    return item["value"]
