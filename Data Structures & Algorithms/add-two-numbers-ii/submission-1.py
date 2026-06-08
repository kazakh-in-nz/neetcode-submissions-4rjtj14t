# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self._reverse(l1)
        l2 = self._reverse(l2)
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s // 10
            val = s % 10

            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        l = l1 if l1 else l2

        while l:
            s = l.val + carry
            carry = s // 10
            val = s % 10

            curr.next = ListNode(val)
            curr = curr.next
            l = l.next
        
        if carry > 0:
            curr.next = ListNode(carry)

        res = self._reverse(dummy.next)

        return res




            
        