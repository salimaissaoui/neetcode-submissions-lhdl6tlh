class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class O1DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lookup = {}  # key -> node

    # Add to front
    def prepend(self, key):
        if key in self.lookup:
            return  # prevent duplicates (optional)

        new_node = Node(key)
        self.lookup[key] = new_node

        if not self.head:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Add to end
    def append(self, key):
        if key in self.lookup:
            return

        new_node = Node(key)
        self.lookup[key] = new_node

        if not self.tail:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # Remove by key
    def remove(self, key):
        if key not in self.lookup:
            return

        node = self.lookup[key]

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        del self.lookup[key]
    
        # Remove last node (O(1))
    def remove_last(self):
        if not self.tail:
            return None  # empty list

        key = self.tail.key
        self.remove(key)
        return key  # useful for LRU-style usage

    # Move node to front
    def move_to_front(self, key):
        if key not in self.lookup:
            return

        node = self.lookup[key]

        if node == self.head:
            return  # already at front

        self.remove(key)
        self.prepend(key)

    # Print list
    def print_list(self):
        current = self.head
        while current:
            print(current.key, end=" <-> ")
            current = current.next
        print("None")
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = O1DoublyLinkedList()
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        else:
            self.queue.move_to_front(key)
            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.queue.move_to_front(key)
        else:
            if len(self.cache) >= self.capacity:
                remove = self.queue.remove_last()
                del self.cache[remove]

            self.cache[key] = value
            self.queue.prepend(key)