/* 1: Brute force approach (Time Limit Exceeded) */
// function longestConsecutive(nums: number[]): number {
//   if (nums.length === 0) return 0
//   let maxStreak: number = 0
//   for (const num of nums) {
//     let curNum: number = num
//     let curStreak: number = 1
//     if (!nums.includes(curNum - 1)) {
//       while (nums.includes(curNum + 1)) {
//         curNum++, curStreak++
//       }
//       maxStreak = Math.max(maxStreak, curStreak)
//     }
//   }
//   return maxStreak
// }

/* 2: Sort the array first and search */
// function longestConsecutive(nums: number[]): number {
//   if (nums.length === 0) return 0
//   nums = nums.sort((a: number, b: number) => a - b)
//   let maxStreak: number = 0
//   let curStreak: number = 1
//   for (let i = 1; i < nums.length; i++) {
//     if (nums[i] === nums[i - 1]) continue
//     if (nums[i] === nums[i - 1] + 1) {
//       curStreak++
//     } else {
//       maxStreak = Math.max(maxStreak, curStreak)
//       curStreak = 1
//     }
//   }
//   return Math.max(maxStreak, curStreak)
// }

/* 3: use set for faster lookup */
function longestConsecutive(nums: number[]): number {
  const set: Set<number> = new Set(nums)
  let max: number = 0

  for (const num of nums) {
    if (!set.has(num - 1)) {
      let cur: number = 0

      while (set.has(num + cur)) cur++
      max = Math.max(max, cur)
    }
  }

  return max
}
