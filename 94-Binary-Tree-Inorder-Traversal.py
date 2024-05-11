class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        def traversal(root: TreeNode) -> None:
            if not root:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        
        traversal(root)
        return res
            
