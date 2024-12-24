function reverseList(head: ListNode | null): ListNode | null {
  let curr = head, prev = null

  while (curr) {
    const next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  }

  return prev
}

function isPalindrome(head: ListNode | null): boolean {
  let fast = head, slow = head

  while (fast.next && fast.next.next) {
    fast = fast.next.next
    slow = slow.next
  }

  let head2 = reverseList(slow)
  while (head && head2) {
    if (head.val !== head2.val) return false

    head = head.next
    head2 = head2.next
  }

  return true
};