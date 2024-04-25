class Solution:
    def removeContiguous(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        if not head:
            return None
        
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        new_head = self.removeContiguous(head, val)
        if not new_head:
            return None
        
        head = new_head
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head
