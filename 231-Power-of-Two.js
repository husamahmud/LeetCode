/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function (n) {
    if (n > 2) return isPowerOfTwo(n / 2)
    else return n === 2 || n === 1;
};
