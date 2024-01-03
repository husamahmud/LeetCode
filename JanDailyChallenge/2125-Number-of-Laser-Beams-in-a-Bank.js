/**
 * Count the number of security devices in a given floor.
 * @param {string} floor
 * @return {number}
 **/
function countLeser(floor) {
    let count = 0;
    for (let i = 0; i < floor.length; i++)
        if (floor[i] === "1") count++;
    return count;
}

/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function (bank) {
    let prevLeserCount = 0,
        currLeserCount = 0,
        total = 0;

    for (let i = 0; i < bank.length; i++) {
        currLeserCount = countLeser(bank[i]);
        if (currLeserCount === 0) continue;

        total += currLeserCount * prevLeserCount;
        prevLeserCount = currLeserCount;
    }

    return total;
};
