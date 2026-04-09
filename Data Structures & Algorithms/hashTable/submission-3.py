class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key: int):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        idx = self._hash(key)
        node = self.table[idx]

        if not node:
            self.table[idx] = Node(key, value)
            self.size += 1
        else:
            prev = None

            while node:
                if node.key == key:
                    node.val = value
                    return

                prev, node = node, node.next

            prev.next = Node(key, value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        idx = self._hash(key)
        node = self.table[idx]

        while node:
            if node.key == key:
                return node.val

            node = node.next
        
        return -1
        
    def remove(self, key: int) -> bool:
        idx = self._hash(key)
        node = self.table[idx]

        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[idx] = node.next
                
                self.size -= 1
                return True

            prev, node = node, node.next

        return False
        
    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_cap = self.capacity * 2
        new_table = [None] * new_cap

        for node in self.table:
            while node:
                idx = node.key % new_cap
                
                if new_table[idx] is None:
                    new_table[idx] = Node(node.key, node.val)
                else:
                    new_node = new_table[idx]
                    while new_node.next:
                        new_node = new_node.next
                    
                    new_node.next = Node(node.key, node.val)

                node = node.next
        
        self.capacity = new_cap
        self.table = new_table
