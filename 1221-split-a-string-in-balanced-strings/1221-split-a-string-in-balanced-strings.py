class Solution:
    def balancedStringSplit(self, s: str) -> int:
        temp: str = ''
        num: int = 0
        for i in range(len(s)):
            temp = s[i::]
            if temp.count('L') == temp.count('R'):
                num += 1
        return num