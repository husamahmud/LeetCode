/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    const map = {}

    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i]
        if (diff in map) return [i, map[diff]]
        else map[nums[i]] = i
    }

    return []
};