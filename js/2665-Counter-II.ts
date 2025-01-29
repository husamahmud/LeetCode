type Counter = {
  increment: () => number,
  decrement: () => number,
  reset: () => number,
}

function createCounter(init: number): Counter {
  let count = init

  return {
    increment: () => {
      return ++count
    },
    decrement: () => {
      return --count
    },
    reset: () => {
      count = init
      return init
    }
  }
}

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */