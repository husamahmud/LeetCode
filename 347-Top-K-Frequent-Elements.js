/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    let freq = new Map()
    for (let num of nums)
        freq.set(num, (freq.get(num) || 0) + 1)

    let freqEntries = Array.from(freq.entries())
    freqEntries.sort((a, b) => b[1] - a[1])

    let res = []
    for (let i = 0; i < k; i++)
        res.push(freqEntries[i][0])

    return res
};
