function isNum(c: string): boolean {
  return !isNaN(+c);
}

function evalRPN(tokens: string[]): number {
  const stack: number[] = [];

  for (const token of tokens) {
    if (isNum(token)) {
      stack.push(+token);
    } else {
      const top1 = stack.pop();
      const top2 = stack.pop();

      if (token === '*') {
        stack.push(top2 * top1);
      } else if (token === '+') {
        stack.push(top2 + top1);
      } else if (token === '-') {
        stack.push(top2 - top1);
      } else if (token === '/') {
        stack.push(Math.trunc(top2 / top1));
      }
    }
  }

  return stack[0];
}