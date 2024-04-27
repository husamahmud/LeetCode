class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return None

        lenA = lenB = 0
        a, b = headA, headB

        while a:
            a = a.next
            lenA += 1

        while b:
            b = b.next
            lenB += 1

        if lenA < lenB:
            for i in range(lenB - lenA):
                headB = headB.next
        else:
            for i in range(lenA - lenB):
                headA = headA.next

        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next

        return None