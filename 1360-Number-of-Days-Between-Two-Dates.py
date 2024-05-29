from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        dateFormat = "%Y-%m-%d"

        d1 = datetime.strptime(date1, dateFormat)
        d2 = datetime.strptime(date2, dateFormat)
        dif = d1 - d2
        
        return abs(dif.days)
