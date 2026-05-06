class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None

        dummy = ListNode()
        dummy.next = head

        l, r, i = dummy, head, 1

        while r:
            if i > n:
                l = l.next

            r = r.next
            i += 1

        if l and l.next:
            l.next = l.next.next

        return dummy.next