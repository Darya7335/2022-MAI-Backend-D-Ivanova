from LRUcache.cache import LRUCache

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
# print(cache.cache)
cache.set('Walter', 'White')
# print(cache.cache)
cache.set('Jesse', 'James')
# print(cache.cache)
cache.get('Jesse') # вернёт 'James'
# print(cache.cache)
cache.rem('Walter')
# print(cache.cache)
cache.get('Walter') # вернёт ''
# print(cache.cache)