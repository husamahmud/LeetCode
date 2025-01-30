type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
  const res: number[] = []

  for (let i = 0; i < arr.length; i++) {
    const num: number = arr[i]
    if (fn(num, i)) res.push(num)
  }

  return res
};