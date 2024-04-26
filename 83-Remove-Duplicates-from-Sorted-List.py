class Solution:
    def removeContiguous(self, head: ListNode) -> ListNode:
        curr, next = head, head.next
        
        while next and curr.val == next.val:
            next = next.next
        
        curr.next = next
        return curr

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if head.val == head.next.val:
            new_head = self.removeContiguous(head)
            head = new_head
        
        curr, next = head, head.next
        while next:
            if next.val == curr.val:
                curr = self.removeContiguous(curr)
                next = curr.next
            else:
                next, curr = next.next, curr.next
        
        return head
        