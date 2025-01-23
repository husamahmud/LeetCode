function twoSum(nums: number[], target: number): number[] {
  const map: Record<number, number> = {}

  for (let i = 0; i < nums.length; i++) {
    const dif = target - nums[i]

    if (map[dif] !== undefined) return [map[dif], i]
    map[nums[i]] = i
  }

  return [-1]
};
