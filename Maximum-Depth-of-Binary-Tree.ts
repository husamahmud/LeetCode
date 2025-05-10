function maxDepth(root: TreeNode | null): number {
  if (!root) return 0

  const lDepth = maxDepth(root.left)
  const rDepth = maxDepth(root.right)

  return Math.max(lDepth, rDepth) + 1
}