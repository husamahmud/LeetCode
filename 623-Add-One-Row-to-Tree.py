class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        def addNodes(node: Optional[TreeNode], curDepth: int):
            if not node:
                return

            curDepth -= 1

            if curDepth == 1:
                newLeft = TreeNode(val)
                newRight = TreeNode(val)
                newLeft.left = node.left
                newRight.right = node.right
                node.left = newLeft
                node.right = newRight
            else:
                addNodes(node.left, curDepth)
                addNodes(node.right, curDepth)

        addNodes(root, depth)
        return root
