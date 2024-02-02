class Solution(object):
    def singleNumber(self, nums):
        sum_of_nums = sum(nums)
        sum_of_uniq = sum(set(nums))

        return 2 * sum_of_uniq - sum_of_nums