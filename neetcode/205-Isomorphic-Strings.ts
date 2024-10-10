function isIsomorphic(s: string, t: string): boolean {
  const sTOt = {}
  const tTOs = {}

  for (let i = 0; i < s.length; i++) {
    // map chars from s to t
    if (!sTOt[s[i]]) sTOt[s[i]] = t[i]
    // map chars from t to s
    if (!tTOs[t[i]]) tTOs[t[i]] = s[i]
  }

  for (let i = 0; i < s.length; i++) {
    // check if it's map to a wrong char 
    if (sTOt[s[i]] !== t[i] || tTOs[t[i]] !== s[i]) return false
  }

  return true
};