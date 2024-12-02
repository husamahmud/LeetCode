function sum(stack: number[]): number {
  let sum: number = 0
  for (const num of stack) sum += num
  return sum
}

function calPoints(operations: string[]): number {
  const stk: number[] = []

  for (const op of operations) {
    const n = stk.length

    if (op === '+') {
      stk.push(Number(stk[n - 1]) + Number(stk[n - 2]))
    } else if (op === 'D') {
      stk.push(Number(stk[n - 1]) * 2)
    } else if (op === 'C') {
      stk.pop()
    } else {
      stk.push(Number(op))
    }
  }

  return sum(stk)
}
