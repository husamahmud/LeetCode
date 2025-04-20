function combinationSum2(candidates: number[], target: number): number[][] {
  const res: number[][] = []
  candidates.sort((a, b) => a - b)

  const rec = (i: number, t: number, ds: number[]): void => {
    if (i === candidates.length) {
      if (t === 0) res.push([...ds])
      return
    }

    if (candidates[i] <= t) {
      ds.push(candidates[i])
      rec(i + 1, t - candidates[i], ds)
      ds.pop()
    }

    while (i + 1 < candidates.length && candidates[i] === candidates[i + 1]) i++

    rec(i + 1, t, ds)
  }

  rec(0, target, [])
  return res
};