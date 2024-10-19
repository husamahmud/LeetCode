/**
 * Do not return anything, modify nums in-place instead.
 */
/* 1: Bucket sort */
function sortColors(nums: number[]): void {
  const count: number[] = new Array(3).fill(0)

  // count each occurrence
  for (const num of nums) count[num]++

  let idx: number = 0

  for (let i = 0; i < count[0]; i++) nums[idx++] = 0
  for (let i = 0; i < count[1]; i++) nums[idx++] = 1
  for (let i = 0; i < count[2]; i++) nums[idx++] = 2
}