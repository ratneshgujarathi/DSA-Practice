class Node:
    def __init__(self, key, val, prev=None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev


    def _add_to_front(self, node):
        front = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = front
        front.prev = node


    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.val

        return -1

    def put(self, key, val):
        if key in self.cache:
            self._remove(self.cache[key])
        new_node = Node(key, val)
        self._add_to_front(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]