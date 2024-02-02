class Solution(object):
    def singleNumber(self, nums):
        uniq = set()

        for num in nums:
            if num in uniq:
                uniq.remove(num)
            else:
                uniq.add(num)

        return uniq
        