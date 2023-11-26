class Solution(object):
    def calPoints(self, operations):
        stk = []

        for x in operations:
            if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
                stk.append(int(x))
            elif x == '+':
                stk.append(stk[-1] + stk[-2])
            elif x == 'C':
                stk.pop()
            elif x == 'D':
                stk.append(stk[-1] * 2)

        return sum(stk)
