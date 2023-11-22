class Solution(object):
    def minOperations(self, logs):
        ops = 0

        for op in logs:
            if op == './':
                continue
            elif op == '../':
                if ops <= 0:
                    ops = 0
                else:
                    ops -= 1
            else:
                ops += 1

        return ops
