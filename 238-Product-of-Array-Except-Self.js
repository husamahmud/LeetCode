/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
    let n = nums.length
    let pref = new Array(n).fill(1)
    let suff = new Array(n).fill(1)
    let ans = new Array(n)

    for (let i = 1; i < n; i++)
        pref[i] = pref[i - 1] * nums[i - 1]

    for (let i = n - 2; i >= 0; i--)
        suff[i] = suff[i + 1] * nums[i + 1]

    for (let i = 0; i < n; i++)
        ans[i] = pref[i] * suff[i]

    return ans
};
var productExceptSelf = function (nums) {
    let n = nums.length
    let ans = new Array(n)
    let product = 1

    for (let i = 0; i < n; i++) {
        ans[i] = product
        product *= nums[i]
    }

    product = 1
    for (let i = n - 1; i >= 0; i--) {
        ans[i] *= product
        product *= nums[i]
    }

    return ans
};
