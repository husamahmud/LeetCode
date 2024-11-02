function reverse(nums: number[], l: number, r: number): void {
  while (l < r) {
    [nums[l], nums[r]] = [nums[r], nums[l]]
    l++, r--
  }
}

/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
  k = k % nums.length

  // reverse the array
  reverse(nums, 0, nums.length - 1)
  // output: 7 6 5 4 3 2 1

  // reverse the first portion
  reverse(nums, 0, k - 1)

  // reverse the second portion
  reverse(nums, k, nums.length - 1)
}

/* Extra space solution */
// function rotate(nums: number[], k: number): void {
//   const n: number = nums.length
//   const res: number[] = []
//   for (let i = 0; i < n; i++) res[(i + k) % n] = nums[i]
//   for (let i = 0; i < n; i++) nums[i] = res[i]
// };