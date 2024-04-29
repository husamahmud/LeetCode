class Solution:
    def deleteNode(self, node):
        deleted, curr = node, node

        while deleted.next:
            deleted.val, deleted.next.val = deleted.next.val, deleted.val
            deleted = deleted.next

        while curr.next != deleted:
            curr = curr.next

        curr.next = None