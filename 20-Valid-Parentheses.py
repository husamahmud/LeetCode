class Solution(object):
    def isValid(self, s):
        stk = []
        n = len(s)

        for c in range(n):
            if s[c] == '(' or s[c] == '{' or s[c] == '[':
                stk.append(s[c])
            else:
                if len(stk) == 0:
                    return False

                top = stk.pop()
                if (s[c] == ')' and top != '(') or \
                   (s[c] == '}' and top != '{') or \
                   (s[c] == ']' and top != '['):
                        return False

        return len(stk) == 0
