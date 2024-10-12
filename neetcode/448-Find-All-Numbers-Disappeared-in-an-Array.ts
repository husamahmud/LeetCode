function findDisappearedNumbers(nums: number[]): number[] {
  const set: Set<number> = new Set(nums)
  const res: number[] = []

  for (let i = 1; i <= nums.length; i++) {
    if (!set.has(i)) res.push(i)
  }

  return res
};