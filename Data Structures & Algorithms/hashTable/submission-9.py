class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.m: List[Node | None] = [None] * capacity
    
    def _hash(self, key):
        return key % self.cap

    def insert(self, key: int, value: int) -> None:
        idx = self._hash(key)
        n = self.m[idx]

        if not n:
            self.m[idx] = Node(key, value)
            self.size += 1
        else:
            prev = None

            while n:
                if n.key == key:
                    n.value = value
                    return
                
                prev, n = n, n.next
            
            prev.next = Node(key, value)
            self.size += 1

        if self.size >= self.cap / 2:
            self.resize()


    def get(self, key: int) -> int:
        idx = self._hash(key)
        n = self.m[idx]

        while n:
            if n.key == key:
                return n.value
            
            n = n.next

        return -1

    def remove(self, key: int) -> bool:
        idx = self._hash(key)
        n = self.m[idx]
        prev = None

        while n:
            if n.key == key:
                self.size -= 1

                if not prev: self.m[idx] = n.next
                else: prev.next = n.next

                return True

            prev, n = n, n.next

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        new_cap = self.cap * 2
        new_m = [None] * new_cap

        for n in self.m:
            while n:
                idx = self._hash(n.key)

                if not new_m[idx]:
                    new_m[idx] = Node(n.key, n.value)
                else:
                    new_n = new_m[idx]
                    while new_n.next:
                        new_n = new_n.next
                    
                    new_n.next = Node(n.key, n.value)

                n = n.next
        self.cap = new_cap
        self.m = new_m



