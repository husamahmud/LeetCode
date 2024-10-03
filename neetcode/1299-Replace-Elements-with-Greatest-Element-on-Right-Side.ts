function replaceElements(arr: number[]): number[] {
  const n: number = arr.length
  const res: number[] = new Array(n).fill(-1)
  let max: number = -1

  for (let i = n - 1; i >= 0; i--) {
    res[i] = max
    if (arr[i] > max) max = arr[i]
  }

  return res
};