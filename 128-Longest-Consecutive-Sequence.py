class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(set(nums)) == 1:
            return 1

        curMax = 1
        maxSeq = 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                curMax += 1
            elif nums[i - 1] == nums[i]:
                continue
            else:
                curMax = 1
            maxSeq = max(curMax, maxSeq)

        return maxSeq
