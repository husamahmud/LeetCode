class Solution(object):
    def singleNumber(self, nums):
        uniq = set()
        for num in nums:
            if num not in uniq:
                uniq.add(num)
            else:
                uniq.remove(num)
        return list(uniq)[0]

    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num) == 1:
                return num

    def singleNumber(self, nums):
        nums.sort()
        for i in range(0, len(nums), 2):
            if i + 1 == len(nums) or nums[i] != nums[i + 1]:
                return nums[i]
