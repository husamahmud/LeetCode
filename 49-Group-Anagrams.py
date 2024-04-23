class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        res = []

        for str in strs:
            sortedStr = tuple(sorted(str))
            if sortedStr in map:
                map[sortedStr].append(str)
            else:
                map[sortedStr] =[str]

        for entry in map:
            res.append(map[entry])

        return res