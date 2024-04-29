class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1, num2, res = \\, \\, 0
        res = i = 0
        dummy = ListNode(0)
        curr = dummy

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        print(num1)

        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        print(num2)

        res = str(int(num1) + int(num2))

        while i < len(res):
            curr.next = ListNode(int(res[i]))
            curr = curr.next
            i += 1

        return dummy.next
