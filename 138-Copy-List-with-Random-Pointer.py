class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None

        hash_nodes = {}

        curr = head
        while curr is not None:
            hash_nodes[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr is not None:
            cpy_node = hash_nodes[curr]
            cpy_node.next = hash_nodes.get(curr.next)
            cpy_node.random = hash_nodes.get(curr.random)
            curr = curr.next

        return hash_nodes[head]
