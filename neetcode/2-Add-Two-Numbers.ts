function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  const num1: number[] = [];
  const num2: number[] = [];

  while (l1) {
    num1.unshift(l1.val);
    l1 = l1.next;
  }
  while (l2) {
    num2.unshift(l2.val);
    l2 = l2.next;
  }

  const sum = BigInt(num1.join("")) + BigInt(num2.join(""));
  const digits = sum.toString().split("").reverse();

  const dummy = new ListNode(0);
  let curr = dummy;

  for (const digit of digits) {
    curr.next = new ListNode(Number(digit));
    curr = curr.next;
  }

  return dummy.next;
}