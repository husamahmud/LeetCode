class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return

            if root.left and not root.left.left and not root.left.right:
                res += root.left.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res
