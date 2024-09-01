function isAlnum(c: string): boolean {
  return !!c.match(/[a-zA-Z0-9]/);
}

function isPalindrome(s: string): boolean {
  let l = 0, r = s.length - 1

  while (l < r) {
    if (!isAlnum(s[l])) {
      l++
    } else if (!isAlnum(s[r])) {
      r--
    } else {
      if (s[l].toLowerCase() !== s[r].toLowerCase()) return false
      l++
      r--
    }
  }

  return true
};