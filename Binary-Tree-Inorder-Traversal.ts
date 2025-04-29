function inorderTraversal(root: TreeNode | null): number[] {
  if (!root) return []

  const dummy: TreeNode = root
  const res: number[] = []

  const rec = (node: TreeNode): void => {
    if (!node) return

    rec(node.left)
    res.push(node.val)
    rec(node.right)
  }
  
  rec(dummy)
  return res
};