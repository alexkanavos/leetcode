class Solution:
    def reformatDate(self, date: str) -> str:
        months: set = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date: list[str] = date.split()
        year: str = date[2]
        month: str = str(months.index(date[1]) + 1)
        if len(month) < 2:
            month = '0' + month
        day: str = date[0]
        if len(day) > 3:
            day = day[:2:]
        else:
            day = '0' + day[:1:]
        return year + '-' + month + '-' + day