from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            print(self.cache[key])
            return self.cache[key]
        
    def set(self, key: str, value: str) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

    def rem(self, key: str) -> None:
        return self.set(key,"")
    
    def getall(self) -> None:
        return print(self.cache)