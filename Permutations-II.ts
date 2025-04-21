function permuteUnique(nums: number[]): number[][] {
  const freq: Record<string, number> = {}
  for (const num of nums) freq[num] = (freq[num] || 0) + 1

  const res: number[][] = []
  const ds: number[] = []

  const rec = () => {
    if (ds.length === nums.length) {
      res.push([...ds])
      return
    }

    for (const num in freq) {
      if (freq[num] === 0) continue

      ds.push(Number(num))
      freq[num]--

      rec()

      ds.pop()
      freq[num]++
    }
  }

  rec()
  return res
}

// const res: number[][] = []
// nums.sort((a, b) => a - b)

// const rec = (f: boolean[], ds: number[]): void => {
//   if (ds.length === nums.length) {
//     res.push([...ds])
//     return
//   }

//   for (let i = 0; i < nums.length; i++) {
//     if (f[i]) continue

//     f[i] = true
//     ds.push(nums[i])

//     rec(f, ds)

//     ds.pop()
//     f[i] = false
//   }
// }

// rec([], [])
// return res