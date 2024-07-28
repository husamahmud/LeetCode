function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  let dummy = new ListNode()
  let curr = dummy

  while (list1 && list2) {
    if (list1.val >= list2.val) {
      curr.next = list2
      list2 = list2.next
    } else {
      curr.next = list1
      list1 = list1.next
    }

    curr = curr.next
  }

  if (list1) curr.next = list1
  if (list2) curr.next = list2

  return dummy.next
};