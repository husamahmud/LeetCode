class Solution:
    def fib(self, n: int) -> int:
        # 3: Recursive solution optimized
        memo = {}

        def fib_memo(i: int) -> int:
            if i == 0 or i == 1:
                return i
            if i in memo:
                return memo[i]

            res = fib_memo(i - 1) + fib_memo(i - 2)
            memo[i] = res
            return res

        return fib_memo(n)

        # 2: Recursive solution
        # if n == 0 or n == 1:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)

        # 1: Iterative solutions
        # if n == 0 or n == 1:
        #     return n
        # memo = [0] * n
        # memo[0], memo[1] = 0, 1

        # for i in range(2, n):
        #     memo[i] = memo[i - 1] + memo[i - 2]
        # return memo[n - 1] + memo[n - 2]
