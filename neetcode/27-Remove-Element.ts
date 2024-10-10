function removeElement(nums: number[], val: number): number {
  let idx = 0

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) nums[idx++] = nums[i]
  }

  return idx
};