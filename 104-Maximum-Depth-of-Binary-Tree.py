class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)

        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1
