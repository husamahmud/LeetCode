function removeElements(head: ListNode | null, val: number): ListNode | null {
  let dummy = new ListNode(0, null)
  dummy.next = head
  let curr = dummy

  while (curr) {
    while (curr.next && curr.next.val === val) {
      curr.next = curr.next.next
    }

    curr = curr.next
  }

  return dummy.next
};