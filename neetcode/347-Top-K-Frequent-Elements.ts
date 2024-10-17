function topKFrequent(nums: number[], k: number): number[] {
  const freq: Record<number, number> = {}
  const count: Record<number, number[]> = []
  const res: number[] = []

  for (const num of nums) freq[num] = (freq[num] || 0) + 1


  for (const [key, val] of Object.entries(freq)) {
    if (count[val]) count[val].push(+key)
    else count[val] = [+key]
  }

  for (let i = nums.length; i > 0 && res.length < k; i--) {
    if (count[i]) res.push(...count[i]);
    if (res.length >= k) break;
  }

  return res
};