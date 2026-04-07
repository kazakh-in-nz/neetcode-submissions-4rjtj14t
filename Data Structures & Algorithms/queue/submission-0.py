class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return not self.head and not self.tail

    def append(self, value: int) -> None:
        n = Node(value)

        if not self.tail:
            self.head = n
            self.tail = n
            return

        n.prev, self.tail.next = self.tail, n
        self.tail = n

    def appendleft(self, value: int) -> None:
        n = Node(value)

        if not self.head:
            self.head = n
            self.tail = n
            return

        n.next, self.head.prev = self.head, n
        self.head = n
        
    def pop(self) -> int:
        if not self.tail:
            return -1

        lst = self.tail

        if not lst.prev:
            self.tail, self.head = None, None
        else:
            self.tail, self.tail.next = lst.prev, None
        
        return lst.value 

    def popleft(self) -> int:
        if not self.head:
            return -1

        fst = self.head

        if not fst.next:
            self.head, self.tail = None, None
        else:
            self.head, self.head.prev = fst.next, None
        
        return fst.value 
        
