function reverseList(head: ListNode | null): ListNode | null {
  let curr = head, prev = null

  while (curr) {
    const next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  }

  return prev
};