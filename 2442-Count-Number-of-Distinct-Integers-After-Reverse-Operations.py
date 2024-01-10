class Solution(object):
    def revNum(self, num):
        if num < 10:
            return num
        return int(str(num)[::-1])

    def countDistinctIntegers(self, nums):
        revNumsList = []
        for num in nums:
            revNumsList.append(self.revNum(num))

        return len(set(nums + revNumsList))
