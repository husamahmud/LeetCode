/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
    let splitted = s.trim().split(' ')
    return splitted[splitted.length - 1].length
};