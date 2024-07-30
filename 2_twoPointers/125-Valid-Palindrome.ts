function isalnum(c: string): boolean {
  return !!c.match(/[a-zA-Z0-9]/);
}

function isPalindrome(s: string): boolean {
  let r = s.length - 1, l = 0;

  while (l < r) {
    if (!isalnum(s[l])) l++;
    else if (!isalnum(s[r])) r--;
    else {
      if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;
      l++;
      r--;
    }
  }

  return true;
}