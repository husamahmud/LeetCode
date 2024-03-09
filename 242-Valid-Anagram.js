/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  if (s.length !== t.length) return false;

  const freq = {};
  for (let c of s) freq[c] = (freq[c] || 0) + 1;

  for (let c of t) {
    if (!freq[c]) return false;
    freq[c]--;
  }

  return true;
};