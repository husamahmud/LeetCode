function removeDuplicates(nums: number[]): number {
  let l = 1;
  let r = 1;

  while (r < nums.length) {
    if (nums[r] !== nums[r - 1]) {
      nums[l] = nums[r]
      l++
    }
    r++
  }

  return l
};