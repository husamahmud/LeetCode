function reorderList(head: ListNode | null): void {
  const nodes: number[] = []
  let curr = head

  while (curr) {
    nodes.push(curr.val)
    curr = curr.next
  }

  const reorderedNodes = []
  let l = 0, r = nodes.length - 1
  while (l <= r) {
    reorderedNodes.push(nodes[l])
    if (l < r) reorderedNodes.push(nodes[r])
    l++, r--
  }

  curr = head
  for (const node of reorderedNodes) {
    curr.val = node
    curr = curr.next
  }
};

/* 
  1 2 3 4
  slow -> 2

  1 2 3 4 5
  slow -> 3
*/