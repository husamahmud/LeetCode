function longestCommonPrefix(strs: string[]): string {
  let res = "";

  strs.sort((a: string, b: string) => a.length - b.length)

  for (let i = 0; i < strs[0].length; i++) {
    let c = strs[0][i]

    if (strs.every((str: string) => str[i] === c)) res += c
    else return res
  }

  return res
};