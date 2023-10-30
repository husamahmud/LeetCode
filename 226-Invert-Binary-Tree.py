class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

    def invertTree(self, root):
        if not root:
            return None

        # swap the left and right children of the current node 
        left = root.left
        right = root.right
        root.left = right
        root.right = left

        # recursively invert the left and right subtrees
        if right:
            self.invertTree(right)
        if left:
            self.invertTree(left)

        return root
