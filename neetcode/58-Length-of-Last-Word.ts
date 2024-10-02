function lengthOfLastWord(s: string): number {
  return s.trim().split(' ').at(-1).length
};