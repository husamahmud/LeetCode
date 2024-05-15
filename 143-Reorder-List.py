class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, nodes = head, []

        while curr:
            nodes.append(curr.val)
            curr = curr.next

        newNodes = []
        l, r = 0, len(nodes) - 1
        while l <= r:
            newNodes.append(nodes[l])
            if l < r:
                newNodes.append(nodes[r])
            l, r = l + 1, r - 1

        for node in newNodes:
            head.val = node
            head = head.next
