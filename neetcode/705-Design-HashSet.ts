class MyHashSet {
  private set: Set<number>

  constructor() {
    this.set = new Set<number>()
  }

  add(key: number): void {
    this.set.add(key)
  }

  remove(key: number): void {
    this.set.delete(key)
  }

  contains(key: number): boolean {
    return this.set.has(key)
  }
}