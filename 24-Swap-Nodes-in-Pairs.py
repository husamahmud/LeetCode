class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr, prev = head, dummy

        while curr and curr.next:
            next = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = next
            prev.next = second

            prev = curr
            curr = next

        return dummy.next
