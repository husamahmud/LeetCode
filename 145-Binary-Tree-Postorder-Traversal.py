class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] 