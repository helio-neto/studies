from collections import deque

class LRUCache:
    """
    Status: WORK IN PROGRESS....
    Data structure that follows the constraints of a Least Recently Used (LRU) cache.
    
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    """

    def __init__(self, capacity: int):
        self.lru_queue_cache = deque(maxlen=capacity)

    def get(self, key: int) -> int:
        print(f"Getting Value by Key: {key}")
        try:
            key_value = self.lru_queue_cache.index(key)
            print(f"Key Value: {key_value}")
            print(f"Cache Value: {self.lru_queue_cache[key_value]}")
            return self.lru_queue_cache[key_value]
        except ValueError:
            print(f"No Value for Key Founded on Cache.")
            return -1

    def put(self, key: int, value: int) -> None:
        print(f"Putting on Cache. Key: {key}, Value: {value}")
        try:
            key_value = self.lru_queue_cache.index(key)
            self.lru_queue_cache[key_value] = value
            print(f"Putting Updating Key Value: {key_value}")
            print(f"Putting Updated Value: {self.lru_queue_cache[key_value]}")
        except ValueError:
            if len(self.lru_queue_cache) == self.lru_queue_cache.maxlen:
                self.lru_queue_cache.appendleft(value)
            else:
                self.lru_queue_cache.append(value)
            print(f"Putting Added Value: {self.lru_queue_cache}")
