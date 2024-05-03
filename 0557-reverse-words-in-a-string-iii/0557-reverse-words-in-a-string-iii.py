class Solution:
    def reverseWords(self, s: str) -> str:
        s: list[str] = s.split()
        s = [word[::-1] for word in s]
        s: str = " ".join(s)
        return s