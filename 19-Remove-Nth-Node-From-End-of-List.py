class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        for _ in range(n):
            head = head.next

        while head:
            head, curr = head.next, curr.next

        curr.next = curr.next.next
        return dummy.next
