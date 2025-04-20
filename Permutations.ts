function permute(nums: number[]): number[][] {
  const res: number[][] = []
  const freq: boolean[] = []

  const rec = (perm: number[], freq: boolean[]) => {
    if (perm.length === nums.length) {
      res.push([...perm])
      return
    }

    for (let i = 0; i < nums.length; i++) {
      if (freq[i]) continue

      freq[i] = true
      perm.push(nums[i])

      rec(perm, freq)

      perm.pop()
      freq[i] = false
    }
  }

  rec([], freq)
  return res
};