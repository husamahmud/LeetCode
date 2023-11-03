class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def middleNode(self, head):
        n = 0

        curr = head
        while curr is not None:
            n += 1
            curr = curr.next

        curr = head
        for _ in range(n // 2):
            curr = curr.next

        return curr
