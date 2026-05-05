# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        if not head.next:
            return False

        fast, slow = head.next.next, head.next

        while slow and fast:
            if fast == slow:
                return True

            slow = slow.next
            fast = fast.next.next if fast.next else None

        return False