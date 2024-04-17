class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def dfs(node: TreeNode, path: str) -> str:
            if not node:
                return ""

            path = chr(node.val + ord("a")) + path

            if node.right and node.left:
                return min(dfs(node.left, path), dfs(node.right, path))
            if node.right:
                return dfs(node.right, path)
            if node.left:
                return dfs(node.left, path)

            return path
        
        return dfs(root, "")