/**
 * Do not return anything, modify nums in-place instead.
 */
/* 1: Bucket sort */
// function sortColors(nums: number[]): void {
//   const count: number[] = new Array(3).fill(0)
//   let idx: number = 0
//   for (const num of nums) count[num]++
//   for (let i = 0; i < count[0]; i++) nums[idx++] = 0
//   for (let i = 0; i < count[1]; i++) nums[idx++] = 1
//   for (let i = 0; i < count[2]; i++) nums[idx++] = 2
// }

/* 2: Quick sort */
function sortColors(nums: number[]): void {
  let l = 0, r = nums.length - 1, i = 0

  while (i <= r) {
    if (nums[i] === 0) {
      [nums[i], nums[l]] = [nums[l], nums[i]]
      l++
    } else if (nums[i] === 2) {
      [nums[i], nums[r]] = [nums[r], nums[i]]
      r--, i--
    }

    i++
  }
}