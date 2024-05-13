class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0

        # Sol1 DFS
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # Sol2 BFS level traversal
        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return level

