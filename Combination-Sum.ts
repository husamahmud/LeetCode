function combinationSum(candidates: number[], target: number): number[][] {
  const res: number[][] = []

  const rec = (i: number, t: number, ds: number[]): void => {
    if (i === candidates.length) {
      if (t === 0) res.push([...ds])
      return
    }

    if (candidates[i] <= t) {
      ds.push(candidates[i])
      rec(i, t - candidates[i], ds)
      ds.pop()
    }

    rec(i + 1, t, ds)
  }

  rec(0, target, [])
  return res
};