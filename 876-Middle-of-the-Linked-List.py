class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, count = head, 0
        while curr:
            curr = curr.next
            count += 1

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        if count % 2 == 0:
            return slow.next
        return slow