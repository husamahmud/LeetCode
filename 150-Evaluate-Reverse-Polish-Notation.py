class Solution(object):
    def calc(slef, op, x, y):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return int(float(x) / y)

    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                stack.append(self.calc(token, x, y))

        return stack[0]
