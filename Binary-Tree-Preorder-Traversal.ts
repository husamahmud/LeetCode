function preorderTraversal(root: TreeNode | null): number[] {
  if (!root) return []

  const dummy: TreeNode = root
  const res: number[] = []

  const rec = (node: TreeNode): void => {
    if (!node) return

    res.push(node.val)
    rec(node.left)
    rec(node.right)
  }

  rec(dummy)
  return res
};