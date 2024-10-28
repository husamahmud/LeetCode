function backspaceCompare(s: string, t: string): boolean {
  let i = s.length - 1, j = t.length - 1;
  let skipS = 0, skipT = 0;

  while (i >= 0 || j >= 0) {
    while (i >= 0) {
      if (s[i] === '#') {
        skipS++, i--
      } else if (skipS > 0) {
        skipS--, i--
      } else {
        break;
      }
    }

    while (j >= 0) {
      if (t[j] === '#') {
        skipT++, j--
      } else if (skipT > 0) {
        skipT--, j--
      } else {
        break;
      }
    }

    let charS = i >= 0 ? s[i] : "";
    let charT = j >= 0 ? t[j] : "";
    if (charS !== charT) return false;

    i--;
    j--;
  }

  return true;
}
