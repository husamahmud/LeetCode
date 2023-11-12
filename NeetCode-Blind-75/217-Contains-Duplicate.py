class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

    def containsDuplicate(self, nums):
        uniq = set()
        for num in nums:
            if num in uniq:
                return True
            uniq.add(nums)
        return False
