class Node:
    def __init__(self, val):
        self.val = val
        self.next, self.prev = None, None

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index > self.length - 1 or self.length == 0:
            return -1

        i = 0
        curr = self.head

        while i <= index:
            if i == index:
                return curr.val
            
            curr = curr.next
            i += 1

    def insertHead(self, val: int) -> None:
        self.length += 1

        new = Node(val)

        if self.head == None:
            self.head = new
            self.tail = new
            return
        
        self.head.prev, new.next = new, self.head
        self.head = new

    def insertTail(self, val: int) -> None:
        self.length += 1

        new = Node(val)

        if self.tail == None:
            self.head = new
            self.tail = new
            return

        self.tail.next, new.prev = new, self.tail
        self.tail = new

    def remove(self, index: int) -> bool:
        if index > self.length - 1 or self.length == 0:
            return False

        i = 0
        curr = self.head

        while i <= index:
            if i == index:
                nxt, prev = curr.next, curr.prev

                if prev: prev.next = nxt
                else: self.head = nxt
                
                if nxt: nxt.prev = prev
                else: self.tail = prev
                
                self.length -= 1
                
                return True
            
            curr = curr.next
            i += 1

    def getValues(self) -> List[int]:
        vals = []
        n = self.head

        while n:
            vals.append(n.val)
            n = n.next
        return vals