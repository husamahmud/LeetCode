class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in freq:
                return [nums.index(dif), i]
            freq[nums[i]] = dif

        return {-1}
