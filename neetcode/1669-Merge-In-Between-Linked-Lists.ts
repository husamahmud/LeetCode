function mergeInBetween(list1: ListNode | null, a: number, b: number, list2: ListNode | null): ListNode | null {
  let start = list1, end = list1, ptr2 = list2

  while (ptr2.next) {
    ptr2 = ptr2.next
  }

  while (a > 1) {
    start = start.next
    a--
  }
  while (b) {
    end = end.next
    b--
  }

  start.next = list2
  ptr2.next = end.next

  return list1
};