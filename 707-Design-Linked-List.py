class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        curr = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = curr
            self.head = new_node
        else:
            for _ in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1
