/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
    return nums.length !== (new Set(nums)).size
};

var containsDuplicate = function (nums) {
    const map = new Map()

    for (let num of nums) {
        if (map.has(num))
            return true
        map.set(num, true)
    }

    return false
};

var containsDuplicate = function (nums) {
    nums.sort()

    for (let i = 1; i < nums.length; i++)
        if (nums[i] === nums[i - 1])
            return true

    return false
}
