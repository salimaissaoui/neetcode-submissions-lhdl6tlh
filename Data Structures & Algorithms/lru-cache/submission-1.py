from collections import deque
class LRUCache:

    def __init__(self, capacity: int, cache = {}, queue = deque()):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache[key]

            


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                remove = self.queue.popleft()
                del self.cache[remove]
            self.queue.append(key)
            self.cache[key] = value