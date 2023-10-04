class Solution(object):
    def threeSum(self, nums):
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            # skip the duplicates values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two pointers technique
            l = i + 1
            r = n - 1
            while l < r:
                threeSum = nums[l] + nums[i] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
                    # check if current nums[l] is equal to the prev element nums[l-1]
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
