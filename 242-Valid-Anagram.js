/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    if (s.length !== t.length)
        return false
    return s.split('').sort().join('') === t.split('').sort().join('')
};

var isAnagram = function (s, t) {
    if (s.length !== t.length)
        return false

    const count = {}

    for (let c of s)
        count[c] = (count[c] || 0) + 1

    console.log(count)

    for (let c of t) {
        if (count[c] === null)
            return false
        count[c]--
    }

    console.log(count)

    for (let key in count)
        if (count[key] !== 0)
            return false

    return true
};

console.log(isAnagram("rat", "car"))
