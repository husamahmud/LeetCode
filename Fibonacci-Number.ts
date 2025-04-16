function fib(n: number): number {
    if (n <= 1) return n
    return fib(n - 2) + fib(n - 1)
};