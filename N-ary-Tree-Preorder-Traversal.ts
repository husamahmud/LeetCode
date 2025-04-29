function preorder(root: _Node | null): number[] {
  if (!root) return []

  const queue: _Node[] = [root]
  const res: number[] = []

  while (queue.length) {
    const node = queue.shift()
    res.push(node.val)
    queue.unshift(...node.children)
  }

  return res
}
