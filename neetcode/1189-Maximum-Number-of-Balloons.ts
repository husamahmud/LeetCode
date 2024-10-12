function maxNumberOfBalloons(text: string): number {
  const freq: Record<string, number> = {}
  const ballon: string = "balloon"
  let res: number = 0

  for (let i = 0; i < text.length; i++) freq[text[i]] = (freq[text[i]] || 0) + 1

  while (true) {
    for (let i = 0; i < ballon.length; i++) {
      if (freq[ballon[i]]) freq[ballon[i]]--
      else return res
    }

    res++
  }

  return res
};