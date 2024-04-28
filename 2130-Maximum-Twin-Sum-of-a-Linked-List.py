class Solution:
    def revList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        tail = self.revList(slow.next)

        res = 0
        while head and tail:
            curMax = head.val + tail.val
            res = max(res, curMax)
            head, tail = head.next, tail.next

        return res
