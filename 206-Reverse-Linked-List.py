class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev
        return head

    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        revTail = head.next
        newHead = self.reverseList(head.next)
        revTail.next = head
        head.next = None

        return newHead
