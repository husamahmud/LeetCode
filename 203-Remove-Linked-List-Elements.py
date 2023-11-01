class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        # handle the case where the list is empty
        if not head:
            return head

        # handle the case where the first node/nodes have the target val
        while head and head.val == val:
            head = head.next

        # traverse the list to remove the nodes with the target val
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
