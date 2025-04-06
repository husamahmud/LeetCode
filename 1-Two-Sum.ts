function twoSum(nums: number[], target: number): number[] {
  const m = {}

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i]

    if (diff in m) return [i, m[diff]]
    m[nums[i]] = i
  }
  return [-1]
};
