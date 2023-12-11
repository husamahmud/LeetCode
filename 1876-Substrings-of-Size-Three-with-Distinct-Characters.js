/**
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function (s) {
    let count = 0
    s = s.split("")

    for (let i = 0; i < s.length - 2; i++) {
        let window = new Set(s.slice(i, i + 3))
        if (window.size === 3) count++
    }

    return count
};
