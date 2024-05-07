class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        count = 0
        mod = 10**9 + 7
        nums.sort()

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                count += pow(2, r - l)
                l += 1

        return count % mod
