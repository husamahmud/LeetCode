class MinStack {
  stack: number[]

  constructor() {
    this.stack = []
  }

  push(val: number): void {
    this.stack.push(val)
  }

  pop(): void {
    this.stack.pop()
  }

  top(): number {
    return this.stack.at(-1)
  }

  getMin(): number {
    return Math.min(...this.stack)
  }
}