class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        memo = [0] * n
        memo[0], memo[1] = 0, 1

        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n - 1] + memo[n - 2]
