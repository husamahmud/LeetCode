class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB

        while nodeA is not None:
            nodeA = nodeA.next
            lenA += 1
        while nodeB is not None:
            nodeB = nodeB.next
            lenB += 1

        nodeA, nodeB = headA, headB
        for _ in range(lenA - lenB):
            nodeA = nodeA.next
        for _ in range(lenB - lenA):
            nodeB = nodeB.next

        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next

        return None
