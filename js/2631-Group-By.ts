interface Array<T> {
  groupBy(fn: (item: T) => string): Record<string, T[]>
}

Array.prototype.groupBy = function (fn) {
  const res = {}

  for (const item of this) {
    const key: string = fn(item)
    if (!res[key]) res[key] = [item]
    else res[key].push(item)
  }

  return res
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */