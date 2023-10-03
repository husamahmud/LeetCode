class Solution(object):
    def threeSum(self, nums):
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

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
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res


if __name__ == '__main__':
    nums = [0, 0, 0]
    res = []
    l = 0
    m = l + 1
    r = len(nums) - 1

    nums.sort()
    while m < r:
        if nums[r] + nums[m] + nums[l] > 0:
            r -= 1
        elif nums[r] + nums[m] + nums[l] < 0:
            l += 1
            m += 1
        if nums[r] + nums[m] + nums[l] == 0:
            res.append([nums[r], nums[m], nums[l]])
            l += 1
            m += 1
    print(res)
