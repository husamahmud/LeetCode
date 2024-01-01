/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
    let count = 0, child = 0, cookie = 0;

    g = g.sort((a, b) => a - b);
    s = s.sort((a, b) => a - b);

    while (child < g.length && cookie < s.length) {
        if (g[child] <= s[cookie]) {
            count++;
            child++;
            cookie++;
        } else {
            cookie++;
        }
    }

    return count;
};
