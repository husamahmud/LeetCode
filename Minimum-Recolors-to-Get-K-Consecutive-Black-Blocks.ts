function minimumRecolors(blocks: string, k: number): number {
  const window: Record<string, number> = { 'W': 0, 'B': 0 }

  for (let i = 0; i < k; i++) window[blocks[i]]++

  let min = window['W']

  for (let i = k; i < blocks.length; i++) {
    window[blocks[i - k]]--
    window[blocks[i]]++

    min = Math.min(min, window['W'])
  }

  return min
}