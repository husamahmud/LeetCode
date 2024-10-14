class MyHashMap {
  private map: Map<number, number>

  constructor() {
    this.map = new Map<number, number>()
  }

  put(key: number, value: number): void {
    this.map.set(key, value)
  }

  get(key: number): number {
    const val = this.map.get(key)
    return val !== undefined ? val : -1
  }

  remove(key: number): void {
    this.map.delete(key)
  }
}