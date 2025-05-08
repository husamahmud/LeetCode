function postorderTraversal(root: TreeNode | null): number[] {
  if (!root) return []

  const dummy: TreeNode = root
  const res: number[] = []

  const rec = (node: TreeNode): void => {
    if (!node) return

    rec(node.left)
    rec(node.right)
    res.push(node.val)
  }

  rec(dummy)
  return res
};