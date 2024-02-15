class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
            
        lDepth = self.maxDepth(root.left)        
        rDepth = self.maxDepth(root.right)

        if lDepth > rDepth:
            return lDepth + 1
        return rDepth + 1 