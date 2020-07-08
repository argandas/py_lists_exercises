"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class LRUCache:
    last_used_key = 0

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_data = {}

    def get(self, key: int) -> int:
        value = 0
        print(f"Get ({key})")
        if key in self.cache_data:
            value = self.cache_data[key]["value"]
            self.last_used_key += 1
            self.cache_data[key]["usage"] = self.last_used_key
        else:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        assert (key > 0)
        if key not in self.cache_data:
            if len(self.cache_data) >= self.capacity:
                lru = min(
                    self.cache_data,
                    key=lambda x: self.cache_data[x]["usage"]
                )
                del self.cache_data[lru]
        # Put data
        self.last_used_key += 1
        self.cache_data[key] = {"value": value, "usage": self.last_used_key}

    def __len__(self):
        return len(self.cache_data)
