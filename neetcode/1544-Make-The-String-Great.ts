function makeGood(s: string): string {
  const stk: string[] = []

  for (const c of s) {
    const top = stk.at(-1)

    if (top && c !== top && c.toLowerCase() === top.toLowerCase()) stk.pop()
    else stk.push(c)
  }

  return stk.join("")
};
