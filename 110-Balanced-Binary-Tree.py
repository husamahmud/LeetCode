class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lHeight = self.height(root.left)
        rHeight = self.height(root.right)
        return max(lHeight, rHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        lHeight = self.height(root.left)
        rHeight = self.height(root.right)
        if abs(lHeight - rHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
