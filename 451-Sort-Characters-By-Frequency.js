/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function (s) {
    let freq = new Map()
    for (let c of s)
        freq.set(c, (freq.get(c) || 0) + 1)

    let sortedEntries = Array.from(freq.entries())
    sortedEntries.sort((a, b) => b[1] - a[1])

    let sorted_s = ""
    for (let [char, count] of sortedEntries)
        sorted_s += char.repeat(count)

    return sorted_s
};
