class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head

        for i in range(k - 1):
            if not fast:
                return head
            fast = fast.next

        st = fast
        fast = fast.next

        while fast:
            slow, fast = slow.next, fast.next

        st.val, slow.val = slow.val, st.val
        return head
