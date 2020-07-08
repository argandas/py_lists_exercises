cache_data = {}
cache_data[1] = {'value': 100, 'usage': 3}
cache_data[2] = {'value': 100, 'usage': 5}
cache_data[4] = {'value': 100, 'usage': 1}

print(cache_data)
x = min(cache_data, key=lambda x: cache_data[x]["usage"])
print(x)
