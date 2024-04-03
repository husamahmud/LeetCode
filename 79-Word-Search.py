class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set() # set to keep track of the visited cells

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word): # base case if the entire word is found
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols or # out of bounds
                word[idx] != board[r][c] or # character mismatch
                (r, c) in visited): # already visited cell
                return False

            visited.add((r, c)) # mark the current cell from as visited

            # explore neighbors using DFS recursively
            res = (dfs(r + 1, c, idx + 1) or # move down
                   dfs(r - 1, c, idx + 1) or # move up
                   dfs(r, c + 1, idx + 1) or # move right
                   dfs(r, c - 1, idx + 1)) # move left

            # unmark the current cell from visited after exploring neighbors
            visited.remove((r, c))

            # return True if the word is found in any exploration path
            return res

        # iterate through all cells in the board
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): # start DFS from each unvisited cell
                    return True

        return False
