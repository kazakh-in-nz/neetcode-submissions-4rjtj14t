class Node:
    def __init__(self, key:int, val:int):
        self.k = key
        self.v = val
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.c = capacity
        self.s = 0
        self.t = [None] * capacity

    def _hash(self, key):
        return key % self.c

    def insert(self, key: int, value: int) -> None:
        idx = self._hash(key)
        node = self.t[idx]

        if not node:
            self.t[idx] = Node(key, value)
            self.s += 1
        else:
            prev = None

            while node:
                if node.k == key:
                    node.v = value
                    return

                prev, node = node, node.next

            prev.next = Node(key, value)
            self.s += 1
        
        if self.s/self.c >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        idx = self._hash(key)
        node = self.t[idx]

        while node:
            if node.k == key:
                return node.v
            
            node = node.next
        
        return -1

    def remove(self, key: int) -> bool:
        idx = self._hash(key)
        node = self.t[idx]
        prev = None

        while node:
            if node.k == key:
                if prev:
                    prev.next = node.next
                else:
                    self.t[idx] = node.next

                self.s -= 1
                return True       

            prev, node = node, node.next

        return False


    def getSize(self) -> int:
        return self.s

    def getCapacity(self) -> int:
        return self.c

    def resize(self) -> None:
        new_c = self.c * 2
        new_t = [None] * new_c

        for node in self.t:
            while node:
                idx = self._hash(node.k)

                if not new_t[idx]:
                    new_t[idx] = Node(node.k, node.v)
                else:
                    new_node = new_t[idx]

                    while new_node.next:
                        new_node = new_node.next

                    new_node.next = Node(node.k, node.v)

                node = node.next

        self.c = new_c
        self.t = new_t

