class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0
        pathToLeaf = []
        path = []

        def traversal(root: TreeNode) -> list:
            # nonlocal result
            # nonlocal pathToLeaf
            # nonlocal path

            if not root:
                return []
            elif not root.left and not root.right:
                path.append(root.val)
                pathToLeaf.append(path.copy())
                path.pop()
                return pathToLeaf

            path.append(root.val)
            traversal(root.left)
            traversal(root.right)
            path.pop()

        traversal(root)
        for p in pathToLeaf:
            res = 0
            for num in p:
                res = res * 10 + num
            result += res

        return result

        