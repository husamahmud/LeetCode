function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let dummy = new ListNode(0, head)
  let slow = dummy
  let fast = head

  while (n--) {
    fast = fast.next
  }

  while (fast) {
    slow = slow.next
    fast = fast.next
  }

  slow.next = slow.next.next
  return dummy.next
};