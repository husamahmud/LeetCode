function findMin(nums: number[]): number {
  let l = 0, r = nums.length - 1

  while (l < r) {
    const m = Math.floor((r - l) / 2) + l

    if (nums[m] < nums[r]) r = m
    else l = m + 1
  }

  return nums[l]
}
