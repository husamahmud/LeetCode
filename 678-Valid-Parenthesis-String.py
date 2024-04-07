class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0  # Minimum number of '(' needed to balance ')'
        max_open = 0  # Maximum number of '(' treated as potential '(' or '*'
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                if min_open > 0:
                    min_open -= 1
                max_open -= 1
            elif char == '*':
                if min_open > 0:
                    min_open -= 1
                max_open += 1
            
            # If at any point, max_open becomes negative, it means too many ')' are used
            if max_open < 0:
                return False
        
        # After processing all characters, all '(' should be balanced
        return min_open == 0
