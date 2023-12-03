/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    let hash = new Map();

    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i]
        if (hash.has(diff))
            return [hash.get(diff), i]
        hash.set(nums[i], i)
    }

    return []
}

var twoSum = function (nums, target) {
    for (let i = 0; i < nums.length; i++)
        for (let j = i + 1; j < nums.length; j++)
            if (nums[i] + nums[j] === target)
                return [i, j]
    return []
}
