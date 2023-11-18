class Solution(object):
    def missingNumber(self, nums):
        """
        1. Calc the expected sum of numbers from 0 to n using formula:
        `(n * (n + 1)) // 2`
        2. Iterate through each element in the nums array and subtract it from
        the expected_sum
        3. The remaining value of expected_sum will be the missing number
        """
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2

        for num in nums:
            expected_sum -= num

        return expected_sum

    def missingNumber(self, nums):
        """
        1. Create a set of numbers from 0 to the length of nums
        2. Convert the nums array into a set to remove duplicates
        3. Calculate the set difference between the two sets to find the missing number
        4. Convert the resulting set into a list and retrieve the first element
        which represents the missing number
        """
        return list(set(range(0, len(nums) + 1)).difference(set(nums)))[0]
