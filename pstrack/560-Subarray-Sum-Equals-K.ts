// prefix sum
function subarraySum(nums: number[], k: number): number {
  const prefixSum = new Map()
  prefixSum.set(0, 1)

  let currSum = 0
  let count = 0

  for (const num of nums) {
    currSum += num
    const diff = currSum - k

    if (prefixSum.has(diff)) {
      count += prefixSum.get(diff)
    }

    prefixSum.set(currSum, (prefixSum.get(currSum) || 0) + 1)
  }

  return count
}

// brute force 
// function subarraySum(nums: number[], k: number): number {
//   let count = 0
//   const n = nums.length

//   for (let start = 0; start < n; start++) {
//     let sum = 0

//     for (let end = start; end < n; end++) {
//       sum += nums[end]
//       if (sum === k) count++
//     }
//   }

//   return count
// };