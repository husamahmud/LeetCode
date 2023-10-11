class MinStack:
    def __init__(self):
        self.stk = []
        self.min_val = float('inf')

    def push(self, val):
        if val < self.min_val:
            self.min_val = val
        self.stk.append(val)

    def pop(self):
        last_num = self.stk.pop()
        if last_num == self.min_val:
            self.update_min()
        return last_num

    def top(self):
        return self.stk[-1]

    def getMin(self):
        return self.min_val

    def update_min(self):
        self.min_val = float('inf')
        for num in self.stk:
            if num < self.min_val:
                self.min_val = num
