class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nums = []
        curr = head

        while curr:
            nums.append(curr.val)
            curr = curr.next

        nums.sort()
        curr = dummy

        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next        