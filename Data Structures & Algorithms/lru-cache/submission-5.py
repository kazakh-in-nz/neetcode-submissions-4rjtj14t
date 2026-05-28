class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity
        self.old = None
        self.new = None

    def _detach(self, n: Node) -> None:
        prev, nxt = n.prev, n.next

        if prev: prev.next = nxt
        else: self.old = nxt

        if nxt: nxt.prev = prev
        else: self.new = prev

        n.next, n.prev = None, None

    def _attach(self, n: Node) -> None:
        if not self.old and not self.new:
            self.old = n
            self.new = n
            return

        self.new.next, n.prev = n, self.new
        self.new = n
        
    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        n = self.m[key]
        self._detach(n)
        self._attach(n)

        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key].val = value
            self._detach(self.m[key])
            self._attach(self.m[key])
            return

        n = Node(key, value)
        self.m[key] = n
        self._attach(n)

        if len(self.m) > self.capacity:
            old = self.old
            self._detach(self.old)
            self.m.pop(old.key)


         
