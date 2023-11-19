class Solution(object):
    def climbStairs(self, n):
        """
        1. Initialize the ways list with [1, 1] representing the number of
            ways to climb the first two steps.
        2. Iterate from 2 to n, representing the remaining steps.
        3. For each step i, calculate the number of ways to reach that step
            by summing the values of ways[i - 1] and ways[i - 2].
        4. Return ways[n], which represents the total number of ways to climb
            n stairs.
        """
        no_of_ways = [1] * (n + 1)

        for i in range(2, n + 1):
            no_of_ways[i] = no_of_ways[i - 1] + no_of_ways[i - 2]

        return no_of_ways[-1]
