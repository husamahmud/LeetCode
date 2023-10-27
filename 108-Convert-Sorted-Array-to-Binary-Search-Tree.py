class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        n = len(nums)
        mid = n // 2

        root = TreeNode(nums[mid])

        # left subtree of the root has values < arr[mid]
        root.left = self.sortedArrayToBST(nums[:mid])
        # rightF subtree of the root has values > arr[mid]
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
