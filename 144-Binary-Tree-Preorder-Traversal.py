class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        def traversal(root: TreeNode) -> None:
            if not root:
                return
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)
        return res        