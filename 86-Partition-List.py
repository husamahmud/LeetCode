class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        bigger, smaller = [], []

        while curr:
            if curr.val >= x:
                bigger.append(curr.val)
            else:
                smaller.append(curr.val)
            curr = curr.next

        curr = head
        i = 0
        while i < len(smaller):
            curr.val = smaller[i]
            i += 1
            curr = curr.next

        i = 0
        while i < len(bigger):
            curr.val = bigger[i]
            i += 1
            curr = curr.next

        return head