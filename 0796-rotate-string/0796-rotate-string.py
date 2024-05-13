class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s: list[chr] = list(s)
        goal: list[chr] = list(goal)
        for _ in range(len(s)):
            temp: chr = s[0]
            s.append(temp)
            s.pop(0)
            if s == goal:
                return True
        return False