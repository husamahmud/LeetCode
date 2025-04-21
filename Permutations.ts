function permute(nums: number[]): number[][] {
  const res: number[][] = []

  const rec = (f: boolean[], ds: number[]): void => {
    if (ds.length === nums.length) {
      res.push([...ds])
      return
    }

    for (let i = 0; i < nums.length; i++) {
      if (f[i]) continue

      f[i] = true
      ds.push(nums[i])

      rec(f, ds)

      ds.pop()
      f[i] = false
    }
  }

  rec([], [])
  return res
};