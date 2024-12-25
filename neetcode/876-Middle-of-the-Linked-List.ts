function middleNode(head: ListNode | null): ListNode | null {
  let n = 0, m = 0

  let curr = head
  while (curr) {
    curr = curr.next
    n++
  }

  m = Math.floor(n / 2)
  curr = head
  while (m--) {
    curr = curr.next
  }

  return curr
};