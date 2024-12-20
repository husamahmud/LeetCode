function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  if (!list1 && !list2) return null

  let dummy = new ListNode(0)
  let cur = dummy

  let head1 = list1
  let head2 = list2

  while (head1 && head2) {
    if (head1.val >= head2.val) {
      cur.next = new ListNode(head2.val)
      head2 = head2.next
    } else {
      cur.next = new ListNode(head1.val)
      head1 = head1.next
    }

    cur = cur.next
  }

  if (head1) cur.next = head1
  if (head2) cur.next = head2

  return dummy.next
};