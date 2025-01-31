type F = (x: number) => number;

function compose(functions: F[]): F {
  return function (x) {
    return functions.reduceRight((acc, fn) => fn(acc), x)
  }
};

// function compose(functions: F[]): F {
//   if (functions.length === 0) {
//     return function (x) {
//       return x
//     }
//   }

//   return function (x) {
//     let res: number = x

//     for (let i = functions.length - 1; i >= 0; i--) {
//       res = functions[i](res)
//     }

//     return res
//   }
// };

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */