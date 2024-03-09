/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const freq = {};

  for (let num of nums) {
    if (freq[num]) return true;
    else freq[num] = 1;
  }

  return false;
};