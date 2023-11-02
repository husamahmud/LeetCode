class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rev(self, head):
        curr = head
        prev_node = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        head = prev_node
        return head

    def isPalindrome(self, head):
        # empty list or a single-node list is a palindrome
        if not head or not head.next:
            return True

        # find the middle node of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linked list
        second_half = self.rev(slow.next)

        # compare the first half and the reversed second half
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
