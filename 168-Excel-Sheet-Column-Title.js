/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function (columnNumber) {
    let res = "";
    let columnChar;

    while (columnNumber > 0) {
        columnChar = String.fromCharCode(65 + (columnNumber - 1) % 26);
        res = columnChar + res;
        columnNumber = Math.floor((columnNumber - 1) / 26);
    }

    return res;
};
