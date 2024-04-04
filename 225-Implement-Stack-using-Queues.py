class MyStack:
    def __init__(self):
        self.stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def empty(self) -> bool:
        return len(self.stk) == 0