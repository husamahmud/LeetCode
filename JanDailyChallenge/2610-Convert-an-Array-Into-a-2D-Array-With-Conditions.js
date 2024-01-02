/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findMatrix = function (nums) {
    const freq = {};

    for (let num of nums) {
        if (freq[num]) freq[num]++;
        else freq[num] = 1;
    }

    const sortedFreq = Object.entries(freq).sort((a, b) => b[1] - a[1]);
    const rows = sortedFreq[0][1];
    const res = [];

    for (let i = 0; i < rows; i++) {
        let row = [];

        for (let j = 0; j < sortedFreq.length; j++) {
            row.push(sortedFreq[j][0]);
            sortedFreq[j][1]--;
            if (sortedFreq[j][1] === 0) {
                sortedFreq.splice(j, 1);
                j--;
            }
        }
        res.push(row);
    }

    return res;
};
