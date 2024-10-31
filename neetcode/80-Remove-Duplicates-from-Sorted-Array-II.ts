function removeDuplicates(nums: number[]): number {
  let idx = 2

  for (let i = 2; i < nums.length; i++) {
    if (nums[i] !== nums[idx - 2]) {
      nums[idx] = nums[i]
      idx++
    }
  }

  return idx
};