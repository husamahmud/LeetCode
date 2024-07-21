/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const freq = {}
  const sorted = []
  const result = []

  nums.forEach(num => freq[num] = (freq[num] || 0) + 1)

  for (const entry in freq) {
    sorted.push([entry, freq[entry]])
  }

  sorted.sort((a, b) => b[1] - a[1])

  return sorted.slice(0, k).map(entry => entry[0])
};