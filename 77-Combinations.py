class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def generate(comb: List[int], idx: int) -> None:
            if len(comb) == k:
                res.append(comb[:])
                return

            for i in range(idx, n + 1):
                comb.append(i)
                generate(comb, i + 1)
                comb.pop()

        generate([], 1)
        return res
