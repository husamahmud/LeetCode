class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def generate(start: int, comb: List[int]) -> None:
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)
                generate(i + 1, comb)
                comb.pop()

        generate(1, [])
        return res
