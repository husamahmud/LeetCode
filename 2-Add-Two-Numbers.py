class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # get the values of the current digits
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            # caculate the sum and curry
            total = num1 + num2 + carry
            carry = total // 10

            # create a new node with the summition of digits
            curr.next = ListNode(total % 10)
            curr = curr.next

            # move to the next nodes in both lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
