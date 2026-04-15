class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index > self.length - 1 or self.length == 0:
            return -1

        i, curr = 0, self.head

        while curr:
            if i == index:
                return curr.val
            
            curr = curr.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        n = Node(val)
        self.length += 1

        if not self.head:
            self.head = n
            self.tail = n
            return
        
        n.next, self.head.previous = self.head, n
        self.head = n

    def insertTail(self, val: int) -> None:
        n = Node(val)
        self.length += 1

        if not self.tail:
            self.tail = n
            self.head = n
            return
        
        n.previous, self.tail.next = self.tail, n
        self.tail = n

    def remove(self, index: int) -> bool:
        if index > self.length - 1 or self.length == 0:
            return False

        i, curr = 0, self.head

        while curr:
            if i == index:
                prev = curr.previous
                nxt = curr.next

                if prev:
                    prev.next = nxt
                else:
                    self.head = nxt

                if nxt:
                    nxt.previous = prev
                else:
                    self.tail = prev

                self.length -= 1
                return True

            curr = curr.next
            i += 1

        return False

    def getValues(self) -> List[int]:
        res = []

        curr = self.head

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res
