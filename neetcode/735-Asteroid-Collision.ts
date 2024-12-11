function asteroidCollision(asteroids: number[]): number[] {
  const stack: number[] = []

  for (let i = 0; i < asteroids.length; i++) {
    const top: number | null = stack[stack.length - 1]
    const ast: number = asteroids[i]

    if (!stack.length || top < 0 || ast > 0) {
      stack.push(ast)
    } else if (-ast == top) {
      stack.pop()
    } else if (-ast > top) {
      stack.pop()
      i--
    }
  }

  return stack
}