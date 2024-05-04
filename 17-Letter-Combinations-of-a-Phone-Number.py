\\\
    map
    res 

    bt:
        base case
\\\
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        valid = [str(i) for i in range(2,10)]

        if not digits:
            return \\

        for digit in digits: # 2 3
            if digit not in valid:
                return \\

        map = {
            \2\: \abc\,
            \3\: \def\,
            \4\: \ghi\,
            \5\: \jkl\,
            \6\: \mno\,
            \7\: \pqrs\,
            \8\: \tuv\,
            \9\: \wxyz\,
        }
        res = []

        def bt(idx: int, comb: str) -> None:
            if len(comb) == len(digits):
                res.append(comb)
                return

            for l in map[digits[idx]]:
                bt(idx + 1, comb + l)

        bt(0, \\)
        return res