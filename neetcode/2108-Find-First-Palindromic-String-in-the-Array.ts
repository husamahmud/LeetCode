function isPalindrome(word: string): boolean {
  let l = 0, r = word.length - 1

  while (l < r) {
    if (word[l] !== word[r]) return false
    l++, r--
  }

  return true
}

function firstPalindrome(words: string[]): string {
  for (const word of words) {
    if (isPalindrome(word)) return word
  }

  return ""
};