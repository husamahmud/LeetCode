class Calculator {
  val: number

  constructor(value: number) {
    this.val = value
  }

  add(value: number): Calculator {
    this.val += value
    return this
  }

  subtract(value: number): Calculator {
    this.val -= value
    return this
  }

  multiply(value: number): Calculator {
    this.val *= value
    return this
  }

  divide(value: number): Calculator {
    if (value === 0) throw new Error("Division by zero is not allowed")
    this.val /= value
    return this
  }

  power(value: number): Calculator {
    this.val = Math.pow(this.val, value)
    return this
  }

  getResult(): number {
    return this.val
  }
}