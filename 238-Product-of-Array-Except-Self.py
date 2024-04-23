class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pre = [1] * n

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        product = 1
        for i in range(n - 1, -1, -1):
            res[i] = product * pre[i]
            product *= nums[i]

        return res