/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function (s, t) {
    let stk_s = []
    let stk_t = []

    for (let i = 0; i < s.length; i++)
        if (s[i] === '#') stk_s.pop()
        else stk_s.push(s[i])
    for (let i = 0; i < t.length; i++)
        if (t[i] === '#') stk_t.pop()
        else stk_t.push(t[i])

    return stk_t.toString() === stk_s.toString()
};
