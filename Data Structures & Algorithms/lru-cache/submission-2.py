from collections import defaultdict
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.m = {}
        self.head = None
        self.tail = None

    def _detach(self, n: Node):
        if n.next:
            n.next.prev = n.prev
        else:
            self.tail = n.prev

        if n.prev:
            n.prev.next = n.next
        else:
            self.head = n.next
        
        n.next, n.prev = None, None

    def _insert_to_head(self, n: Node):
        if not self.head:
            self.head = n
            self.tail = n
            return

        n.next, self.head.prev = self.head, n
        self.head = n

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        n = self.m[key]
        self._detach(n)
        self._insert_to_head(n)

        return n.value

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key].value = value
            self._detach(self.m[key])
            self._insert_to_head(self.m[key])
            return

        n = Node(key, value)
        self.m[key] = n
        self._insert_to_head(n)

        if len(self.m) > self.cap:
            t = self.tail
            self._detach(t)
            self.m.pop(t.key)