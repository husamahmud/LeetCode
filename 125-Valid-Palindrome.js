/**
 * @param {string} c
 * @returns {boolean}
 */
var isAlpha = function (c) {
    return /[a-zA-Z0-9]+$/.test(c)
}

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
    let l = 0
    let r = s.length - 1

    while (l < r) {
        if (!isAlpha(s[l])) {
            l++
            continue
        }
        if (!isAlpha(s[r])) {
            r--
            continue
        }

        if (s[l].toLowerCase() !== s[r].toLowerCase())
            return false

        l++
        r--
    }

    return true
};
