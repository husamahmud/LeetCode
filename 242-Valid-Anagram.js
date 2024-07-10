/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    const freq = {}

    for (const c of s) {
        if (freq[c]) freq[c]++
        else freq[c] = 1
    }

    for (const c of t) {
        if (!freq[c]) return false
        else freq[c]--
    }

    for (const key in freq) {
        if (freq[key] !== 0) return false
    }

    return true
};