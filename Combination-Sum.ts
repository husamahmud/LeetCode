function combinationSum(candidates: number[], target: number): number[][] {
  const res: number[][] = []

  const fn = (i: number, t: number, comb: number[]) => {
    if (i === candidates.length) {
      if (t === 0) res.push([...comb])
      return
    }

    if (candidates[i] <= t) {
      comb.push(candidates[i])
      fn(i, t - candidates[i], comb)
      comb.pop()
    }

    fn(i + 1, t, comb)
  }

  fn(0, target, [])
  return res
};