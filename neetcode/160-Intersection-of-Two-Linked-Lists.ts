function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
  if (!headA || !headB) return null;

  let lenA = 0, lenB = 0
  let ptrA = headA, ptrB = headB
  while (ptrA) {
    ptrA = ptrA.next
    lenA++
  }
  while (ptrB) {
    ptrB = ptrB.next
    lenB++
  }

  let dif = Math.abs(lenA - lenB)
  if (lenA > lenB) {
    while (dif--) headA = headA.next
  } else if (lenA < lenB) {
    while (dif--) headB = headB.next
  }

  while (headA && headB) {
    if (headA === headB) return headA
    headA = headA.next
    headB = headB.next
  }

  return null
};