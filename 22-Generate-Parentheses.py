class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(curr: str) -> None:
            if len(curr) == n * 2:
                if isValid(curr):
                    res.append(curr)
                return

            generate(curr + "(")
            generate(curr + ")")

        def isValid(s: str) -> bool:
            balance = 0

            for c in s:
                if c == "(":
                    balance += 1
                elif c == ")":
                    balance -= 1
                if balance < 0:
                    return False

            return balance == 0

        generate("")
        return res
