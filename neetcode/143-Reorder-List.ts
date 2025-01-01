/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
  if (!head || !head.next) return

  let slow = head, fast = head
  while (fast && fast.next) {
    slow = slow.next
    fast = fast.next.next
  }

  let prev = null, curr = slow, temp = null
  while (curr) {
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  }

  let first = head, second = prev
  while (second.next) {
    let tmp1 = first.next
    let tmp2 = second.next
    first.next = second
    second.next = tmp1
    first = tmp1
    second = tmp2
  }
}