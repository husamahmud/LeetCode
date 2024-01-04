/**
 * @param {number[]} nums
 * @returns {Map<number, number>}
 */
function calcNumsFreq(nums) {
    let freq = new Map();
    for (let num of nums) {
        let count = (freq.get(num) || 0) + 1;
        freq.set(num, count);
    }
    return freq;
}

/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function (nums) {
    let freq = calcNumsFreq(nums);
    let count = 0;

    for (let val of freq.values()) {
        if (val === 1) return -1;
        count += Math.ceil(val / 3);
    }

    return count;
};
