class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        n = len(students)

        for sandwiche in sandwiches:
            if count[sandwiche] > 0:
                n -= 1
                count[sandwiche] -= 1
            else:
                return n
        
        return n