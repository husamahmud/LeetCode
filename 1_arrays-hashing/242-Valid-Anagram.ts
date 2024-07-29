function isAnagram(s: string, t: string): boolean {
  const f = {}

  for (const c of s) {
    if (f[c]) f[c]++
    else f[c] = 1
  }

  for (const c of t) {
    if (!f[c]) return false
    else f[c]--
  }

  for (const key in f) if (f[key]) return false

  return true
};