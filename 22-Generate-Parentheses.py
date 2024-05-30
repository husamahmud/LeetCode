class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(cur: str, opened: int, closed: int) -> None:
            if 2 * n == len(cur):
                res.append(cur)
                return

            if opened < n:
                generate(cur + "(", opened + 1, closed)
            if opened > closed:
                generate(cur + ")", opened, closed + 1)

        generate("", 0, 0)
        return res

    # def generateParenthesis(self, n: int) -> List[str]:
    #     res = []

    #     def generate(cur: str) -> None:
    #         if 2 * n == len(cur):
    #             if isValid(cur):
    #                 res.append(cur)
    #             return
    #         generate(cur + "(")
    #         generate(cur + ")")

    #     def isValid(s: str) -> bool:
    #         balance = 0
    #         for c in s:
    #             if c == "(":
    #                 balance += 1
    #             else:
    #                 balance -= 1
    #             if balance < 0:
    #                 return False
    #         return balance == 0
    #     generate("")
    #     return res
