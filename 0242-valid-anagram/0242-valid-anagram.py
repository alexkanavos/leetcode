class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t: list[chr] = list(t)    
        for char in s:
            if char in t:
                t.remove(char)
        return t == []