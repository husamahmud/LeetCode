function containsNearbyDuplicate(nums: number[], k: number): boolean {
  let count: Set<number> = new Set()

  for (let i = 0; i < nums.length; i++) {
    if (count.has(nums[i])) return true
    count.add(nums[i])
    if (i >= k) count.delete(nums[i - k])
  }

  return false
};