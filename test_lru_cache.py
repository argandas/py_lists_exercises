from lru_cache import LRUCache


def test_lru_cache():
    my_cache = LRUCache(2)

    my_cache.put(1, 1)
    my_cache.put(2, 2)

    assert len(my_cache) == 2
    assert 1 == my_cache.get(1)      # returns 1

    my_cache.put(3, 3)               # evicts key 2
    assert 2 not in my_cache.cache_data

    assert -1 == my_cache.get(2)     # returns -1 (not found)

    my_cache.put(4, 4)               # evicts key 1
    assert 1 not in my_cache.cache_data

    assert my_cache.get(1) == -1     # returns -1 (not found)
    assert my_cache.get(3) == 3      # returns 3
    assert my_cache.get(4) == 4      # returns 4
