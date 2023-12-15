/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function (num) {
    let l = 1, r = num

    while (l <= r) {
        let m = Math.floor((l + r) / 2)

        if (num === Math.pow(m, 2)) return true
        else if (num < Math.pow(m, 2)) r = m - 1
        else l = m + 1
    }

    return false
};
