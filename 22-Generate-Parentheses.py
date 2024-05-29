class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(cur: str, opened: int, closed: int) -> None:
            if len(cur) == 2 * n:
                res.append(cur)
                return
            
            if opened < n:
                generate(cur + "(", opened + 1, closed)
            if closed < opened:
                generate(cur + ")", opened, closed + 1)

        generate("", 0, 0)
        return res

    # BruteForce Solution
    # def generateParenthesis(self, n: int) -> List[str]:
    #     res = []
    #     def generate(cur: str) -> None:
    #         if len(cur) == 2 * n:
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
    #             elif c == ")":
    #                 balance -= 1
    #             if balance < 0:
    #                 return False
    #         return balance == 0
    #     generate("")
    #     return res
