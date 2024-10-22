function mergeAlternately(word1: string, word2: string): string {
  const len1 = word1.length;
  const len2 = word2.length;
  const totalLength = len1 + len2;
  const res = new Array(totalLength);
  let index = 0, i = 0;

  while (i < len1 && i < len2) {
    res[index++] = word1[i];
    res[index++] = word2[i];
    i++;
  }

  while (i < len1) res[index++] = word1[i++];
  while (i < len2) res[index++] = word2[i++];

  return res.join('');
}