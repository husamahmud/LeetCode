function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  const n: number = arr.length
  const res: number[] = new Array(n)

  for (let i = 0; i < n; i++) res[i] = fn(arr[i], i)

  return res
};