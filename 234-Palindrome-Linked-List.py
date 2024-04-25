class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        next_half, cur = self.reverseList(slow.next), head

        while next_half:
            if cur.val != next_half.val:
                return False
            cur, next_half = cur.next, next_half.next

        return True
