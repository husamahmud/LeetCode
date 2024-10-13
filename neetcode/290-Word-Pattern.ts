function wordPattern(pattern: string, s: string): boolean {
  const words = s.split(' ');
  if (pattern.length !== words.length) return false;

  const charToWord = new Map<string, string>();
  const wordToChar = new Map<string, string>();

  for (let i = 0; i < pattern.length; i++) {
    const char = pattern[i];
    const word = words[i];

    if (charToWord.has(char) && charToWord.get(char) !== word) return false;
    charToWord.set(char, word);

    if (wordToChar.has(word) && wordToChar.get(word) !== char) return false;
    wordToChar.set(word, char);
  }

  return true;
}