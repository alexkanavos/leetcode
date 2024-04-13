class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while(s[-1] == ' '):
            s = s.strip()
        count: int = 0
        s = list(s)
        for char in s[-1::-1]:
            if char != ' ':
                count += 1
            else:
                break
        return count
        