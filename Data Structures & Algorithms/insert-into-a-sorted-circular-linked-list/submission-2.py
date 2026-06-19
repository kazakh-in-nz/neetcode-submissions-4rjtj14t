# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new = Node(insertVal)

        if not head:
            new.next = new
            return new

        prev, curr = head, head.next

        while True:
            if prev.val <= new.val <= curr.val:
                break

            if prev.val > curr.val:
                if prev.val <= new.val or new.val <= curr.val:
                    break

            prev, curr = curr, curr.next

            if prev == head:
                break

        prev.next, new.next = new, curr
        return head
        