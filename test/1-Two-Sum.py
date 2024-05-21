class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        map = {}

        # Testing the new feat

        for i in range(n):
            dif = target - nums[i]
            if dif in map:
                return [nums.index(dif), i]
            map[nums[i]] = dif
        
        return {-1}
