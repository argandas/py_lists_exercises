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
        self.cache_usage = {}

    def get(self, key: int) -> int:
        value = 0
        if key in self.cache_data:
            value = self.cache_data[key]
            self.last_used_key += 1
            self.cache_usage[key] = self.last_used_key
            print(f"Get << Key = {key}, Value = {self.cache_data[key]}, Usage = {self.cache_usage[key]}")
        else:
            value = -1
        print(f"Cache Data = {self.cache_data}")
        return value

    def put(self, key: int, value: int) -> None:
        assert (key > 0)
        if key not in self.cache_data:
            if len(self.cache_data) >= self.capacity:
                lru = min(self.cache_usage, key=self.cache_usage.get)
                print(f"LRU = {lru}")
                del self.cache_usage[lru]
                del self.cache_data[lru]
        # Put data
        self.cache_data[key] = value
        self.last_used_key += 1
        self.cache_usage[key] = self.last_used_key
        print(f"Put >> Key = {key}, Value = {self.cache_data[key]}, Usage = {self.cache_usage[key]}")
        print(f"Cache Data = {self.cache_data}")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Example:

cache = LRUCache(2)

cache.put(1, 100)
cache.put(2, 200)
print(cache.get(1))       # returns 1
cache.put(3, 300)    # evicts key 2
print(cache.get(2))       # returns -1 (not found)
cache.put(4, 400)    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))      # returns 3
print(cache.get(4))      # returns 4
