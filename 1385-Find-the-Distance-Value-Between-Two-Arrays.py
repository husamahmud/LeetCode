class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for num1 in arr1:
            close = False
            for num2 in arr2:
                dist = abs(num1 - num2)        
                if dist <= d:
                    close = True
                    break
            if not close:
                count += 1
        return count