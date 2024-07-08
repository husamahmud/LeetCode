/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function (nums) {
    let sign = nums.reduce((acc, num) => {
        if (num > 0) return acc
        else if (num < 0) return -acc
        else return 0
    }, 1)

    return sign
};