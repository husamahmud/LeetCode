/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function diameterOfBinaryTree(root: TreeNode | null): number {
  let res = 0

  const rec = (root: TreeNode) => {
    if (!root) return 0

    const leftHeight = rec(root.left)
    const rightHeight = rec(root.right)

    res = Math.max(res, leftHeight + rightHeight)
    return Math.max(leftHeight, rightHeight) + 1
  }

  rec(root)
  return res
};