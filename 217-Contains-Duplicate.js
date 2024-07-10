/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
    const s = new Set(nums)
    return s.size !== nums.length
};