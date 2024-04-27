class Solution:
    def rearrangeList(self, arr: List) -> List:
        res = []
        l, r = 0, len(arr) - 1

        while l <= r:
            res.append(arr[l])
            if l != r:
                res.append(arr[r])
            l += 1
            r -= 1

        return res

    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes, curr = [], head

        while curr:
            nodes.append(curr.val)
            curr = curr.next

        nodes = self.rearrangeList(nodes)
        for node in nodes:
            head.val = node
            head = head.next
