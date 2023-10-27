class Solution(object):
    def hasCycle(self, head):  # fast and slow pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle(self, head):  # using set
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

    def hasCycle(self, head):  # modifying the linked list
        while head:
            if head.val == float('inf'):
                return True
            head.val = float('inf')
            head = head.next
        return False
