/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    if (!strs.length) return ''
    strs = strs.sort((a, b) => a.length - b.length)
    let pref = ''

    for (let i = 0; i < strs[0].length; i++) {
        let c = strs[0][i]
        if (!c) return ''

        if (strs.every(s => s[i] === c)) pref += c
        else break
    }

    return pref
};