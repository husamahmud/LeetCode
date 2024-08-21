function topKFrequent(nums: number[], k: number): number[] {
  const freq = {}, sorted = []

  for (const num of nums) freq[num] = (freq[num] || 0) + 1

  for (const entry in freq) sorted.push([entry, freq[entry]])

  sorted.sort((a, b) => b[1] - a[1])

  return sorted.slice(0, k).map(entry => entry[0])
};