function isSubsequence(s: string, t: string): boolean {
  let i: number = 0;

  for (const c of t) {
    if (c == s[i]) i++
  }

  return i === s.length
};