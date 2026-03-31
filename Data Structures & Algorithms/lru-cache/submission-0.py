class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # dummy head and tail to simplify pointer logic
        self.head = Node(0, 0)   # LRU side
        self.tail = Node(0, 0)   # MRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    # remove node from DLL
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    # insert node at tail (MRU)
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
            return

        if len(self.cache) >= self.capacity:
            # real LRU is head.next
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

        node = Node(key, value)
        self.cache[key] = node
        self._add(node)