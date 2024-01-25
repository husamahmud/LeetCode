class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def merge(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.merge(list1.next, list2)
            return list1
        else:
            list2.next = self.merge(list2.next, list1)
            return list2

    def mergeTwoLists(self, list1, list2):
        newHead = self.merge(list1, list2)
        return newHead


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val >= list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next
