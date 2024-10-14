function numOfComb(num: number): number {
  return Math.floor((num * (num - 1)) / 2)
}

function numIdenticalPairs(nums: number[]): number {
  const freq: Record<number, number> = {}
  let res: number = 0

  for (const num of nums) freq[num] = (freq[num] || 0) + 1

  for (const val of Object.values(freq)) res += numOfComb(val)

  return res
};